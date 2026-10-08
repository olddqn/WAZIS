# WAZIS Platform Review / プラットフォーム・レビュー

- Date: 2026-06-22
- Scope: WAZIS の kernel を**正しく表現する最小の公開 web プラットフォーム**（public Question Commons / 最初の可視入口）を評価する
- 種別: **レビューのみ**。実装・コード・既存ファイル修正・完成品設計を含まない。
- 規律: **削除を加算より優先。** 新概念・新層を発明しない。プラットフォームは WAZIS *ではない*——kernel を公開的に表現する *view* にすぎない。既存レビューに在るなら「既出」と明記。
- 前提: 既往5レビュー（KERNEL / DANGO_BOUNDARY / META_LOOP / TRANSFORMATION / STRUCTURAL_CONSOLIDATION）は、直接観察で矛盾しない限り正しい。canonical 語: **Question / Transformation / Experiment Candidate / Reality Feedback**。

> **見出しの答え:** 最小プラットフォームは「討議サイト」ではなく **「現実が答えた問いの公開台帳（reality-feedback ledger）」**である。kernel を正しく表現する条件は唯一——**討議でなく Reality Feedback を構造的に前面化し、人や想いを測るカウンタを一つも持たないこと**。この**単一の削除**（人を数える機構の不在）が、Reddit/5ch/Stack Overflow/Discord/DAO/petition への degeneration を**同時に**防ぐ。プラットフォームの唯一の仕事は、Question→Reality Feedback の一周を**公開的に可視化**し、TTFCL と（やがて）2本目 Binding を可能にすること。

---

## 0. 枠組み — プラットフォームは kernel の view であって WAZIS でない

- WAZIS の identity は protocol（kernel）にあり、UI にはない（KERNEL_REVIEW）。よってプラットフォームは **kernel を覗く窓**。窓を WAZIS と取り違えないこと。
- 窓の責務は二つだけ: (1) **Question Commons**（公開入口）を提供する、(2) **現実が裁定する**さまを可視化して、討議でなく Reality Feedback が権威だと体感させる。
- これは neutrality の前提でもある: 公開入口が無ければ多様な問いも 2本目 Binding も現れない（観察の通り）。だが入口の作り方を誤れば、kernel を inversion する（§9）。

---

## 1. kernel を正しく表現する最小プラットフォーム

**＝ Reality Feedback を主役にした公開台帳。** forum の逆。

- forum は *討議* を前面化し、upvote で序列化する。WAZIS は **現実の答え** を前面化し、序列を持たない。
- 最小構成は「読み中心（read-mostly）の公開記録」: **問い → それが変換された実験 → 現実の答え → 開いた新しい問い** の連鎖を、誰でも辿れる形で陳列するだけ。
- 「正しく表現する」の判定基準（kill-test）: ページから **Reality Feedback の優位** を外すと forum に崩落、**「人を数えるカウンタの不在」** を外すと Reddit/DAO/petition に崩落。この二点が在れば最小で kernel を表現できる。

---

## 2. 最小の objects — 例示5つのうち、真に必要なもの

削除優先で kill-test:

| object | 判定 | 理由 |
|---|---|---|
| **Question** | ✅ 必須 | 開いた入力（kernel ③）。Question Commons の実体 |
| **Experiment Candidate** | ✅ 必須（軽量） | Transformation の可視出力（kernel ④）。問い→現実の橋。無いと「答えが魔法で湧く」ように見える。canonical 名で表示 |
| **Reality Feedback** | ✅ 必須（**最前面**） | 裁定者（kernel ⑤）。これを目立たせないと forum になる |
| **Discussion** | ❌ コアから削除 | kernel 非核（CONSOLIDATION §1）。問いは討議を経ずに最小実験へ至れる。**前面化すると Reddit/5ch 化（§9 #1）**。在ってよいが従属・無序列・脇役 |
| **Objection** | △ 分解 | **dignity-objection＝実験への唯一のゲート（property/flag として保持）**。merit-objection＝競合する別 Question に還元（社会的 debate object としては削除）。CONSOLIDATION §2 と一致 |

**結論（最小 object 集合）= 3つ: Question → Experiment Candidate → Reality Feedback。** 付随する*性質*: **dignity-gate** と **consent**（Experiment Candidate に付く flag であって独立 object でない）。**New Question は新 object 型でない**——Reality Feedback から張られた link を持つ、ただの Question（Art 2）。Discussion と Objection-as-debate は削除。

→ これは kernel ループ ③→④→⑤→reopen をそのまま陳列したもの。新概念ゼロ。

---

## 3. ホームページは何であるべきか

**「現実が答えた（／答えつつある）問いの台帳」**であって、「白熱した討議のフィード」ではない。

