# V12 新会话唯一恢复入口

1. **先读取** PROJECT_SPEC.md、PROGRESS.md、NEXT_ACTION.md、DECISIONS.md、ISSUES.md。
2. 验证当前GitHub连接的读/写权限和本仓库最新提交；不得以对话记忆为项目事实。
3. 检查 cangjie-skill 与 nuwa-skill **在当前执行环境中是否真实安装**。读取原始入口与所有需要的依赖；仅能访问GitHub源码≠已经安装。
4. 检查两本 EPUB 在当前会话是否实际可读。对照 research/epub_audit/SUMMARY.md 中的 SHA-256；如果无文件，请用户重新提供，**不可凭索引伪造正文证据**。
5. 读取两本书对应的 books/*/PIPELINE_STATE.md，按照原SKILL必经阶段继续。阶段0需要全书阅读和用户骨架确认；没有通过不能进入阶段1。
6. 正式创作只在最终原创SKILL经实测与恢复测试通过后启用。此时应另行读取未来的创作恢复入口及原创小说状态；当前**尚不存在可激活的正式创作SKILL**。

文件权威分层：PROJECT_SPEC.md及DECISIONS.md=项目规则；PIPELINE_STATE.md和PROGRESS.md=已验证执行状态；research/=证据与候选；tests/=测试资料；正式SKILL另行发布且须标版号。绝不把候选当成正式能力。

不使用旧V10/V11小说剧情、分析、任务状态或存储。
