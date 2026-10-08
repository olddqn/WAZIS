# WAZIS MVP Final Architecture Review / 最終アーキ整合レビュー

- Date: 2026-06-22
- Scope: 提示された MVP アーキが内部整合で launch に十分かを判定する
- 種別: **レビューのみ**。実装・コード生成・既存ファイル修正を含まない。矛盾が見つからない限り再設計しない。
- 規律: **削除を優先・新概念/層/governance/score/moderation/maturity 追跡/claimability 追跡を導入しない・真の矛盾のみを指摘する。**
- 接地: 全レビュー群（kernel・gapability・openness-right・implementation-floor・issue-model・mvp-screen）。

> **見出し: 真の矛盾は無い。四性質（想い 非測定・no-governor・現実が裁定・開放性の権利）はすべて保たれる。本質は何も失われていない。判定＝Build。**
>
> **「Reduction is complete. Build.」**
>
> 実装上の前提（既存・新概念でない）1 つ：`author` を**認証可能な最小 identity** にすること（さもなくば誰でも他者を撤回でき no-governor が崩れる）。既知の限界（launch を阻まない）1 つ：dignity 対 no-moderation のスケール時の緊張（＝U1）——curated な MVP では問題にならず、**現れたとき governance を足さずに**扱う（先に moderation を作らない）。

---

## A. 矛盾の有無

**No contradictions found.**（真の矛盾なし。）

検討した候補と解消:

1. **「verifiable external link」対 「no moderation」。** RF は「↩ Reality Answered」と表示されるが、system は link が*本当に現実か*を検証しない（moderation 禁止）。これは矛盾か?
   → **否。「verifiable」＝読み手が link で*検証できる*（透明性）であって、system が*裁定する*ではない。** system が裁定すれば no-governor 違反。link を*露出*し検証を読み手と objection（返信）に委ねるのは、Dan-Go の「透明性に支えられた社会契約（ブロックチェーンでない）」と同型。**「↩ Reality Answered」＝「検証可能な link を持つ child がある」であって「system が現実と認証した」でない**——この読みで整合。矛盾でなく semantic 明確化。

2. **撤回した root に生きた children（返信/RF）が残る。** 矛盾か?
   → **否。正しい append-only 挙動。** 撤回は*自分の*content を消す（text→「取り下げ」）が、他者の返信は消せない（no-governor）。node は残しスレッド構造を保つ。撤回の事実は残る。整合。

3. **dignity（唯一の法）対 no-moderation。** dignity 侵害的な返信を、moderation 無しでどう除くか?
   → **論理矛盾でない（既知の残余）。** dignity は moderation 権威でなく**透明性＋objection（返信）＋当事者の withdrawal（root を下げて離脱）＋社会契約**で守られる。これは consolidation review の **U1（係争中の第三者 dignity を vote/governor なしにどう扱うか）**そのもので、**先に governance を作れば no-governor を侵す**ため、**現れたとき非 governance で扱う**のが既定方針。curated・小規模の最初のループでは launch を阻まない。**規則は相互に整合（dignity は非 moderation の手段で守られる）；十分性はスケール時の運用問題であって論理矛盾でない。**

4. **全 action 対 全 property。** Create/Reply/Withdraw-own のいずれも measure/govern/close/開放性侵害をしない（§B 表）。**整合。**

5. **禁止 action の不在。** vote/like/score/rank/trending/resolve/close/priority/assign/milestone/reputation/karma/mod-closure/governor——**すべて不在。** 整合。

6. **「RF は type でない」対 「↩ Reality Answered 表示」。** 表示は **property（外部 link の有無）による rendering** であって type 旗でない。整合。

---

## B. 欠けている load-bearing 要素

**None（概念として欠落なし）。**

ただし**既存要素 1 つの実装が load-bearing**ゆえ明記する（新概念でない）:

- **認証可能な最小 identity。** schema は `author` を持ち、規則は「撤回は author のみ」とする——これを*強制*するには、現在の利用者＝author を**認証**できねばならない（handle＋secret/session、または account）。無ければ誰でも他者を撤回でき＝**no-governor が崩れる**。これは**既存の pseudonym/DID identity を床の水準で実装する**ことであって、新概念・新層でない。**これだけは必ず存在せねばならない。**

