"""Offline checks for the WAZIS v0.1 application.

Standard library only. Run from the repository root with the application's environment:

    python -m unittest discover -s tests -v

Each test uses its own temporary database; the real ``app/wazis.db`` is never opened.
"""

import hashlib
import json
import os
import re
import sqlite3
import sys
import tempfile
import unittest

_TMP = tempfile.TemporaryDirectory()
os.environ["WAZIS_DB"] = os.path.join(_TMP.name, "import.db")
os.environ.setdefault("WAZIS_SECRET_KEY", "test-only-not-a-secret")
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "app"))

import app as wazis  # noqa: E402


def tearDownModule():
    _TMP.cleanup()


class WazisTestCase(unittest.TestCase):
    def setUp(self):
        self._dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self._dir.name, "wazis.db")
        self._old_db_path = wazis.DB_PATH
        wazis.DB_PATH = self.db_path
        wazis.init_db()
        self.author = wazis.app.test_client()
        self.other = wazis.app.test_client()

    def tearDown(self):
        wazis.DB_PATH = self._old_db_path
        self._dir.cleanup()

    def csrf(self, client, path="/new"):
        html = client.get(path).get_data(as_text=True)
        return re.search(r'name="csrf" value="([^"]+)"', html).group(1)

    def post_need(self, client, text="a need"):
        return client.post("/entries", data={"text": text, "csrf": self.csrf(client)})

    def query(self, sql, args=()):
        with sqlite3.connect(self.db_path) as db:
            return db.execute(sql, args).fetchall()


class NeedAndReplyTests(WazisTestCase):
    def test_pages_render(self):
        for path in ("/", "/new", "/me", "/recover"):
            self.assertEqual(self.author.get(path).status_code, 200, path)
        self.assertEqual(self.author.get("/e/999").status_code, 404)

    def test_post_need_appears_on_home(self):
        self.assertEqual(self.post_need(self.author, "need one").status_code, 302)
        self.assertIn("need one", self.other.get("/").get_data(as_text=True))

    def test_empty_need_is_not_stored(self):
        self.post_need(self.author, "   ")
        self.assertEqual(self.query("SELECT COUNT(*) FROM entries")[0][0], 0)

    def test_reply_with_link_is_reality_feedback(self):
        self.post_need(self.author)
        r = self.other.post(
            "/entries/1/replies",
            data={"text": "", "link": "https://example.org/result", "csrf": self.csrf(self.other, "/e/1")},
        )
        self.assertEqual(r.status_code, 302)
        self.assertIn("https://example.org/result", self.author.get("/e/1").get_data(as_text=True))
        self.assertEqual(
            self.query("SELECT parent_id, link FROM entries WHERE id = 2"),
            [(1, "https://example.org/result")],
        )

    def test_link_must_be_http_or_https(self):
        self.post_need(self.author)
        self.author.post(
            "/entries/1/replies",
            data={"text": "x", "link": "javascript:alert(1)", "csrf": self.csrf(self.author, "/e/1")},
        )
        self.assertEqual(self.query("SELECT COUNT(*) FROM entries WHERE parent_id IS NOT NULL")[0][0], 0)

    def test_post_without_csrf_token_is_rejected(self):
        self.assertEqual(self.author.post("/entries", data={"text": "x"}).status_code, 400)
        self.assertEqual(self.query("SELECT COUNT(*) FROM entries")[0][0], 0)


class FourAbsencesTests(WazisTestCase):
    """The launch gate: no measurement, no closure, no governor, reality by provenance."""

    def test_only_the_author_can_withdraw(self):
        self.post_need(self.author, "mine")
        r = self.other.post("/entries/1/withdraw", data={"csrf": self.csrf(self.other)})
        self.assertEqual(r.status_code, 403)
        self.assertEqual(self.query("SELECT status, text FROM entries WHERE id = 1"), [("open", "mine")])

    def test_author_withdrawal_leaves_a_tombstone(self):
        self.post_need(self.author, "mine")
        r = self.author.post("/entries/1/withdraw", data={"csrf": self.csrf(self.author, "/e/1")})
        self.assertEqual(r.status_code, 302)
        self.assertEqual(
            self.query("SELECT status, text, link FROM entries WHERE id = 1"), [("withdrawn", "", None)]
        )

    def test_schema_cannot_store_closed(self):
        self.post_need(self.author)
        with self.assertRaises(sqlite3.IntegrityError):
            with sqlite3.connect(self.db_path) as db:
                db.execute("UPDATE entries SET status = 'closed' WHERE id = 1")

    def test_schema_has_no_measurement_columns(self):
        columns = {row[1] for table in ("entries", "authors") for row in self.query(f"PRAGMA table_info({table})")}
        forbidden = {"votes", "score", "rank", "priority", "category", "reputation", "karma", "likes"}
        self.assertEqual(columns & forbidden, set())

    def test_no_route_closes_deletes_or_votes(self):
        rules = [str(rule) for rule in wazis.app.url_map.iter_rules()]
        for word in ("close", "resolve", "delete", "vote", "like", "admin", "moderate"):
            self.assertFalse([r for r in rules if word in r], word)
        methods = set().union(*(rule.methods for rule in wazis.app.url_map.iter_rules()))
        self.assertNotIn("DELETE", methods)


