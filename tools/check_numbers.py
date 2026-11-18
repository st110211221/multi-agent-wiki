#!/usr/bin/env python3
"""數字核對：Wiki（或簡報稿）裡每個帶出處的段落，其中的數字必須出現在被引用來源的擷取筆記裡。

用法：
  python3 tools/check_numbers.py            # 檢查 wiki/
  python3 tools/check_numbers.py slides/drafts   # 檢查其他資料夾
需要本機的 raw/_fulltext/（不上傳），所以只能在本機執行。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw" / "_fulltext"
CITE = re.compile(r"〔([a-z0-9-]+) §[^〕]+〕")
NUM = re.compile(r"\d[\d,]*(?:\.\d+)?")


def norm(n):
    n = n.replace(",", "")
    if "." in n:
        n = n.rstrip("0").rstrip(".") or "0"
    return n


def raw_numbers(sid, cache={}):
    if sid not in cache:
        p = RAW / f"{sid}.md"
        cache[sid] = {norm(x) for x in NUM.findall(p.read_text(encoding="utf-8"))} if p.exists() else None
    return cache[sid]


def main():
    target = ROOT / (sys.argv[1] if len(sys.argv) > 1 else "wiki")
    problems, checked = [], 0
    for p in sorted(target.rglob("*.md")):
        if p.name in ("index.md", "log.md"):
            continue
        text = re.sub(r"^---\n.*?\n---\n", "", p.read_text(encoding="utf-8"), flags=re.S)
        for i, line in enumerate(text.splitlines(), 1):
            sids = CITE.findall(line)
            if not sids:
                continue
            body = CITE.sub("", line)
            body = re.sub(r"FM-\d\.\d|§[\w.]+|\]\([^)]*\)", "", body)  # 失敗模式代號、章節號、連結不算數字
            nums = [norm(n) for n in NUM.findall(body)]
            for n in nums:
                checked += 1
                pools = [raw_numbers(s) for s in sids]
                if any(pool is None for pool in pools):
                    problems.append(f"{p.relative_to(ROOT)}:{i} 找不到來源擷取筆記 {sids}")
                    break
                if not any(n in pool for pool in pools):
                    problems.append(f"{p.relative_to(ROOT)}:{i} 數字「{n}」不在 {sids} 的擷取筆記裡 → {line.strip()[:50]}…")
    for line in problems:
        print(line)
    print(f"── 數字核對：檢查 {checked} 個數字，有問題 {len(problems)} 個")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
