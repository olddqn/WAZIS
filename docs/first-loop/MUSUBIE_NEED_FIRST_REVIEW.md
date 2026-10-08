# Musubie Need-First Review / 需要起点レビュー

- Date: 2026-06-22
- Scope: チャリボンは Dan-Go/WAZIS の kernel を demonstrate するか、単なる donation mechanism か。specific な公開 Musubie need の方が #001B として faithful か
- 種別: **レビューのみ**。実装・コード・既存ファイル修正を含まない。
- 規律: Dan-Go/WAZIS を再設計しない・削除を加算より優先・仮説でなく実需。

> **見出しの判定: ユーザーの指摘は正しい。チャリボンは kernel でなく donation mechanism である。** Dan-Go は **Need → Claim → Contribution → Reality Feedback**（Claim ＝ gap＝差異の宣言）だが、チャリボンは **Contribution → （汎用・常設の）Need**——specific な gap も Claim も無く、RF は「寄付額」という transaction 受領であって「need が満たされた」ではない。**前回 `MUSUBIE_NEED_DISCOVERY` は TTFCL/RF clean さ（利便性）を過大評価し、kernel fidelity を過小評価していた。訂正する。** → **specific な公開 need（特定こども食堂の公開された具体的不足）の方が決定的に faithful** であり、#001B はそれにすべき。チャリボンは fallback の donation 手段に降格。

---

## 1. 構造診断 — チャリボンは Dan-Go の flow を反転している

- **Dan-Go kernel:** `Need（gap の宣言）→ Claim（observed/required/missing）→ Contribution（gap を充填）→ Reality Feedback（gap が閉じたか）`。出発点は**specific な need/差異**。
- **WAZIS kernel:** `開いた問い（gap 状）→ 変換（現実応答可能化）→ Reality Feedback（現実が裁定）`。問いは**開いた gap**。
- **チャリボン:** `Contribution（本を送る）→ ValueBooks 買取 → 汎用の Need（むすびえは常に資金が要る）を充填 → 寄付額の明細`。
  - 出発点が **Contribution**。need は **汎用・常設・無差異**（「資金はいつでも助かる」）。**specific な gap が無い**＝Claim が無い。
  - RF は「N 冊→¥X 寄付」という **transaction 受領**＝「寄付が処理されたか」であって「**ある need が満たされたか／誰かが助かったか**」ではない。

→ ユーザーの「Charibon ≈ Contribution → Need」は正確。**flow が反転し、gap/Claim が抜けている。**

---

## 2. チャリボンの 6 基準評価

★★★＝kernel を可視化 / ★★＝部分的 / ★＝欠。

| 基準 | 評価 | 理由 |
|---|---|---|
| 1. **Visibility of Need** | ★ | 汎用・常設の資金需要のみ。observed/required/missing の **specific な gap が宣言されない**。need は*仮定*され*宣言*されない |
| 2. **Visibility of Claim** | ★ | gap を閉じる Claim が無い。**pipe であって claim 駆動でない**。「本で資金を増やせる」は Claim でなく donation の一般則 |
| 3. **Visibility of Contribution** | ★★ | 本（contribution）は可視だが、**specific need から decouple** され、転売を経て汎用資金プールへ消える |
| 4. **Visibility of Reality Feedback** | ★★ | 明細（受理冊数・寄付額）は clean に可視。**だが transaction-RF（集めた金）であって need-RF（閉じた gap）でない**。「寄付が処理されたか」に答え「need が満たされたか」に答えない |
| 5. **Fidelity to Dan-Go** | ★ | Need→Claim→Contribution→RF を **Contribution→汎用 need に反転**。gap/Claim を skip。**donation mechanism を示し coordination kernel を示さない** |
| 6. **Fidelity to WAZIS** | ★ | **現実が裁定する開いた問いが無い**（outcome は ほぼ確定的な pipe 挙動）。RF は receipt であって「現実が問いに答えた」でない。「討議でなく現実が裁定」が**作動しない**（裁定すべき開きが無い） |

**判定:** チャリボンは **clean で速いが、kernel でなく donation mechanism**。これは QUESTION_001_FINAL_REVIEW の「plumbing/mechanism を証して purpose/kernel を証さない」の**別バージョン**——ループは hollow でないが**形が違う**（Contribution→汎用 need であって Need→Claim→Contribution→RF でない）。**誤った対象を demonstrate する。**

---

## 3. specific な公開 need の方が faithful か — Yes（決定的に）

specific な need（特定こども食堂の「お米が不足」「絵本を募集」「冷凍庫が要る」等の**公開された宣言**）を評価:

| 基準 | specific need | charibon | 差 |
|---|---|---|---|
| Visibility of Need | ★★★（**宣言された gap**：観測＝食堂に X が無い／要件＝運営・子どもに X／欠如＝X） | ★ | **大** |
| Visibility of Claim | ★★★（observed/required/missing に直接写る real Claim） | ★ | **大** |
| Visibility of Contribution | ★★★（**その gap** を閉じる・追跡可能） | ★★ | 中 |
| Visibility of RF | ★★–★★★（食堂が受領＋利用を確認＝**gap が閉じた need-RF**） | ★★ | 中 |
| Fidelity to Dan-Go | ★★★（Need→Claim→Contribution→RF をそのまま） | ★ | **大** |
| Fidelity to WAZIS | ★★★（開いた問い「この食堂の X-gap は閉じうるか?」→現実/食堂が裁定） | ★ | **大** |

