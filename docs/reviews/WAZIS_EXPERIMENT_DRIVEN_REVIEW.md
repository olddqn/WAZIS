# WAZIS Experiment-Driven Review / 実験駆動レビュー

- Date: 2026-06-22
- Scope: ユーザーの「Course Correction（実験駆動への補正）」を受けた WAZIS の再評価
- 種別: **レビューのみ**。実装・コード・リファクタリングを含まない。
- 上位文書: [WAZIS_CONSTITUTION.md](../../WAZIS_CONSTITUTION.md) / [WAZIS_SPEC.md](../history/WAZIS_SPEC.md) / 前レビュー [WAZIS_REPOSITORY_REVIEW.md](WAZIS_REPOSITORY_REVIEW.md)

> **一行結論:** 補正は正しい。WAZIS は**合意生成系ではなく実験生成系**である。重要なのは——憲法は**最初から実験駆動**（第1条: 裁定も多数決もしない／第8条: 現実が問いを再び開く／第9条: fork は正当）であり、**「収束」を密輸したのは SPEC と前レビューの方**だった（[WAZIS_SPEC.md:113](../history/WAZIS_SPEC.md)・[:196](../history/WAZIS_SPEC.md)・[:222](../history/WAZIS_SPEC.md)）。前レビューの R3「投票なしでどう収束するか」は、**収束が必要だという隠れた前提**に立っており、補正により**棄却**される。遷移条件は **Consensus ではなく Experimentability**。

---

## 0. 何が変わったか（補正の核）

| 旧（密輸された前提） | 新（補正後・憲法本来） |
|---|---|
| 討議は合意的に**収束**して Phase が進む | 討議は**収束しなくてよい**。Proposal A/B/C が並立したまま進める |
| 成果物は「洗練された一つの問い／候補」 | 成果物は**複数の Experiment Candidate**（結論ではない） |
| 討議が最終権威（どれが正しいか討議で決める） | **Reality Feedback が裁定者**。討議は決めない |
| 遷移条件＝合意（consensus） | 遷移条件＝**実験可能性（experimentability）** |
| ループは収束→実装→帰着 | ループは**fan-out**（1問い→多 Proposal→多実験→多 RF→多 New Question） |

この補正は SPEC の §1.3「**収束**はするが裁定はしない」・§2「当事者と Forum の**合意的な収束**で Phase が進む」・§4「**収束**は合意的・可逆的」を否定する。これらは憲法（第1条）と矛盾していた **SPEC 側のバグ**であり、補正はバグ修正である。

---

## 1. WAZIS は「実験生成系」か「合意生成系」か

**評価: 実験生成系（experiment-generation system）として理解する方が正しい。** 合意生成系という読みは誤り。

根拠:

- **憲法は既に実験駆動。** 第1条「正解を決めない・多数決をしない・ベストアンサーを選ばない」、第8条「現実が問いを再び開く」、第9条「fork は正当な参加」。これらは討議が真理を決める系では**ない**ことを宣言している。Proposal A/B/C の並立（＝fork）は第9条そのもの。
- **Dan-Go の核とも一致。** Claim は true/false でなく「提案された状態遷移」。Article 2「嘘とは未実現の状態遷移」＝真偽は討議で勝つものでなく現実で閉じる差異。method-agnosticism「助かるなら方法はなんでもいい」＝複数手段（A/B/C）を試し、現実に選ばせる。Voice Commons 理論の Science Commons（厳密実験プロファイル）＝Dan-Go ループ＝科学的方法。
- **権威の所在が移る。** 合意系では権威は**認識論的**（討議で誰が正しいか）。実験系では権威は**経験的**（現実が何を返すか）。WAZIS は後者。だから討議は「最終権威」ではなく「実験を生む工程」。
- **「失敗」の意味が変わる。** 実験系では、Reality Feedback が `failed` でも**WAZIS のループは成功**である（現実が語った＝学習が生じた）。成功＝「合意した」でも「うまくいった」でもなく、**「現実が一度語った」**。これは合意系では捉えられない。

