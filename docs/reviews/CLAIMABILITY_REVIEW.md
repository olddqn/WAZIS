# Claimability Review / Claim 可能性レビュー

- Date: 2026-06-22
- Scope: 「Claimability（Claim 可能性）」は Dan-Go に既に暗在する実在の概念か、それとも既存プロパティの別名か
- 種別: **レビューのみ**。実装・コード・既存ファイル修正を含まない。
- 規律: Dan-Go/WAZIS を再設計しない・新概念/層/ガバナンス/スコアを足さない・削除を加算より優先。**新機構を発明しない。**
- 判定: Reification Test（名を消して何か壊れれば新 entity、壊れなければ lens）。
- 接地: Dan-Go `CLAIM_FORMAT`（observed/required/missing・constitution_check）・`MUJIN_PROTOCOL`（decision: …|**reject**）・Article 1／`GAP_TO_CLAIM_REVIEW`（partial function）。

> **見出し:** **Claimability は実在するが新しくない。** それは Dan-Go に既に暗在する——「この Need は Dan-Go が **reject しない Claim** を生むか?」の**名前**であり、CLAIM_FORMAT の必須 gap 構造 ＋「未観測を観測済みとしない」規則 ＋ constitution_check ＋ reject 決定に**既に符号化済み**。Claimability は **{observable, closable, dignity-safe} のちょうど 3 条件**に還元され、それ以上でも以下でもない。**binary（充足/非充足）であってスコアでない。** ユーザーの仮説「Claimability は WAZIS/Dan-Go の真の境界」は**正しい**——ただし新境界でなく、commit-line（boundary review）／partial function の定義域（gap-to-claim）の**正確な述語名**である。**核心：Claimability は need を *worth（想い）* でなく *form（gap 形か）* で分類する——だから 想い 非測定を守る。**

---

## 1. Claimability は既に Dan-Go にあるか — Yes（符号化済み）

Claimability ＝「Need が valid な Claim になれるか」。Dan-Go の既存要素に逐一対応:

| Claimability の問い | Dan-Go の既存符号化 |
|---|---|
| gap を observed/required/missing で表せるか | **CLAIM_FORMAT の必須構造**（gap が無ければ well-formed な Claim でない） |
| observed は検証可能な事実か | **「未観測を観測済みとして提示しない」規則**（README） |
| dignity 安全か（強制なしか） | **constitution_check**（violates_dignity / uses_coercion） |
| 弾く手段はあるか | **decision: reject**（「憲法違反 or 根本的に不可能」MUJIN_PROTOCOL Phase 1） |

→ **Claimability ＝ これら既存条件の連言の名前**。

**Reification Test:** 「Claimability」という語を消す → Dan-Go は依然、well-formed でない/dignity 不安全な Claim を reject し、WAZIS は依然、問いを開いたまま保持する。**何も壊れない。** → Claimability は**新機構でなく lens**（Voice Commons 理論・meta-loop と同類）。既存境界を**明示するだけ**で、機構を足さない。

---

## 2. 何が Need を claimable にするか — {observable, closable, dignity-safe}（3 つだけ）

- **observable:** observed を検証可能な公開事実として言える（内面・私的でない）。
- **closable:** required と missing を**定まった閉鎖条件（物差し）**で定義できる（gap が*原理上*閉じうる＝yardstick を持つ。※feasibility ではない、§下注）。
- **dignity-safe:** constitution_check を通る（尊厳侵害・強制なし）。

**この 3 つで尽きるか — Yes。** `GAP_TO_CLAIM` の 5 失敗様式は全て 3 条件のいずれかに写る:

| 失敗する Need | 破る条件 |
|---|---|
| 無限定（「もっと支援を」） | **closable** ✗ |
| 内面/想い（「安心を感じたい」） | **observable** ✗（required が検証可能事実でない） |
| 関係/過程（「継続的提携」） | **closable** ✗（離散の閉鎖状態が無い） |
| 強制/尊厳侵害（「○○を排除」） | **dignity-safe** ✗ |
| 非公開観測（「私的に X が要る」） | **observable** ✗ |

→ **3 条件は必要かつ（連言で）十分。** observable＋closable＋dignity-safe なら observed/required/missing/dignity_check を組めて valid Claim になる。

**注（feasibility は第 4 条件でない）:** Dan-Go Article 1「不可能とは交渉がまだ足りないだけ」。**実行可能性は claimability の前で判定せず、Claim *の中の交渉*で扱う。** ゆえに「closable」＝「閉鎖条件（yardstick）が定義できる」であって「今閉じられる」ではない。**feasibility を claimability に入れない**（削除優先）。

---

## 3. Claimability は observed/required/missing の中に既に符号化されているか

**部分的に Yes。**
- **observable** → observed（検証可能事実の要件）に符号化。
- **closable** → required＋missing（定まった物差しを持つ gap）に符号化。
- **dignity-safe** → observed/required/missing には**無い**。**constitution_check**（別フィールド・既存）にある。

→ **Claimability ＝（well-formed な observed/required/missing）＋（constitution_check 通過）。** 2/3 は gap 三つ組、1/3 は constitution_check——**どちらも既存**。新フィールドは要らない。

---

## 4. valid な Need のまま Claimability に失敗しうるか — Yes（決定的）

**Yes。Need は real・重要・正当でありながら claimability に失敗しうる。**

