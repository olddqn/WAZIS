# First Real Need Discovery / 最初の実需の発見

- Date: 2026-06-22
- Scope: Question #001 のループの中心を埋める、**実在する候補 need** を同定・評価する
- 種別: **リサーチ＋評価のみ**。実装・コード・既存ファイル修正を含まない。
- 規律: **WAZIS/Dan-Go を再設計しない・新概念を足さない・削除を加算より優先・仮説より実需・最大インパクトより最小 viable ループ。Reality Feedback が目標、scale でない。**
- 方法: INNER_EXPERIMENT_REVIEW の class（公益組織の公開要請への情報貢献）を、**2026-06 に web 検証**した実在組織で具体化。**特定の現行タスクの実在は人間が最終確認する**（私は稼働を断定しない・知識カットオフ）。

> **見出しの推奨:** 5 候補すべて**現に稼働中の公開貢献機構**を確認した。**Question #001 の inner need には HOT Tasking Manager（人道マッピング）を推奨**——need が特定の人道対応に紐づき、**検証（validation）という明示的・公開・即時の Reality Feedback** を持ち、衛星画像を扱い**個人に一切触れず**、30 日で十分閉じ、Dan-Go の `knowledge`/`coordination` 貢献に綺麗に写る。次点は Wikipedia 健康記事翻訳（最速・最も公開）。

---

## 1. 候補の形（recap）

INNER_EXPERIMENT_REVIEW の結論: **「人」でなく「情報」を扱う、公益組織の既存公開要請への小さな貢献。** 以下 5 件はすべて実在・公開・組織/プロジェクト媒介・個人非接触で、web で現行稼働を確認した。

---

## 2. Top 5 候補

### C-1. HOT Tasking Manager（人道 OpenStreetMap・マッピング）
- **何を:** 実在の災害/保健/開発対応のために、衛星画像から建物・道路を trace。`tasks.hotosm.org` の公開プロジェクトが大タスクを小区画に分割。経験者が validation。
- **貢献:** 1 区画のマッピング（`knowledge`/`coordination`）。
- **Pros:** need が特定対応に紐づき明確／**validation ＝ 明示的で公開・即時の RF**／衛星画像ゆえ個人非接触・私的データ皆無／タスクは数時間・検証は数日＝TTFCL 最短／完了率・編集履歴・データ live で**完全に公開観測可能**。
- **Cons:** 究極受益者は下流（map を対応組織が使い、その先で人が助かる）＝need RF は対応レベル。マッピング技能の最低限の習得が要る（半日）。

### C-2. Wikipedia / WikiProjectMed 健康記事翻訳
- **何を:** 200–500 語の健康トピック要約を、当該言語が乏しい underserved 言語へ翻訳。150+ 言語・「especially smaller languages」で常時募集。
- **貢献:** 1 記事の翻訳（`translation`/`knowledge`）。
- **Pros:** 編集が**即 live ＝ 最速・最も公開**の RF／閲覧数で利用が観測可能／consent 最明瞭（公開・私的データなし）／個人非接触。
- **Cons:** need の所有者が**拡散**（特定組織が「これが要る」と確認するのでなく一般的な健康情報アクセス gap）／RF＝「掲載され統合され閲覧される」で、組織の「使った」確認でない。

### C-3. OpenMRS ローカライゼーション（医療記録 OSS・Transifex）
- **何を:** 低資源の保健施設で使われる OS 医療記録システムの UI/文書を翻訳（Transifex・peer review）。仏 ~54%・西 ~86%＝他言語に明確な gap。
- **貢献:** 文字列/文書翻訳（`translation`/`code`/`knowledge`）。
- **Pros:** 実在の保健ツールの明確な gap／Transifex public stats ＋ merge で観測可能／個人非接触／短 TTFCL。
- **Cons:** need が「ソフトのローカライズ」寄りで人の需要から一段遠い／RF＝merge レベル（施設での利用は下流）。

### C-4. Translators Without Borders / CLEAR Global
- **何を:** 10 万人規模の人道翻訳コミュニティ（TWB Platform）。翻訳・改訂・字幕・用語集。
- **貢献:** 1 文書の翻訳（`translation`）。
- **Pros:** 最も直接的に「人道翻訳」・組織媒介で need 明確／個人非接触。
- **Cons:** **ボランティア審査/言語テストの onboarding latency**（タスク着手前）／受領が**プラットフォーム内**で公開観測性が低い＝RF 可視性中。

