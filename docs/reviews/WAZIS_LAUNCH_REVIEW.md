# WAZIS Launch Review / ローンチ・レビュー

- Date: 2026-06-22
- Scope: 「Repository exists」→「First public closed loop exists」までの**最短経路**と launch readiness
- 種別: **レビューのみ**。実装・コード・既存ファイル修正を含まない。
- 規律: **WAZIS を再設計しない・機能を足さない・概念を足さない・削除を加算より優先。** launch readiness のみに集中。
- 前提: 既往8レビューは有効。ただし**直接観察が前提を覆す場合は観察を優先する**。

> **見出しの答え:** ローンチを阻むのは*哲学*でも*構造*でもなく、ほぼ全て**運用と一つの憲法ゲート**である。最短経路は「もう一周考える」ことではなく、**現実に触れて返ってくる一本のループを公にやり切る**こと。**ただし観察上、前提が崩れている**（§0）。

---

## 0. まず直接観察 — 前提の訂正（最重要）

ユーザー前提「WAZIS already exists as a public GitHub repository」は、**観察により否定される**:

- この作業ディレクトリは **git リポジトリですらない**（`.git` 無し・remote 無し）。**GitHub に公開されていない。**
- ルートの .md 16 件のうち **10 件が review/哲学**（KERNEL/BOUNDARY/META_LOOP/TRANSFORMATION/CONSOLIDATION/PLATFORM/OBJECT_REDUCTION/RF_INTERPRETATION/REPOSITORY/EXPERIMENT_DRIVEN）、canonical な核は 6 件（README/CONSTITUTION/SPEC/MVP_PLAN/CONTRIBUTING/COC）。**訪問者は「公開された討議場」でなく「哲学アーカイブ」に着地する。**

→ ゆえに本書は「公開済み」を装わない。最短経路は **(a) 実際に公開する**＋**(b) 哲学を後景化して一本のループを前景化する**から始まる。これは launch blocker #0。

---

## 1. 最短経路: Repository exists → First public closed loop

削除優先の最小手順（手作業で可・platform 不要・新機能ゼロ）:

```
[0] 公開する           : git init → push（public）。review 群を docs/reviews/ へ後景化。placeholder 2件を実値化
[1] Question #001 を立てる: 小さく・現実の・同意可能・Dan-Go で実行可能・観測明瞭な問い（§6）
[2] handoff             : dignity-check ＋ 当事者 consent を満たし、Dan-Go へ Claim として渡す（bindings/dan-go）
[3] Dan-Go が実行       : 現実に触れる（WAZIS は触れない）
[4] Reality Feedback    : 返った観測を公開記録（feedback/。outcome は何でもよい・failed でも成立）
[5] New Question        : その RF が開く次の問いを公開（link）
```

→ [1]→[5] が見えれば **first public closed loop**。**[4] が `failed` でも成立**（現実が一度語った＝kernel が現実で走った）。これは MVP_PLAN M1→M2 の公開最小版で、新規ゼロ。

---

## 2. 公開前に何が欠けているか（cosmetic / structural / constitutional / operational）

| 区分 | 欠けているもの | launch を阻むか |
|---|---|---|
| **cosmetic** | config.yml の `OWNER`、README の Dan-Go URL（空 placeholder）、dual-license の CC-BY 裏付け、命名ドリフト（Implementation→Experiment Candidate） | ✋ 阻まない（着手ついでに直す） |
| **structural** | `examples/`（記入例）、ループを端から端まで見せる場所 | ✋ ほぼ阻まない（**#001 自体が最初の example かつループ**になる）。review 群の後景化は要（§3） |
| **constitutional** | **#001 の handoff 前の、本物の consent ＋ 本物の dignity-check**／公開表示に投票・序列・想い測定を**入れない**こと | ⛔ **阻む（正しく）**。現実に触れる実験は、同意と尊厳が満たされるまで走らせない（唯一の法・PLATFORM ★） |
| **operational** | **(0) 未公開（git/GitHub）**／**(1) Claim を受け RF を返せる生きた Dan-Go**／**(2) 同意する実在の当事者**／**(3) handoff を回す人（operator）**／**(4) #001 を meta から「閉じられる具体実験」へ** | ⛔ **これが本体の blocker** |

→ **要旨: 阻むのは operational（公開・生きた Dan-Go・同意者・運用者）＋一つの constitutional ゲート（#001 の consent/dignity）だけ。** cosmetic と多くの structural は阻まない。**「考え不足」は blocker ではない**——核は十分（CONSOLIDATION）。