例:
- **「この子が*居場所がある*と感じられること」** — 深く正当な need。だが observable でない（内面）→ claimability ✗。**完全に valid な need。想い 層（0層）に属する。**
- **「地域に*もっと連帯*が要る」** — real な need。だが closable でない（無限定）→ claimability ✗。**valid。開いた Question のまま。**
- **「この人が*悲しみを悼める*こと」** — real。だが閉じる gap でない → claimability ✗。**valid。**

**核心の洞察：Claimability は need の *worth（重要さ・想いの強さ）* を判定しない。*form（gap 形か）* だけを判定する。** ゆえに**最も深い・最も想い を帯びた need（内面）ほど claimability に失敗する**——そしてその失敗こそが**想い の保護**である（Claim/スコアへ還元されず、開いたまま/未介入で残る）。

→ **Claimability ⊥ 想い。** claimability は「どれだけ重要/強いか」を一切問わず「gap 形か」だけを問う。**これが 想い 非測定を*作動させる*膜である**（内面 need は form-test で落ち、想い 層に留まる）。

---

## 5. WAZIS は非 claimable な Need を Claim へ強制せず開いたまま保持する場になるか — Yes

**分業:**
- **WAZIS は*すべて*の Question/Need を host する**（claimable も非 claimable も）。開いたまま保持。
- **Dan-Go は claimable な Need *だけ*を扱う**（{observable, closable, dignity-safe} を満たすもの）。
- **非 claimable な Need は Claim へ強制されない**（強制＝内面に observed/required を捏造＝Saiyan Scouter 禁止）。**WAZIS で開いた Question のまま**、または **想い 層（0層）で未介入**のまま。

→ ユーザーの仮説**「Claimability が WAZIS/Dan-Go の真の境界」は正しい**。ただし新境界でなく、boundary review の **commit-line（asking↔doing）**・gap-to-claim の **partial function の定義域**の、**正確な述語名**。WAZIS は上流（全部を開く）、Dan-Go は下流（claimable のみ commit）——その**通過条件が claimability**。

---

## 6. dignity / 想い 非測定 / Claim=Gap を保つか — すべて Yes

- **dignity:** claimability の 3 条件の 1 つが dignity-safe。非 dignity-safe は弾かれ Claim へ強制されない。✓
- **想い 非測定:** claimability は **form で分類し worth で分類しない**（§4）。need の重要さ/強さを一切測らない。非 claimable（多くは最も 想い を帯びる内面 need）は**開いたまま/未介入**——測られず・ランク付けされず。✓（claimability こそ 想い を 0層 に留める作動機構）
- **Claim = Gap:** claimability ＝「well-formed な gap（observed/required/missing）かつ dignity-safe か」＝**gap-test そのもの**。Claim=Gap を逐語的に前提。✓

---

## 7. Claimability は WAZIS と Dan-Go の最小の共有意味境界か — Yes

- 共有**言語** ＝ gap（observed/required/missing）（gap-to-claim review）。
- 共有**境界** ＝ claimability（何が渡るかを決める述語）。
- claimability は **単一の binary 述語**（claimable: yes/no）で、**ちょうど 3 条件**に還元され、3 つとも**既存**。**いずれを落としても Dan-Go が一部を reject するから 3 つ必要**、**3 つで十分**。→ **これより小さい共有境界は無く、これより大きいものは要らない。最小。**

---

## 8. 削除優先の番人 — Claimability を「スコア」にしない

**Claimability は binary（充足/非充足）に留めること。** 「どれだけ claimable か（0–100）」のような**スケール化は禁止**——それは 想い/need の measurement・ranking を密輸し（§4 の form-vs-worth を破り）、想い 非測定・無スコアに反する。claimability は**門（通る/通らない）**であって**目盛り**でない。新フィールド・新層・スコアを**足さない**（lens のまま）。

---

## 9. 統合（一文で）

**Claimability は実在するが新しくない——「この Need は Dan-Go が reject しない Claim を生むか」の名前であり、CLAIM_FORMAT の必須 gap 構造＋『未観測を観測済みとしない』規則＋constitution_check＋reject 決定に既に符号化済みで、ちょうど {observable, closable, dignity-safe} の 3 条件（2 つは observed/required/missing、1 つは constitution_check）に還元され、feasibility は含まない（Article 1：実行可能性は交渉で扱う）；Need は real で正当なまま claimability に失敗しうり（内面・無限定・関係的 need＝最も 想い を帯びるものほど落ちる）、その失敗は error でなく 想い の保護であって、claimability は need を worth でなく form で分類するがゆえに 想い 非測定を*作動させる膜*であり、WAZIS は全 Question/Need を開いたまま host し Dan-Go は claimable だけを commit する——その通過述語が claimability で、これは新境界でなく commit-line／partial-function の定義域の正確な名であり、dignity・想い 非測定・Claim=Gap をすべて保ち、3 条件すべて既存ゆえ WAZIS と Dan-Go の最小の共有意味境界であって、binary に留める限り（スコア化しない限り）新機構・新層・ガバナンスを一切足さない。**

---

*本書はレビューであり、実装・コード・既存ファイル修正を含まない。Dan-Go/WAZIS を再設計せず・新概念/層/ガバナンス/スコアを足さず・削除を優先した。Claimability は新機構でなく既存プロパティ（CLAIM_FORMAT＋constitution_check＋reject）の連言の名（lens）。3 条件＝{observable, closable, dignity-safe}、feasibility 非含。form で分類し worth で分類しない＝想い 非測定の作動機構。binary に留めること（スコア化禁）。判定は kernel に基づく仮説であり最初の Reality Feedback で反証されうる。*
