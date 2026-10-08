# Object Reduction Review / オブジェクト縮約レビュー

- Date: 2026-06-22
- Scope: Experiment Candidate は本当に fundamental object か、それとも Transformation の可視 trace か。最小 object model を確定する
- 種別: **レビューのみ**。実装・コード・既存ファイル修正を含まない。
- 規律: **削除を加算より優先。** 新概念・新層を発明しない。判定 = Kill Test ＋ Reification Test。既存レビューに在るなら「既出」と明記。
- 前提: 既往6レビュー（KERNEL / DANGO_BOUNDARY / META_LOOP / TRANSFORMATION / STRUCTURAL_CONSOLIDATION / PLATFORM）は、直接観察で矛盾しない限り正しい。

> **見出しの答え:** **Experiment Candidate は fundamental ではない。Transformation の可視 trace（通過スナップショット）である**——これは TRANSFORMATION_REVIEW §1/§10 と STRUCTURAL_CONSOLIDATION §1（load-bearing 集合に EC は無い）で**既に結論済み**。PLATFORM_REVIEW の「object 3つ」はそこから**ドリフトしていた**。正しい最小 object model は **2つ: Question と Reality Feedback**。Experiment Candidate は両者を繋ぐ **handoff edge**（consent ＋ dignity-check ＋ binding 参照を運ぶ辺）へ**溶ける**——これは「変換は node でなく edge」（TRANSFORMATION §1）に忠実。この縮約は **neutrality を改善する**（WAZIS 所有の中間形式という Dan-Go 寄りの漏れを除く）。**失われる本質は無い——ただし handoff edge が consent と dignity-check を明示・監査可能に保つ限りにおいて**（唯一の条件）。

---

## 1. Experiment Candidate は fundamental か — 両 test

### 1.1 Kill Test
**問い:** Experiment Candidate（object）が消えると、WAZIS は identity を失うか?
- それが出力する*操作*（Transformation）は残る。問いは依然「現実が答えられる形」へ変換され、現実は答える。
- WAZIS の identity ＝「開いた問いを現実が答えられる形へ変え、現実に裁定させる」。EC は「その形」の*名付けられたスナップショット*。**操作が残る限り、object を消しても identity は不変。**
- **→ Kill Test 不合格 ＝ EC は identity-load-bearing でない。** load-bearing なのは Transformation（KERNEL の「橋」）。

### 1.2 Reification Test
**問い:** 「Experiment Candidate」という名が消えると、何か壊れるか?
- 変換は依然、境界を越えて実装先へ渡る*何か*（Dan-Go なら Claim、OSS なら PR）を生む。その「何か」は WAZIS が EC と呼ぶか否かに関わらず存在する。
- WAZIS が Question と Reality Feedback を持てば、「Question X を Binding Y へ渡し、Reality Feedback Z が返った」と記録でき、**渡された形は実装先の native 形式（Claim/PR）でよい**。WAZIS 所有の EC object は要らない。
- **→ Reification Test 不合格 ＝ 名を消しても handoff は起きる。EC は trace（lens）であって load-bearing object でない。**

### 1.3 結論（既出の再確認）
両 test 不合格。**EC は Transformation の可視 trace。** これは新発見でなく、TRANSFORMATION_REVIEW（「EC/Claim/PR は通過スナップショット、本質でない」）と CONSOLIDATION（load-bearing 6要素に EC 不在）で**既に確定済み**。本書はそれを object model に**適用**するだけ。

---

## 2. WAZIS は Question ＋ Reality Feedback だけで動くか

**Yes——「handoff edge」を介して。それ以外は外部 Transformation として扱える。**

縮約後の構造:
- **Question**（WAZIS が保持する開いた入力）
- **Reality Feedback**（WAZIS が記録し oracle として読む、現実の答え）
- 両者を繋ぐ **handoff edge**（object でなく、metadata を持つ遷移/辺）: `{consent, dignity-check, binding-ref, 実装先 native 成果物への link}`

