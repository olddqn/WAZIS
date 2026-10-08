# WAZIS Implementation Floor Review / 実装の床レビュー

- Date: 2026-06-22
- Scope: 還元はどこで止まるか。哲学的結論を保ちつつ WAZIS が*使える公開 web* になる最小実装の床
- 種別: **レビューのみ**。実装・コード・既存ファイル修正を含まない。
- 規律: **削除を優先・新概念を発明しない・Dan-Go を再設計しない。** ただし**床より下へは削らない**（web が存在できなくなる）。
- 接地: `OPENNESS_RIGHT_REVIEW`（WAZIS＝開かれた Need の憲法的保護＝right、instantiation が権利を honor する）・`OBJECT_REDUCTION`（Question＋RF＋handoff edge）・`PLATFORM_REVIEW`（人を数えるカウンタを持たない・RF 前景化）・`SELF_TRANSLATION`（拒否の規律）。

> **見出し: 還元は「web が (1) Need を*開いたまま保持*でき、(2) Reality Feedback を*記録*でき、(3) 投票/測定/裁定/強制/統治を*拒める*」点で止まる。** それより下は web でなく*哲学*。**最小 object model ＝ Need ＋ Reality Feedback**（＋ handoff edge、初期は手動）。哲学概念（gapability・self-translation・maturation・transformation・custody・right）は **UI に一切出さない**（design を*形作る*が feature でない）。UI は**平易な人間の言葉**で話す。**WAZIS は哲学的に「a right」のまま web になれる**——web の*拒否*（投票/測定/裁定/強制をさせない）こそが right の instantiation だから。最小：開かれた Need の尊厳ある commons ＋ 記録された Reality Feedback ＋ 拒否。

---

## 1. WAZIS が web として存在するとき何が survive するか

- `OPENNESS_RIGHT`：権利は存在に custodian を要さないが、**実効化（violator に対し honor すること）には instantiation を要しうる**。**web がその instantiation。**
- 権利「Need は開いたままでよい」を honor するため、web が具体に提供せねばならないもの:
  1. Need を**記録し、開いたまま可視に保つ**（discard しない）。
  2. **Claim へ強制しない**（保持＝何かになることを要求しない）。
  3. **測らない**（Need/人にスコア・カウンタを付けない）。
  4. holder が**撤回できる**（唯一の除去）。
  5. gapable aspect が現れたとき **Dan-Go へ届く route**。
  6. **Reality Feedback を記録**（Dan-Go から戻ったとき）。
- → survive するのは **{Need を開いたまま保持・Reality Feedback を記録・拒否（投票/測定/裁定/強制/統治をさせない）}**。

---

## 2. 最小 object model

| 候補 | 評価 |
|---|---|
| Need only | △ 権利（開いたまま保持）は honor するが **kernel（現実が答える）を示さない**＝「誰も助けない wall」に留まりうる |
| Need ＋ Question | ❌ 冗長。**Question ＝ holder が voice した開いた Need**＝同一 object（別立て不要） |
| **Need ＋ Reality Feedback** | ✅ **床**。権利（開いたまま）＋ kernel（現実が答える）を両方 honor |
| その他 | handoff は**別 object でなく edge**（Need→Dan-Go Claim、gap＋consent を運ぶ。初期は手動）＝OBJECT_REDUCTION 通り |

→ **最小 object model ＝ Need ＋ Reality Feedback（＋ handoff edge）。** Need ＝ 旧「Question」（Need-framed）。「Need only」はより早い sub-floor（commons of open needs）だが loop を示さない。**Need＋RF が、launch できて kernel も示す床。**

---

## 3. 訪問者が*できねばならない*こと

- **Need を voice する**（開いた Need を記録。holder の自己翻訳——UI 上は「開いた問い/困りごとを共有」）。
- **読む**（Need の commons と、在れば Reality Feedback を閲覧）。
- **自分の Need を撤回する**（唯一の除去・不可侵条項）。
- （任意/第2床）**自分の Need に「助けになる具体的なこと」を添える**（gapable aspect → Dan-Go route）／戻った **Reality Feedback を記録**（初期は運営が代行可）。

→ 最小 ＝ **voice / read / withdraw-own**。

---

## 4. 訪問者が*できてはならない*こと（＝ right の operative 形）