class IdentityTests(WazisTestCase):
    def test_recovery_key_restores_identity_on_another_device(self):
        self.post_need(self.author, "mine")
        key = re.search(r"<code[^>]*>([^<]+)</code>", self.author.get("/me").get_data(as_text=True))
        self.assertIsNotNone(key, "recovery key should be shown on /me after the first post")
        device = wazis.app.test_client()
        r = device.post("/recover", data={"key": key.group(1).strip(), "csrf": self.csrf(device, "/recover")})
        self.assertEqual(r.status_code, 302)
        r = device.post("/entries/1/withdraw", data={"csrf": self.csrf(device, "/e/1")})
        self.assertEqual(r.status_code, 302)
        self.assertEqual(self.query("SELECT status FROM entries WHERE id = 1"), [("withdrawn",)])

    def test_wrong_recovery_key_restores_nothing(self):
        self.post_need(self.author, "mine")
        device = wazis.app.test_client()
        device.post("/recover", data={"key": "not-a-key", "csrf": self.csrf(device, "/recover")})
        r = device.post("/entries/1/withdraw", data={"csrf": self.csrf(device, "/e/1")})
        self.assertEqual(r.status_code, 403)


class WelcomesTests(WazisTestCase):
    """What responses the author welcomes. Not a category, not consent."""

    def set_intent(self, client, entry_id=1, **form):
        return client.post(f"/entries/{entry_id}/intent",
                           data={"csrf": self.csrf(client, f"/e/{entry_id}"), **form})

    def intents(self):
        return self.query("SELECT entry_id, welcomes FROM need_intents ORDER BY id")

    def test_a_need_starts_with_nothing_said(self):
        self.post_need(self.author)
        self.assertEqual(self.intents(), [])
        page = self.other.get("/e/1").get_data(as_text=True)
        self.assertIn("has not said what kind of response they welcome", page)
        self.assertIn("It is not agreement to", page)

    def test_only_the_author_sees_the_form_and_only_the_author_can_set_it(self):
        self.post_need(self.author)
        self.assertIn('name="welcomes"', self.author.get("/e/1").get_data(as_text=True))
        self.assertNotIn('name="welcomes"', self.other.get("/e/1").get_data(as_text=True))
        self.assertEqual(self.set_intent(self.other, welcomes="mutual_aid").status_code, 403)
        self.assertEqual(self.intents(), [])

    def test_the_author_states_what_they_welcome_and_everyone_can_read_it(self):
        self.post_need(self.author)
        r = self.set_intent(self.author, welcomes=["mutual_aid", "information"])
        self.assertEqual(r.status_code, 302)
        self.assertEqual(self.intents(), [(1, '["information","mutual_aid"]')])
        page = self.other.get("/e/1").get_data(as_text=True)
        self.assertIn("Information or pointers", page)
        self.assertIn("A hand from someone, with no payment", page)
        self.assertNotIn("Someone proposing organised work", page)

    def test_each_change_is_appended_and_the_newest_is_current(self):
        self.post_need(self.author)
        self.set_intent(self.author, welcomes="information")
        self.set_intent(self.author, welcomes="arranged_work")
        self.set_intent(self.author)                      # ticked nothing
        self.set_intent(self.author, say_nothing="1")     # took it back
        self.assertEqual([w for _, w in self.intents()],
                         ['["information"]', '["arranged_work"]', "[]", None])
        page = self.other.get("/e/1").get_data(as_text=True)
        self.assertIn("has not said what kind of response they welcome", page)

    def test_an_unknown_kind_of_response_is_refused(self):
        self.post_need(self.author)
        for value in ("employment", "paid_work", "contact_me", ""):
            self.assertEqual(self.set_intent(self.author, welcomes=value).status_code, 400)
        self.assertEqual(self.intents(), [])

    def test_it_cannot_be_set_on_a_reply_a_missing_or_a_withdrawn_need(self):
        self.post_need(self.author)
        self.author.post("/entries/1/replies",
                         data={"text": "a reply", "csrf": self.csrf(self.author, "/e/1")})
        self.assertEqual(self.set_intent(self.author, entry_id=2, welcomes="information").status_code, 404)
        self.assertEqual(self.author.post("/entries/99/intent",
                                          data={"csrf": self.csrf(self.author)}).status_code, 404)
        self.author.post("/entries/1/withdraw", data={"csrf": self.csrf(self.author, "/e/1")})
        r = self.author.post("/entries/1/intent",
                             data={"csrf": self.csrf(self.author), "welcomes": "information"})
        self.assertEqual(r.status_code, 409)
        self.assertEqual(self.intents(), [])

    def test_it_changes_nothing_about_the_need_itself(self):
        self.post_need(self.author, "the words")
        before = self.query("SELECT * FROM entries")
        self.set_intent(self.author, welcomes=["arranged_work", "mutual_aid"])
        self.assertEqual(self.query("SELECT * FROM entries"), before)

    def test_it_is_not_a_category_and_orders_nothing(self):
        """The home list is newest first whatever anybody welcomes, and says nothing of it."""
        for words in ("first", "second", "third"):
            self.post_need(self.author, words)
        # Posted within one second of each other; give them distinct times.
        with sqlite3.connect(self.db_path) as db:
            for entry_id in (1, 2, 3):
                db.execute("UPDATE entries SET created_at = ? WHERE id = ?",
                           (f"2026-10-08T11:00:0{entry_id}Z", entry_id))
        plain = self.other.get("/").get_data(as_text=True)
        self.set_intent(self.author, entry_id=1, welcomes="arranged_work")
        self.set_intent(self.author, entry_id=3, welcomes="mutual_aid")
        self.assertEqual(self.other.get("/").get_data(as_text=True), plain)
        self.assertLess(plain.index("third"), plain.index("second"))
        self.assertLess(plain.index("second"), plain.index("first"))
        columns = {row[1] for row in self.query("PRAGMA table_info(entries)")}
        self.assertEqual(columns & {"welcomes", "category", "kind", "type", "intent"}, set())
        rules = [str(rule) for rule in wazis.app.url_map.iter_rules()]
        for word in ("category", "filter", "search", "sort", "tag", "match"):
            self.assertFalse([r for r in rules if word in r], word)

    def test_the_page_never_reads_as_consent_or_an_offer_of_work(self):
        self.post_need(self.author)
        self.set_intent(self.author, welcomes=list(wazis.WELCOMES))
        page = self.other.get("/e/1").get_data(as_text=True).lower()
        for phrase in ("consents", "agrees to", "hire", "job", "apply", "contact the author",
                       "accepts work", "available for work"):
            self.assertNotIn(phrase, page, phrase)

    def test_a_database_made_before_this_gains_the_table_and_keeps_its_needs(self):
        self.post_need(self.author, "from before")
        with sqlite3.connect(self.db_path) as db:
            db.execute("DROP TABLE need_intents")
        wazis.init_db()
        self.assertEqual(self.intents(), [])
        self.assertIn("from before", self.other.get("/e/1").get_data(as_text=True))
        self.assertEqual(self.set_intent(self.author, welcomes="information").status_code, 302)


