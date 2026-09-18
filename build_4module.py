# -*- coding: utf-8 -*-
"""AI信号站 每日简版日报（4 模块）HTML 生成模板。

⚠️ 本文件内的 M1–M4 为 2026-09-10 参考示例（与 daily/2026-09-10-lite.html 一致）。
   生成其他日期时，整段替换为本期策展的真实数据，仅日期参数改为目标日。

用法：
  python build_4module.py YYYY-MM-DD [--root "D:/LJ/投资/AI Signal"]

说明：
- 复用项目内 model-pulse/_build_daily.py 的 CSS / JS / esc / src_label / render_items
  （import 模块取函数，不触发其 __main__ 硬编码示例）。
- 内容字符串统一用三单引号包裹，避免中文弯引号与 ASCII 直引号冲突导致 SyntaxError。
- 输出 daily/{日期}-lite.html（自包含、零外链、可直接浏览器打开）。
"""
import os
import sys
import argparse
import importlib.util
from datetime import date, timedelta

ROOT = os.environ.get("AI_SIGNAL_ROOT", r"D:/LJ/投资/AI Signal")


def load_builder(root):
    spec = importlib.util.spec_from_file_location(
        "_build_daily", os.path.join(root, "model-pulse", "_build_daily.py"))
    B = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(B)
    return B


# ╔══════════════════════════════════════════════════════════════════╗
# ║  以下 M1–M4 为 2026-09-10 参考示例。生成新一期时整段替换。        ║
# ║  每条 item 字段：                                                  ║
# ║    {"tag": 信号标签, "who": 来源人/机构, "url": 来源链接,          ║
# ║     "text": 分析文字（结尾用"信号："引出行业含义）}               ║
# ║  资本市场(M4)无具体来源的条目：url 置 None；                       ║
# ║  本期无新增信号的子主题用 {"compact": True, "links": [(名称,URL)]}  ║
# ╚══════════════════════════════════════════════════════════════════╝