- 主役は **Reality Feedback**: 「この問いは実験になり、現実はこう答えた（executed/partial/failed）、そして次にこの問いを開いた」を最上位に。
- **trending / hot / top / 人気 の序列を一切持たない**（持てば Reddit）。並びは時系列か、ループの状態（asked / 実験化 / 現実待ち / 答えが返った）。
- **空状態が kernel を教える:** ローンチ直後は閉じたループ 0 件でよい。「まだ現実は一度も答えていない。最初の一周が進行中」と正直に表示する。*討議の数*でなく*現実の答えの数*をゼロと示すこと自体が「ここでは現実が決める」を伝える。
- 想い・支持・賛同の**数を出さない**（出せば petition）。

→ ホームページ = **無序列・reality-feedback 主役のループ台帳＋正直な空状態。**

---

## 4. 初訪問者が30秒で理解すべきこと

順に三点（What it is／the loop／What it refuses）:

1. **ここは議論に勝つ場ではない。現実が決める。**（差異化）
2. **開いた問いを持ち込むと、現実が答えられる形（実験）になり、現実が答え、それが次の問いを開く。**（ループ）
3. **投票も点数も序列も無い。誰が正しいか・どれだけ強く思うかを測らない。**（拒否）

一行で: **「開いた問いが現実の実験になり、群衆の票でなく現実の答えが効く場。」** 30秒で*間違った mental model（forum/Reddit/petition）を否定*できることが要件。だから hero は「何でないか」も明言する。

---

## 5. Reddit / 5ch / Stack Overflow / Discord / DAO / petition への degeneration をどう防ぐか

各々を、それを*定義する affordance* の**不在**で防ぐ。鏡像は CONSOLIDATION 付録と同型:

| なってはいけないもの | それを定義する affordance | 防ぐ削除（platform 側） |
|---|---|---|
| Reddit / 5ch | upvote/downvote 序列・討議が産物・trending | **票・score・trending を持たない**。討議は従属・無序列 |
| Stack Overflow | accepted answer・reputation・「解決済み」で閉じる | **accepted 無し・reputation 無し。ループは「解決」で閉じず「現実が答えた」で*再び開く***（非終端） |
| Discord | realtime chat・presence・community が産物 | **realtime/presence を持たない**。単位は durable な Question→RF 記録 |
| DAO | token 加重投票・on-chain 統治・treasury | **token 無し・投票無し・統治/金庫無し**。権威は外部現実 |
| petition site | 署名/賛同**数**が梃子（想いの集計） | **署名・賛同・"me too" の数を持たない**（想いを測らない） |

**統一規則（単一の削除）: プラットフォームは『人を数えるカウンタ』を一つも持たない。** upvote も reputation も署名も token 加重も view 数も「賛同 N 人」も無い。**意味を持つ唯一の数は現実の答え（executed/partial/failed）だけ。** この一削除が Reddit/5ch/SO/DAO/petition を**同時に**塞ぐ。Discord は「chat でなく durable 記録」で塞ぐ。

→ kernel を純粋に保つ削除（投票・序列・想い測定の不在）と、platform の degeneration を防ぐ削除は**同一**。加えるべき防御機構は無い。

---

## 6. 公開実演できる最小の Question → Reality Feedback 経路

**一本の最小ループ:**
1. 現実の Question を1件公開（開いた・想い由来）。
2. **最小の** Experiment Candidate 1件へ変換（最小の現実実験＝速い RF・低い dignity リスク。EXPERIMENT_REVIEW §3.1）。dignity-check ＋ consent を付す。
3. 唯一の具体 Binding（Dan-Go）で handoff → Claim → Execution。
4. **Reality Feedback が返り、Question に link して公開**（outcome は何でもよい）。
5. その RF が **New Question** を開く（link）。

→ 公開実演＝この一本の鎖を端から端まで可視化すること。**`failed` でも実演成功**（現実が語った＝kernel が動いた）。「最小経路」は*最小の実験を一つ*通すこと。新規不要——MVP_PLAN M1→M2 の公開版。

---

## 7. Dan-Go はどう現れるべきか — visible / optional / hidden / one Binding among many

**評価: visible ＋ one Binding among many ＋ 明示的に contingent。hidden でも default backend でもない。**

- **hidden は不可:** 現実の答えが*どの現実*から来たか隠すのは透明性違反。RF には出所（`implementer`）が要る。
- **無印の default backend は不可:** 「WAZIS＝Dan-Go の frontend」と学習され、**neutrality が perception で死ぬ**（REPO R2／U2）。2本目 Binding が要らなく見えてしまう。
- **正解 = 可視だが相対化:** UI は **「Binding スロット」**を構造的に*複数*として見せ、現状そこに Dan-Go が*一つ*入り、他は**空（"未"）**と示す。Reality Feedback は「現実が答えた経路: Dan-Go」と**出所帰属**して、WAZIS 自身の答えと混同させない（WAZIS は現実に触れない、を補強）。
- これは boundary review と一致: Dan-Go は WAZIS を知らない一実装先。**plurality を可視化することが neutrality を honest に保つ**（U2 の唯一の見える対策）。

→ **Dan-Go ＝ 可視・出所帰属つき・複数スロットの一つ・暫定的。** 特別扱いしない見せ方そのものが neutrality の表明。

