# Loop #001B Discovery / 実需ループの発見

- Date: 2026-06-22
- Scope: **実在組織に観測可能な benefit を生む**、最小の組織的問題を同定する（Loop #001B）
- 種別: **リサーチ＋評価のみ**。実装・コード・既存ファイル修正を含まない。
- 規律: WAZIS/Dan-Go を再設計しない・新概念を足さない・削除と最小 viable を優先・仮説より実需。**Reality Feedback が目標、scale でない。**
- 方法: 2026-06 に web 検証した実在の非営利 Digital Public Good（DPG）と、その公開 issue 機構で具体化。**特定 issue の現行実在は人間が最終確認する**（私は稼働を断定しない）。

> **Loop #001A（plumbing test）との別:** #001A はパイプが通るかだけを証す。**#001B は、特定の・識別可能な実在組織が、特定の問題で観測可能に改善すること**を証す。
>
> **見出しの推奨:** #001B の最適形は **非営利が運営する DPG の、公開タグ付き「good first issue / help wanted」を 1 件解決する**こと——maintainer の review→merge が**明示的・公開・即時の Reality Feedback** であり、その org（と利用者）が観測可能に benefit を得る。**推奨は Open Library / Internet Archive**（数百万 patron・応答性最高・merge RF が最も clean）。より救済寄りなら次点 **Medic / Community Health Toolkit**。**選定は「For Good First Issue」（DPG 限定の good-first-issue キュレーション）で行う。**

---

## 1. #001B の形

要件（organization-mediated / public / consent-clear / low dignity / 30 日 / contribution-sized / publicly observable RF）の合流点は、**非営利が運営する DPG の公開 issue tracker の「good first issue / help wanted」**:
- **org-mediated:** 特定の非営利が maintainer。
- **public ＋ consent-clear:** issue が公開＝「help wanted」タグが明示的招待＝同意内蔵。
- **low dignity:** code/docs/translation/data。個人非接触。
- **contribution-sized ＋ 30 日:** good-first-issue は定義上小さい。
- **publicly observable RF:** maintainer の review→merge が公開の RF イベント。
- **observable benefit:** merge で org の product/service が改善＝利用者に届く。

→ これは #001A（中心が空でも成立）と違い、**中心に実 org の実 benefit を持つ**。

---

## 2. Top 5 候補

### B-1. Open Library / Internet Archive（非営利デジタル図書館）
- **org/problem:** openlibrary.org（数百万 patron に ebook を貸す非営利）の公開「good first issue」（bug 修正・小機能）。
- **なぜ qualify:** org 明確（Internet Archive）／benefit が**数百万 patron に直結し可視**／**応答性最高**（週次 call・mentor・fellowship）→ review 待ち短／merge＝clean な公開 RF／good-first-issue 活発。
- **TTFCL:** 短（〜1–3 週で good-first-issue PR が merge されうる）。
- **RF clarity:** ★★★（maintainer review→merge、live で確認）。
- **Benefit clarity:** ★★★（fix が openlibrary.org に live＝patron に直接）。

### B-2. Medic / Community Health Toolkit（cht-core・地域保健）
- **org/problem:** Medic（非営利）の CHT——frontline health worker 向けオフラインファースト保健アプリ。公開「Good First Issue」。For Good First Issue 掲載の DPG。
- **なぜ qualify:** **救済寄りの benefit**（地域保健従事者→underserved コミュニティ）／DPG／公開 issue／merge RF。
- **TTFCL:** 中（保健ソフトの review はやや厳格）〜30 日内（小 issue）。
- **RF clarity:** ★★★（review→merge）。
- **Benefit clarity:** ★★★（health worker のツール改善。ただし受益者は一段下流）。

### B-3. OpenMRS（openmrs-core・医療記録）
- **org/problem:** OpenMRS（非営利）の医療記録システム。JIRA/GitHub の「Ready for Work / Good First Issue / help wanted」。
- **なぜ qualify:** 実在の保健ツール／公開 issue／merge RF／org 明確。
- **TTFCL:** 中〜可変——**未割当の good-first-issue が GSoC 新規参加者と競合**し見つけにくい（検証で確認）＝sourcing 摩擦・latency 増。
- **RF clarity:** ★★★（merge）。
- **Benefit clarity:** ★★★（医療施設。一段下流）。