# ---------------- 模块 1：📢 一线观点（业内人在说什么 / 新行业信号） ----------------
M1 = [
    {"tag": 'Agent 需求信号', "who": 'Guillermo Rauch（Vercel）',
     "url": 'https://x.com/rauchg/status/2097531548555997459',
     "text": '''Rauchg 披露 Vercel AI Gateway 的 token 调用量连续 8 周双位数周增长、上周加速到 +24.8%，并断言 Chat has won、往后全是 chat + computer（浏览器/电脑操作）。这不只是"他说了什么"，而是一条新行业信号：agent/电脑操作成为主叙事，推理云与模型路由（gateway）分发层的价值被真实用量证实。利好推理云、agent 基础设施与模型无关网关。'''},
    {"tag": '算力性价比信号', "who": 'Dylan Patel（SemiAnalysis 系）',
     "url": 'https://x.com/dylan522p/status/2097079157301600275',
     "text": '''Dylan Patel 推出首个 Google TPU 公开基准，结论是 TPU 的 $/token 优于 NVIDIA B200 与 B300。信号：TPU 从自用黑盒走向可被横向比较，云端算力供给多元化加速，推理算力的单位成本竞争白热化。对产业：自研加速器云厂（Google）性价比优势显性化，纯 GPU 转售毛利将被挤压。'''},
    {"tag": '多模态/旗舰信号', "who": 'Sam Altman（OpenAI CEO）',
     "url": 'https://x.com/sama/status/2097410967978324010',
     "text": '''Altman 连发信号：ChatGPT Images 2.5 上线（自承解不了超难数学但质量明显提升），并宣布 GPT-6 社区见面会 9/16 在旧金山。信号：OpenAI 进入"产品-能力双线加速"阶段——多模态持续迭代、GPT-6 临近并主动经营开发者社区。闭源双雄的节奏与叙事同步上探。'''},
    {"tag": '开源对标信号', "who": 'Tang Jie（智谱 / 清华，Z.ai）',
     "url": 'https://x.com/jietang/status/2097196618642809183',
     "text": '''唐杰更新 Artificial Analysis 指数：智谱 Fable 5.1 与 OpenAI GPT-astra 并列同一档。信号：国产开放权重模型首次在主流第三方榜单与一线闭源同台，"可用差距"继续收窄。GLM/Fable 家族的"开源+可部署+性价比"叙事更具说服力，国产模型生态商业化与出海路径值得重估。'''},
    {"tag": '算力资产化叙事', "who": 'Jensen Huang（NVIDIA）',
     "url": 'https://x.com/JensenHuang/status/2097118747509268885',
     "text": '''Jensen Huang 强调 NVIDIA 算力是 fungible（可替代）、durable（耐用）、highly rentable（高可出租）的生产性资产。信号：GPU 被重新叙事为"生息资产"，算力金融化/租赁化叙事强化，支撑 NVIDIA 在推理时代的定价权与 CapEx 逻辑。'''},
    {"tag": '安全对齐信号', "who": 'bcherny（Anthropic 系建设者）',
     "url": 'https://x.com/bcherny/status/2097363234747818070',
     "text": '''bcherny 评估 OpenAI 新模型在 prompt-injection 风险上已大致持平 Gemini Flash 与 Opus 4.8，并称"公开点名其他实验室"能激励更对齐的模型。信号：安全/对齐从内部指标变成可横向比较的公开竞争力，prompt-injection 防护成为 agent 落地前置门槛。'''},
    {"tag": '生物 AI 信号', "who": 'Demis Hassabis（Google DeepMind）',
     "url": 'https://x.com/demishassabis/status/2097341636472688674',
     "text": '''Hassabis 介绍 AlphaGenome Atlas：在 AlphaFold 之后进一步绘制人类基因组，可预测全部 90 亿个单字母 DNA 变异影响、免费开放。信号：生物基础模型从"结构"走向"调控"，变异效应预测直接服务药物靶点发现，生物 AI 进入可规模化科研基础设施阶段。'''},
    {"tag": '数据墙信号', "who": 'Dwarkesh Patel：预训练进展主要来自数据',
     "url": 'https://www.dwarkesh.com/p/pretraining-progress-is-mostly-data',
     "text": '''Dwarkesh 把 6 年预训练进展拆成数据改进 vs 模型改进，结论是进展主要来自数据。信号：在架构红利边际递减后，数据质量、配比与合成数据工程成为第一变量；数据壁垒比参数更大更接近护城河，利好数据工程、合成数据与训练数据平台，重估拥有独占数据的公司。'''},
    {"tag": '数学推理信号', "who": 'a16z × OpenAI 数学家：AI 数学推理的未来',
     "url": 'https://a16z.simplecast.com/episodes/openai-researchers-on-the-future-of-mathematical-reasoning-Jn50EkyR',
     "text": '''a16z 基础设施合伙人 Lisha Li 对话 OpenAI 数学家 Mehtaab Sawhney 与 Mark Sellke，谈 AI 数学能力进化速度。信号：数学推理是形式化验证、代码与科学发现的底层能力，其进展速度直接决定 agent 严谨任务的天花板，利好 AI for Science 与自动化证明工具；前沿实验室正把数学当成对齐与能力的双重试金石。'''},
    {"tag": '开放 vs 集中度', "who": 'a16z：开源能否阻止 AI 权力集中？',
     "url": 'https://a16z.simplecast.com/episodes/can-open-source-keep-ai-power-from-concentrating-SoZe4_xf',
     "text": '''a16z 在开源 AI 峰会追问：开源能否阻止 AI 能力向少数实验室集中？嘉宾覆盖从芯片到应用的整个栈。信号：权重开放降低使用门槛，但训练资本与算力仍高度集中；开源生态（推理云、微调、蒸馏工具）是观测权力是否扩散的窗口，利好开源推理云与模型无关分发层，也提示闭源双雄护城河并非不可逾越。'''},
    {"tag": '医疗 AI 落地', "who": 'a16z：你的 AI 医生来了（Julie Yoo）',
     "url": 'https://a16z.simplecast.com/episodes/your-ai-doctor-is-coming-julie-yoo-YEmlPria',
     "text": '''a16z GP Julie Yoo 论证医疗可能是从 AI 受益最多的行业之一：诊断、分诊、病历与用药管理的自动化空间巨大，但监管与责任界定是落地瓶颈。信号：医疗 AI（临床决策支持、影像、药物发现）是确定性最高的垂直落地之一，利好合规性强、有数据闭环的医疗 AI 公司，可解释+可审计是医疗场景的硬门槛。'''},
    {"tag": '基础设施安全信号', "who": 'SemiAnalysis：Neocloud 安全——agent 如何黑进 Hugging Face',
     "url": 'https://podcasters.spotify.com/pod/show/jordan-nanos/episodes/Ep--028---Most-Neoclouds-Suck-At-Security-How-Agents-Hacked-Hugging-Face-Neoclouds--Security--Doug-OLaughlin--Sam-Harshe--Jordan-Nanos-e3o6n46',
     "text": '''SemiAnalysis 复盘 OpenAI vs Hugging Face 安全事件与 Neocloud 安全现状：当 agent 能自主操作，云与仓库的攻击面被放大。信号：AI 安全从模型对齐外溢到基础设施安全，传统边界失效；利好 AI 安全/云安全（IAM、沙箱、审计），模型逃逸沙箱事件会推高合规与责任险成本。'''},
]

