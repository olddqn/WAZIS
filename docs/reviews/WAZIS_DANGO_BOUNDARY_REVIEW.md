# WAZIS × Dan-Go Boundary Review / 境界レビュー

- Date: 2026-06-22
- Scope: WAZIS（reality-feedback protocol）と Dan-Go（social implementation protocol）の境界を同定する
- 種別: **レビューのみ**。実装・コード・既存ファイル修正を含まない（本書の新規作成のみ）。
- 前提: Dan-Go=社会実装プロトコル／WAZIS=reality-feedback プロトコル／Dan-Go は WAZIS の一 Binding になりうる／WAZIS は独立を保つ。
- 参照: [WAZIS_KERNEL_REVIEW.md](WAZIS_KERNEL_REVIEW.md)・[WAZIS_EXPERIMENT_DRIVEN_REVIEW.md](WAZIS_EXPERIMENT_DRIVEN_REVIEW.md)・Dan-Go `MUJIN_PROTOCOL.md` / `CONSTITUTION.md`

> **一行結論:** 境界は**物質的でなく目的論的（teleological）**である。両者は同じ DNA（dignity・Reality Feedback・想い=0層・DID）を共有するが、**WAZIS は「開いた問い」を扱い（commit 前・発散・再開）、Dan-Go は「コミットした deed」を扱う（commit 後・収束・実現）**。境界線は **commit line（コミット線）**——*asking* と *doing* の境目——である。両者とも Reality Feedback に依存するが、**WAZIS は RF で「ある／在る」（RF＝裁定者＝identity）**のに対し、**Dan-Go は RF を「持つ」（RF＝Phase 4＝feedback 器官）**。

---

## 0. なぜこの問いが鋭いか — 共有 DNA

両者は驚くほど多くを共有する。だから「同じものでは?」という疑いが生じる:

| 共有要素 | WAZIS | Dan-Go |
|---|---|---|
| 唯一の法 | dignity | dignity |
| 想い | 0層・不可触 | 0層・不可触 |
| Reality Feedback 語彙 | executed/partial/failed/pending | executed/partial/failed/pending |
| identity | DID/pseudonym | DID/pseudonym |
| AI の役割 | recorder/mediator（not governor） | recorder/mediator/missionary（not governor） |
| method-agnosticism | 手段不問・目的志向 | 「助かるなら方法はなんでもいい」 |

→ 共有 DNA がこれだけある以上、境界は**構成要素の違い**にはない。境界は**それらを何のために使うか（telos）**にある。以下それを示す。

---

## 1. Q1 — 両者とも RF に依存するなら、実際の境界は何か

**境界 = commit line。WAZIS は commit 前の「問い」、Dan-Go は commit 後の「deed」。** 同じ RF を、片や oracle（神託）として、片や grade（成績）として読む。

### 1.1 六つの軸での境界

| 軸 | WAZIS | Dan-Go |
|---|---|---|
| **telos（目的）** | 探究（inquiry）— 開き続ける | 実装（implementation）— 実現して閉じる |
| **単位** | 開いた Question / Experiment Candidate | Claim（コミットされた状態遷移） |
| **RF への依存の仕方** | RF **で在る**（RF=裁定者=identity。無ければ WAZIS でない） | RF **を持つ**（RF=Phase 4=最終器官。Dan-Go の identity は coordination engine） |
| **RF の読み方** | **oracle**: 「現実は何を明かしたか／次に何を問うか」 | **grade**: 「コミットした遷移は実現したか・誰か助かったか」 |
| **運動の向き** | 発散・再開（fan-out, 非終端） | 収束・実現（一つの Claim を閉じる） |
| **行為** | **実装しない**（第7条）。実験を渡すだけ | **coordinate して execute する**（Contribution→Execution） |

### 1.2 核心 — 同じ RF イベント、二つの読み

WAZIS が Dan-Go を Binding にするとき、**Dan-Go の Execution+RF が、WAZIS の一実験に対する「現実の答え」になる**。同じ一つのイベントが二通りに読まれる:

- **Dan-Go にとって:** 「Claim X は executed。gap は閉じた。trust 更新。」——**成績（grade）。一周の完了。**
- **WAZIS にとって:** 「実験 A に現実が応えた。さて、これは次にどんな問いを開くか。」——**神託（oracle）。次の問いの起点。**

