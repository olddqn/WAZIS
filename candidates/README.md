# candidates/ — Implementation Candidate（実装候補）記録

WAZIS と外部実装先の**境界物**の記録。洗練された問いが、外部へ渡せる形になったもの。

## 性質

- 特定の実装先に**事前コミットしない**（実装中立）。
- WAZIS は実装しない。ここにあるのは「渡せる形」であって実装そのものではない。
- `not_yet_decided` を**必ず**含む。これが「WAZIS は正解を決めない」の構造的保証（憲法 第1条）。空にして「すべて解決済み」と装ってはならない。

## ファイル

```
candidates/ic-{topic}-{seq}.md   または   .json
```

スキーマは [WAZIS_SPEC.md](../docs/history/WAZIS_SPEC.md) §1.4 / [schemas/](../schemas/) を正とする。必須: `candidate_id`, `origin_question_id`(トレーサビリティ), `summary`, `problem_framing`, `what_would_change`, `open_constraints`, `not_yet_decided`, `candidate_implementers`, `consent_status`, `dignity_check`, `maturity`。

## 外部へ渡す（handoff）

実装先へは [bindings/](../bindings/) の Implementation Binding を通して渡す。handoff には**当事者の同意が必須**（`consent_status.handoff_consented_by`）。最初の具体 Binding は [bindings/dan-go/BINDING.md](../bindings/dan-go/BINDING.md)（Candidate → Dan-Go Claim）。

`maturity` は討議成果物の**引き渡し準備度**であって、問いや想いの優劣スコアではない。

> Phase M1 で最初の 1 件を起草し、M2 で Reality Feedback を得てループを閉じる。