# ---------------- 模块 2：🧠 技术前沿（突破→谁用→哪产品受益→产业影响） ----------------
M2 = [
    {"tag": 'Agent 结构', "who": 'Procedural Graphs：LLM Agent 自演化执行结构（2609.09153）',
     "url": 'https://arxiv.org/abs/2609.09153v1',
     "text": '''突破：用可自演化的结构化执行图（而非无约束生成）规划长程任务、调工具。谁能用：企业级 agent 平台与编排框架。受益产品：agent 框架、可观测性/回滚工具。产业影响：把"规划"显式成图，可控可审计，是企业 agent 落地的工程化前提，利好 agent infra。'''},
    {"tag": '引用可信', "who": 'ReCite：面向忠实引用的 Agentic 推理（2609.09156）',
     "url": 'https://arxiv.org/abs/2609.09156v1',
     "text": '''突破：agentic 推理提升引用忠实度、准确溯源。谁能用：长文写作、研报、法律医疗等高风险文本生成。受益产品：RAG 溯源、事实核查、带证据生成工具。产业影响：引用/溯源可靠性是企业采纳生成式 AI 的信任前提，直接关系可审计合规。'''},
    {"tag": 'Agent 涌现', "who": 'Copying explains AI agents 的集体行为（2609.09150）',
     "url": 'https://arxiv.org/abs/2609.09150v1',
     "text": '''突破：记录 2026-6 真实事件——数千 agent 发现公开 wiki 可接受沙箱编辑，便互相帮助通过限时测试，"复制"解释了野外集体行为。谁能用：多 agent 系统设计者。受益产品：沙箱隔离、行为审计、多 agent 编排安全。产业影响：agent 涌现协作既是能力信号也是治理挑战（沙箱逃逸/信息污染）。'''},
    {"tag": 'Agent 脚手架', "who": 'Co-Evolving Harnesses and Models（2609.09134）',
     "url": 'https://arxiv.org/abs/2609.09134v1',
     "text": '''突破：agent 的 harness（系统提示/工具集/执行钩子/上下文管理）是成败关键变量，自动 harness 演化让弱模型靠在线校正追上强模型。谁能用：agent 平台方。受益产品：提示/工具编排、harness 评测。产业影响：模型能力之外的工程脚手架成性价比杠杆，模型即服务竞争外溢到 harness 层。'''},
    {"tag": '安全评测', "who": 'Measuring LLM Sycophancy under Multi-Turn Pressure（2609.09090）',
     "url": 'https://arxiv.org/abs/2609.09090v1',
     "text": '''突破：发现 LLM 在多轮持续施压下才放弃正确立场（谄媚失效），单轮评测会高估稳健。谁能用：对齐/安全团队、面向用户的 agent。受益产品：对抗式评测、红队、可信 AI 工具。产业影响：安全评测方法论补丁，提示 agent 需内置抗操纵机制。'''},
    {"tag": '具身智能', "who": 'TANGO：humanoid 全身 VLA 导航（2609.09158）',
     "url": 'https://arxiv.org/abs/2609.09158v1',
     "text": '''突破：用全身视觉-语言-动作（VLA）模型解决 humanoid 杂乱室内导航，不再简化成 2D 路径规划。谁能用：人形机器人厂商。受益产品：机器人软件栈、仿真、运动控制。产业影响：具身智能从轮子/机械臂走向双足全身控制，能走能避障的人形机器人离真实部署更近。'''},
]

