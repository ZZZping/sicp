# 中文译文维护

中文页面以同名英文 XHTML 为内容依据，文件名加 `_zh`。英文正文和 Texinfo 源文件不随翻译修改。

## 内容约束

- 按完整段落、标题和列表项翻译，不把行内标签两侧的句子拆成孤立短语。
- 不增添解释、例子、答案或译者注；不概括或删减原文。
- 代码、程序标识符、公式、插图、脚注编号和锚点采用原文内容；行内元素可随中文语序调整位置。
- 保留书目中的原始作者、文献题名和出版资料，以便检索。
- 中文目录和章节链接指向对应的中文页面，保留原锚点。

## 工具

使用 Python 3.10 或更新版本，安装 `requests`：

```powershell
python -m pip install requests
```

只检查英文源文件、统计翻译块，不调用 API，也不改写页面：

```powershell
python -B translate_v3.py
```

翻译缺少缓存的内容并生成中文页面：

```powershell
$env:DEEPSEEK_API_KEY = '你的 API 密钥'
python -B translate_v3.py --write
```

也可以指定单个文件：

```powershell
python -B translate_v3.py --write --files 1_002e1.xhtml
```

`translation_cache_v3.json` 保存完整语义块的译文，与旧版碎片缓存分开。缓存键包含英文内容和受保护的标签、代码与公式；修改原文后，不会误用其他上下文中的缓存。缓存完整时，重新生成页面不需要 API 密钥。

`translation_overrides.json` 保存经过具体核对的修订，以原文内容的哈希为键。它参与版本控制；生成缓存和校审记录不参与版本控制。

## 在现有译文上用本地模型辅助校订

本次校订使用本地 Ollama 的 `qwen3:8b` 提供建议，逐句对照英文原文后才记录最终决定。最终交付是 `html/*_zh.xhtml` 中文页面；并非只修改翻译代码。逐项修改前后对照见 [TRANSLATION_REVIEW.md](TRANSLATION_REVIEW.md)。

```powershell
python -B review_sentences.py prepare
python -B review_sentences.py suggest --model qwen3:8b
python -B review_sentences.py show --start 0
```

`sentence_review.json` 固定本轮英汉对照基线和文件哈希；`sentence_suggestions.json` 保存模型建议；`sentence_editor_decisions.json` 保存独立的逐句复核决定。模型没有权限自动批准或写回建议。编辑需实际检查每个句子及其上下文，再通过 `record_editor_review` 记录已检查的范围和修正。

所有文本块及句子均有复核决定后，执行：

```powershell
python -B review_sentences.py apply
```

该命令核验原文与原有中文页面的哈希，拒绝缺少句子记录、原文变化、重复块互相冲突或标签损坏的决定；验证所有页面及内部锚点后，备份原译文并直接写入最终中文 XHTML。同时更新缓存和持久化修订，并生成独立校订报告。重复应用同一轮记录会因中文文件已变化而被拒绝，避免覆盖后续修改。新的校订轮次应先归档本轮记录，再建立新的基线。

参考文献保留原始书目信息，代码、标识符、公式及图片内部文字保留原样。复核计数包含标题、导航、术语和参考文献；自动切句得到的数量是“英文句子及短文本片段”，不等同于正文自然句数量。

## 旧版远程校审与验证

对全部译文执行一次英汉对照校审：

```powershell
python -B review_translation.py
```

对包含否定、比较和逻辑条件的长段落进行专项校审：

```powershell
python -B review_translation.py --focus logic --model deepseek-reasoner
```

校审调用 API，修订经过占位符和 XML 检查后写入缓存，不直接改写网页。记录分别存入 `translation_review_v3.json` 和 `translation_logic_review_v3.json`。校审完成后运行 `python -B translate_v3.py --write` 生成页面。

每次替换页面前，脚本先验证全部待写页面：XML 必须有效，块级元素顺序、标签与属性集合必须保留，受保护的代码与公式必须原样保留。验证失败时不替换页面。旧中文文件备份到系统临时目录下的 `sicp-translation-backup-时间戳`，也可用 `--backup` 指定备份目录。

运行离线回归检查：

```powershell
python -B -m unittest test_translate_v3 -v
```

结构校验能发现标签、代码、公式和编号的损坏，不能证明每句话的语义绝对正确。旧版 `translate.py`、`translate_v2.py` 会按碎片翻译并覆盖中文页面。维护当前译文应优先使用上述逐句校订流程；`translate_v3.py --write` 可用于从完整缓存和持久化修订重新生成页面。

## 阅读界面

中英文切换入口直接保存在各 XHTML 页面的工具栏中，禁用 JavaScript 时仍可切换章节；JavaScript 负责保留锚点和整理旧版章节导航。工具栏不参与正文翻译，中文化内部链接时也不会改写其中的英文入口。

如果使用 `make` 从 Texinfo 重建原始 HTML，请随后运行 `python prepare_reader_ui.py` 恢复阅读界面。此命令可重复运行，不改写正文。现有带工具栏的英文页面通过 `translate_v3.py` 重新生成中文时会保留这些控件。
