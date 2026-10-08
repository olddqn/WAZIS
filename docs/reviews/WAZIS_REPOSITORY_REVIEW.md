# WAZIS リポジトリ・レビュー / Repository Review

- Date: 2026-06-22
- Scope: リポジトリルート（WAZIS repo, Phase M0）全 23 ファイル
- 種別: **レビューのみ**。コード・リファクタリング・実装を含まない。
- 評価軸: 定義整合性そのものでなく**救済能力**を主軸（誰が助かるか／取り残されるか／何で反証されるか）。不可侵条項を損なう改善は失敗として扱う。
- 上位文書: [WAZIS_CONSTITUTION.md](../../WAZIS_CONSTITUTION.md) / [WAZIS_SPEC.md](../history/WAZIS_SPEC.md) / [WAZIS_MVP_PLAN.md](../history/WAZIS_MVP_PLAN.md)

> 結論先出し: 構造は健全で、不可侵条項と非測定は全層に一貫している。**ただし2点が実質的に弱い** — (criterion 7) Issue #1 がメタ問いで、それ自体は一周（TTFCL）を駆動できない。(criterion 5/6) 中立性は設計上は担保されているが、Dan-Go への**事実上の依存**が最初のループに残り、二つ目の Binding が出るまで中立性は「主張」のまま未反証である。

---

## 1. 7 基準の判定

| # | 基準 | 判定 | 要点 |
|---|---|---|---|
| 1 | README が現 Constitution / Spec を正確に反映 | ✅ PASS | ループ図・「する/しない」表・不可侵条項・TTFCL すべて整合。軽微な瑕疵2件（下記 R5・R7） |
| 2 | LICENSE が統治モデルと整合 | ⚠️ PASS（要補正） | Apache-2.0 は中立採用・fork 容認と整合。ただし**二重ライセンス主張が裏付け不在**（R5） |
| 3 | Binding 文書が内部整合 | ✅ PASS | 6 invariants が README / dan-go / _template で一致。写像表が SPEC §5.2 と一致 |
| 4 | Issue テンプレートが Constitution に従う | ✅ PASS | dignity_check・同意・撤回・無投票・非測定を全テンプレートが内蔵。軽微（R8） |
| 5 | どのファイルも Dan-Go を暗黙に必須化していない | ⚠️ CONCERN | プロトコル上は非必須。だが **Issue #1 + M1 が最初のループで Dan-Go を事実上必須化**（R2） |
| 6 | WAZIS は実装中立を保つ | ⚠️ PASS（未反証） | 設計上は中立。具体 Binding が Dan-Go のみで、**中立性は M3 まで主張に留まる**（R2） |
| 7 | Issue #1 が最初の TTFCL 取得に適する | ❌ CONCERN | **Issue #1 はメタ問い。それ自体は外部実装→Reality Feedback を生まない**ため TTFCL を駆動しない（R1） |

判定凡例: ✅ PASS / ⚠️ 留意付き合格 / ❌ 要再設計。

---

## 2. Strengths（強み）

- **S1. 不可侵条項が全層を貫通している。** 同意・異議・撤回・尊厳が Constitution 第5条 → README → CODE_OF_CONDUCT → CONTRIBUTING → 4 つの Issue テンプレート → PR テンプレートまで、欠落なく反復される。append-only の objection、ペナルティなき撤回が各所で明示。自己修正可能性の条件が一箇所の宣言で終わらず**手続きに落ちている**。
- **S2. 非測定が構造で担保されている。** 「想いを測らない」が標語に留まらず、(a) スキーマにスコア欄を持たせない（schemas/README）、(b) Question テンプレートが background から内心強度を推定することを禁止、(c) entry_category を「強さの分類でない」と明記、で**フィールドの不在として**実装されている。後から測定機構を足しにくい設計。
- **S3. 無裁定が構造で担保されている。** `not_yet_decided` を Implementation Candidate の**必須**項目にし、Binding invariant (4) で「実装先へ転写しない」と定めた。「正解を決めない」が運用上骨抜きになりにくい。
- **S4. 中立性が抽象インターフェースとして表現されている。** `bindings/_template/BINDING.md` と 6 invariants により、Dan-Go は「最初の一つのプラグイン」として明確に相対化されている。`candidate_implementers` も複数選択。中核が Binding に非依存である旨が README/SPEC で一貫。
- **S5. 失敗様式を名指している。** 「無害なまま誰も助けない」を権力化と並ぶ失敗として TTFCL とともに掲げ、討議の自己目的化に歯止めをかけている（救済主軸と一致）。
- **S6. 上流/実装の分離が崩れていない。** 「WAZIS は実装しない」（第7条）が README・SPEC・各 README で保たれ、Dan-Go との層分担（Question 手前 vs Claim 以降）が首尾一貫。dignity が両者同一のため Binding が無損失。

---

## 3. Risks（リスク）

