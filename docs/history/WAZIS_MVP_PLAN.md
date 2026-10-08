# WAZIS MVP 計画 / WAZIS MVP Plan

**WAZIS — 和智達（ワチス）** / Wisdom Action Zone for Implementation in Society

- Version: 0.1.0-draft
- Status: Open for deliberation（討議に開かれている）
- Date: 2026-06-21
- 上位文書: [WAZIS_CONSTITUTION.md](../../WAZIS_CONSTITUTION.md) / [WAZIS_SPEC.md](WAZIS_SPEC.md)

> 本計画は構築の順序を定める。**まだコードは書かない。** この計画自体が仮説であり、最初の一周（First Closed Loop）で得る Reality Feedback によって修正される。

---

## 0. MVP の目的

WAZIS の MVP が証明すべきは、機能の豊富さではなく、**ループが一周回ること**である。

> 一つの問いが、討議で洗練され、Implementation Candidate になり、外部（初期は Dan-Go）で実装され、Reality Feedback を返し、新しい問いを生む——この一周を、一度、本物で成立させる。

Dan-Go の「Time to First Rescue（TTFR）」に対応する WAZIS の最上位指標を、本計画は **TTFCL — Time to First Closed Loop** と置く:

> **TTFCL = 最初の問いが開かれてから、その問いに由来する Reality Feedback が WAZIS に戻り、最初の New Question を生むまでの時間。**

文書を増やすこと・機能を増やすことは TTFCL に従属する。TTFCL に貢献しない構築は、当面凍結する（Dan-Go の文書モラトリアムと同じ規律）。

---

## 1. 設計原則（MVP に効くもの）

1. **ループに必要な最小しか作らない。** プラットフォーム・UI・スケールは後。
2. **手作業で成立するものは手作業で。** Question = ファイル、Discussion = コメント/PR、Refinement = 版更新、Implementation Candidate = 構造化ファイル。自動化は後。
3. **投票・ランキング・想いの測定を一切作らない**（憲法 第1条・第3条）。MVP で「うっかり」これらを作らないことが最大の品質基準。
4. **Dan-Go Binding を最初の一つとして作り、二つ目の Binding で実装中立性を証明する。** 一つだけでは WAZIS が Dan-Go の付属物でないことを示せない。
5. **不可侵条項（同意・異議・撤回・尊厳）を MVP の最初から組み込む。** 後付けにしない。

---

## 2. マイルストーン

### M0 — 仕様（本納品物） ✅ 進行中
- `WAZIS_CONSTITUTION.md` / `WAZIS_SPEC.md` / `WAZIS_MVP_PLAN.md`。
- コードなし。3 文書の内部整合と Dan-Go 原理との非矛盾を確認する。
- **完了条件:** 憲法・仕様・計画が相互参照で一貫し、不可侵条項と実装中立性が全体に貫かれている。

### M1 — 単一 Binding ループ（Dan-Go のみ・手作業）
- Question を 1 件、本物の関心から開く（§5 の最初の実験）。
- Forum を最小実装: Question / Discussion Entry をファイル（JSON/Markdown）として置き、版管理で append-only・撤回・objection 保存を満たす。git の追記性で代替してよい。
- 洗練を経て **Implementation Candidate を 1 件** 起草。`not_yet_decided` を必ず埋める。
- **Dan-Go Binding を手作業で適用**: Implementation Candidate → Dan-Go Claim(JSON) を生成し、`dango-mujin` へ Claim として提出（PR/issue）。同意（handoff consent）を明示記録。
- **完了条件:** Dan-Go 側で受理可能な Claim が、WAZIS の Candidate から無損失で生成され、handoff が同意付きで記録された。

### M2 — Reality Feedback 受領とループ閉鎖
- Dan-Go 側の Reality Feedback（executed/partial/failed/pending）を、Binding の reverse で WAZIS の Reality Feedback オブジェクトとして受領・記録。
- そこから **New Question を 1 件** 開く（`spawned_questions`）。
- **完了条件:** **最初の一周（First Closed Loop）が成立** = TTFCL を一度計測できた。ここが MVP の核。

### M3 — 二つ目の Binding（実装中立性の証明）
- NPO / OSS のいずれか一つで、同じ Implementation Candidate インターフェースから別の実装先へ handoff できることを示す（写像 1 本でよい）。
- Dan-Go 固有の前提が WAZIS の中核に漏れていないことを、この差し替えで検証する。
- **完了条件:** Dan-Go 以外の実装先へ、同じ Candidate 構造から handoff が成立した。

### M4 — 多人数討議のハードニング
- 同意・撤回・objection の機構を多人数で運用に耐える形にする。
- アイデンティティ（DID / pseudonym）、限定公開の同意二段階、Forum の公開監査性を固める。
- **完了条件:** 複数参加者が、不可侵条項を損なわずに一つの問いを洗練し handoff できる。