---

## 3. リポジトリ前面（README）に何が出るべきか

PLATFORM_REVIEW の判断を launch に適用: **前面はループ／Reality Feedback を前景化し、哲学を後景化する。**

- 先頭 1 行: WAZIS とは（開いた問いを現実が答えられる形へ変え、討議でなく現実が裁定）。
- ループ図 ＋ **「これは何でないか」**（forum/投票/DAO/petition でない）。
- **正直な現状表示:** 「閉じたループ: 0 / 最初の一周（Question #001）進行中」＋ #001 と（やがて）その Reality Feedback への link。**討議数でなく現実の答えの数を出す**（PLATFORM）。
- 参加導線（Question を開く）／不可侵条項（dignity・consent・withdrawal）／Constitution への link。
- **review 10 件を `docs/reviews/` へ移し「research notes（非 canonical）」と明示**（Dan-Go の `docs/research/` と同様）。これは再設計でなく**前面の雑音削除**（削除優先）。訪問者が哲学の壁でなく*一本のループ*を最初に見るために必須。

→ README の大半は既存。launch に要るのは **(a) 正直なループ状態表示、(b) 哲学の後景化** の2点だけ（機能でなく整理）。

---

## 4. 訪問者が30秒で理解すべきこと

PLATFORM §4 ＋ launch 分:
1. **ここは議論に勝つ場でない。現実が決める。**
2. **開いた問い→現実の実験→現実の答え→次の問い。**（ループ）
3. **投票も点数も序列も無い。**
4. **（launch 分）いま最初の本物のループが動いている。** ← 理論でない証拠（#001 への link）。

一行: **「開いた問いが現実の実験になり、群衆の票でなく現実の答えが効く——その最初の一周がここで進行中。」**

---

## 5. 最小の公開ワークフロー: Question → ? → Reality Feedback

**「?」＝ handoff（現実応答可能な形への変換 ＋ Dan-Go への引き渡し ＋ 実行）。** 最小:

```
Question（公開 issue ＋ questions/q-001）
  → ? ＝ handoff{ dignity-check ＋ consent ＋ Dan-Go Claim へ写像 } → Dan-Go が実行
  → Reality Feedback（feedback/rf-001・outcome 任意）
  → New Question（link）
```

最小経路 = **一問・一 handoff（唯一の binding ＝ Dan-Go）・一 RF・一 New Question。手作業。** 「?」を担うのは**人**: 最小の Dan-Go 実行可能な実験へ変換し、consent と dignity を満たし、Dan-Go が実行する。（OBJECT_REDUCTION 通り「?」は handoff edge だが、launch では再設計せず現状の流れで回す。）

---

## 6. Question #001 は何にすべきか（TTFCL で評価）

判定基準（TTFCL ＝ 最初の閉ループまでの時間を最短化）: **最小・現実・同意容易・Dan-Go 実行可能・観測明瞭・dignity 低リスク。**

| 候補 | 規模/速度 | dignity リスク | Dan-Go 実行可能性 | TTFCL 判定 |
|---|---|---|---|---|
| **refugee economic independence** | 巨大・系統的・数ヶ月〜年・多主体 | **高**（脆弱な人・consent 重・言語/法） | 低（一 Claim に収まらない） | ❌ **#001 не適**（閉じるのが遅すぎ・dignity リスク最大・#2「閉じない」失敗様式） |
| **AI elder support** | 大・曖昧（どの実験?）・敏感 | **高**（脆弱な高齢者・安全/consent） | 低〜中（実機を実人へ＝遅く危険） | ❌ **#001 не適**（同上。何の実験か未確定） |
| **another（推奨）= 最小の同意済み Dan-Go 実行可能な micro 実験** | 小・数日〜数週で閉じる | **低**（理想は提案者自身/非脆弱な willing 当事者） | 高（Claim→Contribution→Execution に綺麗に写る） | ✅ **#001 適** |

**評価結論:** **refugee economic independence も AI elder support も #001 にしてはならない**——どちらも閉じるのが遅く、最も dignity リスクが高く、最初の一周（loop-prover）には不適。両者は Commons の正当な*早期 Question*ではあるが、**TTFCL を証明する #001 ではない**。

