AI信号站 每日简版日报
生成自包含、零外链的「AI信号站」每日 AI 投研简报 HTML。报告按用户定下的 4 模块框架组织，数据来自当日真实公开来源（X / 播客 / 官方博客 / arXiv），每条带来源链接，资本市场模块靠人工从技术/产品信号推导（非投资建议）。

何时使用
用户说「完成【日期】AI信号站复盘」→ 拉取该日期最新数据并生成 daily/{日期}-lite.html。
用户要求生成 / 补生成 AI 信号站日报、或要求按 4 模块框架整理当日 AI 资讯。
与日常自动化 automation-1787054389854（每天 07:30 自动 fetch→build→render）同源，本 skill 用于指定日期补生成/复盘。
工作流（端到端）
步骤 1 · 拉取最新 payload
用 ai-signal 专用 venv（需 httpx>=0.27，独立于全局）：

PYTHONPATH="D:/LJ/投资/AI Signal/scripts" \
  "C:/Users/44828/.ai-signal/venv/Scripts/python.exe" \
  "D:/LJ/投资/AI Signal/scripts/prepare_digest.py" --out "C:/Users/44828/.ai-signal/payload"
检查 stdout manifest 的 status / generated_at / feed_sources：远程新鲜则用新 payload；若 429/超时失败，回退本地 C:/Users/44828/.ai-signal/payload/payload.json 缓存（仍可用）。

步骤 2 · 转储内容供策展
运行 skill 自带脚本，把 payload 抽成可读文本（按 X / 播客 / 官方博客 / arXiv 分节，每条带链接）：

"C:/Users/44828/.ai-signal/venv/Scripts/python.exe" \
  "C:/Users/44828/.workbuddy/skills/ai-signal-daily/scripts/dump_payload.py" \
  --payload "C:/Users/44828/.ai-signal/payload/payload.json" --out "D:/LJ/投资/AI Signal/outputs/payload_dump.txt"
步骤 3 · 填 4 模块内容（真实数据，每条带来源链接）
详细框架、硬规则与 item 字段约定见 references/framework.md。要点：

M1 📢 一线观点：X/CEO/播客/官方Blog/行业大佬，按"新行业信号"框架（每条结尾「信号：」引出行业含义，非复述"他说了什么"）；播客展开为个体卡（一卡一来源），不合并紧凑卡。
M2 🧠 技术前沿：arXiv，按「突破→谁用→哪产品受益→产业影响」。
M3 🚀 产品动态：真实产品发布 / Agent 产品（Product Hunt 排行数据源未接入前不放；模型脉搏不放）。
M4 💰 资本市场：技术→产品→产业→资本，覆盖芯片/GPU/光模块/PCB/存储/数据中心/电力/液冷/半导体设备/AI概念股/大厂CapEx；无新增信号的子主题列入"跟踪范围"紧凑清单（明确标注、不编造来源）。
步骤 4 · 生成 HTML
复制 skill 模板脚本并按本期数据改写 M1–M4，再运行：

"C:/Users/44828/.ai-signal/venv/Scripts/python.exe" \
  "C:/Users/44828/.workbuddy/skills/ai-signal-daily/scripts/build_4module.py" 2026-09-10 \
  --root "D:/LJ/投资/AI Signal"
scripts/build_4module.py 复用项目内 model-pulse/_build_daily.py 的 CSS / JS / esc / src_label / render_items（import 模块取函数，不触发其 __main__ 硬编码示例）。
脚本内 M1–M4 为 2026-09-10 参考示例，生成新一期时整段替换为本期策展的真实数据，仅日期参数改为目标日。
内容字符串统一用三单引号 '''...''' 包裹，避免中文弯引号与 ASCII 直引号冲突。
步骤 5 · 校验（交付前逐项核对）
4 个 <section id="m1/m2/m3/m4"> 锚点齐全，导航 4 个锚点可跳转。
每条带来源链接；M1 播客为个体卡（非合并紧凑卡）。
紧凑项（compact）仅出现在 M4"跟踪范围"，且无伪造来源。
首尾 <!DOCTYPE html> / </html> 完整。
模型脉搏、Product Hunt 排行未出现（按当前数据边界）；页脚含「非投资建议」。
步骤 6 · 交付
用 present_files 打开 daily/{日期}-lite.html；同时在聊天中给出摘要。

资源
scripts/
scripts/dump_payload.py — 从 payload.json 抽取可读文本（X / 播客 / 博客 / arXiv），供策展。
scripts/build_4module.py — 参数化 4 模块 HTML 生成器（python build_4module.py YYYY-MM-DD [--root ...]），复用 _build_daily.py 的渲染函数。
references/
references/framework.md — 4 模块框架、品牌/交付约定、payload 字段结构、item 字段约定、硬规则、校验清单。
硬规则（不违反）
不伪造数据；取不到标"—"或说明，不得用随机值填充。
每条带来源链接；模型脉搏旧数据（最新 2026-08-20）不混入今日；Product Hunt 排行未接入前不放。
资本市场为非投资建议，页脚固定声明。
