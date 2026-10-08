# WAZIS MVP Screen Review / 画面レビュー

- Date: 2026-06-22
- Scope: 最小で launch できる**実際の公開 UI（画面）**。哲学でもアーキでもなく screens
- 種別: **レビューのみ**。コード生成・実装・既存ファイル修正を含まない（画面は記述であって markup でない）。
- 規律: **削除を優先・新概念を発明しない・単一 Entry モデルを保つ・Dan-Go を再設計しない。**
- 接地: `WAZIS_ISSUE_MODEL_REVIEW`（単一 Entry・closure なし・撤回のみ・RF＝provenance）・`PLATFORM_REVIEW`（RF 前景化・正直な空状態・人を数えない）・`IMPLEMENTATION_FLOOR`（平易語・哲学概念は不可視）。

> **見出し: 3 画面（Home・Entry・New Entry）／3 操作（Create・Reply±link・Withdraw）／1 テーブル。** Reality Feedback ＝ **外部 link を持つ Reply**（accent ＋ link で前景化、ただし verdict バッジでない）。**NOT-list（vote/close/score/rank/governance）は「実装しないこと（absence）」で enforce——それが forum でなく WAZIS たる所以。** **1 開発者・1 週末で建てられる；難所は build でなく削除（forum 機能を足さない規律）。Yes、3 画面で launch できる。**

---

## 1. Home（新規訪問者が最初に見る画面）

縦 1 カラム、上から:
1. **一行アイデンティティ:** 「**WAZIS — 開いた困りごとを、裁かず・順位付けず、開いたまま保つ場。群衆の票でなく、現実が、答えられるものに答える。**」
2. **「ここにないもの」一行（小さく）:** 「票なし・点数なし・順位なし。何も*閉じられない*。あなたが書いたものを下げられるのは、あなただけ。」← 誤った mental model（forum/Reddit）を 30 秒で否定。
3. **［開いた困りごとを書く］** ボタン → New Entry。
4. **root Entry（開いた Need）の一覧。** *新しい順（時間順・merit でない）。* 各項目：text（抜粋）／author（pseudonym）／時刻／**スレッドに現実の答え（外部 link の child）があれば小さな「↩ 現実が答えた」印**。**票数・点数・人気の表示なし。**
5. **正直な状態行:** 「開いたまま：N ／現実が答えた：M」。*Need/答えの数は可（commons の透明性）。人を測る数は不可。* ローンチ直後＝「まだ何もありません。最初の困りごとを待っています。」

→ Home ＝ **順位なしの開いた Need の列 ＋ 在れば「現実が答えた」印 ＋ 書くボタン ＋ 正直なカウント。** trending/票/score/leaderboard **なし**。

---

## 2. New Entry（root Entry 作成）

縦 1 カラム:
1. **やさしいプロンプト:** 「開いていること——困りごと・問い・未解決のこと——を書いてください。解決しなくて構いません。ここで裁かれず、開いたまま保たれます。」
2. **text フィールド 1 つ**（タイトル/本文を分けない＝削除）。
3. **author**（pseudonym／選んだ handle）。
4. **注記:** 「あとで下げられるのは、あなただけです。」（撤回の期待を設定）＋「これは全員に見えます」（公開の同意・平易に）。
5. **［書く］** → root Entry（status=open）を作り、そのスレッドへ。

**無いもの:** タイトル欄・カテゴリ選択・**type 選択（Need/Question——単一 Entry）**・優先度・緊急度・タグ・公開度スコア。**text ＋ author だけ。**

---

## 3. Entry thread（読む画面）

縦 1 カラム:
1. **root Entry**（上）：text・author・時刻・status（撤回済みなら「［投稿者により取り下げ］」）。
2. **children（スレッド順・時間順）:** 各 child ＝ text・author・時刻。
   - **外部 link を持つ child ＝ Reality Feedback** → **視覚的に区別**（左 accent/枠 ＋ 「↩ 現実が答えた（[Dan-Go/世界] へ）」ラベル ＋ **clickable な link**）。
   - link 無しの child ＝ 継続/コメント → 平易（無装飾）。