class NeedDocumentTests(WazisTestCase):
    """The Need document, contract 1: what another system may rely on."""

    ORIGIN = "https://wazis.example"

    def setUp(self):
        super().setUp()
        self._origin = os.environ.get("WAZIS_PUBLIC_ORIGIN")
        os.environ["WAZIS_PUBLIC_ORIGIN"] = self.ORIGIN

    def tearDown(self):
        if self._origin is None:
            os.environ.pop("WAZIS_PUBLIC_ORIGIN", None)
        else:
            os.environ["WAZIS_PUBLIC_ORIGIN"] = self._origin
        super().tearDown()

    def document(self, entry_id=1):
        response = self.other.get(f"/e/{entry_id}/need.json")
        self.assertEqual(response.status_code, 200, response.get_data(as_text=True))
        return json.loads(response.get_data(as_text=True))

    def test_an_open_need_with_nothing_said(self):
        self.post_need(self.author, "  the words\r\nsecond line  ")
        document = self.document()
        self.assertEqual(sorted(document), [
            "contract", "created_at", "document_digest", "instance", "intent",
            "issued_at", "kind", "need_digest", "need_digest_schema", "need_id",
            "status", "text"])
        self.assertEqual(document["kind"], "wazis.need-document")
        self.assertEqual(document["contract"], 1)
        self.assertEqual(document["instance"], self.ORIGIN)
        self.assertEqual(document["need_id"], 1)
        self.assertEqual(document["status"], "open")
        self.assertEqual(document["text"], "the words\nsecond line")
        self.assertEqual(document["intent"], {"stated": False})

    def test_both_digests_can_be_recomputed_from_the_document_alone(self):
        self.post_need(self.author, "the words")
        document = self.document()
        body = {k: v for k, v in document.items() if k != "document_digest"}
        canonical = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
        self.assertEqual(document["document_digest"],
                         "sha256:" + hashlib.sha256(canonical.encode("utf-8")).hexdigest())
        need = json.dumps({"kind": "wazis.need", "schema": 1, "instance": self.ORIGIN,
                           "need_id": 1, "text": "the words"},
                          sort_keys=True, separators=(",", ":"), ensure_ascii=False)
        self.assertEqual(document["need_digest"],
                         "sha256:" + hashlib.sha256(need.encode("utf-8")).hexdigest())

    def test_it_carries_what_the_author_welcomes(self):
        self.post_need(self.author)
        self.author.post("/entries/1/intent", data={
            "csrf": self.csrf(self.author, "/e/1"),
            "welcomes": ["mutual_aid", "arranged_work"]})
        intent = self.document()["intent"]
        self.assertEqual(intent["stated"], True)
        self.assertEqual(intent["welcomes"], ["arranged_work", "mutual_aid"])
        self.assertRegex(intent["set_at"], r"^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ$")

    def test_what_is_welcome_does_not_change_the_digest_of_the_words(self):
        self.post_need(self.author, "the words")
        before = self.document()
        self.author.post("/entries/1/intent", data={
            "csrf": self.csrf(self.author, "/e/1"), "welcomes": "information"})
        after = self.document()
        self.assertEqual(after["need_digest"], before["need_digest"])
        self.assertNotEqual(after["document_digest"], before["document_digest"])

    def test_it_never_names_the_author_or_includes_replies(self):
        self.post_need(self.author, "the words")
        self.author.post("/me/handle", data={"csrf": self.csrf(self.author, "/me"),
                                             "handle": "a-chosen-name"})
        self.other.post("/entries/1/replies", data={
            "text": "a reply nobody asked to export", "link": "https://example.org/x",
            "csrf": self.csrf(self.other, "/e/1")})
        raw = self.other.get("/e/1/need.json").get_data(as_text=True)
        author_id, token_hash = self.query("SELECT id, token_hash FROM authors")[0]
        for private in (author_id, author_id[:6], token_hash, "a-chosen-name",
                        "a reply nobody asked", "example.org", "author", "handle"):
            self.assertNotIn(private, raw, private)

    def test_a_withdrawn_need_has_no_words_no_digest_and_no_intent(self):
        self.post_need(self.author, "the words")
        self.author.post("/entries/1/intent", data={
            "csrf": self.csrf(self.author, "/e/1"), "welcomes": "information"})
        self.author.post("/entries/1/withdraw", data={"csrf": self.csrf(self.author, "/e/1")})
        document = self.document()
        self.assertEqual(sorted(document), [
            "contract", "created_at", "document_digest", "instance", "issued_at",
            "kind", "need_id", "status"])
        self.assertEqual(document["status"], "withdrawn")
        self.assertNotIn("the words", json.dumps(document))

    def test_a_reply_and_a_missing_need_have_no_document(self):
        self.post_need(self.author)
        self.author.post("/entries/1/replies",
                         data={"text": "a reply", "csrf": self.csrf(self.author, "/e/1")})
        self.assertEqual(self.other.get("/e/2/need.json").status_code, 404)
        self.assertEqual(self.other.get("/e/99/need.json").status_code, 404)

    def test_no_document_is_served_without_a_configured_origin(self):
        self.post_need(self.author)
        for value in (None, "", "wazis.example", "https://wazis.example/path", "ftp://x.example"):
            if value is None:
                os.environ.pop("WAZIS_PUBLIC_ORIGIN", None)
            else:
                os.environ["WAZIS_PUBLIC_ORIGIN"] = value
            self.assertEqual(self.other.get("/e/1/need.json").status_code, 503, value)

    def test_the_origin_is_written_in_its_plain_form(self):
        self.post_need(self.author)
        for value in ("HTTPS://Wazis.Example/", "https://wazis.example:443"):
            os.environ["WAZIS_PUBLIC_ORIGIN"] = value
            self.assertEqual(self.document()["instance"], self.ORIGIN)
        os.environ["WAZIS_PUBLIC_ORIGIN"] = "http://localhost:5000"
        self.assertEqual(self.document()["instance"], "http://localhost:5000")

    def test_reading_a_document_writes_nothing(self):
        self.post_need(self.author)
        before = [self.query(f"SELECT COUNT(*) FROM {t}")[0][0]
                  for t in ("entries", "authors", "need_intents")]
        for _ in range(3):
            self.document()
        self.assertEqual([self.query(f"SELECT COUNT(*) FROM {t}")[0][0]
                          for t in ("entries", "authors", "need_intents")], before)