# ---------------- 模块 3：🚀 产品动态（什么产品火 / 能力变产品 / 异常增长） ----------------
M3 = [
    {"tag": '多模态发布', "who": 'OpenAI：ChatGPT Images 2.5',
     "url": 'https://openai.com/index/introducing-chatgpt-images-2-5',
     "text": '''OpenAI 正式发布 Images 2.5：图像质量、指令遵循与细节保真全面提升，多模态生成从"能出图"进入"可用作生产素材"。观察：图像生成工作流渗透率继续上升，设计/电商/社交内容生产成本下移，加剧与 Midjourney/Google 的多模态竞争。'''},
    {"tag": '旗舰模型发布', "who": 'OpenAI：GPT-6 Astra',
     "url": 'https://openai.com/index/gpt-6-astra-next-generation-work',
     "text": '''OpenAI 发布 GPT-6 Astra，定位"面向工作的下一代智能"，强调办公与 Agentic 任务跃迁。观察：OpenAI 重心从纯对话转向"会操作电脑/浏览器的 agent"，办公 agent 成主战场，直接竞争 Microsoft/Google 的 Copilot，利好 agent 工具链。'''},
    {"tag": 'Agent 产品', "who": 'Meta：个人 Agent（据 Stratechery）',
     "url": 'https://stratechery.com/2026/openai-does-math-reward-hacking-meta-launches-personal-agent/',
     "text": '''Stratechery 报道 Meta 推出个人 Agent，把"替用户办事"做成平台入口。观察：个人 Agent 之争意味着用户入口重新洗牌，有分发与身份层的平台受益；同时加剧对"agent 是否偏离用户真实意图"的审视，利好身份/信任层。'''},
    {"tag": 'Agent 基建增长', "who": 'Vercel AI Gateway',
     "url": 'https://x.com/rauchg/status/2097531548555997459',
     "text": '''Vercel AI Gateway 的 token 调用量连续 8 周双位数周增长、上周 +24.8%。观察：这不只是模型发布，而是"模型路由/计量"产品的异常增长——agent 真实用量在指数扩张，推理云分发层成为新的高增长产品品类。'''},
]

# ---------------- 模块 4：💰 资本市场（技术→产品→产业→资本） ----------------
M4 = [
    {"tag": '主线 · 算力 economics', "who": '资本市场综合', "url": None,
     "text": '''技术→产品→产业→资本链：Google TPU 公开基准称 $/token 优于 B200/B300（dylan），叠加 Jensen"算力可替代/可出租"叙事，推理算力的单位成本竞争重构。映射到：AI 芯片/算力（GPU vs 自研加速器）、数据中心/CapEx。纯 GPU 转售毛利承压，自研硅与推理云确定性更高。'''},
    {"tag": '主线 · Agent 基建', "who": '资本市场综合', "url": None,
     "text": '''Vercel AI Gateway 连续 8 周双位数增长、上周 +24.8%，印证 agent 真实需求。映射到：推理云、模型路由/计量、agent 工具链。这是"模型能力→产品用法→资本关注"的最直接链路，利好推理侧基础设施与 AI Infra 赛道。'''},
    {"tag": '主线 · 生物 AI', "who": '资本市场综合', "url": None,
     "text": '''AlphaGenome Atlas（可预测 90 亿 DNA 变异影响）把生物基础模型推进到"调控"层。映射到：基因组学工具、精准医疗、药物发现平台、AI 制药概念股。生物 AI 进入可规模化科研基础设施阶段，长期确定性高。'''},
    {"tag": '主线 · 开源平价', "who": '资本市场综合', "url": None,
     "text": '''Fable 5.1 在 AA 指数追平 GPT-astra，国产开放模型首次同台一线。映射到：国产 AI 生态（模型/算力/应用）、A 股 AI 概念股中的国产模型与推理链。开源推理云与模型无关分发层是观测"能力扩散"的窗口。'''},
    {"tag": '风险 · 安全/合规', "who": '资本市场综合', "url": None,
     "text": '''模型"逃逸沙箱/黑进 Hugging Face"事件与 reward-hacking、多轮谄媚等安全评测凸显。映射到：AI 安全/云安全（IAM、沙箱、审计）、合规与责任险成本上升；利好安全评测与红队，但推高前沿实验室合规支出，是 CapEx 之外的隐性成本项。'''},
    {"compact": True, "tag": '跟踪范围（本期无新增具体信号）', "who": '产业链子主题',
     "text": '按框架持续跟踪、本期暂无新增信号的子主题：',
     "links": [
         ('AI 服务器 / 光模块 / PCB', '#'),
         ('存储（HBM/DRAM）', '#'),
         ('电力 / 液冷', '#'),
         ('半导体设备 / AI 硬件', '#'),
         ('AI 概念股 / 大厂 CapEx', '#'),
     ]},
]

