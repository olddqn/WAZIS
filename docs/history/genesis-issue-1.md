# Issue #1 — Genesis Question（貼り付け用）

> このファイルは、リポジトリ公開後に最初に立てる Issue（#1）の内容。GitHub の `Question` テンプレートに沿った具体例であり、同時に **the Forum を開く最初の問い**である。タイトル・本文をそのまま Issue にコピーして使う。

---

**Title:** `[Question] WAZIS が最初に一周（TTFCL）させるべき、現実の問いは何か`

**Labels:** `question`, `phase:0`, `genesis`

---

## 問い（statement）

WAZIS の最初の仕事は、機能を増やすことではなく、**ループを一度、本物で一周させること**だ（TTFCL — Time to First Closed Loop）。

そこで最初の問いを開く:

> 想いから生まれた現実の問いのうち、**最初に**「Question → Discussion → Refinement → Implementation Candidate → External Implementation（初期は Dan-Go）→ Reality Feedback → New Question」を一周させるべきものは何か。

この Issue は答えを**決めない**。候補となる現実の問いを集め、洗練し、一周に値する一件を浮かび上がらせるための場である。

## 入口カテゴリ（entry_category）

- [x] unresolved（未解決の問い）— 「最初の一件をどう選ぶか」という未解決の問い
- [ ] discomfort / institutional_design / community_design / long_held / other

## 背景（background）

WAZIS は社会実装の上流工程であり、それ自身は実装しない（憲法 第7条）。だが上流に留まり「無害なまま誰も助けない」ことは、権力化と並ぶ失敗様式である（[WAZIS_MVP_PLAN.md](WAZIS_MVP_PLAN.md) §6）。最初の一周を成立させるまで、新機能は凍結する。

最初の一件の選定条件（MVP §5）:

- 想いから生まれた、当事者にとって**現実の**問いであること。
- 尊厳を侵さず、強制を要しないこと（`dignity_check` を通る）。
- Dan-Go で受理可能な Claim へ翻訳できる見込みがあること（[bindings/dan-go/BINDING.md](../../bindings/dan-go/BINDING.md)）。
- `not_yet_decided` が自然に書けること（WAZIS が裁定しない余地が残る）。

選ぶ基準は「**助かる方向へ一歩でも近づくか**」だけ。理論的な美しさでは選ばない（救済主軸）。

## 派生しうる小さな問い（open_threads）

- 「一周に値する」とは、誰にとってか。
- 最初の一件は WAZIS 自身についての問いでよいのか、それとも外側の現実の問いに限るべきか。
- 候補が複数集まったとき、**多数決を使わずに**どう一件へ収束するか。

## この Issue での討議の作法

- **賛否の投票をしない**。視座・counter-question・objection・need/proposal framing で応じる（憲法 第1条）。
- 候補となる現実の問いは、それぞれ**独立した `Question` Issue** として開き、ここにリンクする。
- 想いの強さで候補を序列化しない（第3条）。

## 不可侵条項チェック

- [x] この問いを開くことは、他者の尊厳を侵さない
- [x] 私はこの問いをいつでも撤回できることを理解している
- [x] 私はこの問いを公開（the Forum に記録）することに同意する

---

> 収束した最初の一件は `questions/q-…md` として保存し、洗練を経て `candidates/ic-…md` を起草、Dan-Go Binding で handoff する。戻った Reality Feedback を `feedback/` に記録し、最初の New Question を開いた時点で **TTFCL を一度計測**する。
