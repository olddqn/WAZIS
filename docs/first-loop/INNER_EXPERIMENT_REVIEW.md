# Inner Experiment Review / 内部実験レビュー

- Date: 2026-06-22
- Scope: Question #001 のループの**空の中心**を埋める、最小の実世界 inner experiment を同定する
- 種別: **レビューのみ**。実装・コード・既存ファイル修正を含まない。
- 規律: **WAZIS/Dan-Go を再設計しない・ガバナンスを足さない・新概念を足さない・削除を加算より優先。**
- 接地: QUESTION_001_SELECTION（C3/C4/C7）／Dan-Go の 11 Contribution 型（code/compute/legal/translation/housing/funding/social_reach/reputation/care/knowledge/coordination）／FIRST_CASE_CANDIDATES（組織レベル・個人非接触・安全ゲート）。

> **見出しの結論:** 最小の inner experiment は **「人」でなく「情報」を扱うものである。** 具体的には、**公益組織/プロジェクトが*既に公開で要請している*、小さな情報貢献（translation または knowledge/documentation を 1 件）を Dan-Go 経由で満たし、その組織が公開で受領/利用を確認する**こと。これは要件をほぼ全て同時に満たす——脆弱な個人に一切触れず（テキストを扱う）、consent が最も明瞭（公開要請された公開文書）、Reality Feedback が速く公開で観測可能、Dan-Go の contribution 型に直接写り、30 日で十分閉じ、**process RF（パイプが動いた）と need RF（実在の組織の実需が満たされた）の両方**を生む。食料配布（C3）より速く・観測明瞭で、同等に dignity 安全。

---

## 1. 要件が含意するもの

| 要件 | 含意 |
|---|---|
| 実 Reality Feedback を要する | 出力が観測される実行為（漠然とした願望でない） |
| 公開観測可能 | 成果物または受領確認が**公開**される経路 |
| dignity リスク低 | 脆弱な個人に触れない → **情報を扱い、人を扱わない** |
| consent 境界が明瞭 | 当事者が**既に公開で要請**＝同意内蔵。私的個人データを含まない |
| 脆弱な個人への直接接触なし | counterparty は**組織/プロジェクト**であって個人でない |
| Dan-Go 実行可能 | 11 contribution 型の*低摩擦・速・観測明瞭*なもの＝**translation / knowledge** |
| New Question を生む | どの outcome も次の問いを開く（§7） |
| TTFCL 最小 | 受領が**公開・即時**の経路を選ぶ（私的メール往復を避ける） |

→ 含意の合流点: **公益組織/プロジェクトの「既に公開された具体的で小さな情報要請」を満たす translation/knowledge 貢献。** これが要件空間の中心。

---

## 2. 最小の viable な inner question

> **「〔特定の公益組織/プロジェクトが既に公開で要請している、特定の小さな情報成果物 — 例: 公開文書 1 件の翻訳、または 1 件の文書/知識〕は、Dan-Go 経由の貢献で満たされ、その組織に公開で受領・利用されるか?」**

代表例（exemplar）: 難民支援・公衆衛生・公益系の NPO/プロジェクトが、ある**公開文書**（権利ガイド・手引き・健康説明資料など）を、組織が欠く言語へ**翻訳してほしい**と公開で要請している——その翻訳を貢献し、組織が受領/公開を確認する。

なぜ translation/knowledge か（11 型の中で）:
- **人に触れない**（テキストを扱う）→ dignity リスク最低・脆弱者非接触を自動充足。
- **consent 最明瞭**（公開要請された公開文書・私的データなし）。
- **速い**（1 文書の翻訳は数日）。
- **観測明瞭**（成果物が公開でき、組織の確認も公開）。
- funding/housing/care（金・人）より低摩擦、code/compute より need 信号が明確、coordination/social_reach より RF が観測しやすい。

**削除優先の注:** 既存の Dan-Go contribution 型と既存の WAZIS 構造（Question→handoff→RF→New Question）だけを使う。新概念・新型・ガバナンスを足さない。

---

## 3. Reality Feedback はどう見えるか

**二層の RF が同時に出る:**

- **Process RF（ループが動いたか）:** 6 ステップ（Question → Binding/Transformation → Dan-Go Claim → Contribution[翻訳提出] → Reality Feedback → New Question）が公開記録される＝パイプが機械的に通った。
- **Need RF（実需が答えられたか）:** 組織の応答。

| outcome | 内容 | 有効か |
|---|---|---|
| **completed** | 組織が受領し、公開/利用する（する意思を確認） | ✅ 有効 RF |
| **partial** | 受領したが要改訂/一部のみ利用可 | ✅ 有効 RF |
| **failed** | 無応答/辞退/利用不可 | ✅ 有効 RF |
| **impossible** | 要請が既に閉じている/組織に到達不能/外部貢献を受け付けない/Dan-Go が Claim を受けられない | ✅ 有効 RF（最も正直で、infra の実態を露わにする） |

**「reality が答えること自体が success」**（Question #001 の成功条件）に完全合致。failed/impossible でも成立。

---

## 4. 他候補より優れる理由

