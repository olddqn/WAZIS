# WAZIS 仕様 / WAZIS Specification

**WAZIS — 和智達（ワチス）** / Wisdom Action Zone for Implementation in Society

- Version: 0.1.0-draft
- Status: Open for deliberation（討議に開かれている）
- Date: 2026-06-21
- 上位文書: [WAZIS_CONSTITUTION.md](../../WAZIS_CONSTITUTION.md)（規範の天井。本仕様は憲法に従属する）

> 本仕様は WAZIS の機構を定義する。コードではない。JSON スキーマは**設計成果物**として記すが、実装はまだ行わない（[WAZIS_MVP_PLAN.md](WAZIS_MVP_PLAN.md) を参照）。本仕様も仮説であり、Reality Feedback によって修正される。

---

## 0. 概要

WAZIS は社会実装の**上流工程**である。測定不能の「想い」から生まれた**問い**を受け取り、討議で洗練し、外部の実装先へ渡せる **Implementation Candidate（実装候補）** を生む。実装そのものは行わない。

```
                       ┌─────────────── WAZIS の範囲 ───────────────┐
 〔0層: 想い〕──self──▶ Question ──▶ Discussion ──▶ Refinement ──▶ Implementation
   (測らない)  translate  (Phase 0)   (Phase 1)      (Phase 2)       Candidate (Phase 3)
                                                                          │
                       └──────────────────────────────────────────────────┼── handoff（同意必須）
                                                                          ▼
                                                          External Implementation (Phase 4)
                                                          Dan-Go / NPO / 企業 / 研究 / OSS / 自治体 …
                                                                          │
                                            New Question ◀── Reality Feedback (Phase 5) ──┘
                                            (Phase 8 → 0 へ還る)
```

### Dan-Go との対応関係

| 層 | WAZIS | Dan-Go |
|---|---|---|
| 単位 | **Question**（開く声・interrogative） | **Claim**（提案された状態遷移） |
| 過程 | Discussion / Refinement（洗練） | Negotiation（交渉） |
| 出力 | **Implementation Candidate** | Contribution → Execution |
| 帰着 | Reality Feedback → New Question | Reality Feedback → 次の Claim |
| 公開状態 | **the Forum（討議卓）** | 素テーブル（sutable） |
| 唯一の法 | dignity | dignity |

WAZIS の Implementation Candidate は Dan-Go の Claim の**手前**に立つ。WAZIS は Voice Commons でいう **Question（最上流・開く起源）** のレイヤであり、Dan-Go は Claim 以降の実装レイヤである。

---

## 1. コアオブジェクト

WAZIS の状態は 5 つのオブジェクトで表される。すべて公開・追記可能（append-only）・撤回尊重を原則とする。

### 1.1 Question（問い）

最上流の単位。「開く声」。状態・欠如・遷移をまだ主張しない、最も原初的な表面。Claim ではない（observed/required/desired をまだ分離しない）。

```json
{
  "question_id": "string — 一意。例: q-{topic}-{seq}",
  "title": "string — 一文要約",
  "speaker": "string — DID または pseudonym",
  "statement": "string — 平易な言葉での問い本体",
  "entry_category": "discomfort | unresolved | institutional_design | community_design | long_held | other",
  "background": "string — 当事者が自ら選んで言語化した状況・文脈（想いの測定ではない。書かなくてよい）",
  "open_threads": ["string — 派生した小さな問い"],
  "status": "open | refining | candidate_drafted | parked | withdrawn | reopened",
  "consent": {
    "public": true,
    "handoff_allowed": false
  },
  "created_at": "ISO 8601",
  "updated_at": "ISO 8601",
  "version": "integer"
}
```

制約:
- `entry_category` は**入口の分類**であって、想いの強さ・優先度の分類ではない（憲法 第3条）。
- `background` は当事者の self-translation。WAZIS がここから内心の強度を推定してはならない。
- `statement` に「観測されていないことを観測済みとして」書かない。問いは問いのまま記録する。
- Question は private key / 認証情報 / 投資約束 / 検証されていない断定を含んではならない（Dan-Go Claim と同じ禁止事項を継承）。

### 1.2 Discussion Entry（討議エントリ）

Phase 1 で Question に付く発言。種類（mode）で区別する。Voice Commons の「モード」に対応する。

