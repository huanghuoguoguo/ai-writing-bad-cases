# AI Writing Bad Cases

这个仓库现在不只收集 bad case。

我想把它做成一个更直接的东西：一边整理“为什么有些文本一眼像 AI”，一边把那些高频句式、结构套路、安抚口气、总结腔收起来，最后沉淀成可以直接复制进 prompt 或 skill 的规则。

现在更进一步，`data/` 里的 JSON bad case 库会作为 source of truth。后续程序检测、SeekDB 检索、规则引擎，都会优先从这套结构化数据读取，而不是从 Markdown 反向抽取。

换句话说，这里有几层东西：

- 理论：解释什么叫 AI 味，它为什么会出现。
- data：程序可直接读取的 bad case JSON 库。
- docs：由 JSON 渲染出来、给人阅读的 Markdown 文档。
- rules / skills：把观察变成可执行约束。

## 仓库怎么用

如果你只是想研究：

- 先看 `theory/`
- 再运行 `python3 render_cases_md.py`
- 然后看 `docs/cases/`

如果你想拿结构化数据做程序：

- 先看 `data/README.md`
- 再看 `data/cases/`

如果你想直接压低模型输出的 AIGC 味：

- 先看 `rules/zh/`
- 再直接复制 `skills/zh/anti-aigc-style.md`

## 目录

- `theory/what-makes-text-sound-ai.md`
- `theory/diagnostic-dimensions.md`
- `data/cases/manifest.json`
- `data/cases/zh/argumentative.json`
- `render_cases_md.py`
- `docs/cases/zh/argumentative.md`
- `rules/zh/negative-rules.md`
- `rules/zh/rewrite-principles.md`
- `skills/zh/anti-aigc-style.md`

## 这个项目的判断

这里说的“AI 味”，通常不是指语法错误，也不是指事实错误。

更常见的情况是：

- 结构太完整
- 解释太显式
- 语气太稳定
- 总结太积极
- 太像一个会交付合格答案的系统

人类作者当然也会清楚、会总结、会组织结构。但真人文本往往没那么平均，也没那么爱把“我要开始解释了”“我要开始总结了”写在脸上。

## 收录原则

- case 不是单纯禁词表，尽量说明它为什么像 AI。
- 尽量给出替代写法，不只做吐槽。
- 同一个表达，如果在不同文体里表现不同，可以分开记。
- 机器可执行数据优先维护在 `data/`，Markdown 文档用于补充解释。
- 可读 Markdown 由 `render_cases_md.py` 从 JSON 生成，不再手工维护 `cases/` 目录。
- 最终目标不是“看出 AI”，而是“让文本更像作者自己写的”。

## 下一步

这个仓库现在先从中文开始，后面会继续补：

- 更多文体
- 更多语言
- 更严格的可执行规则
- 能直接嵌进 agent / workflow 的 skill 版本
