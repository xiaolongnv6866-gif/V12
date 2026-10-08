# V12 两个指定SKILL：上游源码读取记录（**并非已安装证明**）

核查日期：2026-10-08。

| 指定工具 | 当前已安装技能列表 | 公开候选源码 | 完整入口 | blob SHA |
|---|---|---|---|---|
| cangjie-skill | 未发现此技能 | https://github.com/kangarooking/cangjie-skill | SKILL.md (metadata v2.5.0) | 5d0c0b68425847eb12e7bf3d7109a4d63db42fa3 |
| nuwa-skill | 未发现此技能 | https://github.com/alchaincyf/nuwa-skill | SKILL.md (name: huashu-nuwa) | 788669b7b2ab755ae04d6585c28beeacedda41f2 |

**现阶段确认的是GitHub上名称匹配的源码可读取，不等于用户此前安装的版本就是这些，也不等于当前Agent能够以安装形式调用。** cangjie仓库发现367个文件、62个methodology/extractor/template/schema/script/test/doc条目；nuwa仓库发现159个文件、7个references/scripts条目。整个目录树未发现截断。

## cangjie 本次已完整读取的来源文件

- `SKILL.md` (v2.5.0)
- `methodology/00-overview.md`
- `methodology/01-stage0-adler.md`
- `methodology/02-stage1-parallel-extract.md`
- `methodology/03-stage1.5-triple-verify.md`
- `methodology/03b-stage1.6-promotion-gate.md`
- `methodology/04-stage2-ria-plus.md`
- `methodology/05-stage3-zettelkasten.md`
- `methodology/06-stage4-pressure-test.md`
- `methodology/07-stage5-deliver.md`
- `extractors/framework-extractor.md`
- `extractors/principle-extractor.md`
- `extractors/case-extractor.md`
- `extractors/counter-example-extractor.md`
- `extractors/glossary-extractor.md`
- `templates/BOOK_OVERVIEW.md.template`

阶段0的前置方法与模板已读齐；后续阶段需要的完整编译器、Schema、模板和脚本尚待在使用前读取和运行自检。未执行cangjie的 `doctor` 或 `compile`，不可标注为运行通过。

## nuwa 本次已完整读取的来源文件

- `SKILL.md` (共683行)
- `references/extraction-framework.md`
- `references/skill-template.md`
- `references/fidelity-scorecard.md`
- `scripts/download_subtitles.sh`
- `scripts/srt_to_transcript.py`
- `scripts/merge_research.py`
- `scripts/quality_check.py`

上述脚本已经读取源码，**尚未安装或执行功能测试**。其原始标准后置双Agent精炼与独立评分要求不得降成自评。

## 已核对的流程，不得擅自跳过

- 仓颉：阶段0 Adler整书阅读、骨架与用户确认→1五视角提取（无并行Agent可依原文串行）→1.5三重验证及用户轻确认→1.6单Skill晋级门→2 RIA++完整能力卡→3链接→4盲测与真实输出评测→5 bundle编译、验证、安装/发布。
- 女娲：Phase0选人/主题和模式确认→0.5目录初始化→1六个独立来源角度→1.5调研检查点→2心智模型/决策/表达/诚实边界→2.5提炼确认→3构建→4独立测试→5双Agent精炼。

**整合选择**：女娲原文提供“主题Skill”变体；V12要的是作品中可验证的创作机制，而不是用柯山梦的第一人称冒充本人。故拟采用主题变体处理叙事判断/表达机制，保留六维、来源和测试要求。此为V12合规方案，不是宣称女娲作者本人已授权V12成果。

重要原文约束：cangjie阶段0/1.5/5 和nuwa阶段1.5/2.5/4/5各有用户确认节点。V12的“自主连续推进”不撤销原作者明确规定的必要确认。