```json
{
  "entry_id": "string",
  "question_id": "string — 親 Question",
  "speaker": "string — DID または pseudonym",
  "mode": "counter_question | perspective | need_framing | proposal | objection | refinement | reference",
  "body": "string",
  "in_reply_to": "string — 任意。別 entry への応答",
  "withdrawn": false,
  "created_at": "ISO 8601"
}
```

mode の意味:
- `counter_question` — 問いを開き直す問い。
- `perspective` — 視座の提示（賛否ではない）。
- `need_framing` — 「何が欠けているか」を名指す（半開。診断を閉じ、解決を開く）。
- `proposal` — 緩い遷移案（集団に開いたまま差し出す）。Claim ではない。
- `objection` — **不可侵**。閉じかけを開き直す。append-only・上書き不能。
- `refinement` — 問いの言い換え・分割・鋭利化の提案。
- `reference` — 外部資料・先行事例・Reality Feedback の参照。

制約:
- 賛成/反対の**投票**は mode に存在しない（憲法 第1条: 多数決を行わない）。
- `objection` は削除も上書きもできない。撤回（`withdrawn: true`）はできるが、撤回の事実自体は記録に残る。

### 1.3 Refinement（洗練）

Phase 2。Question が鋭利化・分割・収束していく過程の記録。Question のバージョン更新として表現される。**収束はするが裁定はしない**（convergence without verdict）。

洗練の結果は次のいずれか:
- (a) より鋭い **Question**（Phase 0 へループ。問いのまま留まる＝正当）
- (b) 複数の Question への**分割**
- (c) **Implementation Candidate** の起草（Phase 3 へ）

洗練は Question の `version` を増やし、`open_threads` を更新し、必要なら派生 Question を生む。元の問いは git 履歴的に保存される。

### 1.4 Implementation Candidate（実装候補）

WAZIS と外部実装先の**境界物**。実装中立に設計され、Dan-Go の Claim・NPO のプロジェクト要項・企業の提案・OSS の issue・研究の問い・自治体の提案——いずれにも翻訳できるだけの構造を持つが、**どれにも事前コミットしない**。

```json
{
  "candidate_id": "string — 一意。例: ic-{topic}-{seq}",
  "origin_question_id": "string — トレーサビリティ。必須",
  "title": "string — 一文要約",
  "summary": "string — 洗練された問い／方向性の平易な記述",
  "problem_framing": ["string — 討議で確認された状況（検証可能な事実に限る）"],
  "what_would_change": ["string — 望ましい方向（規範的な手段の指定ではない）"],
  "open_constraints": ["string — 尊重すべき制約・記録された objection（多くは尊厳関連）"],
  "not_yet_decided": ["string — WAZIS が意図的に裁定しなかった点（無裁定原則の保存）"],
  "candidate_implementers": ["dan_go | npo | company | research | oss | municipality | other"],
  "consent_status": {
    "handoff_consented_by": ["string — DID/pseudonym"],
    "withdrawable": true
  },
  "dignity_check": {
    "violates_dignity": false,
    "uses_coercion": false,
    "notes": "string — 任意"
  },
  "maturity": "still_open | ready_for_handoff",
  "created_at": "ISO 8601",
  "updated_at": "ISO 8601",
  "version": "integer"
}
```

設計原則:
- `candidate_implementers` は**示唆であって決定ではない**。複数列挙してよい。WAZIS が実装先を選定する権限は持たない。
- `not_yet_decided` を必ず埋める。これが「WAZIS は正解を決めない」（憲法 第1条）の構造的保証。空にして「すべて解決済み」と装ってはならない。
- `maturity` は**討議成果物の引き渡し準備度**であって、想いや問いの優劣スコアではない。
- `what_would_change` に手段を固定しない（method-agnosticism）。目的（誰がどう助かる方向か）をアンカーにする。
- `dignity_check` は自己申告であり、Forum で誰でも異議を申し立てられる。

### 1.5 Reality Feedback（現実フィードバック）

Phase 5。外部実装から戻る観測。WAZIS が生成するのではなく、**実装先から受け取って記録する**。

```json
{
  "feedback_id": "string",
  "candidate_id": "string — どの実装候補についてか",
  "implementer": "string — 実装先の識別子（例: dan_go:claim-xxx）",
  "outcome": "executed | partial | failed | pending",
  "observation": "string — 何が起きたか（独立観測）",
  "who_was_helped": "string — 任意。誰が・どう助かった/助からなかったか",
  "spawned_questions": ["string — ここから生まれた New Question の id"],
  "reported_by": "string — DID/pseudonym",
  "created_at": "ISO 8601"
}
```

