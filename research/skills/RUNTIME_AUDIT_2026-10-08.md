# V12 原始SKILL安装与源码运行审计（2026-10-08，v0.0.5）

> **审计结论：上游原版可运行 ≠ 当前ChatGPT自动安装成功。** V12当前只验证了GitHub CI源码运行和女娲本地原版质量检查脚本；当前ChatGPT技能注册表仍不含两者。

## 一、来源与可复现版本

| 工具 | 固定Git提交 | SKILL.md git blob SHA |
|---|---|---|
| 仓颉 cangjie-skill | `kangarooking/cangjie-skill@a28de55ba881b9928956a55048f743f7a9e3b23e` | `5d0c0b68425847eb12e7bf3d7109a4d63db42fa3` |
| 女娲 nuwa-skill | `alchaincyf/nuwa-skill@fe0374687037c4cc51a65c1e0c145afe2981dc69` | `788669b7b2ab755ae04d6585c28beeacedda41f2` |

上游仓颉标注v2.5.0，已发布版本存在同号补包；不能仅凭版本字符串说明与用户此前安装版一致。固定提交号优先于浮动main。

## 二、GitHub Actions实测——PASS

- Workflow: `.github/workflows/skill-source-smoke.yml`
- Run: https://github.com/xiaolongnv6866-gif/V12/actions/runs/37803997027
- 对应V12提交：`119fd7429aa8d266f020339c5d35bc83818fdf87`
- 运行结论：**completed/success**，两个作业全部success；git checkout固定提交并核对入口blob。
- 仓颉：使用原仓库 `scripts/cangjie.py doctor` 输出 `doctor: PASS`，原仓库 `python3 -m unittest discover -s tests -v` **Ran 26 tests / OK**。测试依赖PyYAML、jsonschema在CI隔离虚拟环境安装，Python版本3.12.3；三项doctor必查schema存在。
- 女娲：git哈希核验 `scripts/quality_check.py` blob `e84d9edd3c4dc6289c598b55d150c59f8bdef87f`；编译3个原版Python脚本通过；质量检测脚本对合成良例返回 `6/6`、对合成坏例返回非零 `1/6`。只有脚本功能通过，没有实际小说SKILL通过质量审查。
- 成功归属：**GitHub Runner中的固定上游源码及其单元测试可运行**。并非当前ChatGPT技能宿主、并非正式书籍能力、并非真实输出盲测。

## 三、当前聊天宿主检查——NOT INSTALLED / NOT ACCESSIBLE

- `skills__list` 实际列出当前技能插件，但未出现 `cangjie-skill` 或 `nuwa-skill`。
- 直接`skills__read`尝试对应URI返回`Resource not found`。
- 容器查找 `/home/oai/skills`、`/mnt/data` 未发现二者原始安装目录；容器执行`git ls-remote https://github.com/kangarooking/cangjie-skill.git HEAD`报`Could not resolve host: github.com`。
- 容器Python 3.13.5、PyYAML和jsonschema均可导入，tiktoken缺失（仓颉doctor里可选）；这是本地环境依赖检查，**不是原版仓颉doctor的本地通过**。
- 本地按原版Git blob哈希完全匹配地放入女娲`scripts/quality_check.py`，用合格/不合格虚拟文件实测：通过样本退出码0，拒绝样本退出码1，且输出与GitHub Runner一致。原版脚本源不上传V12以避免不必要地复制上游仓库。

## 四、尚未解决问题和合理使用边界

1. **无法证明此前用户安装的版本**；没有用户其他软件的技能目录，也没有当前ChatGPT原生注册入口。明确保留 I-001、I-006。
2. **未实现原始SKILL在当前聊天中按技能名自动唤起**。不能把GitHub测试/使用技能文档说成ChatGPT正式安装。
3. 当前可以通过GitHub连接读取**固定源码**，严格遵照SKILL.md规定的阶段、交互质量门和测试；确定性脚本可以在隔离GitHub Runner执行。但部分由当前Agent进行的文档阅读/推理仍非原生安装调用。
4. 若以后在兼容Agent（如Codex CLI、Claude Code或OpenClaw）直接安装，必须安装**完整目录**而非只复制SKILL.md，锁定上述提交，并在目标宿主重新执行doctor/quality-check与实际的触发、输出测试。宿主安装操作须由有相应执行权限的用户或Agent执行，不能视作本次已完成。
5. 仓颉Stage0与女娲的原文检查点不能以CI运行成功而跳过。V12写作SKILL目前仍0份验收、原著30/1103章有实际研究记录。

## 五、结论

已排除“公开候选上游源码本身无法运行”这一风险（上述固定版本及测试覆盖范围内）；但**当前ChatGPT技能宿主安装/按名调用问题尚未解决**。用户要求的“先解决再大规模研究”可分解为：源码运行自检已通过，宿主安装仍需另一个有安装权限的执行环境。未来任何结论必须分项报告。
