# Structural Consolidation Review / 構造統合レビュー

- Date: 2026-06-22
- Scope: 既往4レビュー（KERNEL / DANGO_BOUNDARY / META_LOOP / TRANSFORMATION）を統合し、**現構造が既に十分か**、**何が真に欠けているか**を判定する
- 種別: **レビューのみ**。実装・コード・既存ファイル修正・新プロトコル・新教義を含まない。
- 規律: **削除を加算より優先。** 新概念・新層・新プロトコルを発明しない。既存レビューに在るなら「既出」と明記。判定 = Kill Test ＋ Reification Test。
- 前提: 上記4レビューは、直接観察で矛盾しない限り正しいとみなす。

> **見出しの答え:** **構造は概念的に十分である。新しい概念は欠けていない。** 4レビューは収束済み。欠けているのは*概念*でなく——(1) **証明**（中立性は2本目の Binding まで未反証）、(2) **整合**（仕様本文が4補正に追いついていない）、(3) **一つの本当に難しい未解決問い**（第三者 dignity-objection の裁定）、(4) **fan-out/選択の機構**。以上は加えるべき概念でなく、埋めるべき空白。**「Reality Action」「Bridge」など重複名は削除して canonical 化できる。**

---

## 1. 全レビューを貫く load-bearing 概念の最小集合

両 test を通り、かつ**全て既出**の概念だけを残す（新規ゼロ）。

| # | 概念（canonical） | 役割 | Kill Test | Reification | 出所 |
|---|---|---|---|---|---|
| 1 | **想い（Omoi）** | hub。測られぬ源かつ aim。ループが orbit する地（節点でない） | 除去→aim 喪失、汎用 feedback 系へ | 管理節点でなく境界標。lens として可 | META/Constitution |
| 2 | **Dignity** | 唯一の法。唯一の実験ゲート | 除去→無制約/強制機械 | 制約であって entity でない | 全レビュー/Constitution |
| 3 | **Question（開いた入力）** | 想い側の膜の入口（threshold、起源でない） | 除去→変換対象が無い | openness が核、語彙は置換可 | KERNEL/META |
| 4 | **Transformation** | 問いを「現実応答可能な形」へ変える操作（edge）。= Bridge = Binding = Experimentability（§2） | 除去→RF 不能→forum へ崩落 | 操作は実在、名は lens | TRANSFORMATION/KERNEL |
| 5 | **Reality Feedback** | 外部現実の答え＝裁定者（hinge、ただし中心でない） | 除去→裁定が討議へ→forum | 観測物＋裁定役。実在 | KERNEL/META/BOUNDARY |
| 6 | **Non-termination** | RF が新しい問いを開く。ループは閉じない | 除去→knowledge base 化 | 姿勢（Art 8）。実在 | KERNEL/META |

**= 6 要素。** 幾何で言えば: **想い(hub①)** を、**Question③ ──Transformation④──▶ Reality Feedback⑤ ──reopen⑥──▶ 次の Question** という rim が orbit し、全体を **3不変項**（I 現実が裁定／II 二不可触＝想い+尊厳／III 非終端）が statute する。これは KERNEL_REVIEW の「1ループ＋3不変項＋1橋」と**同一**であり、本統合で新規追加はゼロ。

**削除した（非 load-bearing・足場）:** Discussion / the Forum / 収束・合意 / Refinement / merit-objection / Proposal・Need の細分類 / DID / trust / schema / TTFRF / 名前 / 「Bridge」/「Reality Action」。いずれも除去しても identity 不変（KERNEL §3 で確認済み）。

---

## 2. 別名で重複している概念 → canonical 化

**Yes、重複あり。ユーザー例示の4語は同一構造。** TRANSFORMATION_REVIEW で確立済み:

| 別名 | それが指す相 | canonical 化 |
|---|---|---|
| **Transformation** | 操作（verb・edge）: 問い→現実応答可能形 | ✅ **canonical（これを採る）** |
| Experimentability | その操作の**成功条件**（静的な性質） | Transformation の*条件*（従属） |
| Binding | その操作の**具体実例**（WAZIS↔実装先アダプタ） | Transformation の*インスタンス*（従属） |
| Bridge | 同じものの**比喩** | **冗長→削除** |
| 「Reality Action / 現実作用」 | 同じものの**誤名**（過程の名詞化・node 誤描） | **誤り→削除**（TRANSFORMATION §8） |

→ **最小 canonical 語 = Transformation。** experimentability＝その条件、Binding＝その実例、Bridge と Reality Action＝削除。

その他の小重複（記録のみ・いずれも非核なので canonical 化不要）: 「the Forum / Discussion / sutable」＝venue/記録（足場）。「arbiter / oracle / Reality Feedback」＝RF（読み方の違い、§5/BOUNDARY）。「commit line / interface / handoff」＝変換が WAZIS→実装先へ越す境界（§7）。