（dignity-at-scale ＝ U1 は「欠けた load-bearing 要素」でなく**既知の未解決**。curated MVP を阻まず、governance で先に解いてはならない。）

---

## C. 最終判定

**Build。**

理由:
- **内部整合**（A：真の矛盾なし）。
- **四性質すべて保存**（§下表）。
- **本質は何も失われていない**（§最重要）。
- 唯一の前提＝既存 identity の最小実装（B）。既知の限界（U1）は小規模 launch を阻まず、解法を先取りしない。

→ **Reduction is complete. Build.**

---

## 四性質の検証

| 性質 | 保存か | 根拠 |
|---|---|---|
| **想い 非測定** | ✅ | score/vote/rank/priority/reputation/karma いずれも無し。homepage に per-user count・人気指標なし。Need を測る field なし（created_at＝時間で merit でない） |
| **no-governor** | ✅（identity 前提） | 撤回は author のみ。他者の Entry の close/edit/delete/lock/hide 不可。mod/assign/milestone 無し。※author 認証が要件（B） |
| **現実が裁定** | ✅ | RF＝外部現実 link を持つ child（provenance）。link 無し＝討議であって RF でない。「現実が、討議でなく、答えた」を link で marks |
| **開放性の権利** | ✅ | status は open|withdrawn のみ。closed/solved/resolved/completed 無し。Need は閉じない＝**「閉じられない」を schema の*不在*で構造的に enforce**。RF child は親を閉じず verdict にならない |

---

## 最重要の問い：これを建てれば WAZIS の名に値するか、本質が失われたか

**値する。本質は失われていない。**

本質要素の所在を確認:
- **開放性の権利**（最深の結論）→ closure なし。✅
- **想い 非測定** → score/vote/rank なし。✅
- **no-governor** → 撤回は author のみ（identity 前提）。✅
- **現実が裁定** → RF は外部 link で区別。✅
- **holder の sovereignty／self-translation** → 自分の Need を作り・下げるのは本人；返信は他者だが Need を支配しない。✅
- **非終端** → Need は閉じず、RF が新しい Need を開きうる。✅
- **WAZIS ＝ instantiated な right** → アーキ＝right を*不在*（NOT-list）で operative にしたもの。✅
- **ループ** → Need(root) → Dan-Go link 付き返信（handoff＋RF）→ 新しい問い/root。Entry モデルで表現可（handoff は場外手動・RF は link 付き返信）。✅

→ **どれも present。これ 1 つ（identity）を満たして*これだけ*を建てれば、それは WAZIS である。** 何も essential は落ちていない。

---

## 統合（一文で）

**提示された MVP アーキ（単一 Entry：id/parent_id/author/text/created_at/status[open|withdrawn]/link、role は position＋provenance、操作は Create/Reply/Withdraw-own、禁止は vote〜governor、RF＝外部現実 link を持つ child、status は open|withdrawn のみで closure なし、Dan-Go は外部で link が十分、homepage は新しい順・無順位・per-user count なし）には真の矛盾は無く、四性質（想い 非測定・no-governor・現実が裁定・開放性の権利）はすべて構造的に保存され、本質（right to remain open・holder sovereignty・非終端・reality arbitrates・instantiated right・ループ）は何も失われておらず、唯一の load-bearing な実装前提は既存の `author` を認証可能な最小 identity にすること（さもなくば no-governor が崩れる——新概念でない）、唯一の既知の限界は dignity 対 no-moderation のスケール時の緊張（＝U1）で curated な MVP launch を阻まず governance で先取りしてはならず、ゆえに——A：No contradictions found／B：None（ただし最小 identity の実装は必須・既存）／C：Build——Reduction is complete. Build.**

---

*本書はレビューであり、実装・コード生成・既存ファイル修正を含まない。新概念/層/governance/score/moderation/maturity 追跡/claimability 追跡を導入していない。真の矛盾のみ判定：無し。四性質保存。本質喪失なし。前提＝既存 identity の最小実装（no-governor のため）。既知の限界＝U1（dignity-at-scale、curated MVP を阻まず・先取り禁）。判定＝Build。Reduction is complete. Build. 本判定も kernel に基づく仮説であり最初の Reality Feedback で反証されうる。*
