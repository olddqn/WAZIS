> **Historical document.** This was the repository README during Phase M0 (June 2026), before any code existed. It describes an earlier Question → Discussion → Implementation Candidate model that the implemented application does not follow. The canonical description of WAZIS is the [README](../../README.md) at the repository root. Relative links below have been updated to match the current file layout.

<!-- SPDX-License-Identifier: Apache-2.0 -->

# WAZIS — 和智達（ワチス）

**Wisdom Action Zone for Implementation in Society**
知恵と行動を社会実装へ接続する場

> 社会実装可能な討議場。測定不能の「想い」から生まれた**問い**を、討議で洗練し、外部の実装先へ渡せる **Implementation Candidate（実装候補）** にする。WAZIS 自身は実装しない。社会実装の**上流工程**である。

- Status: **Phase M0 — 仕様のみ。コードは未着手**（[WAZIS_MVP_PLAN.md](WAZIS_MVP_PLAN.md)）
- 唯一の法: **他者の尊厳を侵してはならない**（[WAZIS_CONSTITUTION.md](../../WAZIS_CONSTITUTION.md)）
- License: Apache-2.0（散文仕様は CC BY 4.0 でも利用可。下記 [License](#license)）

---

## WAZIS とは

```
〔0層: 想い〕──self-translate──▶ Question ─▶ Discussion ─▶ Refinement ─▶ Implementation Candidate
  (測らない)                     (問い)      (討議)        (洗練)         (実装候補)
                                                                              │ handoff（同意必須）
                                                                              ▼
                                                  External Implementation … Dan-Go / NPO / 企業 / 研究 / OSS / 自治体
                                                                              │
                                       New Question ◀── Reality Feedback ─────┘
```

WAZIS は議論そのものを目的にしない。目的は社会実装である。しかし実装そのものは行わない。WAZIS は問いを洗練し、実装先へ渡す上流に徹する。

### WAZIS が「すること / しないこと」

| すること | しないこと |
|---|---|
| 問いを開く（誰でも） | 正解・真偽・ベストアンサーを決める |
| 討議で洗練する | 多数決・ランキング |
| 実装候補を起草し、外部へ渡す | 想いを測定・数値化・分類する |
| Reality Feedback を受け取り、新しい問いを開く | 実装そのものを行う |
| 複数の実装先へ中立に接続する | 単一の実装先を特権化する |

WAZIS は **Dan-Go の機能でも UI でも一部でもない**。思想的に近いが、技術的に独立したプロジェクトである。現時点で存在する実装先が Dan-Go のみのため最初の接続先は Dan-Go だが、これは便宜であって優先ではない（[実装中立](#実装中立-implementation-neutral)）。

---

## 不可侵条項（Inviolable Clauses）

参加の前提。これらは WAZIS が**自己修正可能であり続けるための条件**であり、効率のために削ってはならない（憲法 第5条）。

- **同意（Consent）** — 参加・引用・実装先への引き渡しは当事者の同意による。
- **異議（Objection）** — いつでも記録でき、上書きされない（append-only）。閉じかけた問いを再び開く。
- **撤回（Withdrawal）** — 自らの声・問い・貢献をいつでもペナルティなく撤回できる。
- **尊厳（Dignity）** — 唯一の法。すべてに優先する。

---

## 参加する

1. [WAZIS_CONSTITUTION.md](../../WAZIS_CONSTITUTION.md) を読む（唯一の法と不可侵条項）。
2. **問いを開く** → Issues から `Question` テンプレートで Issue を作成。
3. 討議する → 視座・counter-question・**objection**・need/proposal framing。**賛否の投票はしない**。
4. 洗練が実装候補に至ったら → `Implementation Candidate` テンプレートで起草。
5. 実装先から戻った観測を → `Reality Feedback` テンプレートで記録し、**新しい問い**を開く。

最初の問いは [docs/genesis-issue-1.md](genesis-issue-1.md)（Issue #1）を参照。

---

## リポジトリ構成

```
wazis/
├── README.md                     ← 本ファイル（初版）
├── LICENSE                       ← Apache-2.0
├── WAZIS_CONSTITUTION.md         ← 規範の天井（唯一の法・不可侵条項・10条）
├── WAZIS_SPEC.md                 ← 機構（5オブジェクト・ライフサイクル・Binding I/F）
├── WAZIS_MVP_PLAN.md             ← 構築順序（M0–M4・TTFCL・基盤判断）
├── CONTRIBUTING.md               ← 参加の作法（討議が第一級。コードは後）
├── CODE_OF_CONDUCT.md            ← 尊厳に基づく行動規範（≒ 第10条）
│
├── questions/                    ← the Forum: Question 記録（データ。コードでない）
│   └── README.md
├── candidates/                   ← Implementation Candidate 記録
│   └── README.md
├── feedback/                     ← Reality Feedback 記録
│   └── README.md
│
├── bindings/                     ← Implementation Binding（実装中立アダプタの仕様）
│   ├── README.md                 ← Binding インターフェース（抽象）
│   ├── _template/BINDING.md      ← 新規 Binding の雛形
│   ├── dan-go/BINDING.md         ← 具体 Binding #1（参照実装・Candidate→Claim）
│   └── （将来）npo/ company/ oss/ research/ municipality/ …  ← 同一 I/F で追加
│
├── schemas/                      ← JSON スキーマ（仕様成果物。SPEC が単一の正）
│   └── README.md
│
├── docs/
│   ├── glossary.md               ← 用語集
│   └── genesis-issue-1.md        ← Issue #1（最初の問い・貼り付け用）
│
└── .github/
    ├── ISSUE_TEMPLATE/           ← Question / Objection / Candidate / Reality Feedback
    └── PULL_REQUEST_TEMPLATE.md
```

---

## 実装中立（Implementation Neutral）

WAZIS の出力 **Implementation Candidate** は、特定の実装先に事前コミットしない境界物である。各実装先への写像は **Implementation Binding** が担う（[bindings/](../../bindings/)）。

- **Dan-Go**（最初の一つ・参照実装）: Implementation Candidate → Dan-Go **Claim** → Contribution → Execution → Reality Feedback。
- 将来: **NPO / 企業 / 研究機関 / OSS / 自治体 / その他のプロトコル** を、同じインターフェースで追加。

WAZIS の中核は Binding に依存しない。Dan-Go は最初の一つにすぎない。

---

## Dan-Go との関係

WAZIS と [Dan-Go](https://github.com/) は思想的に近く、技術的に独立。両者とも唯一の法は **dignity**。WAZIS は Voice Commons でいう最上流の **Question（開く起源）** レイヤ、Dan-Go は **Claim 以降の実装**レイヤ。WAZIS の Implementation Candidate は Dan-Go の Claim の手前に立つ。詳細は [bindings/dan-go/BINDING.md](../../bindings/dan-go/BINDING.md)。

---

## 最上位指標 — TTFCL

WAZIS が証明すべきは機能の豊富さでなく、**ループが一周回ること**。

> **TTFCL = Time to First Closed Loop** — 最初の問いが、洗練され、実装候補になり、外部で実装され、Reality Feedback を返し、最初の新しい問いを生むまでの時間。

「無害なまま誰も助けない」を、権力化と並ぶ失敗様式として扱う（[WAZIS_MVP_PLAN.md](WAZIS_MVP_PLAN.md) §6）。

---

## License

- 既定: **Apache License 2.0**（[LICENSE](../../LICENSE)）。コード・スキーマ・将来の Binding 実装を含む。特許許諾を伴い、企業・自治体・研究機関による中立な採用を妨げない（実装中立性に資する）。
- 散文仕様（CONSTITUTION / SPEC / MVP_PLAN 等）は追加で **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)** でも利用可（論文・政策文書・他プロトコルの仕様への引用・翻案を容易にするため）。
- SPDX: `Apache-2.0 AND CC-BY-4.0`。
- 英訳その他の言語への翻訳は歓迎する good first contribution（WAZIS の言語中立性の検証にもなる）。

> ライセンスは提案であり、ユーザー判断で差し替え可能。より強い開放性を望むなら AGPL-3.0 / CC BY-SA、純粋に文書のみなら CC BY 4.0 単独も選べる。

---

*この README は初版であり仮説である。WAZIS のすべての文書と同じく Reality Feedback で修正される。ただし不可侵条項（第5条）と尊厳（第10条）を損なう変更はできない。*
