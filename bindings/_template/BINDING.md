# Binding: <TARGET_NAME>（雛形）

<!-- このファイルを bindings/<target>/BINDING.md に複製し、< > を埋めてください。
     コードは不要。これは写像と規律の「仕様」です（runtime は M1 以降）。 -->

- target: `<target_id>`  <!-- 例: npo / company / research / oss / municipality / other -->
- status: `<draft | spec-complete | runtime>`
- 相手側 canonical: `<実装先の受け入れ形式の出典>`

一行説明: Implementation Candidate を `<実装先の受け入れ形式>` へ写し、`<実装先の結果>` を WAZIS の Reality Feedback へ戻す。

## map(candidate) → <実装先の受け入れ形式>

| WAZIS Implementation Candidate | <実装先> |
|---|---|
| `summary` | `<...>` |
| `problem_framing[]` | `<...>` |
| `what_would_change[]` | `<...>` |
| `open_constraints[]` | `<...>` |
| `dignity_check` | `<実装先の尊厳/倫理規律>` |
| `candidate_id` / `origin_question_id` | `<メタに保持>` |

**転写しない:** `not_yet_decided`（invariant 4）。

## consent（必須）
- `candidate.consent_status.handoff_consented_by` を確認後のみ handoff。撤回可能。

## feedback_channel
- `<Reality Feedback を受け取る経路>`

## reverse(feedback) → WAZIS Reality Feedback

| <実装先の結果> | WAZIS Reality Feedback |
|---|---|
| `<...>` | `outcome`（executed/partial/failed/pending に正規化） |
| `<...>` | `observation` |
| `<...>` | `implementer` = `<target>:<id>` |

## invariants 適合（[../README.md](../README.md) の6項目を満たすことを明記）
- (1) consent / (2) dignity 非矛盾 / (3) 無歪曲 / (4) 無裁定の保存 / (5) トレーサビリティ / (6) 同語彙

## 既知の未解決点
- `<...>`

## 複数 Binding との関係
- 同じ Candidate を他 Binding も引き取る場合の Reality Feedback 統合方針: `<...>`
