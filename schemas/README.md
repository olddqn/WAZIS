# schemas/ — JSON スキーマ（仕様成果物）

WAZIS のコアオブジェクトの JSON スキーマを置く場所。**単一の正（source of truth）は [WAZIS_SPEC.md](../docs/history/WAZIS_SPEC.md) の §1** であり、ここはそれを機械可読な形へ抽出したもの。

> スキーマは仕様成果物であってコードではない。M0 では SPEC.md のインラインスキーマを正とし、ドリフトを避けるため `.json` ファイルの切り出しは **Phase M1**（最初の実運用）に行う。

## 予定するスキーマ（SPEC.md §1 に対応）

| ファイル（M1 で追加） | 対応 | SPEC |
|---|---|---|
| `question.schema.json` | Question（問い） | §1.1 |
| `discussion-entry.schema.json` | Discussion Entry（討議エントリ） | §1.2 |
| `implementation-candidate.schema.json` | Implementation Candidate（実装候補） | §1.4 |
| `reality-feedback.schema.json` | Reality Feedback（現実フィードバック） | §1.5 |

（Refinement は Question の版更新として表現されるため独立スキーマを持たない。SPEC §1.3。）

## 原則

- スキーマは**想いを表すフィールドを持たない**。強度・優先度・熱量のスコアを定義しない（憲法 第3条）。
- スキーマに**投票/ランキング**のフィールドを追加しない（第1条）。
- 変更は必ず SPEC.md と同期する。SPEC とスキーマが食い違う場合、SPEC が優先。