3. **返信欄（最下部）:** text フィールド ＋ **任意「現実が答えた場所への link（URL）」フィールド**。［返信］→ child Entry を作る。**link が埋まれば、その child は RF（provenance）。**
4. **［取り下げる（withdraw）］** ボタン — **自分が書いた Entry にのみ表示**。押すと status=withdrawn（text を「［投稿者により取り下げ］」に置換、node は残しスレッド構造を壊さない；撤回の事実は残る）。
5. **無いもの:** close・resolve・vote・like・score・優先度・assignee・label・「ベストアンサー」。

→ Entry ＝ **root ＋ children（RF は link で accent）＋ 返信欄（±link）＋ 自分のだけ withdraw。** 閉じる/投票ボタン**なし**。

---

## 4. Reality Feedback はどう見えるべきか

- **外部 link を持つ child Entry として、前景化して区別**：左 accent ＋ 「現実が答えた」ラベル ＋ **link を主役に**（clickable・検証可能）。
- **verdict バッジでない:** スレッドを閉じない・「採用/ベスト」印を付けない・他より上位に並べない。「現実が、ここで、答えた（検証はこちら）」と示すだけ。
- 強調するのは **link（provenance/検証可能性）**であって「閉じる答え」でない。→ **「現実が、討議でなく、答えた」を link で示しつつ、closure を含意しない。**
- Home では、スレッドに RF を含む root に小さな印。

→ **RF visual ＝ link を帯びた前景化された child（accent ＋「現実が答えた」＋ clickable link）。closing/verdict バッジでない。link が主役。**

---

## 5. 存在する操作

| 操作 | 内容 |
|---|---|
| **Create Entry** | root を書く（開いた困りごと） |
| **Reply** | child を足す（継続、または **±link で現実の答え＝RF**） |
| **Withdraw** | 自分の Entry を下げる（**唯一の terminal・holder のみ**） |
| （plumbing）**identity** | handle/pseudonym（authorship ＋「撤回は本人のみ」を効かせるため。cookie 程度で可） |

→ 「Link external reality」は**独立操作でなく Reply の任意フィールド**。実質 **3 操作（Create・Reply・Withdraw）＋ identity**。**これ以上は無い。**

---

## 6. 存在してはならない操作（＝ right を画面にしたもの）

- **Vote / Like / upvote / downvote / react**（想い 非測定）。
- **Score / rate / star**。
- **Trending / 人気順 / 「Top」**。
- **Resolve / Close / 「完了」**（verdict・closure なし）。
- **Priority / 緊急度 / severity**（Need の順位付けなし）。
- **Assign / assignee / milestone**（governance なし）。
- **他者の Entry の edit/delete/lock/hide**（no-governor——撤回は本人のみ）。
- **follower/karma/評判の数**（人を測らない）。
- **「ベストアンサー/採用」**（RF は採用/最良でない）。

→ **これらを*実装しない*ことが WAZIS を forum でなくする。** NOT-list ＝ right の operative 形。

---

## 7. 最小ナビゲーション

- **Home ↔ Entry ↔ New Entry** の 3 つだけ。
- Home → Entry をタップ → スレッド。
- Home → ［書く］ → New Entry → 送信 → そのスレッド。
- Entry → 戻る → Home。
- **無いもの:** メニューバー（trending/top/カテゴリの区画）・評判付きプロフィールページ・人気検索。
- 「自分の投稿」は各 Entry の withdraw ボタンで足りる（別プロフィール不要）。

→ **最小ナビ ＝ 戻る ＋ ［書く］。区画ナビなし。**

---

## 8. 最小モバイルレイアウト

- **単一カラム。** sidebar なし。
- **Home:** ヘッダ一行 ＋ ［書く］ ＋ 縦リスト（各：text 抜粋・author・時刻・在れば「現実が答えた」印）。タップ → スレッド。
- **Entry:** root（上）→ children（RF は accent）→ **返信欄を最下部に固定** → 自分のに withdraw。
- **New Entry:** プロンプト ＋ textarea ＋ ［書く］。
- モデルが thread リストなので mobile-first は自明（特別な対応不要）。

---

## 9. 3 画面（Home・Entry・New Entry）で launch できるか — Yes

- **Reply・Withdraw・link は Entry 画面に inline**（別画面不要）。**Create のみ New Entry。**
- → **3 画面で十分。**
- 更に削るなら Home に inline 作成欄で **2 画面**も可。だが New Entry を独立にすると、初投稿者へのやさしい framing（裁かない約束）を置けて誤用を防げる。→ **3 が clean な床。**