### B-4. DPG ローカライゼーション（非コード変種）
- **org/problem:** DPG 非営利（CHT/OpenMRS/Open Library 等）の UI/文書を、組織が欠く言語へ翻訳（Transifex/Weblate）。
- **なぜ qualify:** org が**新言語コミュニティに届く**という明確な benefit／公開要請／個人非接触／翻訳は数日。
- **TTFCL:** 短（翻訳数日 ＋ merge 数日〜週）。
- **RF clarity:** ★★（product/release へ merge＝公開だが GitHub merge より一段間接）。
- **Benefit clarity:** ★★（漸進的——文字列単位で benefit が蓄積）。

### B-5. 危機/保健データ DPG（Ushahidi / DHIS2 / KoboToolbox 級）
- **org/problem:** 危機マッピング・保健情報の非営利 DPG の公開 good-first-issue（docs/code/data）。
- **なぜ qualify:** DPG／公開 issue／org 明確／merge RF。
- **TTFCL:** 可変（各 org の応答性次第）。
- **RF clarity:** ★★〜★★★（merge）。
- **Benefit clarity:** ★★〜★★★（org/利用者次第。本セッションで個別 issue は未検証＝class として提示）。

---

## 3. 評価表（5 候補 × 要件/評価軸）

★★★＝#001B に最良 / ★★＝良 / ★＝弱。Dignity は ★★★＝risk 最低、TTFCL は ★★★＝最短。

| 軸 | B-1 Open Library | B-2 Medic/CHT | B-3 OpenMRS | B-4 ローカライズ | B-5 危機/保健DPG |
|---|---|---|---|---|---|
| org-mediated | ★★★ | ★★★ | ★★★ | ★★★ | ★★★ |
| public/consent | ★★★ | ★★★ | ★★★ | ★★★ | ★★★ |
| dignity risk（低=良） | ★★★ | ★★★ | ★★★ | ★★★ | ★★★ |
| 30 日で解決 | ★★★ | ★★ | ★★（競合） | ★★★ | ★★ |
| contribution-sized | ★★★ | ★★★ | ★★★ | ★★★ | ★★★ |
| **RF clarity** | ★★★ | ★★★ | ★★★ | ★★ | ★★ |
| **Benefit clarity** | ★★★ | ★★★ | ★★★ | ★★ | ★★ |
| **TTFCL（短=良）** | ★★★ | ★★ | ★★ | ★★★ | ★★ |
| **総合** | **最良** | **次点（救済寄り）** | 3 | 4 | 5 |

---

## 4. ランキング根拠

**B-1 Open Library > B-2 Medic/CHT > B-3 OpenMRS > B-4 ローカライズ > B-5 危機/保健DPG。**

- #001B で決定的なのは **observable benefit ＋ RF clarity ＋ TTFCL**。
- **B-1** は応答性最高（週次 call・mentor）で review 待ちが短く、benefit が数百万 patron に直結して可視、merge RF が最も clean——**最も確実に 30 日で観測可能に閉じる**。
- **B-2** は benefit が**最も救済寄り**（地域保健）だが、保健ソフトの review がやや厳格＝TTFCL やや長。**「最初の org-benefit ループを救済に寄せたい」なら B-2。**
- **B-3** は良いが good-first-issue が GSoC 新規と**競合**し sourcing 摩擦＝latency リスク。
- **B-4** は benefit が漸進的で RF が一段間接。
- **B-5** は本セッションで個別 issue 未検証＝最も不確実。

---

## 5. 推奨 Loop #001B

**推奨: Open Library / Internet Archive の、現に open な「good first issue」を 1 件解決する。**（より救済寄りを望むなら Medic/CHT。）

inner question の形（既存構造のみ・再設計なし）:
> **「〔Open Library の現 open な good-first-issue X — 特定の bug/小機能〕は、Dan-Go 経由（`code`/`knowledge` 貢献）で解決され、maintainer に merge されるか?」**