handoff edge ＝ **Transformation が境界を越える点を*記録*したもの**（KERNEL ④を edge として）。WAZIS は「現実が答えられる形」の*内容スキーマ*を所有しない——内容整形は **Binding（外部）の仕事**。WAZIS は (a) 問いを開いたまま保持し、(b) dignity/consent で gate し、(c) 現実（Binding）へ route し、(d) RF を oracle として読み再び開く——だけ。

これは boundary review の interface（「流れ①: 成果物＋consent＋dignity-check を一方向に渡す」）に**既出**。EC object が持っていた consent_status / dignity_check / origin_question_id は、すべて **edge の metadata** へ移せる。新概念ゼロ、object を一つ削除。

> 含意（WAZIS の真の寄与の明確化）: **WAZIS は実験の*内容*を整形しない。問いを開いたまま gate し、現実へ route し、現実の裁定を読む——それが WAZIS の本質。** 内容整形は外部（Binding）。これは boundary review の「WAZIS は変換の前半（答えうる形にする）」を、さらに削って「前半 ＝ gate ＋ route であって content-shaping ではない」と精密化したもの。

---

## 3. 縮約は implementation neutrality を改善するか

**Yes、実質的に改善する。**

- WAZIS 所有の Experiment Candidate は、**全 Binding が map *from* する単一の中間形式**。その形式に実装先固有の前提が焼き込まれていれば neutrality 漏れになる。**現に焼き込まれている**: 既存 Binding 写像は EC を Dan-Go の Claim へ寄せて設計（`problem_framing→observed_state`, `what_would_change→required_state`, `summary→statement`）。EC は **Dan-Go の Claim の鋳型に寄っている**。
- WAZIS 所有の中間形式を**削除**し、各 Binding が **生の Question → 自身の native 形式**へ直接変換すれば、WAZIS は**いかなる中間の形も押し付けない**。WAZIS が保持するのは neutral な primitive（開いた Question ＋ 共有語彙の Reality Feedback）だけ。
- **→ object model が構成的に binding-agnostic になる。** これは U2/U4（中立性）への直接の前進——WAZIS の object から Dan-Go 寄りの形を抜く。

**正直な caveat（透明性コスト）:** EC は公開 object として、渡される形・その dignity_check・consent を**WAZIS 上で公開監査可能**にしていた。2 object へ縮約すると「何が渡され、gate を通ったか」が edge か実装先側に寄り、**WAZIS の公開台帳で見えにくくなる**恐れ。これは PLATFORM_REVIEW が EC を残した唯一の理由（「答えが魔法で湧かないよう可視化」）。
**解決:** handoff edge を **公開・監査可能な記録**にする（object でなく、consent ＋ dignity-check ＋ binding-ref ＋ native 成果物への link を持つ logged transition）。これで neutrality 改善と透明性を**両立**。EC が持っていた*内容スキーマ*（中立性漏れ）だけを削り、*ガバナンス metadata*（中立で必須）は edge に残す——これは rename でなく実削減。

---

## 4. 本質的に失われるものはあるか

**無い——handoff edge が consent と dignity-check を明示・監査可能に保つ限り。** 各要素を追跡:

| EC が担っていたもの | 縮約後の所在 | 失われるか |
|---|---|---|
| **made-answerable の内容形式** | Binding（外部・native）へ | いいえ（むしろ neutral 化、§3） |
| **experimentability（答えられるか）** | Binding の intake が判定（受理できる＝答えられる） | いいえ（relocate。各 Binding が自分の語で定義＝より neutral） |
| **dignity-gate ＋ consent** | **handoff edge の metadata（公開・監査可能）** | **いいえ——ただしこれは死守。edge から消えたら本質喪失（憲法）** |
| **no-verdict（`not_yet_decided`）** | fan-out が構造的に保証（1 Question→複数 handoff→複数 RF、決して「解決」と印を付けない） | いいえ（field 不要に。non-termination ＋ fan-out で代替） |
| **traceability（origin_question_id）** | RF→Question link、handoff→Question link | いいえ |
| **複数提案 A/B/C** | 1 Question からの複数 handoff edge | いいえ（fan-out そのもの） |

