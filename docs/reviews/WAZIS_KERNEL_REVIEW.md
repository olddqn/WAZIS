# WAZIS Kernel Review / 核（kernel）抽出レビュー

- Date: 2026-06-22
- Scope: Constitution / Spec / MVP / Experiment-Driven Review / 既往アーキ討議の全体から、WAZIS の**不可分の核**を同定する
- 種別: **レビューのみ**。実装・コード・既存ファイル修正・憲法書き換えを含まない（本書の新規作成のみ）。
- 前提（ユーザー補正・憲法に反しない限り真）: `Question → Discussion → Proposal(s) → Experiment Candidate(s) → Binding(s) → Reality Feedback → New Question(s)`。**収束は任意・合意は任意・Reality Feedback は必須。**

> **一行結論:** WAZIS の核は「議論」でも「実験」でもなく、**権威の所在**にある。WAZIS とは——*討議では正直に決着できない問いを、自らが支配しない現実へ運び、討議でなく現実の応答を裁定とし、その応答が次の問いを開く*——この一巡である。実験はその橋、討議はその足場（任意）。**現実が裁定者であること（Reality Feedback 必須）が、WAZIS を forum でも consensus でも knowledge base でもないものにしている唯一の差異**である。

---

## 0. 判定法（kill-test）

ある概念が**核（load-bearing）**であるとは、**それを取り除くと WAZIS が「WAZIS でないと宣言されたもの」のいずれかに崩落する**こと、と定義する。崩落しなければ**置換可能（replaceable）**。

WAZIS でないもの（ユーザー宣言）: consensus / voting / governance / social network / forum / DAO / knowledge base。

この test は意見でなく機械的判定を与える。以下すべてこの test に基づく。

---

## 1. 最小核（Minimum Kernel）

### 1.1 核の心臓（一文）

**WAZIS は、討議・投票・権威では正直に決着できない問いを、自らが支配しない現実へ運び、現実の応答（Reality Feedback）を——討議でなく——唯一の裁定とし、その応答が次の問いを開く一巡である。**

問いが「開いている（discussion が最終的に閉じられない）」ことと、「現実が裁定する」ことは表裏一体である。**問いが本当に開いているからこそ、現実が要る**。WAZIS の全機構は、この「開いた問いを現実へ運び、偽の決着を拒む」ことに奉仕する。

### 1.2 核 = 1ループ ＋ 3不変項 ＋ 1橋

**ループ（不可分の運動）:**
```
開いた問い → 実験可能化 → 外部の現実へ（Binding）→ Reality Feedback（＝裁定）→ 新しい開いた問い → …
```

**不変項（失えば腐敗する）:**

| | 不変項 | 失うと崩落する先 | 出所 |
|---|---|---|---|
| **I** | **裁定者は討議でなく現実**（RF 必須・WAZIS は自採点しない・合意は任意） | forum / consensus / governance | 第1条・実験駆動補正 |
| **II** | **二つの不可触: 想いを測らない／尊厳を越えない**（想い=0層・dignity=唯一の法かつ唯一の実験ゲート） | scoring/reputation 系／強制実験機械 | 第3条・第10条 |
| **III** | **ループは最終的に閉じない**（あらゆる裁定が次の問いを開く・恒久決着なし） | knowledge base / Q&A | 第8条 |

**橋（不変項を繋ぐ唯一の遷移）:**
- **Experimentability（実験可能性）** — 問いが handoff 可能になる条件は consensus でなく「観測可能/反証可能 ＋ dignity-safe ＋ consent ＋ bindable」。これが無いと**現実が応えるべき対象が存在しない**（実験化しない生の問いに現実は答えられない）。

これだけが核である。`Question/Proposal/Need` の語彙、`Discussion/Forum`、`Refinement`、Binding の具体設計、schema、DID、trust、TTFRF、git、言語、そして「WAZIS」という名すら——**すべて足場（§3）**。

### 1.3 二層の核（差異化核 と 倫理枠）

核は性質の違う二群からなる:

- **差異化核（WAZIS を他の何かでなく WAZIS にするもの）:** I（現実が裁定）＋ III（非終端）＋ 橋（実験可能性）。これらは「forum/KB/consensus でない」を産む。
- **倫理枠（共有された不可触・Dan-Go から継承）:** II（想い非測定・尊厳）。これは「有害な実験機械／採点機械でない」を産む。dignity は WAZIS 固有でなく Dan-Go と共有——ゆえに*差異化*はしないが、*失えば WAZIS が WAZIS であることをやめる*意味で同等に load-bearing。

---

## 2. Load-bearing な概念（核）

各々、kill-test（除去→どこへ崩落するか）で示す。

