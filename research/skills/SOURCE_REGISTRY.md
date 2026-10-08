# 两个指定SKILL的访问核验（不是安装声明）

核查日：2026-10-08。

| 指定名称 | 当前安装识别 | 可访问的上游候选 | 入口文件 | 已验证的源码指纹 |
|---|---|---|---|---|
| cangjie-skill | 未发现 | https://github.com/kangarooking/cangjie-skill | SKILL.md, 声明2.5.0 | blob SHA 5d0c0b68425847eb12e7bf3d7109a4d63db42fa3 |
| nuwa-skill | 未发现 | https://github.com/alchaincyf/nuwa-skill | SKILL.md, 内部name=huashu-nuwa | blob SHA 788669b7b2ab755ae04d6585c28beeacedda41f2 |

本次已通过GitHub连接读取两份完整SKILL.md；cangjie已经读取 methodology/00-overview、01-stage0-adler、BOOK_OVERVIEW模板；nuwa已经读取 references/extraction-framework、skill-template、fidelity-scorecard。其他引用/脚本需要继续逐一读取与验证，**不可宣称全部依赖已部署**。

## 核查到的执行顺序
cangjie: 阶段0整书理解并用户确认→阶段1五提取器(允许串行降级)→1.5三重验证并用户确认→1.6晋级门→2 RIA++能力卡→3链接→4真实压力测试→5编译安装；详细行为与检查点以原SKILL为准。

nuwa: 0入口分流与用途/成本确认→0.5创建目录→1六维素材采集→1.5调研Review→2框架提炼→2.5确认→3Skill构建→4质量验证→5双Agent精炼。用户请求是提取原创机制，故角色扮演或模仿作者口吻并非V12目标；应采用该SKILL的**主题Skill**变体而非冒充作者本人。

两原始SKILL包含用户确认关口；项目“自动推进”指在关口前尽可能做完可做工作，不等于绕过硬性确认。
