# First Claim Review / 最初の Claim レビュー

- Date: 2026-06-22
- Scope: Musubie の specific need を、observed/required/missing を保つ**最小の Claim 表現**にする
- 種別: **レビューのみ**。実装・コード・既存ファイル修正を含まない（Claim 例は spec の図示であってコードでない）。
- 規律: Dan-Go/WAZIS を再設計しない・新概念を足さない・削除を加算より優先。
- 接地: Dan-Go `CLAIM_FORMAT.md`（observed/required/missing_conditions、constitution_check）／前 `MUSUBIE_NEED_FIRST_REVIEW`（need-first）。

> **見出し:** 最小の Claim は **observed ＋ required ＋ missing（gap）＋ dignity_check ＋ need_ref** の 5 要素。中核は 3 行（observed/required/missing）で、**missing_conditions は「gap（Dan-Go の Claim の本質）」であると同時に「Reality Feedback の物差し（何をもって閉じたとするか）」を兼ねる**——だから最小の Claim でも missing は明示せねばならず、これが need→Claim が clean な RF を生む理由（charibon が vague な transaction-RF だったのと対照）。

---

## 1. 最小の Claim 表現（irreducible fields）

| field | なぜ irreducible か | 落とせるか |
|---|---|---|
| **observed**（観測） | 現状の検証可能な事実（＝公開された need 宣言）。gap の一方の端 | ✗ |
| **required**（要件） | need が満たされた状態。gap の他方の端 | ✗ |
| **missing**（gap） | required − observed ＝ 差異。**かつ RF の物差し** | ✗（§5） |
| **dignity_check** | 唯一の法。`violates_dignity:false / uses_coercion:false` | ✗（憲法） |
| **need_ref** | 公開された need 宣言への link。Claim を Need に錨で繋ぐ（need-first の保証） | ✗（さもなくば unanchored） |

付随（trivial scaffolding）: `claim_id`（識別子）、`claim_type: interrogative`（WAZIS Question 由来）。

**落とせるもの（§3）:** risks / possible_contributions / decision / version / created_at 等——導出可能か後付け。

> 形式上は missing ＝ observed と required の差ゆえ「データの irreducible は observed＋required の 2 つ」だが、**RF 生成のため missing は明示する**（§5）。ゆえに「3 行を保つ」が正しい。

---

## 2. 仮想 Musubie 例（hypothetical・実在主張でない）

**例 A：お米（rice shortage）**
```
Claim（最小）
- need_ref : 〇〇こども食堂の「お米が不足」公開告知 <公開URL>
- observed : 〇〇こども食堂は次回の月次食事会に出すお米が不足していると公開で表明している（出典: <URL>）
- required : 同食堂が次回食事会分のお米（約10kg）を有している
- missing  : お米 約10kg          ← gap ＝ RF の物差し
- dignity_check : violates_dignity=false / uses_coercion=false
```

**例 B：絵本（picture books）** — observed「絵本が不足と公開表明」／required「子ども向け絵本 N 冊を有する」／missing「絵本 N 冊」。
**例 C：備品（freezer）** — observed「冷凍庫が無い/故障と公開表明」／required「稼働する冷凍庫 1 台」／missing「冷凍庫 1 台」。

いずれも**名詞と数量を差し替えるだけ**で同型。これが「最小」である所以。

---

## 3. 省いたもの と 理由

- `possible_contributions` — missing から導ける（お米 → funding/現物; 冷凍庫 → funding/備品）。Claim に固定しなくてよい。
- `risks` — 任意。最小では空でよい（小さく安全な need ゆえ）。
- `decision`（negotiate/execute/…） — 交渉の*出力*であって Claim の*構成要素*でない。
- `version` / timestamp — 後付けの台帳メタ。最小の意味論に不要。

→ **observed/required/missing/dignity/need_ref 以外は、最小の Claim から削除できる。**

---

## 4. 4 基準評価