制約:
- `outcome` は Dan-Go の Reality Feedback（executed/partial/failed/pending）と**同じ語彙**を使い、Binding 越しに整合させる。
- Reality Feedback は問いを「解決」として閉じない。`spawned_questions` を通じて New Question を開きうる（憲法 第8条）。

---

## 2. ライフサイクル（Phases）

| Phase | 名称 | WAZIS 内/外 | 主な動き |
|---|---|---|---|
| 0 | Question Submission | 内 | 誰でも問いを開く |
| 1 | Discussion | 内 | 視座・counter-question・objection・need/proposal framing。投票なし |
| 2 | Refinement | 内 | 鋭利化・分割・収束。裁定しない |
| 3 | Implementation Candidate | 内 | 境界物の起草。`not_yet_decided` を明示 |
| 4 | External Implementation | **外** | Dan-Go 等が実装。WAZIS は handoff を記録するのみ |
| 5 | Reality Feedback | 境界 | 実装先から観測を受領・記録 |
| → 0 | New Question | 内 | feedback から新しい問いが開く（ループ） |

Phase 間に「昇格判定」はない。当事者と Forum の合意的な収束で Phase が進む。AI は判定者ではない（§4）。問いはいつでも前の Phase へ戻れる（reopen は失敗でない）。

---

## 3. the Forum（討議卓） — 公開討議状態

すべての Question と Discussion Entry の公開状態。Dan-Go の素テーブル（sutable）に対応する WAZIS の卓。

性質:
- 既定で公開（`consent.public`）。隠れた討議を持たない。
- 誰でも任意の Question の全状態を読める。
- 編集は timestamp と speaker id とともに記録される。
- **objection は append-only・上書き不能**（不可侵条項 §5）。
- **撤回（withdrawal）はいつでも可能**。撤回された声は無効化されるが、撤回の事実は記録に残る。
- ブロックチェーンではない。**透明性に支えられた社会契約**である（Dan-Go と同じ姿勢）。

公開の例外: 当事者が `consent.public: false` を選んだ場合、その Question は限定公開となる。ただし Implementation Candidate として handoff する時点で、引き渡しに必要な範囲の公開について改めて同意を取る（同意の二段階）。

---

## 4. 役割と権限

- **AI エージェント**は recorder / mediator / facilitator である。**governor / judge ではない**（Dan-Go README:1326「AI is not a governor」を継承）。AI は問いの記録・整理・矛盾の指摘・関連付けを行うが、正解の決定・問いの優劣付け・想いの測定をしてはならない。
- **人間の参加者**は問いを開き、討議し、洗練し、実装候補に同意し、撤回する。
- **実装先（external implementer）**は Implementation Candidate を引き取り、実装し、Reality Feedback を返す。WAZIS の外にある。

WAZIS は誰にも「正解を決める権限」を与えない。収束は合意的・可逆的であり、最終決定権はどのノードにも集中しない。

---

## 5. Implementation Binding（実装束縛） — 実装中立インターフェース

Implementation Candidate を、特定の実装先の受け入れ形式へ写す**アダプタ**。WAZIS の実装中立性（憲法 第6条）はこのインターフェースで担保される。

### 5.1 Binding インターフェース（抽象）

各 Binding は次を定義する:

```
Binding {
  target: string              // 実装先の識別子（"dan_go" 等）
  map(candidate) -> payload    // Implementation Candidate → 実装先の受け入れ形式
  consent_required: true       // handoff には当事者同意が必須（不可侵条項）
  feedback_channel: string     // Reality Feedback を受け取る経路
  reverse(feedback) -> Reality Feedback  // 実装先の出力 → WAZIS の Reality Feedback
}
```

原則:
- すべての Binding は handoff 前に `consent_status.handoff_consented_by` を確認する。
- すべての Binding は実装先の dignity 規律と WAZIS の第10条が**矛盾しない**ことを確認する。
- 実装先固有の都合（KPI・締切・資金条件など）が Candidate の中身を遡って歪めてはならない。

### 5.2 具体 Binding #1: Dan-Go（最初の一つ・参照実装）

Implementation Candidate → Dan-Go Claim（CLAIM_FORMAT.md / MUJIN_PROTOCOL Phase 0）。

