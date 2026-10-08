# Gap-to-Claim Review / 差異→Claim レビュー

- Date: 2026-06-22
- Scope: 公開された Need を Dan-Go Claim（observed/required/missing）へ**機械的に**変換できるか
- 種別: **レビューのみ**。実装・コード・既存ファイル修正を含まない。
- 規律: Dan-Go/WAZIS を再設計しない・新概念/ガバナンスを足さない・削除を加算より優先。
- 接地: `FIRST_CLAIM_REVIEW`（最小 Claim＝observed/required/missing/dignity_check/need_ref、missing＝gap かつ RF 物差し）／`OBJECT_REDUCTION_REVIEW`／Dan-Go `CLAIM_FORMAT`。

> **見出し:** Need→Claim は **partial function（部分写像）**である。**(1)** 量が定まった gap-need は**ほぼ機械的**に変換できる（例A）。**(2)** 量/質が未定の need は、**need-holder による1つの明確化ステップ**（閾値/受理基準）を要する（例B/C）。**(3)** gap でない need（内面/想い・無限定・関係的・強制的）は**変換に失敗する——そしてその失敗は正しい**（それらは 想い 層に属するか、開いた Question のまま留まるべきで、Claim にしてはならない）。observed/required/missing は **gap そのもの**であり、かつ **WAZIS と Dan-Go の共有言語**（普遍・中立な need の論理形）である。

---

## 1. 3 例の変換

### 例A：こども食堂が「お米 10kg 不足」と公開表明
1. **Question:** 「〇〇食堂のお米不足は閉じうるか?」
2. **Need:** 次回食事会のお米が不足。
3. **変換:** observed「〇〇食堂はお米 10kg 不足と公開表明（出典 URL）」／required「同食堂が 10kg のお米を有する」／missing「お米 10kg」
4. **完全か:** ✅ 完全。gap が量で定義済み（10kg）。
5. **RF:** 「10kg は今届いたか?」を食堂が確認。
6. **RF 型:** executed（10kg 配達）/ partial（5kg）/ failed（届かず）/ impossible（需要既充足・連絡不能）。
→ **最も機械的**：need が既に量を含むため、observed＝表明、required＝gap 充填後、missing＝表明された量。

### 例B：こども食堂が「絵本」を募集
1. **Question:** 「〇〇食堂の絵本募集は満たせるか?」
2. **Need:** 子ども向け絵本が欲しい。
3. **変換:** observed「〇〇食堂は絵本を募集と公開表明」／required「絵本を有する——**ただし何冊/どの種類?未定**」／missing「絵本——**量/種類未定**」
4. **完全か:** ⚠️ **不完全**。gap が質的で**量化されていない**＝RF 物差しが曖昧。「絵本が来た」が executed か partial か判定不能。
   → **need-holder が閾値を定義**すれば完全化（例「3–6 歳向け絵本 10 冊」）。**定義するのは食堂であって WAZIS でない**（consent・想い非測定を保つ）。
5. **RF:** 閾値次第。未定なら曖昧／定義済みなら crisp。
6. **RF 型:** 閾値があれば executed/partial/failed/impossible が明確。
→ **教訓：open-ended な need は、まだ完全な Claim でない。閾値（need-holder 定義）を要する。**

### 例C：支援団体が「公開ガイドの翻訳」を必要
1. **Question:** 「〇〇団体のガイド G の翻訳ニーズは満たせるか?」
2. **Need:** ガイド G を言語 L に翻訳。
3. **変換:** observed「団体は G（日本語）の L 訳が無いと公開表明（G は N 頁）」／required「G が L で存在し、団体が使える品質である」／missing「G の L への翻訳」
4. **完全か:** ◯ **scope は機械的に定義可（G→L）、だが完了条件に質的判断（『使える品質』）を含む**。missing＝scope（機械的）＋受理（need-holder が判定）。
5. **RF:** 「G は L で存在し、団体が受理/利用するか?」を団体が確認。
6. **RF 型:** executed（訳了・受理・公開）/ partial（要改訂・一部）/ failed（未了・却下）/ impossible（需要消失・外部訳不可）。
→ **教訓：scope は機械的、完了条件に質的受理（need-holder 判定）が入る。**

---

## 2. すべての公開 Need は observed/required/missing に還元できるか — **No**

還元に**失敗する need の種類**（いずれも失敗が*正しい*）:

| 失敗する need | なぜ失敗するか | どこへ行くべきか |
|---|---|---|
| **無限定/量化不能**（「もっと支援を」「認知を」） | required が定義不能→missing 無し→RF 物差し無し | 開いた Question のまま（まだ Claim でない） |
| **内面/想い 形**（「安心を感じたい」「信頼」「幸せ」） | required が公開観測可能な事実でない。内面は測れない | **想い 層（0層）・未介入**（Dan-Go が管理してはならない＝失敗が正しい） |
| **過程/関係的**（「継続的なボランティア」「提携」） | 離散の閉鎖状態が無い→単一 RF 不能 | 離散 sub-need へ分解すれば Claim 化可。関係自体は Claim でない |
| **強制/尊厳侵害**（「○○を排除」） | dignity_check 不通過 | **却下**（正しく弾かれる） |
| **非公開観測**（「私的に X が要る」） | observed が検証可能な公開事実にならない（未観測を観測済みとしない） | 当事者の self-translation を待つ／非公開のまま |

