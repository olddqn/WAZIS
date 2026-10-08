"""Offline checks for the WAZIS v0.1 application.

Standard library only. Run from the repository root with the application's environment:

    python -m unittest discover -s tests -v

Each test uses its own temporary database; the real ``app/wazis.db`` is never opened.
"""

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


if __name__ == "__main__":
    unittest.main()