| 候補 | 対比 |
|---|---|
| **食料配布（C3）** | need は viscerally「救済」だが、RF が**遅く・間接**（誰が食べたか観測困難）、生鮮物流、30 日内の閉鎖が不確実。**翻訳は速く・観測明瞭・物流ゼロ。** |
| **個人への直接支援** | 脆弱な個人接触＝dignity/consent 最大複雑。**翻訳は人に触れない。** |
| **OSS の修正のみ** | 速いが need 信号が「documentation」寄り。**公益組織の*明示された実需*の方が need RF が明確**（ただし§8: 受領経路は公開・即時を選ぶ）。 |
| **大義（難民の経済的自立 / AI 高齢者ケア）** | 巨大・遅い・dignity リスク高・閉じない。**翻訳は境界づけられ閉じる。** |
| **hollow plumbing test** | 中心が空＝救済ゼロの「成功」。**翻訳は実在組織の実需を運ぶ＝中心が空でない。** |

→ 翻訳/知識貢献は、**速度・観測性・consent 明瞭・dignity 安全・need の実在性**の全軸で、最小かつ充足的。

---

## 5. 30 日で閉じるか

**閉じる。** 律速は組織/プロジェクトの受領確認であって翻訳作業ではない（翻訳は数日）。**公開・応答性の高い受領経路（活発な公開要請ページ/issue tracker）を選べば**受領確認も期間内。**かつ、30 日内に無応答でも、それ自体が valid RF（pending/failed）** であり、ループは「reality が答えた（沈黙という形で）」として閉じる。よって **TTFCL は 30 日で上限づけられる**——outcome に関わらず。

---

## 6. process RF と need RF の両方を生むか

**両方生む（これが hollow との決定的差）:**
- **process RF**: 6 ステップの公開記録 → WAZIS↔Dan-Go のパイプが現実で一度動いた（Question #001 の Title への答え）。
- **need RF**: 組織の受領/利用確認 → 実在の組織の実需（文書の翻訳）が現実で満たされた（中心の救済）。

中心が実需ゆえ、「パイプは証明したが誰も助けていない」を回避する（QUESTION_001_FINAL_REVIEW の懸念の解消）。

---

## 7. 自然に Question #002 になるもの（outcome 分岐＝非終端の実演）

どの outcome も次の問いを開く（non-termination）:

- **completed →** 「翻訳は**意図した読者に実際に届いた/役立ったか**?」（究極受益者へ一歩近い need RF）／または「**Dan-Go 以外の binding**（OSS/研究/別 NPO）で同型の貢献を運べるか?」（中立性の反証・U2）。
- **partial →** 「何が**部分的にしか使えなかった**のか——その gap を WAZIS はより鋭い問いとして surface できるか?」
- **failed（無応答）→** 「実装先/組織が**外部貢献を受領・確認する**には最小限何が要るか?」（実摩擦を露出）。
- **impossible（生きた binding/組織が無い）→** 「**Dan-Go が WAZIS 由来の Claim を受け実行できる**最小条件は何か?」（infra gap を露出——これ自体が極めて価値ある正直な RF）。

→ **どの結果でも #002 が自然に開く**＝WAZIS が「問いを生かし続ける」protocol であることの実証。

---

## 8. 正直な限界（隠さない）

- **特定の生きた組織/要請は捏造しない。** 推奨は*形（class）*——「公益組織の既存公開要請への小さな translation/knowledge 貢献」。**現行の公開要請の実在・稼働は人間が検証する**（知識カットオフ・未検証。SELECTION §5・FIRST_CASE_CANDIDATES の手順に同じ）。
- **need RF は組織レベルであって究極受益者レベルでない。** 「文書が翻訳され組織が使う」は実需だが、「その文書を読む人が助かった」は #002 以降。**#001 は一歩手前で止める——それが dignity 安全と速度の代償でなく*手段***。
- **Reach Gap は解決しない。** 安全ゲートを通る情報貢献は、最も孤立した声を含まない（SELECTION §6 と同じ）。
- **「使われた」は WAZIS が測らない。** 組織が確認する（想い非測定・RF は集計でなく個別観測。RF_INTERPRETATION）。
- **受領経路の latency に注意。** 私的メール往復は TTFCL を伸ばす——**公開・即時の受領経路を選ぶ**（§5）。

---

## 9. 統合（一文で）

**Question #001 のループの空の中心を埋める最小の inner experiment は、人でなく情報を扱うもの——すなわち、公益組織/プロジェクトが既に公開で要請している小さな translation または knowledge 成果物を 1 件、Dan-Go 経由（既存 contribution 型のみ）で満たし、その組織が公開で受領を確認すること——であり、これは脆弱な個人に一切触れず（テキストを扱う）、consent が公開要請ゆえ最も明瞭で、Reality Feedback が速く公開で観測可能で、30 日内に（無応答でも valid RF として）閉じ、process RF（パイプが動いた）と need RF（実在組織の実需が満たされた）の両方を生み、completed/partial/failed/impossible のいずれの結果も自然に Question #002（究極受益者へ一歩／第二 binding／受領摩擦／infra 条件）を開く；食料配布より速く観測明瞭で、同等に dignity 安全であり、中心が実需ゆえ「パイプは証明したが誰も助けない」を回避する。残る唯一の作業は AI でなく人間が現行の公開要請の実在を検証することだけであり、足すべき機能・概念・ガバナンスは無い。**

---

*本書はレビューであり、実装・コード・既存ファイル修正を含まない。WAZIS/Dan-Go を再設計せず・新概念/ガバナンスを足さず・削除を優先した（11 型のうち最小の情報貢献に絞り、人接触を削除）。Dan-Go の既存 contribution 型と既存 WAZIS 構造のみを使用。実在組織の確定は人間の検証を要し、私は稼働を断定しない。判定は TTFCL/dignity 主軸の仮説であり、最初の Reality Feedback で反証されうる。推奨: 公益組織の公開要請への最小 translation/knowledge 貢献。*
