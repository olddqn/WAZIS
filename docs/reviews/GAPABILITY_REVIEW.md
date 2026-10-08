# Gapability Review / Gap 可能性レビュー

- Date: 2026-06-22
- Scope: claimability は更に gapability へ還元されるか。dignity は gapability の一部か、後段の憲法ゲートか
- 種別: **レビューのみ**。実装・コード・既存ファイル修正を含まない。
- 規律: Dan-Go/WAZIS を再設計しない・新概念/機構を足さない・削除を加算より優先。
- 接地: `CLAIMABILITY_REVIEW`（本書が refine）・`GAP_TO_CLAIM_REVIEW`・Dan-Go `CLAIM_FORMAT`（observed/required/missing・constitution_check）・Article 10（dignity ＝唯一の法・常時優先）。

> **見出し: ユーザーの指摘は正しい。Claimability は fundamental でなく、Gapability が fundamental である。** Gapability ＝ **{observable, closable}** ＝ gap の*形*の test（CLAIM_FORMAT の observed/required/missing が well-formed か）。**dignity は別物**——あらゆる Dan-Go 行為に適用される**普遍の憲法ゲート（constitution_check）**で、**WAZIS と Dan-Go の両側が共有する天井**であり、gap の*形*でなく**閉じる*手段*に適用される。**決定的論証：gap は dignity 中立である。同じ gap（例「食堂はボランティアが要る」）は、強制で閉じれば dignity-fail、招待で閉じれば dignity-safe——ゆえに dignity は gap の属性ではありえず、行為の check でなければならない。** よって **gapability が真の膜（membrane）**、dignity は両側共有の天井（膜でない）。本書は CLAIMABILITY_REVIEW が dignity を膜に束ねていた点を**訂正**する。**削除優先**（dignity を束から外す＝還元）。

---

## 1. Claimability は gapability へ更に還元できるか — Yes

- CLAIMABILITY_REVIEW: claimability ＝ {observable, closable, **dignity-safe**}。
- だが dignity は gap の形の条件でなく、**あらゆる行為への普遍の制約**（Article 10：常時優先）。**gapability（形）と dignity（法）は直交。**
- → claimability ＝ **gapability（{observable, closable}）AND dignity-gate**。**fundamental な gap-property は gapability**。dignity を束ねていたのが claimability の冗長性。**還元：claimability → gapability ＋（別の)dignity ゲート。**

---

## 2. Gapability は {observable, closable} だけか — Yes

- **observable:** observed が検証可能な公開事実（gap の「現状」端が実在）。
- **closable:** required＋missing が定まった閉鎖条件（yardstick）を持つ gap。
- これで gap は尽きる。**dignity を外す**（§3）。feasibility は元から除外（Article 1）。

**GAP_TO_CLAIM の 5 失敗様式の再分類:**

| 失敗する Need | 破る条件 | 区分 |
|---|---|---|
| 無限定 | closable ✗ | **gapability** |
| 内面/想い | observable ✗ | **gapability** |
| 関係/過程 | closable ✗ | **gapability** |
| 非公開観測 | observable ✗ | **gapability** |
| **強制/尊厳侵害（例「○○を排除」）** | **dignity ✗（observable・closable は ◯）** | **dignity（別ゲート）** |

→ **5 つ中 4 つは gapability 失敗、1 つ（強制）は *gapable な need* の dignity 失敗。** これが「gapability ⊥ dignity」の証拠。dignity を gapability から外すと、gapability ＝ {observable, closable} に純化する。

---

## 3. dignity は gapability に属すか、後段の憲法ゲートか — 後段の普遍ゲート

**dignity は gapability に属さない。三つの理由:**

1. **gap は dignity 中立。** 同じ gap が手段次第で dignity-safe にも -fail にもなる（§4）。属性が手段で変わる以上、それは**行為の check** であって**gap の形の属性**でない。
2. **dignity は普遍・常時。** Article 10「常時優先」。Claim 検証時だけでなく **Contribution・Execution の各行為**で check される（continuous）。gapability は Need→gap の**一度きりの形 test**。**check の種類が違う**（一度・構造 vs 常時・倫理）。
3. **dignity は両側共有。** WAZIS も不可侵条項（dignity 含む）を持つ（boundary review の共有 DNA）。**両側にある以上、両者を分ける*膜*ではありえない**——共有する*天井*である。

→ ユーザーの flow が正確: `Need → Gapability → Claim → Constitution Check（dignity）→ Contribution → Reality Feedback`。dignity は **Claim 後・行為の各点**で効く普遍ゲート。

**注（一般化）:** dignity だけでなく不可侵条項すべて（dignity・consent・objection・withdrawal）が**普遍の憲法ゲート**であって gap-property でない。gapability は純粋に {observable, closable}。

---

## 4. gapable だが dignity に失敗する Need はあるか — Yes（例）

- **「X は腎臓が要る／Y は健康な腎臓を 2 つ持つ」** — gapable（observed：X に無い／required：X が持つ／missing：腎臓 1 つ＝well-formed・観測可能・閉鎖可能）。だが Y から強制摘出で閉じれば **dignity-fail**。**gapable ∧ dignity-fail。**
- **「この住居は新家族のため現入居者の退去が要る」** — gapable（gap は明確）。強制退去で閉じれば **dignity-fail**。
- **「我が組織は競合を貶める必要」** — gapable 風。閉じる手段が他者の尊厳侵害 → **dignity-fail**。
- **「食堂はボランティアが要る」（決定的な例）** — gapable。**強制すれば dignity-fail、招待すれば dignity-safe。同じ gap が手段で分岐する。** → **dignity は gap でなく*手段（Contribution/Execution）*に宿る。**