> M0→M2 が「証明」、M3 が「中立性の証明」、M4 が「運用化」。M3 より前に UI やスケールへ進まない。

---

## 3. MVP が**作らない**もの（明示的 Non-goals）

- 投票・ランキング・スコアボード・「ベストアンサー」表示。
- 想いの強度推定・感情分析・優先度の自動付け。
- 自動実装・自動 handoff（同意を飛ばす自動化）。
- 凝った UI、リアルタイム機能、スケール最適化。
- AI による問いの優劣判定・収束の強制。
- Dan-Go への密結合（WAZIS が Dan-Go なしには動かない設計）。

---

## 4. 基盤（substrate）の選択 — 未決定（要判断）

WAZIS をどの土台に置くかは M1 までに決める。実装中立性を壊さないことが条件。候補:

| 候補 | 長所 | 懸念 |
|---|---|---|
| **gitlawb**（現在の作業ディレクトリ。federated git + DID + UCAN + bounty/PR） | DID アイデンティティ・追記性・PR ベース討議・federation が「公開・監査可能・撤回尊重・pseudonymous」と自然に対応 | WAZIS を特定基盤に welding しないよう、Binding と同様に基盤も抽象化が要る |
| **dango-mujin の git + ファイル方式** | Dan-Go と同じ運用知見を流用できる。Claim Binding が近い | Dan-Go との独立性が外形上あいまいに見えるリスク（憲法 上は独立） |
| **スタンドアロン（最小 git リポジトリ）** | 依存最小・独立性が明確 | アイデンティティ/同意機構を一から用意する手間 |

**推奨（暫定）:** M1〜M2 は最も独立性が明確な**スタンドアロンな git リポジトリ**で手作業ループを回し、基盤機能（DID・federation）が必要になった M3〜M4 で gitlawb への載せ替えを検討する。これにより「WAZIS は基盤に依存しない」ことを構造で示せる。

> これは判断を要する論点。ユーザー確認の上で確定する（本計画は提案）。

---

## 5. 最初の実験（First Concrete Experiment）

MVP は抽象論で止めない。**本物の問いを 1 件**選び、M1→M2 を通す。条件:

- 想いから生まれた、当事者にとって現実の問いであること。
- 尊厳を侵さず、強制を要しないこと（`dignity_check` を通る）。
- Dan-Go で受理可能な Claim へ翻訳できる見込みがあること（Dan-Go の `FIRST_CASE_CANDIDATES.md` / `FIRST_REAL_CASE_PROTOCOL.md` と整合させてよい）。
- `not_yet_decided` が自然に書ける = WAZIS が裁定しない余地が残ること。

最初の一件は「**助かる方向へ一歩でも近づくか**」だけで選ぶ。理論的な美しさでは選ばない（救済主軸）。

---

## 6. リスクと失敗様式

| 失敗様式 | 兆候 | 防ぎ方 |
|---|---|---|
| **無害なまま誰も助けない** | 文書と討議は増えるが Implementation Candidate が外へ出ない | TTFCL を唯一の北極星にする。一周するまで機能凍結 |
| **想いの測定への滑落** | 「良い問い」スコア・優先度・熱量指標が登場 | 第3条をレビュー必須項目に。スコア的構造の追加を即時 reject |
| **裁定への滑落** | 多数決・ベストアンサー・AI 判定が忍び込む | `not_yet_decided` 必須・mode に投票を作らない |
| **Dan-Go 付属物化** | WAZIS が Dan-Go なしに動かない / Dan-Go の都合で問いが歪む | M3 の二つ目 Binding を中立性の試金石にする |
| **権力化** | 特定ノード/実装先/想いの優遇が固定化 | trust はゲートでなく情報（仕様 §6）。collapse シナリオを定期レビュー |
| **不可侵条項の摩耗** | 同意の暗黙化・撤回の困難化・objection の埋没 | M1 から組み込み、後付けにしない |

---

## 7. 進め方（当面）

1. **M0 を確定**（本 3 文書のレビューと合意）。
2. 基盤を判断（§4）。
3. 最初の問いを 1 件選ぶ（§5）。
4. M1→M2 を手作業で回し、**TTFCL を一度計測**する。
5. その Reality Feedback で本計画・仕様・憲法を見直す（すべて仮説）。

実装はこの順で、ユーザーの合意を得てから着手する。**本納品（M0）の時点ではコードを書かない。**

---

*本計画は構築の順序であり、実装ではない。最上位指標は TTFCL（最初の一周までの時間）。憲法・仕様に従属し、不可侵条項と実装中立性を損なう近道は取らない。*
