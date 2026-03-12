# ZH / argumentative

> This file is generated from `data/cases/*.json` by `python3 render_cases_md.py`.

## 1. 不是……而是……

- `id`: `zh.arg.not_x_but_y`
- `severity`: `0.93`
- `diagnostic_dimensions`: structure_symmetry, closure_impulse
- 描述：典型的对举式判断句，容易把观点写成模板化结论。
- 别名：不是X而是Y, 对举式金句
- 为什么像 AI：AI 很喜欢用这种结构快速收束论点，因为它足够完整、足够稳，也足够像标准答案。
- 匹配规则：
- `regex`: `不是.{0,24}而是` (weight=1.0)
- 示例：
  - 真正重要的不是速度，而是你是否能长期坚持。
- 更像人的写法：
  - 速度没那么重要，难的是你能不能一直做下去。
- 改写提示：如果确实需要对比，优先改成具体判断或场景描述，不要写成口号式对举。
- Prompt 规则：Avoid contrastive slogan structures such as “不是……而是……”. Rewrite them as concrete judgments instead.

## 2. 不是关于 X，而是关于 Y

- `id`: `zh.arg.not_about_x_but_y`
- `severity`: `0.88`
- `diagnostic_dimensions`: structure_symmetry, abstract_over_specific
- 描述：抽象转义句，常把具体问题拔高成概念对立。
- 别名：It's not about X, it's about Y
- 为什么像 AI：这类句子很适合快速上价值，但也容易让文本显得悬空、模板化。
- 匹配规则：
- `regex`: `不是关于.{0,24}而是关于` (weight=1.0)
- `regex`: `不只是.{0,16}是` (weight=0.6)
- 示例：
  - 这不是关于效率，而是关于认知。
- 改写提示：把抽象概念落回具体对象，明确问题发生在什么地方，不要只做概念转换。
- Prompt 规则：Avoid abstract “not about X but about Y” framing. State the concrete issue directly.

## 3. 稳稳接住你

- `id`: `zh.arg.steadily_catch_you`
- `severity`: `0.96`
- `diagnostic_dimensions`: emotional_servicing, posture_before_content
- 描述：安抚型情绪表达，常见于悬浮的陪伴式文案。
- 为什么像 AI：它给的是情绪承诺，不是具体帮助，AI 又特别爱补这种安抚口气。
- 匹配规则：
- `phrase`: `稳稳接住你` (weight=1.0)
- 示例：
  - 这套方法会稳稳接住你，让你从混乱里走出来。
- 更像人的写法：
  - 这套方法至少能帮你先把信息整理清楚，再决定下一步怎么做。
- 改写提示：改写成具体动作或可验证帮助，不要做空泛的情绪托底。
- Prompt 规则：Avoid emotional reassurance phrases like “稳稳接住你”. Replace them with concrete help.

## 4. 你只管……，剩下的交给……

- `id`: `zh.arg.you_just_do_rest_to`
- `severity`: `0.9`
- `diagnostic_dimensions`: emotional_servicing, posture_before_content
- 描述：广告式托管承诺，容易让文本像投放文案。
- 为什么像 AI：这类句子过度承诺结果，像在兜售一个万能方案。
- 匹配规则：
- `regex`: `你只管.{0,20}剩下的交给` (weight=1.0)
- 示例：
  - 你只管表达，剩下的交给模型。
- 改写提示：写清楚边界和条件，不要用全包式承诺替代说明。
- Prompt 规则：Avoid all-inclusive promise templates like “你只管……，剩下的交给……”.

## 5. 把 X 拉满

- `id`: `zh.arg.max_out_x`
- `severity`: `0.76`
- `diagnostic_dimensions`: average_style, posture_before_content
- 描述：口语化强化句，看起来有网感，但很容易被批量复用。
- 为什么像 AI：它像一个现成的强度按钮，用来快速制造情绪，不需要真实描写。
- 匹配规则：
- `regex`: `把.{1,12}拉满` (weight=1.0)
- 示例：
  - 把氛围感直接拉满。