1. **Reality Feedback ＝ 裁定者（必須）.** 除去 → 裁定が討議に戻る → **forum / consensus** に崩落。**最も load-bearing**（§4）。
2. **外部の現実（WAZIS は実装しない・自採点しない）.** 除去（WAZIS 自身が実装し自己評価）→ feedback が**自採点**になり「現実」でなくなる → I が崩壊 → forum 化。第7条。
3. **Experimentability / Experiment Candidate（橋）.** 除去 → 現実へ渡す**観測可能な対象が無い** → ループが現実に届かない → 討議が宙に浮く（forum 化）。*format は置換可だが、実験可能化という機能は不可分*。
4. **想いの非測定（0層）.** 除去（想いにスコア/順位）→ **scoring / reputation / recommendation** 系に崩落。第3条。
5. **Dignity ＝ 唯一の限界かつ唯一の実験ゲート.** 除去 → 実験を止める唯一の力が消える → **無制約な（強制を含みうる）実験機械** ＝ governance/coercion に崩落。また Binding の無損失性も失う。第10条。
6. **非終端ループ（RF が New Question を開く）.** 除去（問いが「最終回答」で閉じうる）→ **knowledge base / Q&A** に崩落。第8条。
7. **開いた入力（問い）.** 除去（閉じた提案のみ受理）→ 上流性を失い **Dan-Go の Claim 層へ吸収**（独立 identity 喪失）。*ただし語彙 Question/Proposal/Need は置換可（§3）。openness が核*。

**注（Objection の分解）:** Objection は一様でない。**dignity-objection は核**（5 の実験ゲートそのもの＝唯一の停止力、人でなく artifact を止める）。**merit-objection は置換可**（§3-e：fan-out＝競合実験/New Question に還元できる）。前者は dignity 不変項に含まれ、後者は足場。

---

## 3. 置換可能な概念（足場）

除去しても WAZIS は WAZIS のまま——を示す。

- **(a) Discussion / the Forum.** 単独者が `問い → Experiment Candidate → 現実` を通せる以上、討議は**典型的だが必須でない**venue。ユーザーが「forum でない」と明言。除去しても核ループは回る。→ **WAZIS は discussion protocol ではない**（§5）。
- **(b) Convergence / Consensus.** 補正で明示的に**任意**。除去しても可（むしろ要求すると憲法違反、前 R3）。
- **(c) Proposal/Need/Question の細分類.** 「開いた入力」一次プリミティブに圧縮可。taxonomy は説明上の便宜。
- **(d) Refinement（鋭利化）.** 各 Proposal を実験可能にするのに**有用だが必須でない**（最小実験は鋭利化を経ずに出せる）。
- **(e) merit-objection プリミティブ.** 「B の方が良い／効かない」は**競合 Experiment Candidate** か **反証可能な対立予測**に還元（同じ RF が裁く）。独立プリミティブとして不要。
- **(f) Binding の具体設計.** *外部現実へ届く要件*は核だが、*アダプタの具体形*（写像表・I/F の形）は置換可。
- **(g) Implementation Neutrality の「複数 Binding」.** *単一実装先へ welding しない独立性*は load-bearing（さもなくば「Dan-Go の front-end」化＝independent でない）が、*binding の数・どの実装先か*は任意（M0 で Dan-Go 1本でも核は保たれる）。
- **(h) DID/pseudonym・trust-as-information・JSON schema・TTFRF という指標名・git 基盤・公開方式.** すべて実装詳細。
- **(i) AI = recorder/mediator（not governor）.** 「内部に裁定権威を置かない」＝不変項 I の系。独立核でなく**派生**。
- **(j) 「WAZIS」という名・言語（日本語/英語）.** 置換可。

**圧縮の含意:** no-vote・no-verdict・no-governor・no-measurement といった**否定的制約は独立核でなく、I と II からの帰結**である。核が小さく生成的であることの証左。

---

## 4. 取り除くと WAZIS を殺すもの（致死順）

| 順 | 除去対象 | 死に方 | 致死度 |
|---|---|---|---|
| 1 | **Reality Feedback ＝ 裁定者（＋外部現実）** | 裁定が討議へ戻り forum/consensus に崩落。WAZIS の identity 消失 | 🔴 即死 |
| 2 | **想いの非測定** | scoring/reputation 機械化。源を managed object に。第3条破棄 | 🔴 即死 |
| 3 | **Dignity（唯一の限界・実験ゲート）** | 実験を止める唯一の力が消え、強制を含みうる実験機械に。唯一の法の喪失 | 🔴 即死 |
| 4 | **非終端ループ** | 問いが恒久決着し knowledge base 化。第8条破棄 | 🟠 緩慢死 |
| 5 | **Experimentability（橋）** | 現実が応える対象が消え、ループが現実に届かない | 🟠 機能不全 |

**最も致死的な単一要素 = #1。** forum・consensus・voting・governance・DAO・knowledge base のすべては**権威を内部に置く**（討議・票・統治・蓄積知）。WAZIS だけが**権威を外部の現実に置く**。これを抜けば、WAZIS は宣言した全ての「でないもの」のどれかに必ずなる。**Reality Feedback の非任意性こそ identity の最後の砦**——ユーザーの「Reality Feedback is not optional」は核の正確な指摘。