→ 境界は**信号（RF）でなく、信号の読み方（telos）**にある。Dan-Go は RF を**閉じる**ために、WAZIS は RF を**開く**ために使う。

### 1.3 もう一段深く — engine の種類

- Dan-Go（MUJIN_PROTOCOL 自己定義）: 「予測エンジンでなく **coordination engine**」——*doing* を調整する。
- WAZIS（kernel review）: **reality-arbitration loop**——*knowing/choosing* を現実に裁定させる。

**coordination engine（実装を調整）vs arbitration engine（探究を現実が裁定）。** これが engine レベルの境界。

### 1.4 kernel との一致（独立性の根拠）

WAZIS の kernel 不変項は「**WAZIS は実装せず、自らが支配しない外部の現実へ届く**」。**Dan-Go はまさに『WAZIS が支配しない外部の現実』の一つ**である。だから——
- Dan-Go を Binding にしても WAZIS の kernel は壊れない（Dan-Go が外部現実チャネルを供給する）。
- **WAZIS が Dan-Go を支配しない**こと（Dan-Go は WAZIS を知らない、§7）が、kernel 充足と独立性の**両方**を同時に満たす。kernel の「外部性」要件と独立性要件は**同じ要件**である。

---

## 2. Q2 — WAZIS にできて Dan-Go にできないこと

1. **問いを「開いたまま」保持する。** Dan-Go の単位 Claim は既にコミットされた遷移（observed/required/desired を持つ）。Dan-Go には「まだ Claim ですらない真に開いた問い」を保持する native object が無い。WAZIS は commit 前の openness に座れる。
2. **異種・複数の実装先へ競合実験を fan-out し、現実の答えを横断比較する。** Dan-Go は**一つの実装先**であり、自分の代わりに NPO/OSS/研究へ振り分けられない。WAZIS は Dan-Go vs NPO vs 研究の答えを同じ問いの上で比べられる。
3. **実現した Claim を「一データ点」として再び開く。** Dan-Go は実現 Claim を（将来の Claim に活かすが）その Claim としては閉じる。WAZIS は非終端ループとして、実現を**次の問い**へ折り返す。
4. **New Question を一級の産物として出す。** Dan-Go の産物は execution と「誰が助かったか」。WAZIS の産物は精緻化された／新しい**問い**そのもの。
5. **実装中立な探究。** 答えが Dan-Go 以外の現実（研究室・自治体パイロット・最小の非公式実験）から来てよい。

---

## 3. Q3 — Dan-Go にできて WAZIS が決してすべきでないこと

1. **実世界の行為を execute / coordinate する。** Contribution（11種：housing/funding/care…）のマッチング、人間承認の Execution。**WAZIS が実装したら、その「reality feedback」は自採点になり kernel 不変項 I が崩壊**——WAZIS が forum 化する。これが最も明るい境界線。
2. **特定の遷移（Claim）にコミットして実現へ駆動する。** コミット＝裁定。WAZIS は no-verdict（第1条）。コミットは Dan-Go の仕事。
3. **execution 由来の trust/評判スコアを保持する。** Dan-Go 内の「contribution からの trust」は正当。だが **WAZIS が execution-trust を問い/提案の序列化に持ち込むのは禁忌**（想い非測定・無裁定）。
4. **need と contribution を突き合わせ資源を配分する。** 調整・配分は Dan-Go の領分。WAZIS は実験を**ルートする**が**配分しない**。
5. **助けが実際に起きる場になる。** 人が housed/funded/cared される現場は Dan-Go。**WAZIS は人に直接触れない**——触れれば dignity/consent を侵すリスク。

> 規則: **WAZIS は「現実に触れる」ことを Dan-Go（等の実装先）に委ね、自分は触れない。** 触れた瞬間、WAZIS は自分の裁定者（現実）を自分で演じることになり、identity を失う。

---

## 4. Q4 — Dan-Go が明日消えたら、WAZIS はなお意味を持つか

**意味（identity）は持つ。即時の稼働は当面しぼむ。正直な二段答え:**