---

## 3. WAZIS が存在する最小構造（削るだけ削る）

identity が変わる直前まで削除すると:

> **WAZIS = 開いた問いを、自らが支配しない現実が答えられる形へ変換し（現実には触れない）、戻る Reality Feedback を裁定（oracle）として読み、問いを再び開く——を、想い非測定・尊厳の下で行う。**

不可分な区別子（これを欠くと WAZIS でない）:
- **変換するが現実に触れない**（触れたら自採点＝実装先化＝forum）。
- **RF を裁定（oracle）として読む**（討議でなく現実が決める）。
- **少なくとも1本の外部 Binding**（無いと現実に届かず——identity は残るが稼働不能、§8/BOUNDARY 非対称）。

→ 一文の最小: **「自らが支配しない現実が答えられる形に問いを変え、その現実に裁定させる」**。Discussion・Forum・複数提案・taxonomy は全て削除可。

---

## 4. Dan-Go が存在する最小構造（同じ削減）

> **Dan-Go = コミットされた状態遷移（Claim＝gap）を単位に、Contribution を調整し、Execution（人間承認・現実への行為）で実現し、Reality Feedback を grade として読む——を、尊厳・想い非測定の下で行う。**

不可分な区別子:
- **Claim（gap）を単位にコミットする**（提案された遷移）。
- **Contribution を調整する**（"coordination engine"・MUJIN_PROTOCOL）。
- **Execution で現実に触れる**（WAZIS が持たない決定的差）。
- **RF を grade として読む**（実現したか・誰か助かったか）。

→ 一文の最小: **「コミットした遷移を、貢献を調整して現実で実現する」**。11貢献型・sutable・trust・State Zero は実装特異（§6）で、最小には不要。

**鏡像（最小の弁別ビット）:** *現実に触れるか?* WAZIS=No／Dan-Go=Yes。これが commit line（BOUNDARY）の一語要約。

---

## 5. 真に共有される構造

**核レベルで共有（両者の identity に必須）:**
- **Dignity**（唯一の法）。
- **想い＝測られぬ0層**。
- **Reality Feedback**（primitive としての「現実の答え」）。
- **ループの形**（… → Transformation/Execution → RF → reopen、想い hub を orbit）＝META_LOOP の既出循環。

**規約レベルで共有（置換可な足場・核でない）:**
- DID identity、RF 語彙トークン（executed/partial/failed/pending）、公開・append-only の慣行。

→ 共有の核は **3つ（dignity・想い0層・RF）＋ループ形**。それ以外の「共有」は規約であって核でない。

---

## 6. 実装特異な構造（共有でなく、相手の存在に不要）

- **WAZIS 特異:** Question/Experiment Candidate、Discussion/the Forum、**現実不可触の規律**、RF=oracle 読み、複数実験の fan-out、実装中立（複数 Binding）。
- **Dan-Go 特異:** Claim 形式（gap/observed/required/missing）、11 Contribution 型、sutable、Execution log/人間承認、contribution-trust、RF=grade 読み、State Zero/YacypherPunks。

→ これらは相手が存在しなくても各自成立する範囲（BOUNDARY §4/§5 と一致）。**相手を定義しない。**

---

## 7. WAZIS と Dan-Go の最小インターフェース（インターフェースのみ記述）

内部に触れず、境界（commit line）を越える流れだけを記す。**二つの一方向流＋三つの性質**:

- **流れ①（外向き・handoff）:** 「現実応答可能形にされた成果物（Experiment Candidate）」＋ **consent 記録** ＋ **dignity-check** を、受け手の受理形式へ写して一方向に渡す。
- **流れ②（内向き・帰還）:** 受け手の公開 Reality Feedback を、共有語彙（executed/partial/failed/pending ＋ observation）へ正規化して一方向に読み戻す。
- **性質 A（consent-gated）:** ①は当事者同意が前提。撤回可能。
- **性質 B（dignity-lossless）:** 両者の唯一の法が同一（dignity）ゆえ、尊厳検査は無損失で対応。
- **性質 C（受け手は送り手を知らない／逆依存ゼロ）:** 渡された成果物は受け手にとって native と区別不能。→ 受け手の独立は自動（BOUNDARY §7）。

→ 最小: **「同意・尊厳検査済みの成果物を一方向に渡し、現実の答えを共有語彙で一方向に読み戻す。逆依存なし。」** これは**既出**（BOUNDARY §7・bindings/dan-go/BINDING.md）。新規不要。

---

## 8. 未解決のまま残るもの（arch / constitutional / neutrality のみ・装飾と命名は除外）

すべて既存レビューに在る。新規ゼロ。