**残る収束語（要削除・推奨§6）:** SPEC §1.3/§2/§4 の「収束」「合意的な収束」、§1.4 の `maturity: still_open | ready_for_handoff`（成熟＝一本化の含意）。これらが残ると、補正前の合意系の読みに引き戻される。

---

## 2. 収束（convergence）は本当に必要か

**評価: 必要ない。のみならず、収束を「要求」すると憲法違反を強いる。**

### 2.1 収束は前提でない
- Experiment Candidate は**並列に複数**発行できる。A も B も C も、それぞれ実験可能なら、それぞれ handoff される。互いに排他でない。
- 討議は**永遠に続いてよい**（補正の明言）。Reality Feedback は討議終了を**待たない**。RF が討議の最中に届き、RF 自体が New Question を生む。よって収束はどの遷移の前提でもない。
- 構造は **funnel（多→一）ではなく fan-out（一→多）**。1 つの Question が多 Proposal を生み、複数が Experiment Candidate になり、複数の Reality Feedback が返り、複数の New Question を開く。

### 2.2 収束を要求すると、憲法が禁じた手段を呼び込む
投票なしに討議を一本へ収束させる方法は3つしかなく、**すべて憲法違反**:
1. **多数決** → 第1条違反。
2. **裁定者（governor）が選ぶ** → no-governor（SPEC §4）違反。
3. **全会一致を待つ** → 最も頑固な objection が事実上の**拒否権＝独裁**になる。尊厳の平等（第3条）と「objection は再開であって veto でない」に反する。

→ つまり前レビュー R3「投票なしでどう収束するか」は、**答えのある問いではなく、問うべきでない問い**だった。収束は不要であり、要求すれば必ず上の3つのいずれかに堕ちる。**R3 は棄却する。**

### 2.3 残余（正直な留保）— 「選択」は消えず、場所が移る
収束は不要だが、**実装先の有限容量**は消えない。Dan-Go や NPO は無限の並列実験を走らせられない。では誰が「どの Experiment Candidate を実際に走らせるか」を選ぶか?
- **WAZIS は選ばない**（第7条「実装しない」＝「実装先の代わりに選ばない」）。WAZIS は実験可能な候補を**すべて**発行する。
- 容量の制約による選択は**実装先の自律**に属する（実装先が自分の資源で決める）。これは WAZIS の裁定ではない。
- 重要: この選択を WAZIS 側に戻して「優先度」「ランキング」を付け始めると、第3条（想い非測定）・第1条（無裁定）に違反する。**選択は実装先へ押し出したままにする**こと。

---

## 3. Discussion → Experiment Candidate の遷移条件

**評価: 遷移条件は Consensus ではなく Experimentability（実験可能性）。**

Proposal が Experiment Candidate になる条件は、討議の同意ではなく、次の4点:

1. **観測可能・反証可能（falsifiable/observable）** — 実行されたか（executed/partial/failed/pending）、誰が助かった/助からなかったかが**観測できる**こと。Reality Feedback を**生みうる**形であること。これが核。
2. **尊厳安全（dignity-safe）** — `dignity_check`（violates_dignity=false, uses_coercion=false）を通ること。**これが唯一の遮断条件**（§4 参照）。
3. **同意（consent）** — handoff への当事者同意（撤回可能）。実験が誰かに対して行われるなら、その人の同意が要る（不可侵条項）。
4. **接続可能（bindable）** — それを運べる Binding が1つ以上存在すること。

**要求しない:** それが最善だという合意／成功するという合意／merit についての objection の解消／A/B/C の一本化。

### 3.1 「最小の実験」が美徳
補正の Issue #1 示唆「**Reality Feedback を生む最小の現実実験は何か**」は正しい。小さい実験ほど:
- Reality Feedback が**速い** → 最初の現実応答までの時間が短い。
- 尊厳リスクが**低い**（小さく、可逆に近い）。
- **並列性**が高い（小実験を多数）。