- **投票・upvote/downvote・順位付け**。
- **スコア・rating・人/Need の測定**（「N 人賛同」「人気」「karma」）。
- **他者の Need を「解決済み」と閉じる**（裁定なし・撤回は holder のみ）。
- **Need を Claim へ強制・「対応可」と権威が印付け**。
- **trending/人気での並べ替え・検索**。
- **想い の測定**（「どれだけ強く思うか」スライダー）。
- **他者の Need を削除・管理**（governor/admin が Need を閉じない）。

→ **この NOT-list が「開かれた Need の権利」の operative 形。** web は*できること*と同じだけ*拒むこと*で定義される（§7）。

---

## 5. 哲学のみ＝ UI に出さない概念

**UI/DB に一切出さない:** gapability・claimability・self-translation・maturation・transformation・custody・right・kernel・想い（理論名として）。
- これらは **design を形作る**（投票・測定の削除、撤回のみ除去、RF 前景化）が、**feature でない**。
- 出せば (a) jargon で混乱、(b) **reify の危険**（「gapability スコア」「maturation 待ち行列」＝禁じた測定）。
- **UI は平易な言葉:** Need＝「開いた問い/困りごと」、voice＝「共有する」、gapable aspect＝「助けになる具体的なこと」、Reality Feedback＝「どうなったか／現実の答え」、withdraw＝「取り下げる」。

→ **哲学は invisible な足場、UI は人間の言葉。**

---

## 6. 機能のため*可視*でなければならない概念（平易語で）

- **開いた問い/Need**（保持される物）。
- **どうなったか／現実の答え（Reality Feedback）**（在るとき）。
- **取り下げる（withdraw）**（holder の制御）。
- （任意）**助けになる具体的なこと**（gapable aspect を平易語で）。
- **正直な状態**（「これは開いたまま」「現実の答え：…」）。

→ 可視 ＝ Need・Reality Feedback・Withdraw（＋具体的な助け）。他はすべて invisible。

---

## 7. 哲学的に「a right」のまま、運用上 web でいられるか — Yes

- web は **権利の instantiation（honor する器）**（OPENNESS_RIGHT）。権利と矛盾せず、**権利を*enforce* する**。
- web の **NOT-list（投票/測定/裁定/強制/統治をさせない）こそが right を operative にしたもの。** affordance（voice/read/withdraw）が access、refusal が right。
- → **NOT-list の上に建てた web ＝ instantiated な「a right」。** WAZIS は哲学的に right のまま、運用上 web でいられる。器は権利に*仕える*（管理しない）＝置換可。

---

## 8. 最小ホームページ

- 一行：**「開いた問いを、裁かず・順位付けず・強制せず、開いたまま保つ場。群衆の票でなく、現実が、答えられるものに答える。」**
- **順位なしの「開いたまま保持中の Need」一覧**（時系列/無序列）。在れば各 Need に Reality Feedback を併記。
- **voice する／自分のを取り下げる**導線。
- **正直なカウント:** 「開いたまま保持：N ／現実が答えた：M」。**※Need/答えの数は可（commons の透明性）。人/Need を*測る・順位付ける*カウンタは不可**（§4）。
- **trending/upvote/score/leaderboard なし。** 支配的メッセージ＝「ここでは Need は裁かれず保たれる；現実は答えられるものに答える」。
- ローンチ直後は「現実が答えた：0／最初の一周 進行中」と正直に。

---

## 9. 最小データベーススキーマ（2＋1 テーブル）

```
needs
  id            …  識別子
  holder        …  DID/pseudonym（評判でなく識別）
  text          …  voice された開いた Need（平易語）
  created_at
  status        …  open | withdrawn        ← 「closed」状態なし（NON_GAPABLE）
  consent_public…  bool（可視範囲の同意）
  〔NO score / NO priority / NO votes / NO category-rank〕

reality_feedback
  id
  need_id       …  FK → needs
  implementer   …  例 "dan_go:claim-xxxx"
  outcome       …  executed | partial | failed | impossible   （Dan-Go 既存語彙）
  observation   …  何が起きたか（独立観測）
  created_at
  reported_by

handoff（任意・初期は手動可）
  id
  need_id       …  FK → needs
  gap           …  observed / required / missing（平易語・Dan-Go Claim へ）
  consent_by    …  handoff への holder 同意
  target        …  例 "dan_go"
  claim_ref
  created_at
```

→ **最小 ＝ needs ＋ reality_feedback（＋ handoff）。NO users-with-karma・NO votes・NO scores テーブル。** identity は needs の pseudonym フィールド（評判 profile でない）。