| # | 未解決 | 種別 | 出所 |
|---|---|---|---|
| **U1** | **第三者の dignity-objection を、投票も governor も無しに誰が裁くか。** 当事者なら consent/撤回で閉じるが第三者は閉じない。最難問 | 憲法整合 | EXPERIMENT §4.3 |
| **U2** | **中立性が未反証。** 具体 Binding が Dan-Go のみ。≥2本目が出るまで「独立・中立」は反証不能の主張。WAZIS は ≥1 Binding に operationally 依存（非対称） | 中立性＋arch | REPO R2/M-e・BOUNDARY §5.1 |
| **U3** | **fan-out の選択機構が未規定。** 複数 Experiment Candidate を、有限容量の実装先へ、WAZIS が**ランク付けせず**全て露出する仕組み（選択は実装先の自律）が未仕様 | arch＋中立性 | EXPERIMENT §2.3 |
| **U4** | **RF 語彙の宛先中立性が未検証。** executed/partial/failed/pending は Dan-Go 由来。研究の再現・OSS の merge 等、非 Dan-Go の現実にこの4状態が自然か未確認 | 中立性 | BOUNDARY/EXPERIMENT |
| **U5** | **仕様本文が補正に未追従。** SPEC §1.3/§2/§4 に「収束/合意的な収束」が残存（実験駆動補正と矛盾）。Implementation→Experiment Candidate、Reality Action→Transformation も未反映。これは*命名でなく*遷移条件の食い違い（構造的） | 憲法/仕様整合 | EXPERIMENT・TRANSFORMATION |

**除外した（装飾/命名/運用ゆえ）:** OWNER プレースホルダ・git init・dual-license 裏付け・examples/・候補順序（REPO R5–R8）。これらは整合・運用であって構造でない。

**構造の十分性についての判定:** 上記 U1–U5 は**新概念の不在**でなく、(U1) 一つの深い未解決、(U2/U4) 中立性の未証明、(U3) 既知方針の未仕様、(U5) 本文の未整合。**核構造そのものは欠落していない。**

---

## 9. 今日開発を続けるなら、次に何をレビューすべきか（architectural importance 順）

1. **U5 — 仕様本文を4補正へ整合させるレビュー。** 最優先。canonical 仕様が現に corrected model と矛盾（収束語・旧命名）。本文が核とずれたまま実装に入れば、実装者が**間違ったもの**を作る。最大の構造リスクで、かつ最も解決可能。*（レビュー/計画として。実装でない。）*
2. **U2 — 2本目の具体 Binding を置くレビュー（中立性の反証）。** 高。実装中立は核 identity だが現在**未反証**。非 Dan-Go の Binding 一本で「独立」が falsify-or-confirm される。U4 はここで自然に露見する（従属）。
3. **U3 — fan-out/選択アーキテクチャのレビュー。** 中高。複数 Experiment Candidate の露出と、ランク無し・実装先選択の機構は核（実験駆動）に直結し未仕様。想い非測定・無裁定を侵さない設計が要件。
4. **U4 — RF 語彙の宛先中立性レビュー。** 中。U2 の 2本目 Binding 構築時に併せて検証するのが効率的（U2 に従属）。
5. **U1 — 第三者 dignity-objection の扱いのレビュー。** 憲法的には最深だが、architectural には**保留が正しい**。実際の係争事例が来るまで機構を先に作ると、no-governor を侵す governance 機械を生む危険（未観測の管理層を reify）。**「機構を急造しない」こと自体が正しい設計判断。** 深い未解決として明示し、事例発生時にのみ扱う。

> ランクの含意: 構造は十分なので、次にすべきは**新発見でなく、(1) 本文整合 → (2) 中立性の証明 → (3) fan-out 仕様**。U1 は深いが急がない（急ぐと憲法を侵す）。

---

## 10. 統合（一文で）

**4レビューは収束し、WAZIS の核は『想い(hub)・Question・Transformation(=Bridge=Binding=Experimentability、canonical は Transformation)・Reality Feedback・Non-termination』の6要素と3不変項に最小化され、Dan-Go との差は唯一『現実に触れるか』に、両者の接面は『同意・尊厳検査済み成果物を一方向に渡し現実の答えを共有語彙で読み戻す（逆依存なし）』に縮約される——いずれも既出で新規はない。ゆえに構造は概念的に十分であり、真に欠けているのは概念でなく、本文整合(U5)・中立性の証明(U2)・fan-out 仕様(U3)・語彙中立の検証(U4)という空白、そして急いで機構化してはならない一つの深い未解決——第三者 dignity-objection の裁定(U1)——だけである。削除すべき重複は『Bridge』と『Reality Action』。加えるべき層は無い。**

---

*本書はレビューであり、実装・コード・既存ファイル修正・新概念/層/プロトコルを含まない（§1 は新規ゼロ、§8 は全て既出）。削除を加算より優先した（Bridge・Reality Action を削除、6要素へ縮約）。判定は kill+reification test に基づく仮説であり、最初の Reality Feedback で反証されうる。次レビュー優先順: U5 > U2 > U3 > U4 > U1。*