**核心：observed/required/missing は classifier（分類器）である。** claimable な gap（離散・観測可能・閉鎖可能・尊厳安全）を**通し**、非 claimable（内面/想い・無限定・関係・強制）を**弾く**。**弾かれた need は error でなく「Claim でない——別の場所（想い 層、または開いた Question）で扱う」。** これは想い非測定・dignity・kernel と完全整合し、削除優先（非 gap を無理に Claim 化しない・そのための機構を作らない）。

---

## 3. observed/required/missing は最小の*完全な* Claim か — Yes（条件付）

- **gap の意味論としては完全**：observed＋required＋missing が gap を完全に指定。
- **完全性の条件**：missing が**定まった閉鎖条件（量/閾値/受理基準）**を持つこと。例A は量で満たす；例B は閾値が要る；例C は受理基準が要る。**missing が真の物差しでなければ Claim は不完全**（crisp な RF を生まない）。
- **valid かつ actionable には**＋dignity_check（法）＋need_ref（錨）。よって最小の*完全 valid* Claim＝5 要素（FIRST_CLAIM_REVIEW）。
- 形式上 missing＝required−observed（導出可）だが、**RF 物差しゆえ明示する**。

→ **observed/required/missing（＋dignity＋need_ref）が最小の完全 Claim。** 足すものは無い。

---

## 4. Dan-Go の「Claim ＝ Gap」を保つか — Yes（逐語的）

observed/required/missing は Dan-Go の定義そのもの（CLAIM_FORMAT：「missing_conditions＝observed と required の gap」）。**再定義も追加もしない。** Claim＝Gap を逐語的に保存。

---

## 5. WAZIS と Dan-Go の共有言語を作るか — Yes（中立な gap 言語）

- **gap（observed/required/missing）が lingua franca。** WAZIS は gap を**問い**として発見（「この gap は閉じうるか?」）、Dan-Go は gap を**Claim**として表現、RF は gap を**測る**（閉じたか?）。**missing は三者が共有する物差し**（WAZIS の問い＝missing は閉じうるか／Dan-Go の Claim＝missing を狙う／RF＝missing が満ちたか）。
- **重要（OBJECT_REDUCTION との整合）：これは WAZIS 所有の Dan-Go 寄りスキーマを再導入しない。** observed/required/missing は need の**普遍的論理形**であって Dan-Go 固有でない（OSS：壊れている/動く/修正；NPO：欠く/有る/その物）。**共有されるのは gap 概念（中立）**であり、各 binding がそれを**native 形にレンダー**する。よって「共有言語」は中立で、OBJECT_REDUCTION の「中間の内容スキーマを WAZIS が所有しない」と矛盾しない。
- boundary review の共有 DNA（dignity・RF 語彙・想い0層・DID）に、**gap（observed/required/missing）という意味論的共有契約**が加わる。

---

## 6. 正直な限界（隠さない）

- **完全に機械的ではない**：量化済み gap-need は機械的だが、未定 need は need-holder の明確化ステップ（閾値/受理）を要し、非 gap need は失敗する（§1–2）。**明確化は need-holder が行う**（WAZIS が量や「正解」を決めない＝想い非測定）。
- **仮想例**。量（10kg・N 冊・N 頁）も実在主張でない。実 observed/required は人間が現行公開告知から起こす。
- **observed は公開で表明された検証可能事実に限る**（未観測を観測済みとしない）。
- benefit は org レベル（gap 閉鎖）で究極受益者でない＝#002 以降。Reach Gap 非解決。

---

## 7. 統合（一文で）

**公開 Need の Dan-Go Claim への変換は partial function であり、量が定まった gap-need（例A：お米10kg）はほぼ機械的に observed/required/missing へ落ち、量/質が未定の need（例B：絵本、例C：翻訳）は need-holder が閾値/受理基準を定義する1ステップで完全化し、内面/想い・無限定・関係的・強制的な need は変換に失敗する——その失敗は error でなく、observed/required/missing が claimable な gap だけを通し非 claimable を 想い 層や開いた Question へ送り返す classifier として正しく働いている証拠である；missing は gap であると同時に RF 物差しを兼ね、量/閾値/受理基準という定まった閉鎖条件を持つ限りで Claim を完全にし、dignity_check と need_ref を加えた observed/required/missing が最小の完全 valid Claim であり、これは Dan-Go の Claim＝Gap を逐語的に保ち、gap（need の普遍的論理形）を WAZIS と Dan-Go の中立な共有言語（missing＝共有物差し）として確立しつつ、WAZIS 所有のスキーマを再導入しない（各 binding が native にレンダーする）。足すべき機能・概念・ガバナンスは無い。**

---

*本書はレビューであり、実装・コード・既存ファイル修正を含まない。Dan-Go/WAZIS を再設計せず・新概念/ガバナンスを足さず・削除を優先した。Need→Claim は partial function（量化 gap＝機械的／未定＝need-holder 明確化／非 gap＝失敗＝想い層へ）。observed/required/missing＝最小の完全 gap・Claim＝Gap を逐語保存・中立な共有言語。仮想例は実在主張でなく、実 observed/required は人間が現行公開告知から起こす。判定は kernel に基づく仮説であり最初の Reality Feedback で反証されうる。*
