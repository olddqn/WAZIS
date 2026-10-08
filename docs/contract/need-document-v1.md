# The Need document — contract 1

This is the whole of what WAZIS promises another system about the shape of a Need.
A system that wants to read a Need reads this document. It should not read the
WAZIS database or scrape a page: neither is a promise.

- Route: `GET /e/<need_id>/need.json`
- Fixtures: [`contract/need-document-v1/fixtures.json`](../../contract/need-document-v1/fixtures.json)
- Status: implemented in WAZIS v0.1. Read-only. Nothing is written by reading it.

## What it is not

- **Not proof of where it came from.** Anyone can write a document with a correct
  digest. The digests show a document is intact. They do not show WAZIS issued it.
  Only fetching it from the instance's own address shows that.
- **Not consent.** `intent` says what kinds of response the author is open to
  hearing. It is not agreement to any response, and it authorises nobody to act for
  the author, contact them, or commit them to anything.
- **Not a category.** `intent` describes responses the author welcomes, never what
  kind of Need this is. WAZIS does not sort, filter or rank by it, and a reader
  should not either.

## Fields

An **open** Need has exactly these keys:

| Key | Type | Meaning |
|---|---|---|
| `kind` | string | Always `wazis.need-document` |
| `contract` | integer | Always `1` for this contract |
| `instance` | string | This WAZIS instance, as an origin in plain form |
| `need_id` | integer | The Need's number on this instance |
| `status` | string | `open` |
| `created_at` | string | When the Need was posted, UTC, `YYYY-MM-DDTHH:MM:SSZ` |
| `issued_at` | string | When this document was made, same form |
| `text` | string | The words of the Need, normalised (see below) |
| `need_digest` | string | Digest of the words (see below) |
| `need_digest_schema` | integer | Always `1` |
| `intent` | object | What the author welcomes (see below) |
| `document_digest` | string | Digest of every other key in this document |

A **withdrawn** Need has `status: withdrawn` and no `text`, `need_digest`,
`need_digest_schema` or `intent`. Its author removed the words, so the document
has none.

The document never contains the author, the author's handle, or any reply.

A reply has no document (404). An instance with no `WAZIS_PUBLIC_ORIGIN`
configured serves no documents (503), because a document naming the wrong
instance would be worse than none.

## `intent`

Either `{"stated": false}` or:

```
{"stated": true, "welcomes": [...], "set_at": "YYYY-MM-DDTHH:MM:SSZ"}
```

`welcomes` is a sorted list of zero or more of:

| Value | Shown in WAZIS as |
|---|---|
| `information` | Information or pointers |
| `mutual_aid` | A hand from someone, with no payment |
| `arranged_work` | Someone proposing organised work |

- **`stated: false`** means the author has said nothing. Every Need posted before
  this contract existed is in this state. It is not the same as an empty list.
- **An empty list** means the author answered and ticked none.
- The author can change it at any time. The words of the Need do not change when
  they do, so `need_digest` stays the same and `document_digest` changes.

## The two digests

Both are `sha256` over the UTF-8 bytes of a JSON object serialised with keys
sorted, separators `,` and `:`, no whitespace, and non-ASCII characters written
as themselves. Both are stated as `sha256:` followed by 64 lower-case hex digits.

**`need_digest`** identifies the words. It covers exactly:

```
{"instance": <instance>, "kind": "wazis.need", "need_id": <need_id>, "schema": 1, "text": <text>}
```

**`document_digest`** shows the document is intact. It covers every key of the
document except `document_digest` itself.

## Normalisation

- **`instance`**: lower case; no trailing slash; the scheme's own port (`80` for
  `http`, `443` for `https`) removed. `http` or `https`, an ASCII host, and
  optionally a port. Nothing else.
- **`text`**: Unicode normalisation form C; then CRLF and lone CR become LF; then
  leading and trailing whitespace removed. Nothing inside the text is changed.

WAZIS stores the words as they were sent, which from a browser means CRLF line
endings. The document always carries the normalised form.

## Versions

A change to any key, any meaning or either digest is a new contract number and a
new fixture file. Contract 1 is never changed in place: a WAZIS test compares the
committed fixtures with what the code produces, byte for byte.

A reader must refuse a `contract` number it does not know. It must not guess.
