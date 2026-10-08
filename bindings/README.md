# bindings/ — Implementation Binding（実装束縛）

Implementation Candidate を、特定の実装先の受け入れ形式へ写す**アダプタの仕様**。WAZIS の実装中立性（憲法 第6条）はこの層で担保される。

> WAZIS の中核は Binding に依存しない。実装先は差し替え可能なプラグインであり、Dan-Go は**最初の一つ**にすぎない。

## ディレクトリ構造

```
bindings/
├── README.md            ← 本ファイル（抽象インターフェース）
├── _template/
│   └── BINDING.md       ← 新規 Binding の雛形（複製して使う）
├── dan-go/
│   └── BINDING.md       ← 具体 Binding #1（参照実装・Candidate → Dan-Go Claim）
│
└── （将来・同一インターフェースで追加）
    ├── npo/BINDING.md            ← Candidate → プロジェクト要項 / 助成申請の素地
    ├── company/BINDING.md        ← Candidate → 社内提案 / PoC 要件
    ├── research/BINDING.md       ← Candidate → 研究上の問い / プロトコル / 倫理審査の素地
    ├── oss/BINDING.md            ← Candidate → issue / RFC / discussion
    ├── municipality/BINDING.md   ← Candidate → 政策の素地（Dan-Go Policy Commons / Globe に近い）
    └── other/BINDING.md          ← その他のプロトコル
```

各実装先は 1 ディレクトリ。`BINDING.md` が写像と規律を定義する（コードではない。M1 以降に runtime を追加する場合も、この仕様が正）。

## 抽象インターフェース

すべての Binding は次を定義する:

```
Binding {
  target: string                          // 実装先の識別子（"dan_go" 等）
  map(candidate) -> payload                // Implementation Candidate → 実装先の受け入れ形式
  consent_required: true                   // handoff には当事者同意が必須（不可侵条項）
  feedback_channel: string                 // Reality Feedback を受け取る経路
  reverse(feedback) -> RealityFeedback     // 実装先の出力 → WAZIS の Reality Feedback
}
```

## すべての Binding が守る不変条件（invariants）

1. **同意（Consent）** — `map()` の前に `candidate.consent_status.handoff_consented_by` を確認する。同意なき handoff は禁止。
2. **尊厳（Dignity）** — 実装先の dignity 規律と WAZIS 第10条が**矛盾しない**ことを確認する。矛盾する実装先へは渡さない。
3. **無歪曲** — 実装先固有の都合（KPI・締切・資金条件など）が Candidate の中身を**遡って歪めてはならない**。
4. **無裁定の保存** — `not_yet_decided` は実装先へ転写しない。WAZIS が裁定しなかった点は、実装先（の交渉）で当事者が決める。WAZIS が代わりに決めない。
5. **トレーサビリティ** — `candidate_id` / `origin_question_id` を payload のメタに保持する。
6. **同じ Reality Feedback 語彙** — `reverse()` は `executed/partial/failed/pending` の語彙へ正規化する。

## 新しい Binding の追加

1. [`_template/BINDING.md`](_template/BINDING.md) を `bindings/<target>/BINDING.md` に複製。
2. 写像表（Candidate → 実装先形式）と reverse 表を埋める。
3. 上記 invariants を満たすことを明記。
4. PR（`bindings` ラベル）。複数実装先が同じ Candidate を引き取る場合の Reality Feedback 統合方針も記す。

> 二つ目の Binding（npo / oss 等）の追加が、WAZIS が Dan-Go の付属物でないことの試金石（[WAZIS_MVP_PLAN.md](../docs/history/WAZIS_MVP_PLAN.md) M3）。