- 改写提示：把程度词改成具体动作、具体变化或具体效果。
- Prompt 规则：Avoid “把 X 拉满” style intensifiers. Describe what actually changed.

## 6. 不绕弯子类开场

- `id`: `zh.arg.direct_to_point_opening`
- `severity`: `0.8`
- `diagnostic_dimensions`: over_explicitness, meta_discourse_density
- 描述：先声明自己要直接说重点，而不是直接进入内容。
- 别名：开门见山, 直奔主题, 长话短说
- 为什么像 AI：人类写作者通常直接讲，AI 更爱在句首暴露自己的组织动作。
- 匹配规则：
- `phrase`: `不绕弯子` (weight=1.0)
- `phrase`: `开门见山` (weight=0.8)
- `phrase`: `直奔主题` (weight=0.8)
- `phrase`: `长话短说` (weight=0.8)
- 示例：
  - 不绕弯子，直接说重点。
- 改写提示：去掉组织动作声明，直接写你真正要说的内容。
- Prompt 规则：Do not announce that you are about to get to the point. Just get to the point.

## 7. 没有 X，没有 Y，只有 Z

- `id`: `zh.arg.no_x_no_y_only_z`
- `severity`: `0.89`
- `diagnostic_dimensions`: structure_symmetry, closure_impulse
- 描述：口号式排比句，经常拿来制造干脆、狠、直接的感觉。
- 为什么像 AI：排比过于整齐，像广告语或培训稿，不像自然分析。
- 匹配规则：
- `regex`: `没有.{0,16}没有.{0,16}只有` (weight=1.0)
- `regex`: `不.{0,8}不.{0,8}只` (weight=0.7)
- 示例：
  - 没有废话。没有套路。只有干货。
- 改写提示：拆掉排比骨架，把真正的判断和边界说出来。
- Prompt 规则：Avoid slogan-like triplets such as “没有 X，没有 Y，只有 Z”.

## 8. X。Y。Z。短句三连

- `id`: `zh.arg.short_triplet`
- `severity`: `0.74`
- `diagnostic_dimensions`: structure_symmetry, average_style
- 描述：三个短句并列，像演示文稿标题或口号。
- 为什么像 AI：这类结构很省力，既显得有节奏，也很容易被批量套用。
- 匹配规则：
- `regex`: `^[^。！？]{1,8}。[^。！？]{1,8}。[^。！？]{1,8}。$` (weight=0.8)
- 示例：
  - 专注。对齐。可衡量。
- 改写提示：把短句三连改成自然句子，说明这些词之间的实际关系。
- Prompt 规则：Avoid slogan-like three-part short sentence chains.

## 9. 问题是 X？答案是 Y

- `id`: `zh.arg.question_answer_template`
- `severity`: `0.82`
- `diagnostic_dimensions`: over_explicitness, closure_impulse
- 描述：设问自答模板，经常被用来制造强结论感。
- 为什么像 AI：它看起来像有互动，其实只是把结论塞进一个固定框架里。
- 匹配规则：
- `regex`: `问题.{0,16}[？?].{0,16}(答案|关键|在于|就是)` (weight=1.0)
- 示例：
  - 问题在哪？在认知。
- 改写提示：去掉设问壳子，直接陈述你的判断。
- Prompt 规则：Avoid rhetorical question-answer templates when a direct statement would do.

## 10. 综上所述 / 总而言之

- `id`: `zh.arg.conclusion_signals`
- `severity`: `0.68`
- `diagnostic_dimensions`: connector_driven, over_explicitness
- 描述：显式总结信号，本身不是禁词，但高密度使用会让文本像在执行模板。
- 为什么像 AI：AI 很依赖这类标记来推进结构，容易让段落显得拼接感很强。
- 匹配规则：
- `phrase`: `综上所述` (weight=1.0)
- `phrase`: `总而言之` (weight=1.0)
- `phrase`: `归根结底` (weight=0.7)
- 示例：
  - 综上所述，我们需要重新理解效率。
- 改写提示：如果结论已经自然出现，就不要额外打总结标签。
- Prompt 规则：Use explicit summary markers sparingly. Do not rely on them to create structure.