**#001 は、いま実在する・同意の取れる・小さく観測明瞭で Dan-Go が速く実行できる micro 実験**にすべき。具体ケースは捏造できない——**Dan-Go の `FIRST_CASE_CANDIDATES.md` / `FIRST_REAL_CASE_PROTOCOL.md` から実在の一件を採り、WAZIS の #001 ＝ Dan-Go の最初の実ケースに揃える**のが最短（WAZIS の TTFCL と Dan-Go の TTFR を一致させる）。**現状の `docs/genesis-issue-1.md`（「最初にどの問いを選ぶか」というメタ問い）は #001 не適**——それ自体は現実に渡せず RF を生まない（REPO R1）。#001 は**閉じられる具体実験**でなければならない。

---

## 7. どの未解決が launch を阻み、どれは待てるか

**阻む（最初の公開ループの前に必須）:**
- **B0 公開**（git init → GitHub public）。
- **B1 生きた Dan-Go**（Claim を受け RF を返せる）。binding が動かねば閉じない。
- **B2 #001 の実在する同意当事者 ＋ 本物の dignity-check**（唯一の法・PLATFORM ★）。
- **B3 handoff を回す operator**。
- **B4 #001 を meta から「閉じられる具体実験」へ**（§6）。

**待てる（最初のループを阻まない・後回し）:**
- **U5** 仕様の命名/収束語整理（Implementation→Experiment Candidate、Reality Action→Transformation、収束語削除）。重要だが手作業一周は阻まない。
- **OBJECT_REDUCTION** EC→handoff edge 化。現状 object でループは回る。
- **U2/M-e** 2本目 binding（中立性の証明）。**ループが回ることを先に証明し、中立性は後**。
- **U3** fan-out 選択機構（候補多数で初めて要る）。**U1** 第三者 dignity 裁定（実ケース発生時のみ・#001 は起こさない選択を）。
- **cosmetic** placeholder・CC-BY・examples/。

→ **launch を阻むのは思考でなく*行為***: 公開・生きた Dan-Go・同意当事者・operator・閉じられる #001。

---

## 8. 今週ただ一つやるなら

**「閉じられる本物の #001（小・同意済み・Dan-Go 実行可能）を確定し、Dan-Go への handoff を開始する。」**

理由: 他（前面整理・placeholder・仕様整理）は二次。**律速段階は『実在し同意の取れる小さな閉じられる実験を見つけること』**で、最もリードタイムが長く、急げない。これさえ動けば残りは速い。（**公開（B0）は同日できる前提作業**であって今週の難所ではない。哲学を増やすことではない。）

---

## 9. WAZIS が本物だと証明する最小の公開デモ

**公開された一本の閉ループ:**
```
Question #001（公開） → handoff（公開: consent ＋ dignity-check ＋ Claim） → Reality Feedback（公開・任意 outcome） → New Question（公開・link）
```

証明の核は「実験が**成功した**こと」ではない。**「問いが現実へ出て、現実が公に答え、その答えが次の問いを開いた」**こと——kernel が紙上でなく**現実で一度走った**こと。**一本、端から端まで、公開で。** これが「WAZIS は本物」の最小証明（TTFCL/TTFRF 達成・`failed` でも成立）。

---

## 10. 統合（一文で）

**WAZIS のローンチを阻むのは哲学でも構造でもなく、ほぼ全て運用——未公開（git/GitHub にすら無い）・Claim を受け RF を返せる生きた Dan-Go・同意する実在の当事者・handoff を回す人——と、一つの憲法ゲート（#001 の本物の consent と dignity-check）であり、最短経路は『もう一周考える』ことでなく、公開して哲学を後景化し（review 10 件を docs/reviews/ へ）、閉じられる小さな同意済みの Question #001（refugee economic independence でも AI elder support でもなく、Dan-Go の最初の実ケースに揃えた micro 実験）を立て、Dan-Go へ渡し、返った Reality Feedback（failed でも可）を公開し、それが開く New Question を公開する——この一本の公開ループを最後までやり切ること；今週ただ一つやるなら、その閉じられる #001 を確定して handoff を始めること。U5・2本目 binding・object 縮約・命名整理は launch 後でよい。足すべき機能も概念も無い。**

---

*本書はレビューであり、実装・コード・既存ファイル修正を含まない。WAZIS を再設計せず・機能/概念を足さず・削除を優先した（review の後景化、#001 の縮小、待てる項目の切り分け）。**直接観察により前提「公開済み」を訂正した（§0：未 git・未公開）**。判定は launch readiness に基づく仮説であり、最初の Reality Feedback で反証されうる。最大 blocker は思考でなく行為（B0–B4）。今週の一手＝閉じられる #001 の確定と handoff 開始。*