→ **唯一、絶対に失ってはならないのは dignity-gate ＋ consent の*可視性*。** EC（object）はそれを first-class field として legible にしていた。edge へ移すなら、edge が**公開・監査可能に**それを運ばねばならない。ここが reduction の唯一の条件であり、構成上の最重要点（U1 隣接・憲法整合）。それ以外は失われない。

---

## 5. kernel を保つ最小 object model

```
〔hub〕想い（測られない・入らない）
   │ self-translation
   ▼
[ Question ] ──handoff edge { consent, dignity-check, binding-ref → 実装先 native 成果物 } ──▶ 外部 Transformation / Binding / 現実
   ▲                                                                                              │
   │ reopen（New Question ＝ ただの Question）                                                     ▼
   └────────────────────────────── [ Reality Feedback ] ◀────────────────────────────────────────
        （RF → Question link。RF は独立観測・oracle 読み。1 Question → 複数 RF 可）

  Objects（2）       : Question, Reality Feedback
  Edge（1・object でない）: handoff（不可侵 gate を運ぶ。WAZIS 所有の内容 object ではない）
  Links             : RF→Question（どの問いへの答えか）, RF→New Question（再開）, handoff→Question
  Invariants（object でない）: dignity・想い非測定・現実が裁定・非終端
```

- **下限は 2。1 へは縮約できない:** RF は独立観測（Dan-Go Phase 4 / 裁定者）で、Question の属性に潰すと*独立性*を失う。かつ 1 Question→複数 RF（複数 Binding/handoff）ゆえ、RF は別 object（one-to-many）でなければならない。Question も入口として必須。**2 が床。**
- Experiment Candidate / Discussion / Objection-as-debate / not_yet_decided は object として**不要**（前者は edge へ溶け、後三者は CONSOLIDATION/PLATFORM で削除済み）。

---

## 6. 本書が修正するもの

- **PLATFORM_REVIEW §2 の「最小 object 3つ」→「2つ ＋ handoff edge」へ修正。** PLATFORM は EC を「答えが魔法で湧かないため」残したが、その公開可視化は **handoff edge-record** が果たす。これで PLATFORM は TRANSFORMATION（「edge であって node でない」）と整合する。
- **U5（仕様本文の整合）への追加項:** SPEC §1.4 の Implementation/Experiment Candidate は、**object でなく handoff edge（不可侵 gate 付き）として**再記述すべき。EC が持つ Dan-Go 寄りの写像は Binding 側へ移し、WAZIS の object は Question/RF の 2 つに保つ。*（これはレビュー指摘であり、本書では変更しない。）*

---

## 7. 統合（一文で）

**Experiment Candidate は fundamental object でなく Transformation の可視 trace であり（Kill/Reification 両 test 不合格、TRANSFORMATION・CONSOLIDATION で既出）、WAZIS の最小 object model は Question と Reality Feedback の 2 つに縮約され、Experiment Candidate は両者を繋ぐ handoff edge（consent ＋ dignity-check ＋ binding 参照を運ぶ辺）へ溶ける——この縮約は WAZIS 所有の中間形式（現状 Dan-Go の Claim に寄った neutrality 漏れ）を除くぶん implementation neutrality を改善し、experimentability は各 Binding の intake へ、no-verdict は fan-out へ、traceability は link へ移って本質は何も失われない；ただし唯一、dignity-gate と consent の*可視性*だけは handoff edge 上で公開・監査可能に死守せねばならず、それが満たされる限り、object は 2 つで kernel を完全に保つ。加えるべき object も層も無い。削除すべきは Experiment Candidate を*独立 object として持つこと*である。**

---

*本書はレビューであり、実装・コード・既存ファイル修正を含まない。新概念/層を発明していない（handoff edge は boundary review の interface に既出、consent/dignity-check は EC の既存 field の移設）。削除を加算より優先した（object を 3→2、EC を edge へ溶解）。判定は kill+reification test に基づく仮説であり、最初の Reality Feedback で反証されうる。唯一の死守条件: handoff edge 上の dignity-gate ＋ consent の公開監査可能性。*
