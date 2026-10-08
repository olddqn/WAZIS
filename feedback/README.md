# feedback/ — Reality Feedback（現実フィードバック）記録

外部実装先から戻った観測の記録。WAZIS が**生成する**のではなく、実装先から**受け取って記録する**。

## 性質

- 問いを「解決済み」として最終的に閉じない。`spawned_questions` を通じて**新しい問い**を開きうる（憲法 第8条）。reopen は失敗ではない。
- `outcome` は Dan-Go の Reality Feedback と**同じ語彙**（`executed` / `partial` / `failed` / `pending`）を使い、Binding 越しに整合させる。

## ファイル

```
feedback/rf-{candidate}-{seq}.md   または   .json
```

スキーマは [WAZIS_SPEC.md](../docs/history/WAZIS_SPEC.md) §1.5 / [schemas/](../schemas/) を正とする。必須: `feedback_id`, `candidate_id`, `implementer`, `outcome`, `observation`, `reported_by`。任意: `who_was_helped`, `spawned_questions`。

## ループの閉鎖と TTFCL

最初の Reality Feedback が戻り、そこから最初の **New Question** が開いた時点で、WAZIS の最初の一周（First Closed Loop）が成立する。これが最上位指標 **TTFCL**（[WAZIS_MVP_PLAN.md](../docs/history/WAZIS_MVP_PLAN.md) §0）の計測点。

```
candidate → External Implementation → Reality Feedback（ここ）→ New Question → questions/
```

> 未観測を断定しないこと。観測は実装先からの独立観測として記録する。
