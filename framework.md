# AI信号站 日报框架与硬规则（详细参考）

本文件是 `ai-signal-daily` skill 的详细参考，供撰写每期日报时查阅。
SKILL.md 只保留流程步骤，细节在此。

## 一、品牌与交付约定

- 品牌名：**AI信号站 —— 每天追踪 AI 世界正在发生什么。**
- 频率：每天；语言：中文；领域：全部。
- 详细度：详版每项 300–500 字、简版每条约 50 字（**默认简版**）。
- 输出：自包含 HTML（零外链、可直接浏览器打开）。
  - 详版 `daily/YYYY-MM-DD.html`，简版 `daily/YYYY-MM-DD-lite.html`。
- 投递：文件 + 聊天双发；推送时间默认 07:30 Asia/Shanghai。
- 每条信息**必须附来源链接**（X 推文 / 播客 / 博客 / arXiv 均可点击跳转）。
- 页脚固定附带「非投资建议」声明。

## 二、4 模块内容框架

1. **📢 一线观点** — 业内真正的人在说什么？来源：X/Twitter、Podcast 访谈、创始人/CEO 发言、官方 Blog、行业大佬公开观点。
   - 重点不是"他说了什么"，而是**有没有出现新的行业信号**。
   - 每条结尾用「信号：」引出行业含义，**不要复述"他说了什么"**。
   - 播客**展开为个体卡（一卡一来源）**，不合并紧凑卡。
2. **🧠 技术前沿** — 技术本身往哪走？来源：arXiv/Papers、GitHub 新模型、Benchmark、开源项目、AI Infra、Agent/多模态/推理。
   - 不做论文新闻，要回答「技术突破 → 谁能用 → 哪个产品受益 → 有没有产业影响」。
3. **🚀 产品动态** — AI 产品市场在发生什么？来源：Product Hunt AI 产品榜、模型排行榜、Agent 产品、新发布产品、SaaS/AI App。
   - 观察：什么产品突然火、什么能力从模型变产品、哪些产品异常增长。
   - **Product Hunt 排行数据源未接入前不放；模型脉搏不放。**
4. **💰 资本市场** — 把 AI 技术趋势连到产业与股票。
   - 覆盖：AI 融资/大额投资、AI 服务器/芯片/GPU/光模块/PCB/存储/数据中心/电力/液冷/半导体设备、AI 硬件、AI 概念股、大厂 CapEx。
   - 逻辑链：技术变化 → 产品变化 → 产业变化 → 资本变化。
   - 无新增信号的子主题列入"跟踪范围"清单（用 `compact` 项，明确标注、不编造来源）。

## 三、数据来源（payload.json）

由 `prepare_digest.py` 生成，结构：

- `generated_at`：数据生成时间（UTC ISO）。
- `status`：`ok` 表示远程新鲜；`429`/超时失败则回退本地缓存。
- `x`：列表，每项 `{handle, name, domain, tier, tweets:[{id,text,created_at,like_count,retweet_count,reply_count,engagement_score,url}]}`。
- `podcasts`：列表，每项 `{channel, title, pub_date, link, description, transcript_available, ...}`。
- `articles`：列表（官方博客），每项 `{source, source_name, title, url, published, summary}`。
- `papers`：列表（arXiv），每项 `{arxiv_id, title, authors, abstract, primary_category, abs_url, pdf_url, published}`。
- `stats`：`{podcast_episodes, x_builders, total_tweets, arxiv_papers, blog_articles, ...}`。
- **无 `investment` 字段** —— 资本市场模块靠人工从技术/产品信号推导，不伪造。

## 四、item 字段约定（传给 render_items）

普通条目：
```python
{"tag": "信号标签", "who": "来源人/机构", "url": "来源链接", "text": "分析文字"}
```
- 资本市场(M4)无具体来源的条目：`url` 置 `None`（渲染为无链接卡）。
- "跟踪范围"紧凑清单：
```python
{"compact": True, "tag": "跟踪范围（本期无新增具体信号）", "who": "产业链子主题",
 "text": "按框架持续跟踪、本期暂无新增信号的子主题：",
 "links": [("AI 服务器 / 光模块 / PCB", "#"), ("存储（HBM/DRAM）", "#"), ...]}
```
- 内容字符串**统一用三单引号 `'''...'''`** 包裹，避免中文弯引号 " " 与 ASCII 直引号 `"` 冲突导致 SyntaxError。

## 五、硬规则（不违反）

1. **不伪造数据**：取不到标"—"或说明，不得用随机值填充。
2. 每条带来源链接（M4 综合条目可 `url=None`，但"跟踪范围"链接不得伪装成真实来源，占位用 `"#"`）。
3. 模型脉搏旧数据（最新可用 2026-08-20）**不混入今日**日报。
4. Product Hunt 排行未接入前**不放**。
5. 资本市场为**非投资建议**，页脚声明。

## 六、校验清单（交付前逐项核对）

- [ ] 4 个 `<section id="m1/m2/m3/m4">` 锚点齐全，导航 4 个锚点可跳转。
- [ ] 每条带来源链接；M1 播客为个体卡（非合并紧凑卡）。
- [ ] 紧凑项（`compact`）仅出现在 M4 的"跟踪范围"，且无伪造来源。
- [ ] 首尾 `<!DOCTYPE html>` / `</html>` 完整。
- [ ] 模型脉搏、Product Hunt 排行未出现（按当前数据边界）。
- [ ] 页脚含「非投资建议」。