### 3.2 指標の補正（推奨）: TTFCL → **TTFRF**
前レビューの **TTFCL（Time to First Closed Loop）** は「ループが一周」を見るが、補正後の核は「**現実が一度語ること**」。よって主指標は **TTFRF — Time to First Reality Feedback**:

> **TTFRF = 最初の Experiment Candidate が外部実装され、Reality Feedback が一度返るまでの時間。** outcome が `failed` でも達成とみなす（現実が語った）。

TTFRF は Dan-Go の TTFR（Time to First Rescue）に最も近い WAZIS 指標。TTFCL（New Question まで含む一周）は RF が自動で New Question を生むため TTFRF の自然な後続。**主は TTFRF、従は TTFCL。**

---

## 4. 実験駆動モデルにおける Objection の働き

**評価: Objection は二役に分かれる。鍵は「Objection は実験への veto ではない（dignity を除く）」。**

合意系では objection は「解消されるまで提案を止める拒否権」になりがち。実験系では、それは最も頑固な者を governor 化する（§2.2 の3）。よって Objection を**対象で二分**する:

### 4.1 尊厳への Objection ＝ 唯一の遮断
「この実験は尊厳を侵す／強制を要する」という objection は、**Experiment Candidate の handoff を止める**。これは唯一の停止力であり、**唯一の法（dignity）に直結する**から正当。
- 重要: 止めるのは**実験（artifact）**であって**人**ではない。人を排除する権限（前レビュー R4）は要らない。dignity-objection は候補をゲートするだけ。
- 解決は投票でなく、**当事者の同意 ＋ 実装先自身の尊厳規律**（Binding invariant 2）による。WAZIS が裁定しない。

### 4.2 merit/method への Objection ＝ 競合実験 or 反証可能な対立予測
「Proposal A は誤り／B の方が良い／これは効かない」という objection は、**実験を止めない**。代わりに:
- **(a) 競合する Experiment Candidate を生む。** 「B の方が良い」は B を別の実験として走らせればよい（fan-out）。objection が**新しい実験の種**になる。
- **(b) 反証可能な対立予測として記録される。** 「これは効かない」は、それ自体が**現実で検証される仮説**。同じ Reality Feedback がこの予測を裁定する。**objector でなく現実が裁く。**

→ これにより Objection は Voice Commons 理論の「**保存された開放性（preserved openness）**」を保つ——いつでもループを再び開けるが、**誰も現実への問い合わせを止められない**。append-only・上書き不能（[WAZIS_SPEC.md:103](../history/WAZIS_SPEC.md)）はこの二役と完全に整合する。merit-objection は「閉じる veto」でなく「もう一つの実験 ＋ RF への賭け」になる。

### 4.3 残る難問（正直な明示）
**争いある dignity-objection を誰が裁くか。** 当事者本人が関わる実験なら同意/撤回で閉じる。だが「**第三者**の尊厳を侵す」という objection は、当事者同意だけでは閉じない。ここは WAZIS（と Dan-Go）の最難問であり、本補正でも解けない。ただし範囲は「全討議の収束」から「**係争中の第三者 dignity-objection の扱い**」へ大幅に縮小した。これは小さく、正当で、扱うに値する残余。

---

## 5. 前回 M0.5 の懸念は、補正後も成立するか