### C-5. Cochrane Crowd（市民科学・健康エビデンス分類）
- **何を:** 研究記述を読み RCT を分類し、Cochrane の登録に投入。短い訓練・agreement algorithm。
- **貢献:** 記録分類（`knowledge`）。
- **Pros:** 実在の健康エビデンス need／個人非接触／分類は数分＝速い。
- **Cons:** **RF が集計的**（自分の分類は他者と合議アルゴリズムで束ねられる）＝「自分の貢献が need を満たした」が観測しにくい。**集計＝metric パターン**（RF_INTERPRETATION の警告）に最も近く、個別 need-answering の可視性が最弱。

---

## 3. 評価表（5 候補 × 8 基準）

★★★＝最初の公開ループに最良 / ★★＝良 / ★＝弱（Dignity Risk は ★★★＝risk 最低、TTFCL は ★★★＝最短）。

| 基準 | C-1 HOT | C-2 Wikipedia | C-3 OpenMRS | C-4 TWB | C-5 Cochrane |
|---|---|---|---|---|---|
| Need clarity | ★★★ | ★★ | ★★ | ★★★ | ★★ |
| Consent clarity | ★★★ | ★★★ | ★★★ | ★★★ | ★★★ |
| Dignity risk（低=良） | ★★★ | ★★★ | ★★★ | ★★★ | ★★★ |
| Reality Feedback clarity | ★★★ | ★★★ | ★★ | ★★ | ★ |
| Dan-Go compatibility | ★★★ | ★★★ | ★★★ | ★★★ | ★★ |
| WAZIS compatibility | ★★★ | ★★★ | ★★ | ★★ | ★★ |
| Expected TTFCL（短=良） | ★★★ | ★★★ | ★★★ | ★★ | ★★★ |
| 公開観測可能性 | ★★★ | ★★★ | ★★ | ★★ | ★ |
| **総合** | **最良** | **次点** | 3 | 4 | 5 |

---

## 4. ランキング根拠

**C-1 HOT > C-2 Wikipedia > C-3 OpenMRS > C-4 TWB > C-5 Cochrane。**

- **#001 で決定的なのは RF clarity ＋ 公開観測性 ＋ need clarity**（process RF と need RF の両方を*観測可能*に出すこと）。
- **C-1 が唯一、8 基準すべてで ★★★。** validation という**明示的・公開・即時の RF イベント**を持ち、need が特定対応に紐づく。「organization-mediated/publicly requested」を最も満たす（特定の対応組織が公開プロジェクトとして要請）。
- **C-2** は最速・最も公開だが need 所有が拡散（「誰の need か」が薄い）ため #001 の need RF が一段弱い→次点。
- **C-3** は clean だが need が software-localization 寄り（人の需要から一段遠い）。
- **C-4** は最も「人道翻訳」だが onboarding latency と in-platform の低可視 RF が #001 には不利。
- **C-5** は RF が集計的＝**個別 need-answering が観測できず、metric パターンに最接近**。#001（RF clarity が要）に最も不向き→最下位。

---

## 5. Question #001 への推奨候補

**推奨: C-1 HOT Tasking Manager の、現に稼働中の小さな1プロジェクトのマッピング need。**

inner question の形（既存構造のみ・再設計なし）:
> **「〔現に稼働中の HOT プロジェクト X — 特定対応 Y のための領域 Z の建物/道路マッピング〕は、Dan-Go 経由（`knowledge`/`coordination` 貢献）で貢献され、HOT の validation で検証されるか?」**

- **process RF:** WAZIS Question → handoff/Binding → Dan-Go Claim → 貢献（マッピング提出）→ Reality Feedback → New Question の 6 ステップが公開記録される。
- **need RF:** HOT の validation（validated / needs-fixing / invalidated）＋プロジェクト完了率の前進 ＝ 実在の対応組織のマッピング need が、観測可能に（部分的に）満たされる。
- **30 日:** 余裕（タスク数時間・検証数日）。無検証でも valid RF。
- **outcome 別 Question #002:** validated →「map data は対応に実際に届いた/使われたか?」or「**Dan-Go 以外の binding**（C-2 翻訳型）で同型貢献を運べるか?」（中立性・U2）／needs-fixing →「何が部分的だったか?」／貢献不可 →「Dan-Go がマッピング貢献を route する最小条件は?」／稼働プロジェクト無し →「Dan-Go が WAZIS 由来 Claim を受ける最小条件は?」（infra gap）。

