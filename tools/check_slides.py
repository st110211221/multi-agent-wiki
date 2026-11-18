#!/usr/bin/env python3
"""關卡 ⑥（自動部分）：逐頁檢查內容稿 slides/drafts/NN.md。

內容稿格式：
---
slide: 02
title: 頁面標題
type: cover | content | summary
---
## 重點
一句話〔wiki: concepts/xxx〕
## 要點
- 要點文字〔wiki: concepts/xxx〕
- 純比喻的句子〔比喻〕
```visual
type: bars | compare | flow | hub | debate | pair | none
- 標籤 | 數值或說明〔wiki: concepts/xxx〕
```
## 講者備註
（不檢查字數）

用法：python3 tools/check_slides.py [NN ...]   （不給就檢查全部）
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DRAFTS = ROOT / "slides" / "drafts"
TAG = re.compile(r"〔(wiki: [^〕]+|比喻)〕")
NUM = re.compile(r"\d[\d,]*(?:\.\d+)?")
MAX_POINTS, MAX_CHARS = 5, 40
ABSOLUTE = ["一定", "所有", "永遠", "完全", "絕對", "必定", "只", "都"]
SYSTEMS = ["ChatDev", "CAMEL", "MetaGPT", "GPT-Engineer", "Anthropic", "Claude", "Generative Agents", "AG2", "Bard", "ChatGPT", "MMLU", "GSM8K"]
WARNINGS = []


def norm(n):
    n = n.replace(",", "")
    return (n.rstrip("0").rstrip(".") or "0") if "." in n else n


def wiki_numbers(ref, cache={}):
    if ref not in cache:
        p = ROOT / "wiki" / f"{ref}.md"
        cache[ref] = {norm(x) for x in NUM.findall(p.read_text(encoding="utf-8"))} if p.exists() else None
    return cache[ref]


def section(text, name):
    m = re.search(rf"^## {name}\n(.*?)(?=^## |^```visual|\Z)", text, re.S | re.M)
    return m.group(1) if m else ""


def check_line(no, kind, line, errors, length_limit=True):
    tags = TAG.findall(line)
    plain = TAG.sub("", line).strip()
    if not tags:
        errors.append(f"{no} {kind}：沒有出處標記 → {plain[:30]}")
        return
    if length_limit and len(plain) > MAX_CHARS:
        errors.append(f"{no} {kind}：{len(plain)} 字，超過 {MAX_CHARS} 字 → {plain[:30]}…")
    refs = [t[5:].strip() for t in tags if t.startswith("wiki:")]
    refs = [r.strip() for ref in refs for r in ref.split(",")]
    for r in refs:
        if wiki_numbers(r) is None:
            errors.append(f"{no} {kind}：Wiki 頁 {r} 不存在")
            return
    nums = [norm(n) for n in NUM.findall(plain)]
    hits = [w for w in ABSOLUTE if w in plain]
    if hits:
        WARNINGS.append(f"{no} {kind}：絕對用語 {hits}，請對照 Wiki 確認沒有說過頭 → {plain[:30]}")
    for n in nums:
        for r in refs:
            page = ROOT / "wiki" / f"{r}.md"
            lines = [l for l in page.read_text(encoding="utf-8").splitlines() if n in {norm(x) for x in NUM.findall(l)}]
            named = {sname for l in lines for sname in SYSTEMS if sname in l}
            if named and not any(sname in plain for sname in named):
                WARNINGS.append(f"{no} {kind}：數字「{n}」在 Wiki 裡屬於 {sorted(named)}，簡報沒寫出是哪個系統，可能過度概括 → {plain[:30]}")
    if nums and not refs:
        errors.append(f"{no} {kind}：有數字卻只標〔比喻〕→ {plain[:30]}")
    for n in nums:
        if refs and not any(n in wiki_numbers(r) for r in refs):
            errors.append(f"{no} {kind}：數字「{n}」在 {refs} 找不到 → {plain[:30]}")


def check(path):
    errors = []
    text = path.read_text(encoding="utf-8")
    no = path.stem
    fm = dict(re.findall(r"^(\w+):\s*(.+)$", text.split("---")[1], re.M)) if text.startswith("---") else {}
    if not fm.get("title"):
        errors.append(f"{no}：缺 title")
    key = [l for l in section(text, "重點").splitlines() if l.strip()]
    if len(key) != 1:
        errors.append(f"{no}：「重點」要剛好一句")
    for l in key:
        check_line(no, "重點", l, errors)
    points = [l[2:] for l in section(text, "要點").splitlines() if l.startswith("- ")]
    if fm.get("type", "content") == "content" and not points:
        errors.append(f"{no}：內容頁沒有要點")
    if len(points) > MAX_POINTS:
        errors.append(f"{no}：要點 {len(points)} 個，超過 {MAX_POINTS} 個")
    for p in points:
        check_line(no, "要點", p, errors)
    vis = re.search(r"```visual\n(.*?)```", text, re.S)
    if vis:
        for l in vis.group(1).splitlines():
            if l.startswith("- "):
                check_line(no, "圖", l[2:], errors, length_limit=False)
    return errors


def main():
    args = sys.argv[1:]
    d = DRAFTS
    if args and args[0] == "--dir":
        d, args = Path(args[1]), args[2:]
    wanted = args
    files = sorted(d.glob("*.md"))
    if wanted:
        files = [f for f in files if f.stem in wanted]
    total = []
    for f in files:
        errs = check(f)
        print(f"{'✓' if not errs else '✗'} {f.stem}" + ("" if not errs else f"（{len(errs)} 個問題）"))
        for e in errs:
            print("   ", e)
        total += errs
    for w in dict.fromkeys(WARNINGS):
        print("  ⚠", w)
    print(f"── 逐頁檢查：{len(files)} 頁，問題 {len(total)} 個，警告 {len(dict.fromkeys(WARNINGS))} 個（警告交給審稿判斷）")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