| 旧懸念 | 補正後の判定 | 理由 |
|---|---|---|
| **R3** 投票なしの収束手続きが未定義 | **棄却（解消）** | 収束は不要。要求すれば憲法違反（§2.2）。category error だった |
| **M-b** 同意ベース収束手続きを作る | **削除** | 同上。作るべきでない |
| **R1** Issue #1 がメタ問いで TTFCL を駆動しない | **存続・鋭利化** | 補正が修正方向を確定: Issue #1＝「**RF を生む最小の現実実験**」（§6） |
| **M-a** 具体的な最初の現実 Question | **存続・再定義** | 「最小の実験可能な現実の問い」へ |
| **R2** 最初のループで Dan-Go 事実上必須 | **降格** | 実験系では「**ある**実装先が RF を返せれば可」。Dan-Go が唯一の生 Binding なのは事実だが、Experiment Candidate が Dan-Go の Claim 形に**寄せて**いない限り中立。Issue #1 の「Dan-Go 受理可能性」フィルタは「**何らかの実装先で観測可能か**」へ緩める |
| **M-e** 二つ目の Binding 雛形 | **降格（残すと有益）** | 中立性の反証には有益だが、TTFRF には不要。最小実験を優先 |
| **R4** CoC の離脱執行が宙吊り | **縮小** | 停止力は dignity-objection が候補をゲートするのみ（人を排除しない）。残るのは §4.3 の第三者 dignity 裁定だけ |
| **R5/R6** 二重ライセンス裏付け不在／規範は fork へ非伝播 | **不変** | 概念補正と直交。なお有効 |
| **R7/R8** プレースホルダ・未 git init・候補順序 | **不変** | housekeeping。なお有効 |
| **強み S1–S6** | **維持・強化** | 特に S3（無裁定＝`not_yet_decided` 必須）は実験系で更に自然に。S4（中立 I/F）も fan-out と整合 |

**要旨:** 補正は前レビューの**最大の手続き懸念（R3）と M-b を消し**、**真の懸念（R1）を確定的に鋭利化**し、R2/R4/M-e を**降格**、ライセンス・housekeeping（R5–R8）は**そのまま**残す。

---

## 6. 推奨（レビューのみ・実装しない）

実装・編集は行わない。以下は次に着手する際の指針:

1. **命名:** `Implementation Candidate` → **`Experiment Candidate`**（実装＝作る、ではなく実験＝学ぶ。`failed` でも成功）。SPEC §1.4 / 各 README / Issue テンプレ `03` / Binding 表が対象。
2. **収束語の削除:** SPEC §1.3「収束はするが」・§2「合意的な収束で Phase が進む」・§4「収束は合意的」を、「**実験可能になった候補が（合意なしに）handoff される**」へ。Phase 2「Refinement」は「**各 Proposal を実験可能にする鋭利化**（一本化ではない）」と明記。
3. **遷移条件の明文化:** `maturity: still_open | ready_for_handoff` を **`experimentability`**（falsifiable + dignity-safe + consented + bindable の4条件）へ。
4. **指標:** 主指標を **TTFRF**（§3.2）に。`failed` を達成に数える旨を MVP に明記。
5. **Issue #1 再定義:** [docs/genesis-issue-1.md](../history/genesis-issue-1.md) を「最初に一周させる問いはどれか（メタ選定）」から「**Reality Feedback を生む最小の現実実験は何か**」へ。Dan-Go 受理可能性フィルタ → 「何らかの実装先で観測可能か」へ緩める。
6. **Objection の二役を SPEC に追記:** dignity-objection＝唯一の handoff ゲート（artifact 単位）／merit-objection＝競合実験 or 反証可能な対立予測（§4）。
7. **残余の難問を OpenQuestions に明示:** 「係争中の**第三者** dignity-objection を、投票・governor なしにどう扱うか」（§4.3）。これは WAZIS 自身の最初の Question 候補にもなる。
8. **不変項目:** ライセンス確定（R5/R6）・公開整地（R7/R8）は前レビュー通り。

---

## 7. 補正後の WAZIS（一文で）

**WAZIS は、測定不能の想いから生まれた問いを討議し、合意を待たずに——尊厳に反しない限り——複数の Proposal を「最小の現実実験（Experiment Candidate）」へ変え、外部実装先へ渡して Reality Feedback を得る、実験生成系である。裁定するのは討議でなく現実であり、収束は不要、Objection は（尊厳を除いて）実験を止めず競合実験か反証可能な予測になる。最初の成功は「合意」でも「成功した実験」でもなく、現実が一度語ること（TTFRF）である。**

---

*本書はレビューであり、実装・コード・リファクタリングを含まない。判定は現ファイル（M0）とユーザー補正に基づく仮説であり、最初の Reality Feedback で更新される。前レビューに対し: R3 棄却・M-b 削除・R1 鋭利化・R2/R4/M-e 降格・R5–R8 存続。*