**残る唯一の人間作業:** 着手時に `tasks.hotosm.org` で**現に稼働中の、初心者可・小区画のプロジェクト 1 件を選び実在を確認**し、WAZIS Question #001 の inner experiment として記録する。私（AI）は特定プロジェクトの稼働を断定しない（プロジェクトは日々入れ替わる・私の検索結果も snapshot）。

**fallback:** HOT で適切な小プロジェクトが無い週は **C-2 Wikipedia 健康記事翻訳**（即 live で最速・最も公開の RF）。

---

## 6. 正直な限界（隠さない）

- **貢献*機構*の現行稼働は web で確認した（2026-06）。だが特定タスク/プロジェクト/記事の選定と実在は人間が最終確認する**（日々入れ替わる）。私は specific を pin しない。
- **need RF は対応/組織レベルで、究極受益者レベルでない**（「領域がマップされ対応が使える」≠「その地の人が助かった」）。後者は #002 以降。一段手前で止めるのが dignity 安全の*手段*。
- **Reach Gap は解決しない**（安全ゲートを通る情報貢献は最困窮の声を含まない）。
- **「使われた/検証された」は WAZIS が測らない**——HOT/組織が確認する（想い非測定・RF は個別観測であって集計でない）。**C-5 を最下位にしたのはこの原則の帰結**（集計 RF を避ける）。

---

## 7. 統合（一文で）

**実在し現に稼働する 5 候補（HOT マッピング・Wikipedia 健康翻訳・OpenMRS ローカライズ・TWB 翻訳・Cochrane Crowd 分類）を 8 基準で評価した結果、Question #001 の inner need には HOT Tasking Manager が最良である——need が特定の人道対応に紐づいて明確で、validation という明示的・公開・即時の Reality Feedback を持ち、衛星画像を扱い個人に一切触れず（dignity 最低リスク・consent 最明瞭）、30 日で十分閉じ、Dan-Go の knowledge/coordination 貢献に綺麗に写り、process RF と need RF の両方を観測可能に生み、どの outcome も自然に Question #002 を開く；次点は最速・最も公開の Wikipedia 健康記事翻訳、最下位は RF が集計的で個別 need-answering を観測できず metric パターンに最接近する Cochrane Crowd であり、残る唯一の作業は AI でなく人間が tasks.hotosm.org で現行の小プロジェクト 1 件を選び実在を確認することだけである。足すべき機能・概念・スケールは無い——目標は Reality Feedback であって規模でない。**

---

*本書はリサーチ＋評価であり、実装・コード・既存ファイル修正を含まない。WAZIS/Dan-Go を再設計せず・新概念を足さず・削除と最小 viable を優先した（11 contribution 型のうち最小の情報貢献に絞り、集計 RF 候補を最下位に）。貢献機構の稼働は 2026-06 web 検証だが、特定タスクの実在確定は人間が行い、私は稼働を断定しない。推奨: HOT Tasking Manager。fallback: Wikipedia 健康記事翻訳。*

## Sources

- HOT Tasking Manager: [tasks.hotosm.org](https://tasks.hotosm.org/) · [Humanitarian OSM Team (OSM Wiki)](https://wiki.openstreetmap.org/wiki/Humanitarian_OSM_Team) · [Missing Maps – HOT Tasking Manager](https://missingmaps.org/hot-tasking-manager/)
- Translators without Borders / CLEAR Global: [clearglobal.org/translators-without-borders](https://clearglobal.org/translators-without-borders/) · [translatorswithoutborders.org](https://translatorswithoutborders.org/) · [TWB Platform](https://twbplatform.org/)
- Wikipedia / WikiProjectMed Translation Task Force: [WikiProject Medicine Translation task force (Wikipedia)](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Medicine/Translation_task_force/History) · [WikiProjectMed Translation task force](https://mdwiki.org/wiki/WikiProjectMed:Translation_task_force) · [TWB Translation Task Force](https://translatorswithoutborders.org/translation-task-force/)
- OpenMRS localization: [How to Translate OpenMRS](https://openmrs.atlassian.net/wiki/spaces/docs/pages/105512985/How+to+Translate+OpenMRS) · [Localization and Languages](https://openmrs.atlassian.net/wiki/spaces/docs/pages/25465620/Localization+and+Languages)
- Cochrane Crowd: [crowd.cochrane.org](https://crowd.cochrane.org/) · [Be a Cochrane Citizen Scientist](https://www.cochrane.org/about-us/news/be-cochrane-citizen-scientist-and-contribute-health-evidence)
