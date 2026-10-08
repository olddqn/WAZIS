# WAZIS Issue-Model Review / Issue モデルレビュー

- Date: 2026-06-22
- Scope: WAZIS は最小の Issue system（単一 Entry object）として実装できるか
- 種別: **レビューのみ**。実装・コード・既存ファイル修正を含まない。
- 規律: **削除を優先・新概念を発明しない・Dan-Go を再設計しない。**
- 接地: `WAZIS_IMPLEMENTATION_FLOOR_REVIEW`（Need＋RF・open/withdrawn・closure なし）・`OBJECT_REDUCTION`（handoff＝edge・WAZIS 所有スキーマなし）・`RF_INTERPRETATION`（討議を RF と認めれば kernel inversion）・`OPENNESS_RIGHT`（撤回は holder のみ）。

> **見出し: Yes。Need と Reality Feedback は単一の Entry に collapse する**（root＝Need、child＝RF/継続；**role であって type でない**）。**Entry テーブル 1 つ・RF テーブル不要・closure 完全消滅（status は open|withdrawn のみ）・撤回が唯一の terminal・Dan-Go は link のみ（スキーマ所有なし）**。これは**「closed」フィールドの*不在*で「閉じられない」を*構造的*に強制する**ため、開放性の権利をより良く保つ。**最重要の答え：GitHub Issues から {votes・ranking・closure} を除き author-only-withdrawal にすれば、構造的に WAZIS に*極めて近い*——ただし最深の削除は close ボタンでなく*権威モデル*（maintainer/owner が他者の Issue を閉じ/lock/編集できないこと＝no-governor）。WAZIS ＝「governance なき Issues」。** collapse で唯一保つべき点：**RF は type でなく provenance（外部現実への link）で討議と区別する**——さもなくば討議が RF を僭称（kernel inversion）。

---

## 1. Need と RF は単一 Entry に collapse するか — Yes

- Need と RF の構造的差は**位置（root か child か）**だけ。Need＝originate する root、RF＝応答する child。
- RF の「特別」フィールド（outcome＝executed/partial/failed/impossible、implementer）は **Dan-Go の Claim に在り**（link）、WAZIS に置く必要がない。WAZIS の RF ＝「現実が答えた」を text にした child Entry（＋ Dan-Go への link）。
- → **Need/RF は relationship role。別の object type でない。** 2 object → 1 object（Entry）への更なる削除。

---

## 2. 別の RF テーブルは必要か — No

- RF ＝ child Entry。構造化 Dan-Go フィールドは Dan-Go（link 先）に在る。
- → **`entries` テーブル 1 つで足りる。**

---

## 3. closure は完全に消えるか — Yes（そして重要）

- status は **open | withdrawn のみ。「closed」は無い。**
- **「closed」フィールドの*不在*が「開放性の権利」を*構造的に*enforce する**——誰も閉じられない（schema が「閉じる」を表現できない）。これは規則でなく**データモデルによる強制**ゆえ侵されえない。
- 現実が答えても（child RF Entry が付いても）**親 Need は open のまま**（NON_GAPABLE：open/withdrawn のみ）。
- → **closure 完全消滅。** GitHub Issues との最大の構造差＝**closed 状態の除去**（closed ＝ verdict 機構）。

---

## 4. 撤回が唯一の terminal state か — Yes

- open → withdrawn、**holder のみ**が行う。resolved/done/closed は無い。
- 撤回は holder の sovereign な行為（OPENNESS_RIGHT：Need は holder のもの）。
- → **唯一の terminal ＝ withdrawal（holder only）。**

---

## 5. これは開放性の権利をより良く保つか — Yes（床より良く）

1. **構造的 enforcement:** open|withdrawn のみの単一 Entry は **closed を表現*できない*** ゆえ、誰も Need を閉じられない。規則でなく schema が権利を守る（より robust）。
2. **RF が verdict にならない:** RF を別 type にせず child Entry にすると、**RF は他の Entry より「最終的」な地位を持たない**。RF child は親を閉じない＝**RF-as-verdict を構造的に防ぐ**（RF_INTERPRETATION の懸念）。
- → 「閉じない」と「RF は裁定でない」を**規則でなく構造**にする＝床より良く権利を保つ。

---

## 6. Dan-Go 統合は link のみで（スキーマ所有なしに）成立するか — Yes

- WAZIS は **Dan-Go スキーマを一切所有しない**（gap/outcome/Claim フィールドを持たない）。
- Entry が **Dan-Go Claim への link** を持つ（URL/参照）。構造化データ（observed/required/missing・outcome）は Dan-Go に在る。
- link は Dan-Go でも**他の実装先（NPO/OSS）でも**指せる → **binding 中立**（OBJECT_REDUCTION の「Dan-Go 寄りスキーマを所有しない」中立性の勝ち）。
- → **Dan-Go 統合＝link のみ。** そして**この link が RF role を*marks* する**（§10）。

---

## 7. 最小 UI

- **Entry の tree（threaded）。** 各 Entry：text・author・time・open/withdrawn。
- **root Entry を voice**（Need を共有）。
- **返信＝child Entry を足す**（継続・現実の答え・Dan-Go への link）。
- **自分の Entry を取り下げる（withdraw）**。
- **読む。**
- **vote/close/score/rank ボタン無し。**
- → **stripped な issue thread：post / reply / withdraw-own / read。それだけ。**

---

## 8. kill-test を生き残るもの