---

## 10. 最小の最初の公開ループ

1. holder が Need を voice（web に開いたまま保持）。
2. holder（or 討議）が **gapable aspect を自己翻訳**（「助けになる具体的なこと」——例：むすびえの特定こども食堂のお米不足）。
3. **運営が手で Dan-Go へ運ぶ**（observed/required/missing の Claim 化）。**route は初期 手動でよい。**
4. Dan-Go → Contribution → Execution → Reality Feedback。
5. **Reality Feedback を web に記録**（Need に link）。outcome は何でも可（failed でも成立）。
6. Need は開いたまま（holder が撤回しない限り）；RF が新しい問いを開きうる。

→ web に要るのは **「Need を記録・Reality Feedback を記録」だけ。Dan-Go route は手動。** （LAUNCH_REVIEW「最初の loop は手作業可」と一致。）

---

## 11. 実装の床（最重要の問いへの答え）

**還元はここで止まる：web が**
1. **Need を開いたまま保持できる**（visible・withdrawable・unmeasured）＝権利を honor、
2. **Reality Feedback を記録できる**（gapable aspect が Dan-Go を巡ったとき）＝kernel を honor、
3. **投票/測定/裁定/強制/統治を拒める**（§4）＝right を operative に。

**これより下は web でなく哲学。** この床に立つと、最小で使える公開 WAZIS が得られる：**開かれた Need の尊厳ある commons ＋ 記録された現実の答え ＋ 拒否**。

**launch できる最小 ＝** needs ＋ reality_feedback の 2 テーブル、homepage（§8）、voice/read/withdraw、手動 Dan-Go route の一周（§10）。**全哲学的結論が保たれる**（開いたまま保持＝right／撤回のみ除去・測定なし／gapability は不可視で「助けになる具体的なこと」／現実が答える＝RF 記録／no-governor・no-verdict＝他者の Need を閉じない／想い 非測定＝スコアなし）。

> **「還元が永遠に続けば何も建たない」への答え：床は『Need を開いたまま保持し、現実の答えを記録し、測定/投票/裁定を拒む web』。それが最小で建てられるもの。**

---

## 12. 統合（一文で）

**WAZIS の実装の床は、web が Need を開いたまま保持でき（visible・withdrawable・unmeasured＝権利を honor）・Reality Feedback を記録でき（gapable aspect が Dan-Go を巡ったとき＝kernel を honor）・投票/測定/裁定/強制/統治を拒める（＝right を operative にする）点で止まり、それより下は web でなく哲学である；最小 object model は Need ＋ Reality Feedback（＋初期手動の handoff edge、Need＝旧 Question）で、最小スキーマは needs ＋ reality_feedback の 2 テーブル（karma/votes/scores なし）、訪問者は voice/read/withdraw-own ができ投票/測定/裁定/他者の Need を閉じることはできず（この NOT-list こそ right の operative 形）、gapability・self-translation・maturation・transformation・custody・right といった哲学概念は UI に一切出さず（design を形作るが feature でない・出せば jargon と reify の危険）UI は平易語で Need・現実の答え・取り下げ・助けになる具体的なことだけを可視にし、ゆえに WAZIS は哲学的に「a right」のまま運用上 web でいられる（web の拒否こそ権利の instantiation で、器は権利に仕え置換可）；最小ホームページは順位なしの開いた Need 一覧＋在れば現実の答え＋voice/withdraw＋正直なカウントで trending/票/スコアを持たず、最小の最初の公開ループは一つの Need →（手動の）gapable aspect → Dan-Go → 記録された Reality Feedback であり、これが「還元が永遠なら何も建たない」への答え＝建てられる最小である。**

---

*本書はレビューであり、実装・コード・既存ファイル修正を含まない。削除を優先しつつ床を定めた（床より下は哲学）。最小 object model ＝ Need ＋ Reality Feedback（＋手動 handoff）。最小スキーマ ＝ needs ＋ reality_feedback（karma/votes/scores なし）。哲学概念は UI 不可視、UI は平易語。NOT-list ＝ right の operative 形。WAZIS は a right のまま web になれる（web の拒否が権利の instantiation）。最小ローンチ ＝ 開いた Need の commons ＋ 記録された RF ＋ 拒否。新概念を発明せず・Dan-Go を再設計せず。判定は kernel に基づく仮説であり最初の Reality Feedback で反証されうる。*