- **Dan-Go 写像:** Claim「issue X を org Y のために解決」→ Contribution（PR）→ Execution（PR 提出）→ Reality Feedback（merge / request-changes / declined）。
- **process RF:** 6 ステップ（Question→handoff→Claim→Contribution→RF→New Question）が公開記録。
- **need/benefit RF:** maintainer の **merge**（org の product が live で改善）＝**明示的・公開・即時**の benefit RF。request-changes/declined も valid RF。
- **30 日:** B-1 の応答性なら余裕。無応答でも valid RF（pending/failed）。
- **outcome 別 Question #002:** merged →「この修正は patron に実際に届いた/使われたか?」or「**Dan-Go 以外の binding**で同型貢献を運べるか?」（中立性・U2）／request-changes →「何が不足したか?」／declined →「org が外部貢献を受ける条件は?」／適切な open issue 無し →「Dan-Go が code 貢献を route する最小条件は?」（infra）。

**選定ツール（推奨）:** **For Good First Issue**（DPG 限定の good-first-issue キュレーション）で、現に open・未割当・小さい issue を 1 件選ぶ。**残る唯一の人間作業＝着手時に open/未割当/小規模を確認すること**（私は特定 issue の稼働を断定しない）。

---

## 6. 正直な限界（隠さない）

- **貢献*機構*の稼働は web 検証（2026-06）。特定 issue の現行 open/未割当は人間が最終確認**（issue は日々変わる）。私は specific を pin しない。
- **benefit は org/利用者レベルで、究極受益者レベルでない**（「Open Library の bug が直り patron が使いやすくなる」≠「特定の人が救われた」）。後者は後続ループ。一段手前で止めるのが dignity 安全の*手段*。
- **「merge された/使われた」は WAZIS が測らない**——maintainer/org が確認する（想い非測定・RF は個別観測であって集計でない）。
- **Reach Gap は解決しない**（公開貢献は最困窮の声を含まない）。
- B-3 の競合・B-5 の未検証は上記評価に反映済み。

---

## 7. 統合（一文で）

**Loop #001B（#001A の plumbing と別に、実在組織への観測可能 benefit を証す）の最小形は、非営利が運営する Digital Public Good の公開「good first issue / help wanted」を 1 件解決することであり、maintainer の review→merge が明示的・公開・即時の Reality Feedback として org の product を観測可能に改善する；web 検証した 5 候補のうち Open Library / Internet Archive が最良（数百万 patron に直結・応答性最高・merge RF が最 clean・30 日で確実に閉じる）、より救済寄りなら次点 Medic / Community Health Toolkit、OpenMRS は good-first-issue の GSoC 競合で latency リスク、ローカライズは benefit 漸進、危機/保健データ DPG は未検証ゆえ最下位であり、選定は For Good First Issue（DPG 限定キュレーション）で現 open・未割当・小規模の 1 件を人間が確認することだけが残る作業で、足すべき機能・概念・スケールは無い——目標は Reality Feedback であって規模でない。**

---

*本書はリサーチ＋評価であり、実装・コード・既存ファイル修正を含まない。WAZIS/Dan-Go を再設計せず・新概念を足さず・最小 viable を優先した。機構の稼働は 2026-06 web 検証だが、特定 issue の確定は人間が行い、私は稼働を断定しない。推奨: Open Library good-first-issue（救済寄りなら Medic/CHT）。選定: For Good First Issue。*

## Sources

- For Good First Issue（DPG 限定キュレーション）: [forgoodfirstissue.github.com](https://forgoodfirstissue.github.com/) · [GitHub Blog 紹介](https://github.blog/open-source/social-impact/for-good-first-issue-introducing-a-new-way-to-contribute/)
- Open Library / Internet Archive: [github.com/internetarchive/openlibrary](https://github.com/internetarchive/openlibrary) · [CONTRIBUTING.md](https://github.com/internetarchive/openlibrary/blob/master/CONTRIBUTING.md) · [openlibrary.org/volunteer](https://openlibrary.org/volunteer)
- Medic / Community Health Toolkit: [github.com/medic/cht-core](https://github.com/medic/cht-core) · [communityhealthtoolkit.org](https://communityhealthtoolkit.org/)
- OpenMRS: [github.com/openmrs/openmrs-core](https://github.com/openmrs/openmrs-core) · [talk.openmrs.org（good first issue threads）](https://talk.openmrs.org/t/looking-for-a-good-first-issue-to-contribute/47067)