→ **specific need は kernel そのもの。** need-first（宣言された差異）、real Claim（gap）、need-RF（差異が閉じた）。WAZIS の「開いた問いを現実が裁定」も Dan-Go の「Claim＝gap を Contribution で閉じる」も**両方作動する**。

### fidelity スペクトラム
```
charibon（汎用 need・Contribution起点）   <   物資仲介の高ニーズ品目リスト（need-カテゴリ起点）   <   特定こども食堂の公開された具体的 need（specific gap 起点）
   最も donation 寄り                          中間（何が欠けるか名指すが企業向け・特定 gap でない）            最も kernel 忠実
```

---

## 4. 推奨 — #001B は specific な公開 need へ

**推奨: 特定のこども食堂が公開で宣言している具体的な need 1 件**（公開ほしい物リスト／SNS・サイトの「○○食堂：お米不足／絵本募集」等）を、**運営者へ org-to-org で**（子どもに触れず）充填し、食堂が受領・利用を確認する。

inner question（既存構造のみ・再設計なし）:
> **「〔特定こども食堂が公開で宣言した具体的 need X（例：お米／絵本／指定備品）〕は、Dan-Go 経由で充填され、その食堂に受領・利用を確認されるか?」**

- **Dan-Go 写像（kernel が全段可視）:** **Need**（食堂の公開宣言：observed＝X が無い／required＝X が要る／missing＝X）→ **Claim**（その gap を Z で閉じられる）→ **Contribution**（X/Z を org-to-org で提供）→ **Reality Feedback**（食堂が受領・利用を確認＝**gap が閉じた need-RF**）。
- **RF outcome:** `executed`（受領・利用）／`partial`（一部）／`failed`（届かない・不適）／`impossible`（需要が既充足・連絡不能）——全て valid。
- **30 日:** 購入→配送→確認で可。
- **dignity:** org-to-org（運営者）・子ども非接触＝低。
- **Question #002:** 受領→「X は子どもに実際に届いたか?」or「**Dan-Go 以外の binding**で同型 need を運べるか?」（中立性）／部分→「何が不足したか?」／不適→「食堂が外部充填を受ける条件は?」。

**代替（より構造化だが企業向け・遅い）:** むすびえ **物資仲介の高ニーズ品目**（米/インスタント 等）——need-カテゴリ起点ゆえ charibon より faithful だが、特定 gap でなく企業向け・マッチング latency。

**fallback（kernel でなく donation でよい場合のみ）:** チャリボン——ただし「これは kernel の demonstration でなく donation 手段」と明示する。

**残る人間作業:** むすびえのこども食堂検索（[musubie.org/search](https://musubie.org/search)）等で、**現に公開で具体的 need を宣言している食堂 1 件を確認**し、運営者の公開募集に沿って充填する。私は特定食堂の現況を断定しない。

---

## 5. 正直な訂正（前回の過誤）

前 `MUSUBIE_NEED_DISCOVERY` はチャリボンを第一推奨したが、**RF の clean さと TTFCL（利便性）を過大評価し、kernel fidelity を過小評価していた**。ユーザーの指摘「Charibon ≈ Contribution → Need」は正しい。**#001 の目的は kernel（Need→…→Reality Feedback）を demonstrate することであり、clean でも形の違うループ（donation pipe）は kernel を証さない。** よって recommendation を **specific な公開 need** へ訂正し、チャリボンは fallback の donation 手段に降格する。

---

## 6. 正直な限界（隠さない）

- specific need は**食堂の確認が charibon の自動明細ほど保証されない**（人手・応答依存）。だがその確認こそ**need-RF**＝kernel が要するもの。利便性より fidelity を採る。
- **現に公開で具体的 need を宣言している食堂の特定は人間が確認**（散在・変動）。私は pin しない。
- benefit は食堂レベルで究極受益者でない（「食堂が X を得る」≠「子どもが助かった」）＝#002 以降。dignity 安全の*手段*。
- 「使われた/助かった」は WAZIS が測らない——食堂が確認する（想い非測定）。
- Reach Gap 非解決。

---

## 7. 統合（一文で）

**チャリボンは clean で速いが、Dan-Go の Need→Claim→Contribution→Reality Feedback を Contribution→汎用 need に反転し、specific な gap も Claim も持たず、RF が「寄付額」という transaction 受領であって need-RF でないため、kernel でなく donation mechanism を demonstrate するにすぎない（6 基準のうち 4 つで ★）；対して特定こども食堂が公開で宣言した具体的 need（お米・絵本・備品等）は、need-first の宣言された gap が real Claim（observed/required/missing）に写り、Contribution がその gap を閉じ、食堂の受領・利用確認が need-RF を成すため、Dan-Go にも WAZIS にも全段 faithful であり、#001B はチャリボンでなくこの specific な公開 need にすべきである——前回の charibon 推奨は利便性を fidelity より過大評価した過誤として訂正する。残る作業は人間が現に公開で具体的 need を宣言している食堂 1 件を確認することだけで、足すべき機能・概念は無い。**

---

*本書はレビューであり、実装・コード・既存ファイル修正を含まない。前回推奨（charibon）を kernel fidelity の観点から訂正した。Dan-Go＝Need→Claim→Contribution→RF、charibon＝Contribution→汎用 need（反転）。推奨: 特定こども食堂の公開された具体的 need。代替: 物資仲介の高ニーズ品目。fallback: charibon（donation 手段と明示）。判定は kernel に基づく仮説であり最初の Reality Feedback で反証されうる。*
