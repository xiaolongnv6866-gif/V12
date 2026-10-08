# V12 原始SKILL在不同宿主中的使用方式

目的：避免把“复制提示词”“GitHub可读源码”“原版CLI测试通过”和“宿主已安装可自动触发”混为一谈。

## 当前ChatGPT对话
当前`skills__list`没有两套SKILL，不能以`@cangjie-skill`或`@nuwa-skill`的原生技能方式成功调用。GitHub连接可读取固定源文件和V12记录；本会话可按完整原文流程人工编排，并将可重复的确定性脚本交给GitHub Actions执行。**这不是宿主安装成功**。

## 已固定的上游源码
- Cangjie: https://github.com/kangarooking/cangjie-skill/tree/a28de55ba881b9928956a55048f743f7a9e3b23e
- Nuwa: https://github.com/alchaincyf/nuwa-skill/tree/fe0374687037c4cc51a65c1e0c145afe2981dc69
- 本项目可复现原版代码测试：https://github.com/xiaolongnv6866-gif/V12/actions/runs/37803997027

## 在有终端和Agent Skills加载能力的宿主中安装（需要有权限的用户/Agent实际操作）
以Codex CLI为例，宿主默认skills目录为`~/.codex/skills/`（在实际安装前应以所用软件当前文档确认）：

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/kangarooking/cangjie-skill.git ~/.codex/skills/cangjie-skill
git -C ~/.codex/skills/cangjie-skill checkout a28de55ba881b9928956a55048f743f7a9e3b23e
git clone https://github.com/alchaincyf/nuwa-skill.git ~/.codex/skills/nuwa-skill
git -C ~/.codex/skills/nuwa-skill checkout fe0374687037c4cc51a65c1e0c145afe2981dc69
python3 -m pip install pyyaml jsonschema
python3 ~/.codex/skills/cangjie-skill/scripts/cangjie.py doctor
python3 -m unittest discover -s ~/.codex/skills/cangjie-skill/tests -v
```

这些是上游源码完整拷贝至兼容宿主的**建议命令**；未经在用户机器实跑，不得宣称完成。Nuwa Phase4 `quality_check.py` 接收待检**原创SKILL.md文件路径**，对无产物阶段不应拿示例结果冒充正式验收。

## 恢复和验收
1. 记录目标宿主、skills目录、两套Git commit、doctor/测试的真实日志。
2. 让目标Agent启动新会话，实际列出可用技能，并直接触发一个完整的非生产模拟任务。
3. 未满足注册表可见、调用成功、任务输出证据3项时仍标`host_not_verified`。
4. V12不得将个人EPUB上传公开仓库或CI；脚本测试仅使用合成样本。
