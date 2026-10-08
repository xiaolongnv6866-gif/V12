# V12 无安装运行契约（执行规则 v0.0.6）

## 决策与目标
用户于2026-10-08明确授权：**无需将cangjie-skill、nuwa-skill注册到当前ChatGPT的原生技能列表**。只要可以实际依据其完整原版指令执行，且未来V12新会话能再次读取来源、接续进度即可。此决定**只免除安装要求，不免除完整原流程、依赖读取、真实测试、源版本核对和作者规定的确认节点**。

## 固定上游来源（不要调用浮动的main）
- Cangjie Git: `kangarooking/cangjie-skill@a28de55ba881b9928956a55048f743f7a9e3b23e`
- Cangjie入口 `SKILL.md` blob: `5d0c0b68425847eb12e7bf3d7109a4d63db42fa3`
- Nuwa Git: `alchaincyf/nuwa-skill@fe0374687037c4cc51a65c1e0c145afe2981dc69`
- Nuwa入口 `SKILL.md` blob: `788669b7b2ab755ae04d6585c28beeacedda41f2`
- 用户已接受这两套**明确固定的公开原始源码**作为V12执行依据；这不等于我们知道用户在其他软件曾安装何种版本。

## 每次新会话启动要真实执行，而非口头保证
1. 从唯一仓库 `https://github.com/xiaolongnv6866-gif/V12` 读取 `START_HERE.md`、`PROJECT_SPEC.md`、`DECISIONS.md`、`PROGRESS.md`、`NEXT_ACTION.md`、`ISSUES.md`、两书 `books/*/PIPELINE_STATE.md`，优先查明上次提交SHA、上次验证完成的章节和当前阶段。
2. 阅读本契约和 `research/skills/SOURCE_REGISTRY.md`、`research/skills/RUNTIME_AUDIT_2026-10-08.md`，从**上面锁定的Git提交**读取两套完整SKILL.md及当前阶段要求的全部methodology/references/templates/extractors/scripts/schema。不得用简单总结或模型印象冒充已重读完整原版。引用文件按需逐一追溯，不因未安装而删减步骤。
3. 执行模式：Agent人工负责需理解、论证、提取及写作的环节；脚本负责可验证的确定性任务。在有权限的隔离执行环境（包括已通过的GitHub Actions）运行原版脚本，并保存真实输入、日志和输出。**不能把运行脚本的能力说成原生Agent Skills安装。**
4. 先确认原版EPUB可被该会话实际读取，再继续文学研究。定位审计和GitHub已有研究**不等于原著正文**。若缺原文，停止依赖正文的新研究，只做与原文无关的工程项或请用户添加原版EPUB。不得将完整版权文本上传公共GitHub仓库。
5. 执行原版cangjie Stage0→1→1.5→1.6→2→3→4→5 和nuwa Phase0→0.5→1→1.5→2→2.5→3→4→5；按照当期原文实际规定执行。各原版质量门、用户确认、证据检验和测试均保留，不允许一次性跳过；若宿主不支持某项，并不假称已完成，记录阻碍并选用原文允许的降级方法。
6. GitHub进度以**本次实际完成工作**写入研究、测试和状态，并提交后重新读取确认。任何失败/未通过标注原因。新会话不以聊天记忆或旧项目替代仓库事实。

## 跨会话能力边界
- **可跨会话恢复**：GitHub中的规约、固定SKILL版本定位、章节笔记、状态与测试证据，只要新会话拥有GitHub读取能力。若GitHub插件不可用，可在公开网页读取；写入仍须另行验证权限。
- **不可凭空保证**：当前会话的临时Python/容器内容、未上传GitHub的本地CSV和审计包、用户未放到项目或新会话无法访问的两本EPUB、未持久化的临时推理。发现缺失先补恢复依赖，不能假装可见。
- 在同一V12项目中新开会话通常比其他项目更利于读取同项目附属文件，**但仍需真实检查文件是否可读**。
- 源SKILL是流程执行依据；以后产生的V12原创SKILL才是最终供小说创作的产品。当前正式原创写作能力尚未验收，不得把前者等同后者。

## 会话最小恢复指令
`继续V12。以GitHub仓库xiaolongnv6866-gif/V12的START_HERE.md为唯一入口，按NO_INSTALL_SKILL_EXECUTION.md恢复固定仓颉和女娲原始流程，核对EPUB与状态，从NEXT_ACTION.md真实断点执行，完成一批提交并验证；不使用其他项目数据、不虚报。`

本契约与项目硬边界如有冲突，只豁免“必须先原生安装”这一额外约束，**不降低研究质量、源版本追踪或原SKILL步骤标准**。
