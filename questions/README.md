# questions/ — the Forum（討議卓）

WAZIS の公開討議状態。すべての **Question（問い）** の記録が置かれる。Dan-Go の素テーブル（sutable）に対応する WAZIS の卓。

## 原則

- **既定で公開**。隠れた討議を持たない。
- 誰でも任意の Question の全状態を読める。
- **objection は append-only・上書き不能**（不可侵条項）。
- **撤回（withdrawal）はいつでも可能**。撤回された声は無効化されるが、撤回の事実は履歴に残る。
- ブロックチェーンではない。透明性に支えられた社会契約である。

## 1つの Question の表し方

GitHub の **Issue**（`Question` テンプレート）が一次的な入口。確定・長期保存する問いは、このディレクトリに 1 ファイルとして写す:

```
questions/q-{topic}-{seq}.md   または   .json
```

スキーマは [WAZIS_SPEC.md](../docs/history/WAZIS_SPEC.md) §1.1 / [schemas/](../schemas/) を正とする。最小フィールド: `question_id`, `title`, `speaker`(DID/pseudonym), `statement`, `entry_category`, `status`, `consent`, `created_at`, `version`。

## status の遷移

```
open → refining → candidate_drafted → （candidates/ へ）
  ↑        │
  └─ reopened ←── parked / withdrawn / Reality Feedback からの New Question
```

Phase 間に「昇格判定」はない。当事者と Forum の合意的な収束で進み、いつでも前段へ戻れる（reopen は失敗でない）。

## してはいけないこと

- 想いの強度・優先度のスコア付け（憲法 第3条）。
- 賛否の投票・ランキング（第1条）。
- 表面（問い）から背後の想いを推定する記録（Saiyan Scouter 禁止）。

> このディレクトリは Phase M1 で実運用を開始する。M0 では構造のみ。
