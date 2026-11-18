#!/usr/bin/env python3
"""Wiki 健檢（lint）：依 CLAUDE.md §4–§7 檢查 wiki/ 的結構與出處。

用法：python3 tools/lint_wiki.py [--quiet]
檢查項目：
  E1 front matter 缺欄位
  E2 出處代號不存在（〔代號 §節〕的代號必須是 wiki/sources/ 裡的檔名）
  E3 Markdown 連結壞掉
  E4 重點段落沒有出處（來源頁：怎麼做／主要發現／限制與注意；概念頁：各來源怎麼說）
  E5 概念頁 front matter 的 sources 和內文實際引用不一致
  E6 缺少必要章節
  W1 孤兒頁（沒有任何頁面連到它）
  W2 來源頁沒有被任何概念頁引用
回傳碼：有 E 類錯誤時為 1。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
CITE = re.compile(r"〔([a-z0-9-]+) §[^〕]+〕")
LINK = re.compile(r"\[[^\]]*\]\(([^)#\s]+)(?:#[^)]*)?\)")

SOURCE_FIELDS = ["type", "title", "authors", "year", "url", "ingested"]
CONCEPT_FIELDS = ["type", "sources"]
SOURCE_SECTIONS = ["一句話摘要", "它想解決什麼問題", "怎麼做", "主要發現", "限制與注意", "相關概念"]
CONCEPT_SECTIONS = ["一句話定義", "白話說明", "例子", "各來源怎麼說", "說法不同", "相關概念"]
SOURCE_CITED_SECTIONS = ["怎麼做", "主要發現", "限制與注意"]
CONCEPT_CITED_SECTIONS = ["各來源怎麼說", "例子"]  # v2：例子也要有出處，或標（整理者舉例）


def front_matter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.split("←")[0].strip()
    return fm, text[m.end():]


def sections(body):
    out, cur = {}, None
    for line in body.splitlines():
        h = re.match(r"^##\s+(.+?)\s*$", line)
        if h:
            cur = h.group(1)
            out[cur] = []
        elif cur:
            out[cur].append(line)
    return out


def paragraphs(lines):
    """把章節拆成段落／清單項目，忽略空行、引言標頭、表頭分隔線。"""
    items, buf = [], []
    for line in lines + [""]:
        s = line.strip()
        if not s or s.startswith("|---"):
            if buf:
                items.append(" ".join(buf))
                buf = []
            continue
        if re.match(r"^([-*]|\d+\.)\s", s) or s.startswith(">"):
            if buf:
                items.append(" ".join(buf))
            buf = [s]
        else:
            buf.append(s)
    return [i for i in items if not re.fullmatch(r">?\s*(⚠️\s*)?\**說法不同\**\s*", i)]


def main():
    quiet = "--quiet" in sys.argv
    errors, warns = [], []
    pages = sorted(WIKI.rglob("*.md"))
    source_ids = {p.stem for p in (WIKI / "sources").glob("*.md")}
    inbound = {p: 0 for p in pages}
    cited_sources = set()

    for p in pages:
        rel = p.relative_to(ROOT)
        text = p.read_text(encoding="utf-8")
        fm, body = front_matter(text)

        for m in LINK.finditer(text):
            target = m.group(1)
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            dest = (p.parent / target).resolve()
            if not dest.exists():
                errors.append(f"E3 {rel}: 連結壞掉 → {target}")
            elif dest in inbound and dest != p:
                inbound[dest] += 1

        cites = set(CITE.findall(text))
        for c in cites:
            if c not in source_ids:
                errors.append(f"E2 {rel}: 出處代號不存在 〔{c} …〕")

        kind = fm.get("type")
        if p.parent.name == "sources":
            need, secs, cited = SOURCE_FIELDS, SOURCE_SECTIONS, SOURCE_CITED_SECTIONS
        elif p.parent.name == "concepts":
            need, secs, cited = CONCEPT_FIELDS, CONCEPT_SECTIONS, CONCEPT_CITED_SECTIONS
            cited_sources |= cites
            declared = set(re.findall(r"[a-z0-9-]+", fm.get("sources", "")))
            if declared != cites:
                errors.append(f"E5 {rel}: front matter sources={sorted(declared)}，內文引用={sorted(cites)}")
        else:
            continue  # index.md、log.md 不檢查格式

        for f in need:
            if not fm.get(f):
                errors.append(f"E1 {rel}: front matter 缺 {f}")
        secmap = sections(body)
        for s in secs:
            if s not in secmap:
                errors.append(f"E6 {rel}: 缺少章節「## {s}」")
        for s in cited:
            for item in paragraphs(secmap.get(s, [])):
                if not CITE.search(item) and not any(k in item for k in ("整理者註", "擷取未涵蓋", "整理者舉例")):
                    errors.append(f"E4 {rel} §{s}: 沒有出處 → {item[:40]}…")

    index = WIKI / "index.md"
    for p, n in inbound.items():
        if p.name in ("index.md", "log.md"):
            continue
        if n == 0:
            warns.append(f"W1 {p.relative_to(ROOT)}: 孤兒頁（沒有頁面連到它）")
    for sid in sorted(source_ids - cited_sources):
        warns.append(f"W2 wiki/sources/{sid}.md: 還沒有任何概念頁引用這個來源")

    n_src = len(source_ids)
    n_con = len(list((WIKI / "concepts").glob("*.md")))
    for line in errors + warns:
        print(line)
    if not quiet or errors or warns:
        print(f"── lint 結果：來源頁 {n_src}、概念頁 {n_con}；錯誤 {len(errors)}、警告 {len(warns)}")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