| WAZIS Implementation Candidate | Dan-Go Claim |
|---|---|
| `summary` | `statement` |
| `problem_framing[]`（検証可能な事実のみ） | `observed_state[]` |
| `what_would_change[]` | `required_state[]` ＋ desired（方向） |
| 充足すべき差異（problem_framing と what_would_change の差） | `missing_conditions[]` |
| `open_constraints[]`（手段以外の制約） | `risks[]` |
| `dignity_check` | `constitution_check`（`violates_dignity` / `uses_coercion`） |
| — | `claim_type` = **interrogative**（Question 由来のため初期は interrogative） |
| `candidate_id` / `origin_question_id` | `claim_id` のメタに保持（トレーサビリティ） |

Reverse（Dan-Go → WAZIS）:

| Dan-Go Reality Feedback | WAZIS Reality Feedback |
|---|---|
| `executed / partial / failed / pending` | `outcome`（同じ語彙） |
| feedback の本文 | `observation` |
| Phase 4 の観測 | `who_was_helped`（任意） |

注意:
- `not_yet_decided` は Claim に転写しない。WAZIS が裁定しなかった点は、Dan-Go 側の交渉（Negotiation）で当事者が決める。WAZIS が代わりに決めてはならない。
- WAZIS の尊厳と Dan-Go の尊厳は同一の法のため、`dignity_check` ↔ `constitution_check` は無損失で対応する。

### 5.3 将来の Binding（スタブ・未実装）

インターフェースのみ定義し、写像は未確定:

- `npo` — Implementation Candidate → NPO のプロジェクト要項 / 助成申請の素地。
- `company` — → 社内提案 / PoC 要件。
- `research` — → 研究上の問い / プロトコル / 倫理審査の素地。
- `oss` — → OSS の issue / RFC / discussion。
- `municipality` — → 自治体の提案 / 政策の素地（Dan-Go の Policy Commons／Globe に近い）。
- `other` — その他のプロトコル。

これらは Dan-Go Binding と**同じインターフェース**で後から追加される。Dan-Go はあくまで最初の一つであり、WAZIS の中核は Binding に依存しない。

---

## 6. Trust（信頼）— ゲートではなく情報

- 信頼は付与されるものではなく、貢献によって蓄積される（Dan-Go と同じ）。
- WAZIS における貢献 = 良い問いを開き、洗練を進め、その実装候補が Reality Feedback で「誰かが助かった」方向を示したこと。
- 信頼スコアは**ゲートではなく情報**である。高信頼 = 討議でより重く参照される、であって、他者の問いをブロックする権力ではない。
- **想いの強度では序列を作らない**（憲法 第3条）。評価は status ではなく contribution（行為とその Reality Feedback）から来る。

---

## 7. Non-goals / 不可侵の設計制約

WAZIS は次を**設計として行わない**:

- 想いの数値化・スコア・強度推定・分類スキーマ・記録様式（第3条）。
- 表面（問い・発言）から背後の想いを逆算する仕組み（Saiyan Scouter 禁止）。
- 正解・真偽・ベストアンサーの裁定、および多数決（第1条）。
- 実装そのもの（第7条）。WAZIS は上流工程に留まる。
- 単一実装先の特権化・実装先による討議内容の歪曲（第6条）。
- AI への決定権・統治権の付与（§4）。
- 同意なき引き渡し、撤回の不能化、objection の上書き（第5条）。

---

## 8. 未解決の問い（WAZIS 自身についての Open Questions）

WAZIS 自身も問いを持つ。これらは WAZIS 上で討議されるべき:

- 「収束（convergence）はしたが裁定（verdict）はしない」をデータ構造としてどう保証するか。`not_yet_decided` 必須化で十分か。
- 限定公開（`public: false`）の問いと、透明性原則の緊張をどう扱うか。
- 複数の Binding が同じ Candidate を引き取った場合、Reality Feedback の統合をどうするか。
- 「良い洗練」を Reality Feedback で評価するとき、想いの測定に滑り落ちない線引きをどう保つか。
- WAZIS の基盤（substrate）を何に置くか（[WAZIS_MVP_PLAN.md](WAZIS_MVP_PLAN.md) §4 で扱う）。

---

*本仕様は機構の設計であり、実装ではない。すべて仮説であり Reality Feedback で修正される。憲法（[WAZIS_CONSTITUTION.md](../../WAZIS_CONSTITUTION.md)）に従属し、第5条・第10条を損なう仕様変更はできない。構築計画は [WAZIS_MVP_PLAN.md](WAZIS_MVP_PLAN.md)。*