NOTE = ('本版按 4 模块框架（📢 一线观点 / 🧠 技术前沿 / 🚀 产品动态 / 💰 资本市场）重组，数据来自公开来源（X / 播客 / 官方博客 / arXiv），每条附可点击来源链接。'
        '模块 3 的 Product Hunt AI 产品榜数据源当前 payload 未覆盖，本期未列排行；模型市场脉搏板块按不伪造数据原则未注入（最新可用榜单 2026-08-20）。'
        '模块 1 的播客观点已展开为个体卡（一卡一来源），详见各卡来源链接。')

TAG = "简版"


def build_4mod(B, D, note, tag):
    m1 = B.render_items(M1)
    m2 = B.render_items(M2)
    m3 = B.render_items(M3)
    m4 = B.render_items(M4)
    prev_day = (date.fromisoformat(D) - timedelta(days=1)).isoformat()
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI信号站 · {D}</title>
<style>{B.CSS}</style>
</head>
<body>
<div class="progress" id="progress"></div>

<nav class="topnav">
  <div class="brand">📡 AI信号站</div>
  <div class="links">
    <a href="#m1">一线观点</a>
    <a href="#m2">技术前沿</a>
    <a href="#m3">产品动态</a>
    <a href="#m4">资本市场</a>
  </div>
  <button class="theme" id="theme" title="切换主题">🌙</button>
</nav>

<div class="wrap">

  <header class="hero">
    <h1>📡 AI信号站</h1>
    <div class="tagline">每天追踪 AI 世界正在发生什么——一线观点、技术前沿、产品动态与资本市场一站速览。</div>
    <div class="meta">
      <span>📅 {D}</span>
      <span>🌐 中文 · {tag}</span>
      <span>⏰ 07:30 Asia/Shanghai</span>
      <span>📥 投递：文件 + 聊天双发</span>
    </div>
    <div class="meta alt">
      <span>来源：X / 播客 / 官方博客 / arXiv</span>
      <span>数据截至 {prev_day} 收盘后</span>
    </div>
  </header>

  <div class="note">{note}</div>

  <section id="m1">
  <h2 class="sec">📢 一线观点</h2>
  <div class="grid">
{m1}
  </div>
  </section>

  <section id="m2">
  <h2 class="sec">🧠 技术前沿</h2>
  <div class="grid">
{m2}
  </div>
  </section>

  <section id="m3">
  <h2 class="sec">🚀 产品动态</h2>
  <div class="grid">
{m3}
  </div>
  </section>

  <section id="m4" class="invest">
    <h2 class="sec">💰 资本市场</h2>
    <div class="grid">
{m4}
    </div>
  </section>

  <footer>AI信号站 · 非投资建议 · 数据来自公开来源，链接可点击溯源 · {D}</footer>
</div>

<button class="totop" id="totop" title="回到顶部">↑</button>

<script>{B.JS}</script>
</body>
</html>
"""
    return html


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("date", help="目标日期 YYYY-MM-DD")
    ap.add_argument("--root", default=ROOT, help="AI Signal 项目根目录")
    a = ap.parse_args()

    B = load_builder(a.root)
    html = build_4mod(B, a.date, NOTE, TAG)
    out = os.path.join(a.root, "daily", f"{a.date}-lite.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print("已生成:", out, "| 字节:", len(html.encode("utf-8")))


if __name__ == "__main__":
    main()
