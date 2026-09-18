# -*- coding: utf-8 -*-
"""从 AI信号站 payload.json 抽取可读文本，供人工策展每日简报使用。

用法：
  python dump_payload.py [--payload PATH] [--out PATH]
默认 payload 路径：~/.ai-signal/payload/payload.json
不传 --out 则直接打印到 stdout。

输出按 4 个数据源分节：X / 播客 / 官方博客 / arXiv，
每条带可点击链接，便于撰写时直接复制来源 URL。
"""
import json
import os
import argparse

DEFAULT_PAYLOAD = os.path.join(os.path.expanduser("~"), ".ai-signal", "payload", "payload.json")


def dump(payload_path, out_path=None):
    with open(payload_path, encoding="utf-8") as f:
        p = json.load(f)

    ga = p.get("generated_at", "?")
    lines = [f"# AI信号站 payload 转储 (generated_at={ga})\n"]

    # ---- X / Twitter ----
    lines.append("## X / Twitter")
    for b in p.get("x", []) or []:
        name = b.get("name") or b.get("handle") or "?"
        handle = b.get("handle") or "?"
        for t in b.get("tweets", []) or []:
            txt = (t.get("text") or "").replace("\n", " ")
            url = t.get("url") or ""
            eng = t.get("engagement_score")
            tag = f" [互动 {eng}]" if eng is not None else ""
            lines.append(f"- [{name} (@{handle})]{tag} {txt}\n  {url}")

    # ---- 播客 ----
    lines.append("\n## 播客")
    for ep in p.get("podcasts", []) or []:
        ch = ep.get("channel") or "?"
        title = ep.get("title") or "?"
        link = ep.get("link") or ""
        desc = (ep.get("description") or "").replace("\n", " ")
        lines.append(f"- [{ch}] {title}\n  {link}\n  {desc}")

    # ---- 官方博客 / 文章 ----
    lines.append("\n## 官方博客 / 文章")
    for a in p.get("articles", []) or []:
        src = a.get("source_name") or a.get("source") or "?"
        title = a.get("title") or "?"
        url = a.get("url") or ""
        summary = (a.get("summary") or "").replace("\n", " ")
        lines.append(f"- [{src}] {title}\n  {url}\n  {summary}")

    # ---- arXiv 论文 ----
    lines.append("\n## arXiv 论文")
    for pa in p.get("papers", []) or []:
        aid = pa.get("arxiv_id") or "?"
        title = pa.get("title") or "?"
        abs_url = pa.get("abs_url") or ""
        authors = ", ".join((pa.get("authors") or [])[:3])
        abst = (pa.get("abstract") or "").replace("\n", " ")
        lines.append(f"- [{aid}] {title}\n  {abs_url}\n  作者: {authors}\n  {abst[:300]}")

    text = "\n".join(lines)
    if out_path:
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"已写出: {out_path} | {len(text.encode('utf-8'))} 字节")
    else:
        print(text)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--payload", default=DEFAULT_PAYLOAD)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    dump(a.payload, a.out)