深刻度: 🔴 高 / 🟠 中 / 🟡 低。

### 🔴 R1 — Issue #1 がメタ問いで、TTFCL を駆動しない（criterion 7）
[docs/genesis-issue-1.md](../history/genesis-issue-1.md) の問いは「最初に一周させるべき現実の問いは何か」という**選定についての問い**である。これは外部（Dan-Go）で実装され Reality Feedback を返す対象に**なり得ない**（「どの問いを選ぶか」は Dan-Go の Claim として実行→救済に結びつかない）。
- 帰結: TTFCL を得るには、Issue #1 がまず別の**具体的な現実の問い**を生み、その問いが一周する必要がある。**一段の間接が最初のループの前に挟まる。**
- 救済軸での評価: 「誰かが助かるまでの時間」を縮める指標 TTFCL に対し、Issue #1 は時間を**伸ばす**側に働く。genesis 自身が open_threads で「WAZIS 自身についての問いでよいのか」と自覚しているが、自覚は緩和ではない。これは「無害なまま誰も助けない」（S5 が警戒する失敗様式）の入口になりうる。

### 🟠 R2 — 最初のループで Dan-Go が事実上必須（criterion 5/6）
プロトコル上は非必須だが、次の3点が**事実上の依存**を作る:
1. [docs/genesis-issue-1.md:36](../history/genesis-issue-1.md) が最初の一件の選定条件に「**Dan-Go で受理可能な Claim へ翻訳できる見込み**」を入れている。これは最初の問いを Dan-Go 適合性で**フィルタ**する＝中立でない選別。
2. 具体 Binding が Dan-Go のみ。他は雛形のみ。中立性は M3（二つ目の Binding）まで**反証不能の主張**。
3. Reality Feedback の語彙 `executed/partial/failed/pending` は Dan-Go/Mujin 由来。SPEC は「同語彙で整合」とするが、非 Dan-Go 実装先でこの4状態が自然かは未検証（reverse() の正規化責務に押し付けられている）。
- 帰結: 「Dan-Go は便宜であって優先でない」という宣言（README:40）と、運用の最初の一歩が衝突する。宣言が**運用で裏切られる**リスク。MVP M3 が緩和策だが、M1/M2 の時点では中立性は紙の上にある。

### 🟠 R3 — 「多数決なしの収束」手続きが未定義
Issue #1 自身が open_threads で「候補が複数集まったとき多数決を使わずどう一件へ収束するか」を未解決と認めている。これは**最初の実運用の最初の動作**（一件への収束）に**手続きが無い**ことを意味する。
- 帰結: (a) 収束せず停滞（TTFCL 未達）、または (b) 誰かが事実上の裁定者になり「無裁定」「no-governor」を侵す。R4 と連動。

### 🟠 R4 — CoC の「場から外れる」に執行主体・手続きが無い
[CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md) は「第10条を侵し続ける参加は WAZIS の場から外れる」とするが、**誰が・どう**決めるかが無い。WAZIS は意図的に governor を持たない（SPEC §4「AI は governor でない」、no-verdict）。
- 帰結: 排除の権限が宙に浮く。権限を誰かに与えれば no-governor と衝突、与えなければ CoC が執行不能の宣言に留まる。尊厳保護（不可侵）と無権力（中立）の**未解決の緊張**。

### 🟡 R5 — 二重ライセンス主張が裏付け不在
[README.md:137](../../README.md) は `SPDX: Apache-2.0 AND CC-BY-4.0` を主張するが、(a) CC-BY のライセンス本文/ファイルが無い、(b) README 冒頭の SPDX ヘッダは `Apache-2.0` のみ（README.md:1）、(c) 散文ファイル（CONSTITUTION/SPEC 等）に per-file SPDX が無い。
- 帰結: 「仕様を論文・政策文書へ引用しやすく」という二重ライセンスの目的（中立採用に資する）が、法的に曖昧なまま。引用者が CC-BY 適用を確信できない。

### 🟡 R6 — permissive license は不可侵条項を fork へ伝播しない
Apache-2.0 は閉じた/改変 fork を許す。fork が Constitution と不可侵条項を**剥ぎ取る**ことを license は妨げない。
- 評価: これは Dan-Go の姿勢（規範は license でなく社会契約・透明性で担保）と**整合的**であり、欠陥ではない。ただし README/Constitution に「不可侵条項は license でなく社会契約として効く（fork には伝播しない）」と**明示が無い**ため、読者が license が規範を守ると誤解しうる。明示が要る（criterion 2）。

### 🟡 R7 — README の Dan-Go リンクがプレースホルダ
[README.md:119](../../README.md) の `[Dan-Go](https://github.com/)` は空 URL。公開時に実 URL へ。