class ContractFixtureTests(unittest.TestCase):
    """The committed fixtures are what this code produces, byte for byte.

    Another system tests against `contract/need-document-v1/fixtures.json`. If
    this fails, the document changed: either put it back, or it is a new
    contract number and a new fixture file — never a silent change to this one.

    To write the file after a deliberate change: WAZIS_WRITE_FIXTURES=1.
    """

    PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                        "contract", "need-document-v1", "fixtures.json")
    INSTANCE = "https://wazis.example"
    WORDS = ("近所の子ども食堂で、来月から配膳を手伝える人が足りません。\n"
             "平日の夕方に一時間ほど来られる方がいると助かります。\n\n"
             "We are short of people to help serve meals at a neighbourhood children's "
             "cafeteria from next month.")

    @classmethod
    def build(cls):
        def case(name, need_id, *, status="open", text=None, welcomes=None, stated=False):
            entry = {"id": need_id, "status": status,
                     "text": "" if status == "withdrawn" else (text or cls.WORDS),
                     "created_at": "2026-10-08T11:34:26Z"}
            intent = {"stated": stated, "welcomes": list(welcomes or []),
                      "set_at": "2026-10-08T12:00:00Z" if stated else None}
            return {"name": name, "document": wazis.need_document(
                instance=cls.INSTANCE, entry=entry, intent=intent,
                issued_at="2026-10-09T00:00:00Z")}

        return {
            "about": ("Canonical examples of the WAZIS Need document, contract 1. "
                      "Synthetic: no real person, place or organisation, and never "
                      "posted to an instance. Generated by WAZIS's own serializer "
                      "and checked by its tests; consumers should test against this "
                      "file and refuse any contract number they do not know."),
            "kind": wazis.NEED_DOCUMENT_KIND,
            "contract": wazis.NEED_DOCUMENT_CONTRACT,
            "welcomes_values": list(wazis.WELCOMES),
            "cases": [
                case("open, nothing said (every Need made before contract 1)", 12),
                case("open, welcomes information", 13, stated=True, welcomes=["information"]),
                case("open, welcomes mutual aid", 14, stated=True, welcomes=["mutual_aid"]),
                case("open, welcomes arranged work", 15, stated=True, welcomes=["arranged_work"]),
                case("open, welcomes mutual aid and arranged work", 16, stated=True,
                     welcomes=["mutual_aid", "arranged_work"]),
                case("open, welcomes all three", 17, stated=True,
                     welcomes=["information", "mutual_aid", "arranged_work"]),
                case("open, stated and welcomes none of the three", 18, stated=True, welcomes=[]),
                case("open, stored with CRLF and decomposed accents", 19,
                     text="  Cafe\u0301 で手伝いが必要です\r\n二行目\r\n  "),
                case("withdrawn", 20, status="withdrawn"),
            ],
        }

    def test_the_committed_fixtures_are_what_the_serializer_produces(self):
        built = json.dumps(self.build(), ensure_ascii=False, indent=2) + "\n"
        if os.environ.get("WAZIS_WRITE_FIXTURES") == "1":
            os.makedirs(os.path.dirname(self.PATH), exist_ok=True)
            with open(self.PATH, "w", encoding="utf-8") as handle:
                handle.write(built)
        with open(self.PATH, encoding="utf-8") as handle:
            self.assertEqual(handle.read(), built)

    def test_every_fixture_document_is_internally_consistent(self):
        with open(self.PATH, encoding="utf-8") as handle:
            fixtures = json.load(handle)
        self.assertEqual(fixtures["contract"], 1)
        for case in fixtures["cases"]:
            document = case["document"]
            body = {k: v for k, v in document.items() if k != "document_digest"}
            self.assertEqual(document["document_digest"], wazis.sha256_of(body), case["name"])
            if document["status"] == "open":
                self.assertEqual(document["text"], wazis.normalise_need_text(document["text"]))
                self.assertEqual(document["need_digest"], wazis.need_digest(
                    document["instance"], document["need_id"], document["text"]))
                if document["intent"]["stated"]:
                    self.assertEqual(document["intent"]["welcomes"],
                                     sorted(document["intent"]["welcomes"]))
                    self.assertLessEqual(set(document["intent"]["welcomes"]), set(wazis.WELCOMES))


if __name__ == "__main__":
    unittest.main()