---

## 5. WAZIS は根本的に何か

| 候補 | 判定 | 理由 |
|---|---|---|
| discussion protocol | ❌ | 討議は任意の足場（§3-a）。「forum でない」と明言。討議が無くても核ループは回る |
| experiment protocol | ◯（機構として） | 実験は**現実へ到達する唯一の橋**＝必須。だが**手段**であって目的でない。実験は「現実に裁定させるため」に在る |
| **reality-feedback protocol** | ✅（identity として） | **裁定者＝現実**が WAZIS を全ての「でないもの」から分かつ唯一の差異。RF 必須 |
| something else | ✅（最精密） | 本質は **「開いた問いの裁定権を、討議から現実へ移す」プロトコル**＝*authority-relocation / reality-arbitration loop*。実験はその transducer |

**結論:** WAZIS は **reality-feedback protocol** である。より精密には、**「討議が正直に決着できない問いを実験へ変換し、現実に裁定させ、また問いへ戻す」authority-relocation loop**。三層が入れ子:

```
問い（燃料・開いた入力）
  └ 実験（transducer・現実へ届かせる橋）        ← experiment protocol の層
      └ Reality Feedback（裁定・唯一の権威）     ← ここに identity が宿る
```

identity は**裁定の層**に宿る。だから「experiment protocol」は機構として正しく、「reality-feedback protocol」は identity として正しい。一語なら後者。

---

## 6. 最も単純で、なお正確な定義（ladder）

- **一行（最圧縮）:**
  > **WAZIS は、開いた問いの裁定者を討議でなく現実にするために、問いを実験へ変えるプロトコルである。**

- **一文:**
  > WAZIS は、討議・投票・権威では決着できない問いを、尊厳を越えず想いを測らないまま、最小の実験（Experiment Candidate）へ変換し、自らが支配しない現実へ渡し、その Reality Feedback を唯一の裁定として次の問いを開く——終わらない一巡である。

- **完全（核を全て含む）:**
  > WAZIS は reality-feedback protocol である。測定不能の想い（0層・不可触）から生まれた開いた問いを、合意を待たず——尊厳に反しない限り——複数の実験へ変換し、外部実装先（Binding 経由・WAZIS は実装しない）へ渡して Reality Feedback を得る。裁定するのは討議でなく現実であり、収束も合意も任意、Reality Feedback だけが必須。あらゆる裁定は新しい問いを開き、ループは最終的に閉じない。

三つとも、§1 の核（I 現実が裁定・II 二不可触・III 非終端・橋 実験可能性）を漏らさない。これより短くすると、必ずいずれかの不変項が落ち、WAZIS が「でないもの」へ崩れる。

---

## 付録 A. 「WAZIS でないもの」を阻む核要素（鏡像検証）

各「でないもの」は、ある核要素によって**阻止されている**。その核要素を抜けば WAZIS は*そのもの*になる——核が過不足ないことの裏取り。

| WAZIS でないもの | それを阻む核要素 | 抜くと… |
|---|---|---|
| consensus system | I（現実が裁定／合意は任意） | 合意が目的化 |
| voting system | I＋III からの帰結（no-vote） | 票が裁定に |
| governance system | I（内部権威を置かない／no-governor） | 統治機関化 |
| social network | identity が「graph の接続」でなく「問い→現実の巡回」 | 接続が目的化 |
| forum | I（討議は権威でも産物でもない・産物は実験と RF） | 議論自体が目的化 |
| DAO | I＋II（票・トークン・on-chain 統治権威なし） | 投票統治体化 |
| knowledge base | III（恒久決着なし・生きた問いを保持） | 決着回答の貯蔵庫化 |

七つすべてが核要素で塞がれている。塞ぐ要素＝§2 の load-bearing 集合。**過剰でも過少でもない。**

## 付録 B. 前レビュー群との接続

- 実験駆動補正（[WAZIS_EXPERIMENT_DRIVEN_REVIEW.md](WAZIS_EXPERIMENT_DRIVEN_REVIEW.md)）の「裁定者は RF・遷移は experimentability・Objection 二役」は、本核抽出と完全整合（本書はそれを*最小集合*へ煮詰めたもの）。
- 前 R3（収束手続き）棄却は核レベルで再確認: 収束は §3-b の足場であり、核は fan-out（非収束）を要求する。
- M0.5 の TTFRF は核の「現実が一度語る」を測る指標——核でなく**核の観測装置**（置換可だが有用）。

---

*本書はレビューであり、実装・コード・既存ファイル修正・憲法改定を含まない。核の同定は kill-test に基づく仮説であり、最初の Reality Feedback で反証されうる——その反証可能性自体が、本書が核と呼んだもの（III・I）の作動である。*
