# Binding: Dan-Go（具体 Binding #1・参照実装）

- target: `dan_go`
- status: **仕様のみ（M0）**。写像は確定。runtime は M1 で手作業から開始。
- 相手側 canonical: Dan-Go `CLAIM_FORMAT.md` / `MUJIN_PROTOCOL.md`（Phase 0–4）

Implementation Candidate を Dan-Go の **Claim** へ写し、Dan-Go の **Reality Feedback** を WAZIS へ戻す。WAZIS と Dan-Go の唯一の法はともに **dignity** のため、尊厳チェックは無損失で対応する。

## map(candidate) → Dan-Go Claim

| WAZIS Implementation Candidate | Dan-Go Claim |
|---|---|
| `summary` | `statement` |
| `problem_framing[]`（検証可能な事実のみ） | `observed_state[]` |
| `what_would_change[]` | `required_state[]` ＋ desired（方向） |
| `problem_framing` と `what_would_change` の差 | `missing_conditions[]` |
| `open_constraints[]`（手段以外の制約） | `risks[]` |
| `dignity_check`（`violates_dignity` / `uses_coercion`） | `constitution_check` |
| —（Question 由来のため初期は） | `claim_type` = **interrogative** |
| `candidate_id` / `origin_question_id` | `claim_id` のメタに保持（トレーサビリティ） |
| `candidate_implementers` に `dan_go` を含むこと | handoff の前提 |

**転写しない:** `not_yet_decided`。WAZIS が裁定しなかった点は Dan-Go 側の Negotiation で当事者が決める（invariant 4）。WAZIS が代わりに決めない。

## consent（必須）

- `candidate.consent_status.handoff_consented_by` を確認してからのみ Claim を生成・提出する。
- 同意は撤回可能（`withdrawable: true`）。撤回された場合、未実行なら handoff を取り下げる。

## feedback_channel

- Dan-Go 側で Claim が辿る Phase 1–4（Negotiation → Contribution → Execution → Reality Feedback）。
- WAZIS は Dan-Go の `sutable/reality_feedback`（Phase 4）を購読/参照して受領する。

## reverse(feedback) → WAZIS Reality Feedback

| Dan-Go Reality Feedback | WAZIS Reality Feedback |
|---|---|
| `executed` / `partial` / `failed` / `pending` | `outcome`（同一語彙） |
| feedback 本文 | `observation` |
| Phase 4 の観測（誰が助かったか） | `who_was_helped`（任意） |
| Claim id | `implementer` = `dan_go:claim-xxxx` |

戻った Reality Feedback は `feedback/` に記録し、`spawned_questions` から **New Question** を開きうる（ループ閉鎖・TTFCL）。

## invariants 適合

- (1) consent: 上記 consent 節で確認。
- (2) dignity: WAZIS 第10条 = Dan-Go Article 10。`dignity_check` ↔ `constitution_check` 無損失。
- (3) 無歪曲: Dan-Go の trust/negotiation 都合を Candidate へ遡及させない。
- (4) 無裁定の保存: `not_yet_decided` 非転写。
- (5) トレーサビリティ: `candidate_id` / `origin_question_id` をメタ保持。
- (6) 同語彙: outcome は executed/partial/failed/pending。

## 既知の未解決点

- WAZIS が Dan-Go の Reality Feedback を受領する具体経路（購読 vs 手動参照）は M1 で確定。
- Dan-Go 側の `claim_id` 採番と WAZIS 側 `candidate_id` の対応表の保持場所。

> M0 では本写像の妥当性を机上確認するに留める。実提出は M1（手作業）から。
