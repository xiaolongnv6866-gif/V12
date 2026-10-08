# EPUB spine 跨会话可重复生成（2026-10-09）

此目录存储**不含小说正文的重建程序** `rebuild_spine_portable.py`，仅处理用户在本地合法持有并向Agent提供的两本原始EPUB。程序会校验整本EPUB的SHA256，在真实OPF manifest+spine顺序中按既有V12规则辨别叙事章，输出各卷序号、实际ZIP路径、原章节SHA256及正文字符数的CSV，但**不会输出任何原著正文**。

## 真实测试结果（2026-10-09）

脚本在本地实际重跑用户EPUB：
- 《晚明》: 588条spine、571叙事章节；
- 《铁血残明》: 551条spine、532叙事章节；
- 对比前期本地权威CSV，两个输出**所有单元格完全一致、差异0**。这是工程索引检验，非全文文学阅读或阶段0通过。
- 测试需Python>=3.10与`lxml`。

## 运行

```bash
python3 -m pip install lxml
python3 research/epub_audit/rebuild_spine_portable.py \
  --wanming "/path/to/晚明.epub" \
  --tiexue "/path/to/铁血残明.epub" \
  --output "/local/private/research/epub_audit"
```

路径与本地实际文件名可不同，只要内容SHA与已固定版本完全一致。若校验不通过即报错，禁止用其它内容冒充同一小说版本。**不要上传EPUB到公共仓库**。未来在新对话框要先确认有实际可读的用户EPUB、再运行此脚本；上传此脚本只解决“如何重建”，**目前仍未把两份完整CSV实际上传到远程仓库**（问题I-005部分处理）。

重要：《晚明》换卷非叙事文件存在，不能根据`narrative_ordinal+8`猜章节ZIP路径；需每次从脚本真实CSV`narrative_ordinal`对应行读取`epub_path`。
