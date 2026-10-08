# v0.1.2 定位勘误：《晚明》卷二换卷时EPUB文件序号不是叙事序号+8

2026-10-09 在提交#046—055阶段记录时，曾直接以章节序号`n+8`生成EPUB路径，导致《晚明》**叙事#052—055**的文件定位错误（尽管各章SHA前缀和标题采用的是实际spine审计数据）。

| 叙事序号 | 先前错误路径 | 原审计CSV确认正确路径 |
|---|---|---|
| #052（卷二第1章） | `Chapter_0060.xhtml` | `Chapter_0061.xhtml` |
| #053（卷二第2章） | `Chapter_0061.xhtml` | `Chapter_0062.xhtml` |
| #054（卷二第3章） | `Chapter_0062.xhtml` | `Chapter_0063.xhtml` |
| #055（卷二第4章） | `Chapter_0063.xhtml` | `Chapter_0064.xhtml` |

原因：`Chapter_0060.xhtml`为卷间非叙事内容，不能按编号推算真实章节路径。**原始文件hash通过 ≠ 自动写出来的路径就正确。** 现已修复`research/stage0/chapter-notes/wanming-0051-0055.md`和`research/stage0/EVIDENCE_INDEX_0046_0055.csv`。以后应始终依据`spine.csv`内的`narrative_ordinal→epub_path`映射，严禁用简单算式代替卷内位置。

其他#046—055章节路径不涉及本次错误；并未把错误索引当成新读章节。本次勘误也不使Stage0通过。
