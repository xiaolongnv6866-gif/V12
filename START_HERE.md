# V12 新会话唯一恢复入口（v0.0.6）

**第一条：原SKILL无需原生安装。** 用户已明确授权**直接使用原版源码完整执行**，详情 `research/skills/NO_INSTALL_SKILL_EXECUTION.md`。请不要再次把“当前ChatGPT未注册仓颉/女娲”作为研究停止的理由，也不得谎称它们已安装。

## 恢复顺序
1. 读取 `PROJECT_SPEC.md`、`DECISIONS.md`、`PROGRESS.md`、`NEXT_ACTION.md`、`ISSUES.md`，核实本仓库main最新提交并以已验证状态为事实基础。**不依赖V10/V11任何资料**。
2. 读取 `research/skills/NO_INSTALL_SKILL_EXECUTION.md` 和 `research/skills/SOURCE_REGISTRY.md`。从其中锁定的**两个Git commit**分别获取cangjie/nuwa原版完整SKILL.md及当前阶段要求的所有引用文件、模板、脚本与模式，而非套用自己编写的摘要。必要时再次核对入口Git blob。
3. 原版仓颉脚本GitHub CI`doctor PASS`且26/26 unit test；女娲原版quality_check正反合成样本判断正确，证据在 `research/skills/RUNTIME_AUDIT_2026-10-08.md`。这是**源码可执行证据**，不是原生安装也不是正式V12写作SKILL通过。
4. 确认两本EPUB真正可读取，与 `research/epub_audit/SUMMARY.md` SHA256一致。缺原著时不得依据索引伪造研究。当前GitHub没有全书原文；详细CSV本地副本尚未入库。
5. 分别读取 `books/wanming/PIPELINE_STATE.md`、`books/tiexuecanming/PIPELINE_STATE.md`，从真实章节断点依原始cangjie Stage0及nuwa相应阶段推进，不跳过作者规定的用户确认门。
6. 在一轮结束时更新 `PROGRESS.md`、`NEXT_ACTION.md`、相关阶段文件，提交Github并回读验证。按照真实证据汇报“已做/未做/失败”。

## 优先入口
简短可复制的重新启动提示词见 `RESTART_PROMPT.md`。需要详尽实施规则读 `research/skills/NO_INSTALL_SKILL_EXECUTION.md`。

**目前已证实的研究基线**：两书各15章、总30/1103，下一章节各#016，仓颉Stage0未通过，正式原创SKILL 0份验收。将来以远程最新提交为准。