→ gapability と dignity は直交。**gap は「何が欠けるか」、dignity は「どう閉じてよいか」。**

---

## 5. Dan-Go は需要(need)でなく gap を分類しているか — Yes

- Claim の単位は **gap**（observed/required/missing ＝ Dan-Go の Claim＝Gap）。Dan-Go は **need（想い を帯びた lived なもの）を分類せず、gap（形）を分類する**。
- need は **想い 層（源）に留まり**、当事者が選んで表面化させた **gap だけが Dan-Go に入る**。**Dan-Go は need に決して触れず、gap にだけ触れる。**
- **gapability は、need から gap-form を抽出する膜**（gap が在れば通し、無ければ need を 想い に残す）。

→ **Dan-Go は本質的に gap を分類する（need でなく）。** gapability はその分類の入口述語。

---

## 6. これは 想い 非測定をより良く保つか — Yes（claimability より）

- **gapability は純粋に form（observable, closable）**——dignity の価値判断すら混ざらない。**最も form-only。**
- **Dan-Go は gap を分類し need を分類しない**（§5）ゆえ、**need（想い を帯びた lived なもの）は分類・測定・管理の*対象に一度もならない***——抽出された gap-form だけが対象。need と その 想い は 0層 で未介入。
- claimability は dignity（倫理判断）を束ねていたため「gap-test に価値判断が混じる」誤読を許した。**gapability はそれを外し、純 form に純化**——想い 非測定を**より clean に**作動させる。

→ **gapability は 想い 非測定の最も純粋な作動機構。**

---

## 7. gapability は WAZIS と Dan-Go の真の膜か — Yes

- **膜（membrane）＝ 両側を分け、何が渡るかを決めるもの。** WAZIS は全 need/question を開いたまま host、Dan-Go は **gapable なものだけ** Claim として取る。**渡るか否かを決めるのは gapability（form）。**
- **dignity は膜でない。** 両側が共有する（WAZIS の不可侵条項にも dignity）＝**共有の天井**。両側にあるものは両者を*分けない*。dignity-violating な gapable Claim は Dan-Go に**入ってから** constitution_check で reject される（内部ゲート、Article 3「誰でも Claim を提案できる」＋ decision: reject）——**膜の手前で弾くのでなく、膜の中で弾く**。
- → **真の膜 ＝ gapability（{observable, closable}）。dignity ＝ 両側の天井＋ Dan-Go 内部の reject ゲート。**

---

## 8. 正直な訂正（CLAIMABILITY_REVIEW）

前 `CLAIMABILITY_REVIEW` は dignity を claimability（膜）の 3 条件に**束ねていた**。ユーザーの分離が**より faithful**：dignity は gap の形の属性でなく、**両側共有の普遍ゲートで、閉じる手段に適用される**。よって**膜は gapability（{observable, closable}）に純化**し、dignity は膜から外して天井／内部 reject ゲートに位置づけ直す。**これは加算でなく削除**（束ねを解く）。claimability は依然 valid な*複合語*（gapability ＋ dignity）だが、**fundamental は gapability**。

---

## 9. 削除優先の番人

- **gapability も binary に留める**（observable ∧ closable：満たす/満たさない）。**スケール化禁**（「どれだけ gapable」は need の measurement 密輸＝想い 非測定違反）。
- **gapability を新機構へ reify しない。** それは CLAIM_FORMAT の既存要件（observed/required/missing が well-formed）の名であって、**dignity を束から外しただけ**。Reification Test：「gapability」を消しても Dan-Go は ill-formed gap を Claim にできず、constitution_check が dignity を弾く——何も壊れない＝lens。

---

## 10. 統合（一文で）

**Claimability は fundamental でなく、Gapability ＝ {observable, closable} が fundamental である——gapability は gap の*形*の test（CLAIM_FORMAT の observed/required/missing が well-formed か）であり、dignity はそこに属さず、あらゆる行為に常時適用され WAZIS と Dan-Go の両側が共有する普遍の憲法ゲート（constitution_check）であって、gap の形でなく*閉じる手段*に宿る（同じ gap が強制なら dignity-fail・招待なら dignity-safe ゆえ dignity は gap の属性ではありえない）；GAP_TO_CLAIM の 5 失敗様式は 4 つが gapability 失敗・1 つ（強制）が gapable な need の dignity 失敗で両者の直交を示し、Need は gapable のまま dignity に失敗しうり（腎臓・退去・ボランティア例）、Dan-Go は need（想い を帯びた lived なもの）でなく gap（形）を分類するため need は分類・測定の対象に一度もならず 想い は 0層 に未介入で残る——ゆえに gapability は 想い 非測定を claimability より純粋に作動させ、WAZIS と Dan-Go を分ける真の膜は gapability であり（dignity は両側共有の天井かつ Dan-Go 内部の reject ゲートで膜でない）、これは CLAIMABILITY_REVIEW が dignity を膜に束ねていた点の訂正＝削除であって、gapability を binary に留めスコア化しない限り新機構・新層を一切足さない。**

---

*本書はレビューであり、実装・コード・既存ファイル修正を含まない。Dan-Go/WAZIS を再設計せず・削除を優先した（dignity を膜から外す＝claimability の束ねを解く）。Gapability ＝ {observable, closable}（CLAIM_FORMAT の既存 gap 要件の名・lens）。dignity ＝ 両側共有の普遍ゲート・閉じる手段に宿る・膜でなく天井。gap は dignity 中立（同じ gap が手段で分岐）。Dan-Go は gap を分類し need を分類しない＝想い 非測定の純粋な作動。binary に留めること（スコア化禁）。判定は kernel に基づく仮説であり最初の Reality Feedback で反証されうる。*