### 🟡 R8 — 公開前プレースホルダ・軽微な中立性の見た目
- `.github/ISSUE_TEMPLATE/config.yml` の `OWNER/wazis` は要置換（公開ブロッカー）。
- `03-implementation-candidate.md` の `candidate_implementers` チェックリストが **dan_go を先頭**に置く。既定チェックではないが、順序が微かな優先印象を与える。アルファベット順か無作為順が無難。
- リポジトリは未 `git init`（ファイルとしては存在するが版管理史が無い）。「repository」としては未確定。

---

## 4. Missing pieces（欠落）

| # | 欠落 | なぜ要るか | 深刻度 |
|---|---|---|---|
| M-a | **具体的な最初の現実 Question**（Issue #1 と別 or 統合） | TTFCL は具体問いでしか計測できない（R1） | 🔴 |
| M-b | **同意ベースの収束手続き**（投票なしで一件へ） | 最初の動作に手続きが無い（R3）。no-governor と両立する設計が要る | 🟠 |
| M-c | **執行/離脱の手続き** または「離脱権限は存在しない」の明言 | CoC の宙吊りを解消（R4） | 🟠 |
| M-d | `examples/`（Question / Candidate / Reality Feedback の記入例） | M1 の手作業を de-risk。Dan-Go も examples/ を持つ | 🟠 |
| M-e | **二つ目の Binding 雛形（skeletal npo/ or oss/）** | 中立性を M3 を待たず**反証可能**にする（R2） | 🟠 |
| M-f | CC-BY ライセンス本文 + per-file SPDX、または二重主張の撤回 | 二重ライセンスの法的裏付け（R5） | 🟡 |
| M-g | 「不可侵条項は license でなく社会契約」明記 | 規範の効き方の誤解防止（R6） | 🟡 |
| M-h | **Issue ↔ `questions/*.md` の同期手続き・責任者** | live 討議と永続記録の往復が未定義（誰がいつ写すか） | 🟡 |
| M-i | SECURITY.md（公開リポジトリ衛生） | 報告経路の明示。標準的 | 🟡 |
| M-j | 実 JSON スキーマ（`schemas/*.json`） | M1 で SPEC から切り出す予定として記録済み。許容 | 🟡（既知） |

---

## 5. Recommended next milestone（推奨する次のマイルストーン）

**機能を作らない。最初のループを「実際に到達可能」にし、中立性を「反証可能」にする。** これを暫定 **M0.5 — "First-Loop Readiness"** と呼ぶ。M1 着手の前提条件であり、実装は含まない。

### M0.5 の完了条件（すべて文書/手続きのみ）

1. **Issue #1 を作り直す or 補完する（R1・M-a／最優先）。**
   メタ問いを残すなら、**それと同時に具体的な現実 Question を 1 件**開き、TTFCL の計測対象を最初から具体問いに固定する。推奨は後者: Issue #1 自体を「救済方向へ一歩進む具体的な現実の問い」にし、選定の議論は付随スレッドに降格する。**TTFCL を伸ばす間接を除く。**
2. **同意ベースの収束手続きを定義する（R3・M-b）。** 多数決でも単独裁定でもない収束（例: 一定期間 objection が解消されたら当事者が candidate へ進められる、を SPEC の収束規律として明文化）。no-governor と両立させる。
3. **CoC の執行を解決する（R4・M-c）。** 「離脱を強制する権限は存在しない。objection と非協力のみが手段」と明言するか、最小限の手続きを置く。どちらでも可だが**宙吊りを終わらせる**。
4. **中立性を反証可能にする（R2・M-e）。** 二つ目の Binding の skeletal 雛形（oss/ か npo/）を 1 つ置き、genesis の選定条件から「Dan-Go 受理可能性」フィルタを外すか相対化する。
5. **公開ブロッカーを潰す（R5・R7・R8・M-f/M-g）。** `git init` → `OWNER` と Dan-Go URL を実値化 → 二重ライセンスを確定（CC-BY 本文を置くか、主張を撤回）→ 不可侵条項の効き方（社会契約）を README に一文。
6. **`examples/` を 1 セット置く（M-d）。** 記入例があれば M1 の最初の一件が滑り出す。

### M0.5 の後

M0.5 が終われば、当初計画通り **M1（Dan-Go Binding・手作業ループ）→ M2（Reality Feedback → New Question = 最初の TTFCL 計測）→ M3（二つ目の Binding で中立性を反証）** へ進める。M0.5 はその M1 を「空回りしないループ」にするための整地である。

> 一文で: **「まず一周を実際に回せる状態にする（具体 Question・収束手続き・第二 Binding 雛形・公開整地）。それまで新機能は凍結。」** ——これは救済主軸（TTFCL を縮める方向）と完全に一致する。

---

*本書はレビューであり、実装・リファクタリングを含まない。判定はすべて現ファイル（M0, 23 ファイル）に基づく仮説であり、最初の Reality Feedback で更新される。指摘のうち R1・R2・R7 が TTFCL に直結する。*