| 基準 | 評価 | 理由 |
|---|---|---|
| **Visibility** | ★★★ | observed/required/missing が gap を 3 行で**完全に可視化**。誰でも「何が・どれだけ欠けるか」を一目で見える |
| **Simplicity** | ★★★ | 中核 3 行＋dignity＋ref。各 field 1 文。**認知負荷最小**・同型で複製容易 |
| **Public observability** | ★★★ | observed が**公開出典**を引く。Claim 全体が公開・監査可能。gap は第三者が独立検証できる（食堂の公開告知を確認） |
| **Reality Feedback generation** | ★★★ | **missing が成功条件を厳密に定義**するため RF が crisp: 「missing は今満たされたか?」→ executed（お米10kg 届き gap 閉鎖）/ partial（一部）/ failed（届かず）/ impossible（需要既充足・連絡不能）。全て明確に観測可能 |

---

## 5. 鍵 — missing_conditions は「gap」かつ「RF の物差し」

最小の Claim で最も load-bearing なのは **missing**。それは二役を一身に兼ねる:
1. **gap**（Dan-Go の Claim の本質＝差異）。
2. **Reality Feedback の物差し**（何が満たされれば「閉じた」か、の唯一の定義）。

→ ゆえに **need→Claim は clean な RF を必ず生む**（missing が yardstick を与える）。逆に charibon は missing（specific gap）が無いため、RF が「寄付額」という transaction 受領に留まった（MUSUBIE_NEED_FIRST_REVIEW §2）。**「最小の Claim が RF を生む」のは、missing が RF 仕様そのものだから。** これが need-first を選ぶ構造的理由。

---

## 6. Dan-Go / WAZIS への忠実性

- **Dan-Go:** Claim ＝ gap（observed/required/missing）をそのまま保つ。constitution_check ＝ dignity。need-first（observed は公開された need 宣言）。→ 全段忠実。
- **WAZIS:** この最小 Claim は、WAZIS の handoff edge（consent＋dignity-check＋need_ref）が Dan-Go-native へ写ったもの。WAZIS の開いた問い「この gap は閉じうるか?」が observed/required/missing に結晶し、RF（missing 充足の観測）で現実が裁定する。→ 忠実（OBJECT_REDUCTION の handoff edge と整合）。
- 想い非測定・無裁定も保たれる（Claim は gap の宣言であって、想いの強度も「正解」も含まない）。

---

## 7. 正直な限界（隠さない）

- **仮想例。** 数量（10kg・N 冊）も含め実在主張でない。実際の observed/required は**食堂の現行公開告知から人間が起こす**（私は断定しない）。
- **observed は「公開で表明された」事実に限る**（未観測の内心や推定を observed に入れない＝Dan-Go の「未観測を観測済みとしない」）。
- benefit は食堂レベル（gap 閉鎖）で究極受益者でない＝#002 以降。
- missing の数量は**食堂が定義する**（WAZIS が測らない・想い非測定）。

---

## 8. 統合（一文で）

**Musubie の specific need を保つ最小の Claim は observed＋required＋missing（gap）＋dignity_check＋need_ref の 5 要素で、中核は 3 行（例：observed「〇〇食堂がお米不足を公開表明」／required「次回分の米約10kgを有する」／missing「米約10kg」）に過ぎず、名詞と数量を差し替えれば絵本・備品にも同型適用でき、visibility・simplicity・public observability・RF generation の 4 基準すべてで最良である——その鍵は missing_conditions が gap（Dan-Go の Claim の本質）であると同時に Reality Feedback の物差し（何をもって閉じたとするかの唯一の定義）を兼ねる点にあり、これこそ need→Claim が clean な RF を必ず生み（charibon の transaction-RF と対照）、Dan-Go（Claim＝gap）にも WAZIS（開いた gap を現実が裁定）にも全段忠実である理由である。残る作業は人間が食堂の現行公開告知から observed/required を起こすことだけで、足すべき field は無い。**

---

*本書はレビューであり、実装・コード・既存ファイル修正を含まない。Dan-Go CLAIM_FORMAT（observed/required/missing_conditions・constitution_check）に接地。最小 Claim ＝ observed＋required＋missing＋dignity_check＋need_ref。鍵: missing は gap かつ RF 物差し。仮想例は実在主張でなく、実 observed/required は人間が現行公開告知から起こす。判定は kernel に基づく仮説であり最初の Reality Feedback で反証されうる。*
