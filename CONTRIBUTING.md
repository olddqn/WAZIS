# CONTRIBUTING to WAZIS

WAZIS への貢献は、まず**討議**であり、コードではない（コードは Phase M1 以降）。問いを開くこと・洗練すること・異議を述べること・実装候補を起草すること・Reality Feedback を返すこと——これらすべてが一級の貢献である。

## 参加の前提

1. [WAZIS_CONSTITUTION.md](WAZIS_CONSTITUTION.md) を読む。唯一の法は **dignity（他者の尊厳を侵さない）**。
2. **不可侵条項**（同意・異議・撤回・尊厳）を守る。これらを損なう提案は、たとえ効率的でも受け入れない。
3. WAZIS は **正解を決めない・多数決をしない・想いを測らない**。これに反する仕組み（投票・スコア・ランキング・熱量推定）は提案しない。

## 貢献の流れ（Phase 対応）

| したいこと | 方法 | Phase |
|---|---|---|
| 問いを開く | `Question` Issue を作成 | 0 |
| 討議する | Issue にコメント（視座・counter-question・**objection**・need/proposal framing） | 1 |
| 問いを洗練する | `refinement` ラベルのコメント / Question 版更新の PR | 2 |
| 実装候補を起草する | `Implementation Candidate` Issue + `candidates/` への PR | 3 |
| 実装先へ渡す | Binding に従い handoff、**同意を明示記録** | 4 |
| 現実を返す | `Reality Feedback` Issue + `feedback/` への PR | 5 |
| 新しい Binding を提案する | `bindings/_template/BINDING.md` を複製して PR | — |

## 異議（Objection）の扱い

- 異議は **append-only**。既存の異議を削除・上書きする PR は受け付けない。
- 異議者は自分の異議を**撤回**できる（撤回の事実は残る）。
- 異議は「閉じかけた問いを再び開く」正当な参加である（憲法 第5条・第9条）。

## レビューの評価軸

定義の整合性そのものではなく、**「この貢献で、現実に誰かが助かる方向へ近づくか」**で評価する。優先する問い: 誰を助けるか / 誰が取り残されるか / どの Reality Feedback で反証されるか / 不可侵条項を損なわず改善できるか。

## ライセンス

貢献は [LICENSE](LICENSE)（Apache-2.0）の下で提供されたものとみなす。散文への貢献は追加で CC BY 4.0 でも利用されうる（README の License 参照）。

## まだやらないこと

- 実装コード（Phase M1 まで凍結）。
- 投票・ランキング・想いの測定機構。
- 単一実装先への密結合。
