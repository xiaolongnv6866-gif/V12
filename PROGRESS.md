# V12 实际进度

核查日期：2026-10-08；对应研究提交 v0.0.2。**不报告主观完成百分比。**

| 工作单元 | 状态 | 可复核证据 |
|---|---|---|
| V12 GitHub | API读写及两次提交验证 | main仓库提交链，详见CHANGELOG |
| cangjie-skill | 16项主文/流程/提取器/阶段0模板源码已完整读取；已安装状态未验证 | research/skills/SOURCE_REGISTRY.md |
| nuwa-skill | 8项入口/参考/脚本源码已完整读取；已安装状态未验证 | research/skills/SOURCE_REGISTRY.md |
| 两本EPUB | ZIP CRC、OPF、spine、提取与SHA-256核验 | research/epub_audit/SUMMARY.md |
| 全部有效章的结构定位 | **1103/1103** | 晚明571、铁血残明532；完整CSV在本次本地审计包中 |
| 逐章实际文学研读 | **10/1103** | 每书前五叙事章；OPENING_PILOT + chapter-notes/ |
| 晚明 cangjie阶段0 | 阅读5/571；质量门未达标 | books/wanming/PIPELINE_STATE.md |
| 铁血残明 cangjie阶段0 | 阅读5/532；质量门未达标 | books/tiexuecanming/PIPELINE_STATE.md |
| nuwa正式蒸馏 | 未开始 | 未达到其完整前置条件 |
| V12正式原创SKILL | 0份通过验收 | 尚未构建 |
| 原创小说正文 | 未开始 | 按规定不得先行 |

**计数规则**：程序遍历1110余段XHTML解析标题和正文长度只是结构索引；只有实际阅读并编制章节因果/人物/叙事判断记录才计入10章。
**完整目录文件**：本会话本地 `V12-EPUB-AUDIT-v0.0.1.zip` 含两本全spine CSV、manifest JSON及重跑脚本；仓库暂只保存摘要，待解决原始CSV上传路径（I-005）。