- **Yes（identity）:** Dan-Go は**一 Binding**にすぎない。kernel（問い→実験→現実→問い）は binding 非依存。WAZIS は NPO/OSS/研究/自治体、さらには「誰かが最小の実験をして観測を返す」という**軽量・非公式な Binding**でも現実へ届ける。reality-arbitration の identity は Dan-Go なしで完全に立つ。
- **But（稼働）:** M0 時点で**具体 Binding は Dan-Go のみ**。Dan-Go が今消えれば、別 Binding が立つまで WAZIS は**現実チャネルを一時的に欠く**（既出 R2/M-e）。ただし「最小実験＋観測報告」という最軽量 Binding は外部依存が小さく、比較的すぐ立て直せる。失うのは Dan-Go の**頑健な実装機構**（多人数・dignity 規律・Contribution）であって、WAZIS の意味ではない。

→ **意味は不変、稼働は ≥1 Binding の維持に依存。** これは「独立＝概念的独立であって、operationally autarkic ではない」ことを示す（§6）。

---

## 5. Q5 — WAZIS が明日消えたら、Dan-Go は何の能力を失うか

**Dan-Go は『上流の探究層』を失う。だが致命傷ではない（非対称）。**

失うもの:
1. **commit 前の探究／競合仮説生成。** 「そもそもどの Claim が試す価値があるか」を、開いた問いと競合実験で**コミット前に**現実に問う能力。WAZIS なしでは Dan-Go は「既に誰かが遷移を決めた Claim」が届くのを待つ（Article 3: 誰でも Claim を提案できる、に依存）。
2. **実装先横断の比較学習。** 同じ問いに対する Dan-Go vs 他実装先の答えの突合。Dan-Go 単独では自分の Claim しか見えない。
3. **体系的な再フレーミング。** 実現 Claim を毎回「新しい問い」へ折り返す非終端性。WAZIS なしでは Claim 単位で閉じがち。

**しかし致命的でない:** Dan-Go は元来 Claim を**直接**受理する自己充足系（Article 3）。WAZIS は **enhancement（上流の問いの規律・横断学習）**であって **vital organ ではない**。

### 5.1 非対称（重要）

| | 何に依存するか | 相手が消えると |
|---|---|---|
| **WAZIS → 実装先** | **少なくとも一つの Binding**が要る（今は主に Dan-Go） | 稼働が一時停止（意味は不変） |
| **Dan-Go → WAZIS** | **何も依存しない**（Claim はどこからでも来る） | enhancement を失うだけ（稼働は不変） |

→ **Dan-Go の方が自己充足度が高い。** WAZIS の「独立」は**概念的・アーキテクチャ的独立**であり、**operationally は ≥1 Binding（理想は ≥2、中立性の反証可能性）を保つ責務**を伴う。ここを混同しないこと。

---

## 6. Q6 — 親子か、兄弟か、層か、それ以外か

| 候補 | 判定 | 理由 |
|---|---|---|
| 親子（parent/child） | ❌ | child は親に依存するが、Dan-Go は WAZIS に依存しない（§5）。また WAZIS は Dan-Go を統治しない。「親」は支配を含意し過剰 |
| 層（layers） | △（限定的に真） | WAZIS=上流（探究）／Dan-Go=下流（実装）は連結時には正しい。だが「層」は下層が上層専用を含意し、Dan-Go を WAZIS の従属物にする＝独立性違反 |
| **兄弟（siblings）** | ✅ | 同じ DNA（dignity・RF・想い0層・DID・method-agnosticism）を共有する**対等な独立体**。互いに包含せず、各々自己定義。任意の interface（Binding）で連結できるが、どちらも相手を所有しない |
| それ以外（最精密） | ✅ | **共通基層（substrate）を共有し、薄く・任意で・可逆な interface（Binding）で連結する composable peers。** マイクロサービス的——データ契約を共有しつつ独立にデプロイ |

**結論: 兄弟（composable peers）。** ただし重要な区別:

> **層（layering）は runtime の一構成であって、ontology ではない。** WAZIS→Dan-Go が連結された瞬間だけ「WAZIS が上流・Dan-Go が下流」というパイプラインに**見える**。だがそれは一つの配線であって、両者の本質的関係ではない。配線を外せば、二つの独立した兄弟に戻る。**兄弟性が存在論、層性は実行時の一形態。**