---

## 8. TTFCL を達成しうる最小 MVP

**＝ 一本のループを公開可視化できる append-only 台帳 ＋ 最小の Question 投入口。** それ以上は不要。

**保持（最小）:**
- Question を投稿して公開記録にする。
- Experiment Candidate を1件付す（dignity-check ＋ consent ＋ Binding=Dan-Go）。
- 返ってきた Reality Feedback を Question に link して記録。
- New Question を RF に link。
- すべて公開・**読み中心・append-only**。

**削除（MVP に不要）:** アカウント/プロフィール/karma、投票・score・序列、検索、通知、realtime、moderation ツール、フィードの順位付け。**最初のループは curated/手作業でよい**（運用者が Dan-Go の RF を転記）。MVP の仕事は scale でなく、**一周を公開的に・kernel として legible に見せる**こと。

→ MVP_PLAN（M1 手作業ループ）の公開最小版。新規ゼロ。**「人を数える機構」をMVPに一つも入れないことが、後から純度を回復する手間より安い。**

---

## 9. 最初のプラットフォームの最も危険な失敗様式（severity 順）

二軸で評価する（identity 腐敗 × 不可逆性）。

| 順 | 失敗様式 | 種別 | なぜ危険 |
|---|---|---|---|
| **#1** | **kernel inversion — 討議/投票が事実上の裁定者になる。** discussion を前面化し、upvote/署名/score を足す | identity 即死 | あらゆる公開 forum の**重力**（利用者は票を期待し、運用者は engagement 機能を足す）。名は WAZIS のまま中身が Reddit に。最も起きやすく最も致命（不変項 I＋II 破壊） |
| **#2** | **どのループも閉じない — 全部討議で、Reality Feedback が一度も返らない。** 「無害なまま誰も助けない」 | 存在の不成立 | 活発（問い・コメント）に*見える*が kernel が一度も走らない＝forum の cosplay。活動が現実不在を覆い隠す（MVP_PLAN §6） |
| **#3** | **想い測定の侵入 — view/支持/フォロワー/人気の数が湧く（petition drift）** | 不変項 II 破壊 | metrics は成長の定石で無害に見える。集計された想いが現実を代替し始める |
| **#4** | **Dan-Go が暗黙の必須 backend 化 — neutrality が perception で崩れる** | 中立性の死 | 「WAZIS＝Dan-Go frontend」と学習され 2本目が来ない（§7／U2）。緩慢だが core 主張を殺す |
| **★** | **dignity/consent harm — 実 experiment が実在の人を傷つける** | 憲法（唯一の法）・**不可逆** | 確率は低いが**一件の重大度は最大**。他は feature を直せるが、傷つけた人は un-harm できない。Dan-Go 経由で現実に触れる以上、ゲート不全が実害に直結 |

**最も危険なもの（結論）:** *起きやすさ×identity 腐敗*では **#1（kernel inversion）**——放置すれば必ずそこへ落ちる重力。*不可逆性×憲法的 stakes*では **★（dignity harm）**——稀だが一度も起こしてはならない。この二つは別軸であり、**#1 を設計の常時の敵**として、**★ を絶対に超えてはならない線**として、両方扱うのが正しい。#2/#3 は #1 の親戚（forum 化の受動/metric 版）、#4 は時間差の中立性死。

---

## 10. 統合（一文で）

**WAZIS の最初の公開プラットフォームは『討議サイト』でなく『現実が答えた問いの公開台帳』であり、最小 object は Question→Experiment Candidate→Reality Feedback の3つ（＋dignity-gate と consent という性質、＋RF から link された New Question）に縮約され、Discussion と Objection-as-debate は削除される；ホームページは Reality Feedback を主役にし序列も想い測定も持たず、初訪問者は30秒で『群衆の票でなく現実が決める』と理解し、Dan-Go は隠さず・default にもせず『複数スロットの一つ・出所帰属つき・暫定』として現れ、最小 MVP は一本の Question→Reality Feedback ループを公開可視化する append-only 台帳（手作業可）で TTFCL を狙う——そして Reddit/5ch/SO/Discord/DAO/petition への degeneration は、kernel を純粋に保つのと*同じ単一の削除*、すなわち『人を数えるカウンタを一つも持たない』ことで同時に防がれる。最も危険な失敗は、放置すれば必ず陥る kernel inversion（討議/投票が裁定者になる）であり、最も超えてはならない線は、実 experiment による不可逆な dignity 侵害である。加えるべき層も概念も無い。**

---

*本書はレビューであり、実装・コード・既存ファイル修正・完成品設計を含まない。新概念/層を発明していない（§2 は kernel object の取捨、§5 は削除規則）。削除を加算より優先した（Discussion/Objection-as-debate を core から削除、object を3つへ）。canonical 語（Experiment Candidate / Transformation）を用いた。判定は kill+reification test に基づく仮説であり、最初の Reality Feedback で反証されうる。最危険: #1 kernel inversion（常敵）／★ dignity harm（不可逆の線）。*