```
Entry（唯一の object）
  id
  parent_id      … null＝root。Need←RF/継続 の関係を表現
  text
  author         … DID/pseudonym（評判 profile でない）
  created_at
  status         … open | withdrawn     （closed なし）
  〔link〕        … 任意。他 Entry/外部実装先（Dan-Go Claim 等）への参照
```

- Need/RF は **position（root/child）＋ provenance（外部 link の有無）による role**。
- 削除されたもの：RF テーブル・outcome enum・gap フィールド・score・vote・closed 状態・category-rank・assignee/milestone。
- → **survive ＝ 1 object（Entry）＋ parent_id（tree）＋ link。** これ以下に削ると関係（Need↔応答）を表現できなくなる＝床。

---

## 9. 最重要：votes/ranking/closure なし・撤回のみの GitHub Issues は、既に構造的に WAZIS に近いか — Yes（深い caveat 付き）

GitHub Issues ＝ issue（root）＋ comments（children）＋ **closed 状態** ＋ reactions（票）＋ labels ＋ assignees/milestones（管理）＋ links。

**Issues から削除すると:**
| 削除 | WAZIS 原則 |
|---|---|
| reactions（👍） | 想い 非測定（票/測定なし） |
| reaction での並べ替え | ranking なし |
| **closed 状態** | **開放性の権利（閉じない）** |
| **author 以外による close** → author-only withdrawal | **no-governor（撤回は holder のみ）** |

→ **構造的に極めて近い。** WAZIS ≈「**votes・ranking・closure を除き author-only-withdrawal にした Issue tree**」。

**深い caveat（最重要）：最深の削除は close ボタンでなく*権威モデル*。**
- GitHub Issues は **repo に所有され、maintainer/owner が他者の Issue を close/lock/edit/hide できる**。「stripped Issues」でもこの**権威**が残る。
- WAZIS は **no-governor**：自分の Entry の撤回以外、誰も他者の Entry に権威を持たない（close も lock も edit も hide も不可）。
- → **WAZIS ＝「governance なき Issues」。** 削るのは可視 feature（票/ranking/close ボタン）だけでなく、その下の**権威の構造**（所有者・maintainer が他者を支配できること）。

→ 結論：**WAZIS の床は exotic でない。familiar な issue tree に、精密な削除集合 {票・ranking・closure・権威} を施したもの。** philosophy（a right）が、見慣れた構造に*異なる規範*（票/ranking/closure/governance なし・撤回のみ）で instantiate される。

---

## 10. collapse で唯一保つべき点：RF は provenance で discussion と区別する

- RF と discussion-comment は**ともに child Entry**——type で区別しない。
- だが**何も区別しないと、討議が RF を僭称しうる**（RF_INTERPRETATION §8-1：討議の結論を RF と認める＝kernel inversion＝最危険）。
- **区別は type でなく provenance：RF ＝ 外部現実への link（Dan-Go Claim の execution・実装先の結果）を持つ child Entry。** 外部 link 無し＝ただの discussion/継続。
- → **「現実が答えた」は外部 link で marks される**（型旗でなく property ＝ role のまま）。UI は外部 link を持つ Entry（RF）を前景化しうる（PLATFORM の「RF 前景化」を型なしで実現）。**これだけは collapse で消してはならない。**

---

## 11. 統合（一文で）

**WAZIS は単一 Entry object（id・parent_id・text・author・created_at・status＝open|withdrawn・任意 link）の最小 Issue system として実装でき、Need は root Entry・Reality Feedback は外部現実への link を持つ child Entry という*位置と provenance の role*であって別 type でなく（RF テーブル不要・構造化 Dan-Go データは link 先の Dan-Go に在る）、status から「closed」を*除去*することで「閉じられない＝開放性の権利」を規則でなく構造として enforce し（撤回が唯一の terminal・holder のみ・RF child は親を閉じず verdict にならない）、Dan-Go 統合は WAZIS がスキーマを所有せず link のみで成立して binding 中立を保ち、最小 UI は post/reply/withdraw-own/read の stripped な thread（vote/close/score/rank ボタンなし）であり；最重要の問いへの答えは「GitHub Issues から votes・ranking・closure を除き author-only-withdrawal にすれば構造的に WAZIS に極めて近い——ただし最深の削除は close ボタンでなく権威モデル（maintainer/owner が他者の Entry を close/lock/edit できないこと＝no-governor）で、WAZIS ＝『governance なき Issues』」であり、philosophy（a right）が familiar な issue tree に異なる規範で instantiate される；collapse で唯一保つべきは RF を type でなく provenance（外部現実への link）で discussion と区別すること（さもなくば討議が RF を僭称して kernel inversion）——足すべき機構は無く、これが建てられる最小である。**

---

*本書はレビューであり、実装・コード・既存ファイル修正を含まない。削除を優先した（2 object → 1 Entry、RF テーブル/outcome enum/gap フィールド/closed 状態/票/score を削除）。Need/RF ＝ role（position＋provenance）であって type でない。closure 消滅・撤回が唯一の terminal（holder only）。Dan-Go 統合＝link のみ（スキーマ所有なし・binding 中立）。最重要：votes/ranking/closure を除き author-only-withdrawal の Issues は構造的に WAZIS に近いが、最深の削除は権威モデル（no-governor）＝「governance なき Issues」。唯一の保存：RF は provenance（外部 link）で discussion と区別（type でなく）。新概念を発明せず・Dan-Go を再設計せず。判定は kernel に基づく仮説であり最初の Reality Feedback で反証されうる。*