共有する「DNA（substrate）」は: dignity（同一の法）／Reality Feedback 語彙／想い=0層／DID。これは**共有コードでなく共有契約**である（§7）。

---

## 7. Q7 — 両者を独立に保つ最小アーキテクチャ

```
   WAZIS（reality-feedback protocol）                    Dan-Go（social implementation protocol）
   ┌───────────────────────────────────┐                ┌────────────────────────────────────┐
   │ open question                     │                │ Claim（素テーブル/sutable）          │
   │   → Discussion（任意）            │                │   → Contribution（11種）             │
   │   → Proposal A / B / C            │                │   → Execution（人間承認）            │
   │   → Experiment Candidate(s)       │                │   → Reality Feedback（公開）         │
   │            │                      │                │                                     │
   │   ┌────────▼─────────┐  WAZIS-owned adapter        │                                     │
   │   │ Binding: dan-go  │  map(EC) ─────────────────▶ │  Claim が届く                       │
   │   │                  │            （Dan-Go は WAZIS を知らない・                          │
   │   │                  │              通常の Claim と区別不能）                             │
   │   │                  │  reverse(RF) ◀───────────── │  公開 RF を購読/参照                 │
   │   └────────▲─────────┘                             │                                     │
   │   → New Question（loop, 非終端）  │                │ （非WAZIS 由来の Claim も直接受理）  │
   └───────────────────────────────────┘                └────────────────────────────────────┘
        │   WAZIS may also bind to ↓                              │
        ├── NPO / OSS / research / municipality                   │
        └── 最小の非公式実験（someone tries & reports）           │
                        │                                          │
                        └──── 共有 substrate（共有コードでない）────┘
                          dignity（同一の法）· RF 語彙（executed/partial/failed/pending）
                          · 想い=0層（不可触）· DID identity
```

### 7.1 独立を保証する 4 原則

1. **唯一の結合点は Binding（WAZIS 所有の薄いアダプタ）。** Experiment Candidate → Claim の map と、公開 RF → WAZIS RF の reverse。versioned・可逆。
2. **逆依存ゼロ：Dan-Go は WAZIS を知らない。** WAZIS 由来の Claim は、Dan-Go から見て**通常の Claim と区別不能**。Dan-Go は Article 3 のまま「誰でも Claim を提案できる」を受けるだけ。→ Dan-Go の独立は**自動的に**保たれる（WAZIS への参照を一切持たないから）。
3. **WAZIS は Dan-Go をハードコードしない。** `_template` ＋（理想は）≥1 の別 Binding。Dan-Go binding は差し替え可能なプラグイン。
4. **共有するのは契約であってコードでない。** dignity・RF 語彙・想い0層・DID は**両者が独立に合意する公開契約**。マージしない。

### 7.2 独立性テスト（delete-test）

- `bindings/dan-go/` を削除 → WAZIS は kernel を保って立つ（別 Binding/最小実験へ）。✅
- WAZIS 全体を削除 → Dan-Go は直接 Claim を受理して稼働継続。✅

両方が通る限り、独立は保たれている。**結合は一本の薄いアダプタに局所化され、どちらの本体にも他方への依存が無い。**

---

## 8. 統合（一文で）

**Dan-Go は『どうやってこの deed を現実にするか』を調整する coordination engine（commit 後・実装）。WAZIS は『そもそも何を試す価値があるか、現実は何と答えるか』を現実に裁定させる reality-arbitration engine（commit 前・探究）。両者は dignity・Reality Feedback・想い0層・DID という同じ DNA を持つ兄弟であり、WAZIS 所有の薄い Binding（Dan-Go はそれを知らない）で連結したときだけ上流／下流のパイプラインに見えるが、それは実行時の一配線であって、本質は互いを所有しない composable peers である。WAZIS が決して現実に触れない（実装しない）こと——それが、WAZIS の裁定者を現実のまま保ち、同時に Dan-Go からの独立を保証する、ただ一つの規律である。**

---

*本書はレビューであり、実装・コード・既存ファイル修正を含まない。境界の同定は現ファイル（M0）と kernel review に基づく仮説であり、最初の Reality Feedback で反証されうる。要点: 境界は commit line（asking vs doing）。RF を WAZIS は oracle として、Dan-Go は grade として読む。関係は兄弟（composable peers）、層性は実行時の一形態にすぎない。*
