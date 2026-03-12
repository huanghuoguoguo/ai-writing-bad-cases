# Data Library

`data/` 是这个项目最核心的部分。

这里放的不是给人读的总结，而是给程序读取的 bad case 源数据。后续无论接规则引擎、SeekDB、向量检索，还是接 LLM 做定向改写，都应该优先依赖这里的数据，而不是直接解析 `md` 文档。

## 设计原则

- `JSON` 是 source of truth。
- 人类可读文档由根目录脚本 `render_cases_md.py` 从 JSON 生成。
- 每条 case 尽量同时保留：
  - 可读标签
  - 诊断维度
  - 可执行 matcher
  - 示例
  - 改写提示

## 目录

- `schema/bad-case.schema.json`: 单条 case 的数据结构约束。
- `cases/manifest.json`: 数据文件索引。
- `cases/zh/argumentative.json`: 中文议论文 bad cases。
- `cases/zh/narrative.json`: 中文记叙文 bad cases。
- `cases/zh/academic.json`: 中文论文 bad cases。

## 使用建议

- 规则匹配优先读 `matchers`
- 语义召回优先读 `label`、`description`、`examples`、`rewrite_hint`
- 文档展示可以读 `label`、`description`、`diagnostic_dimensions`

## 生成 Markdown

在仓库根目录运行：

```bash
python3 render_cases_md.py
```

输出会写到 `docs/cases/`。