---

## 10. 最重要：1 開発者・1 週末で、WAZIS と呼ぶに値する最小版

**建てるもの（容易）:**
- **1 テーブル `entries`**（id・parent_id・author・text・created_at・status[open|withdrawn]・link）。
- **3 画面**（Home・Entry・New Entry）。
- **3 操作**（Create・Reply±link・Withdraw）＋ handle 程度の identity。
- **正直な空状態。**

**WAZIS と呼ぶに値させる 4 つの identity-critical な性質（ほぼ「不在」ゆえ実装はタダ）:**
1. **vote/score/rank が無い**（想い 非測定）。
2. **closure が無い**（status は open|withdrawn のみ＝開放性の権利を構造で）。
3. **撤回は本人のみ・他者支配なし**（no-governor）。
4. **RF は外部 link で区別**（現実が討議でなく答える＝kernel）。

→ **この 4 つのどれか 1 つでも欠ければ、それは forum であって WAZIS でない。** そして 4 つは**主に「足さないこと」**——実装コストはほぼゼロ。**ゆえに週末で建つ。難所は build でなく*削除の規律***：あらゆる framework と本能が「like ボタン」「close ボタン」を足させようとする——それを*拒む*ことが、この週末 MVP の唯一の難関。

**最初の実ループはこの MVP で手動完走できる:** むすびえの困りごとを root Entry に書き、gapable aspect と Dan-Go handoff は場外（手動）、現実が答えたら **Dan-Go Claim への link を付けた返信（＝RF）** を投稿。**Dan-Go 連携コードは不要——返信の link だけ。**

→ **週末版 ＝ 「1 テーブル・3 画面・3 操作の thread commons ＋ 4 つの不在（vote/close/governor/non-link-RF を持たないこと）」。** これが WAZIS と呼ぶに値する最小。

---

## 11. 統合（一文で）

**WAZIS の最小公開 UI は 3 画面（Home＝順位なしの開いた Need 一覧＋在れば「現実が答えた」印＋書くボタン＋正直なカウント、New Entry＝やさしいプロンプト＋text ＋ author だけ、Entry＝root＋children で RF は外部 link を持つ child として accent＋clickable link で前景化＋返信欄±link＋自分のだけ withdraw）と 3 操作（Create・Reply±link・Withdraw、identity は authorship と「撤回は本人のみ」のための plumbing）から成り、Reality Feedback は verdict バッジでなく provenance（外部 link）を主役に前景化され、Vote/Like/Score/Trending/Resolve/Close/Priority/Assign/他者支配/ベストアンサーは*実装しないこと*で禁じられ（この NOT-list こそ right を画面にしたもの）、ナビは Home↔Entry↔New Entry の戻る＋書くだけ・モバイルは単一カラム＋最下部固定の返信欄で、3 画面で launch でき；1 開発者・1 週末で建てられる最小版は 1 テーブル・3 画面・3 操作に「vote/score/rank が無い・closure が無い・撤回は本人のみ・RF は外部 link で区別」という 4 つの identity-critical な不在を備えたもので、その 4 つのどれを欠いても forum であって WAZIS でなく、実装はほぼ不在ゆえタダで難所は build でなく forum 機能を足さない削除の規律であり、最初の実ループ（むすびえ）は Dan-Go Claim への link を付けた返信＝RF として連携コードなしで手動完走できる——足すべき機構は無く、これが WAZIS と呼ぶに値する建てられる最小である。**

---

*本書はレビューであり、コード生成・実装・既存ファイル修正を含まない。削除を優先し単一 Entry モデルを保った。3 画面（Home・Entry・New Entry）・3 操作（Create・Reply±link・Withdraw）＋identity。RF＝外部 link を持つ child を accent＋clickable link で前景化（verdict バッジでない）。NOT-list（vote/score/rank/close/resolve/priority/assign/他者支配/ベストアンサー）＝実装しないことで enforce。週末版＝1 テーブル・3 画面・3 操作＋4 つの identity-critical な不在（no-vote/score/rank・no-closure・撤回のみ・RF は link で区別）。難所は削除の規律。最初の実ループは link 付き返信で連携コードなしに完走。新概念を発明せず・Dan-Go を再設計せず。判定は kernel に基づく仮説であり最初の Reality Feedback で反証されうる。*
