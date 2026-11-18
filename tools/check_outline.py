#!/usr/bin/env python3
"""關卡 ③：大綱自動檢查（docs/workflow.md）。

slides/outline.md 格式：
## 01｜頁面標題
- 類型：封面／內容／總結
- 重點：這頁要讓觀眾記住的一句話
- 目標：0（不對應）／1／2／3（對應 CLAUDE.md 的學習目標，可多個，用逗號）
- 出處：concepts/xxx, sources/yyy
- 事實：「要用的 Wiki 原句片段」〔wiki: concepts/xxx〕   ← v2：可多行；「」裡的字必須真的出現在該 Wiki 頁
- 術語：prompt, token                                  ← v2：這頁第一次出現的術語，必須收在 wiki/glossary.md
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def parse(path):
    slides, cur = [], None
    for line in path.read_text(encoding="utf-8").splitlines():
        h = re.match(r"^##\s+(\d+)｜(.+)$", line)
        if h:
            cur = {"no": h.group(1), "title": h.group(2).strip(), "fields": {}, "facts": [], "terms": []}
            slides.append(cur)
            continue
        f = re.match(r"^-\s*(類型|重點|目標|出處|事實|術語)：\s*(.*)$", line)
        if f and cur:
            if f.group(1) == "事實":
                cur["facts"].append(f.group(2).strip())
            elif f.group(1) == "術語":
                cur["terms"] += [t.strip() for t in re.split(r"[,，、]", f.group(2)) if t.strip()]
            else:
                cur["fields"][f.group(1)] = f.group(2).strip()
    return slides


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "slides" / "outline.md"
    slides = parse(path)
    errors = []
    if not 10 <= len(slides) <= 12:
        errors.append(f"頁數 {len(slides)}，規定 10～12 頁")
    goals_hit = set()
    for s in slides:
        tag = f"{s['no']}｜{s['title']}"
        f = s["fields"]
        for k in ("類型", "重點", "目標", "出處"):
            if not f.get(k):
                errors.append(f"{tag}：缺「{k}」")
        if len(f.get("重點", "")) > 40:
            errors.append(f"{tag}：重點超過 40 字（{len(f['重點'])} 字）")
        for g in re.findall(r"\d", f.get("目標", "")):
            goals_hit.add(g)
        refs = [r.strip() for r in f.get("出處", "").split(",") if r.strip()]
        if f.get("類型") == "內容" and not refs:
            errors.append(f"{tag}：內容頁沒有 Wiki 出處")
        for r in refs:
            if not (ROOT / "wiki" / f"{r}.md").exists():
                errors.append(f"{tag}：出處 {r} 不存在")
    glossary = (ROOT / "wiki" / "glossary.md")
    gloss = glossary.read_text(encoding="utf-8") if glossary.exists() else ""
    squash = lambda t: re.sub(r"\s+", "", t)
    for s in slides:
        tag = f"{s['no']}｜{s['title']}"
        if s["fields"].get("類型") == "內容" and not s["facts"]:
            errors.append(f"{tag}：內容頁沒有列出要用的事實（v2）")
        for fact in s["facts"]:
            m = re.match(r"「(.+?)」〔wiki: ([^〕]+)〕", fact)
            if not m:
                errors.append(f"{tag}：事實格式不對 → {fact[:30]}")
                continue
            anchor, ref = m.group(1), m.group(2).strip()
            page = ROOT / "wiki" / f"{ref}.md"
            if not page.exists():
                errors.append(f"{tag}：事實的出處 {ref} 不存在")
            elif squash(anchor) not in squash(page.read_text(encoding="utf-8")):
                errors.append(f"{tag}：Wiki 缺資料——「{anchor}」在 {ref} 找不到 → 先回 Wiki 補")
        for t in s["terms"]:
            if not re.search(rf"^## .*{re.escape(t)}", gloss, re.M | re.I):
                errors.append(f"{tag}：術語「{t}」不在 wiki/glossary.md")
    for g in ("1", "2", "3"):
        if g not in goals_hit:
            errors.append(f"學習目標 {g} 沒有任何一頁負責")
    for e in errors:
        print("✗", e)
    print(f"── 大綱檢查：{len(slides)} 頁，問題 {len(errors)} 個")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
