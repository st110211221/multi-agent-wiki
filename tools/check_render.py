#!/usr/bin/env python3
"""關卡 ⑧：成品檢查。用無頭瀏覽器實際打開 slides/index.html。

檢查：
  R1 桌機 1280×720：每頁內容沒有超出投影片（scrollHeight > clientHeight 就算跑版）
  R2 手機 375×812：每頁沒有水平捲動
  R3 方向鍵翻頁：按 → 會到下一頁、按 ← 會回上一頁
  R4 沒有 JavaScript 錯誤
用法：python3 tools/check_render.py [截圖資料夾]
需要：pip install playwright，以及系統上的 Chrome（預設 /usr/bin/google-chrome）。
"""
import asyncio
import sys
from pathlib import Path

from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parent.parent
PAGE = (ROOT / "slides" / "index.html").as_uri()
SHOTS = Path(sys.argv[1]) if len(sys.argv) > 1 else None


async def main():
    problems = []
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
        for label, vp in [("桌機", (1280, 720)), ("手機", (375, 812))]:
            pg = await b.new_page(viewport={"width": vp[0], "height": vp[1]})
            errs = []
            pg.on("pageerror", lambda e: errs.append(str(e)))
            await pg.route("**/fonts.googleapis.com/**", lambda r: r.fulfill(body="", content_type="text/css"))
            await pg.goto(PAGE)
            await pg.wait_for_timeout(300)
            total = await pg.evaluate("deck.total")
            for i in range(total):
                await pg.evaluate(f"deck.show({i})")
                await pg.wait_for_timeout(60)
                m = await pg.evaluate("""() => {
                    const s = document.querySelector('.slide.active .slide-inner');
                    return {no: s.parentElement.dataset.no, sh: s.scrollHeight, ch: s.clientHeight,
                            sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth};
                }""")
                if label == "桌機" and m["sh"] > m["ch"] + 1:
                    problems.append(f"R1 {label} 第 {m['no']} 頁跑版：內容高 {m['sh']}px > 投影片 {m['ch']}px（超出 {m['sh'] - m['ch']}px）")
                if label == "手機" and m["sw"] > m["cw"] + 1:
                    problems.append(f"R2 {label} 第 {m['no']} 頁水平溢出：{m['sw']}px > {m['cw']}px")
                if SHOTS:
                    SHOTS.mkdir(parents=True, exist_ok=True)
                    await pg.screenshot(path=str(SHOTS / f"{'desk' if label == '桌機' else 'mobile'}-{m['no']}.png"),
                                        full_page=(label == "手機"))
            if label == "桌機":
                await pg.evaluate("deck.show(0)")
                await pg.keyboard.press("ArrowRight")
                a = await pg.evaluate("deck.index")
                await pg.keyboard.press("ArrowLeft")
                c = await pg.evaluate("deck.index")
                if (a, c) != (1, 0):
                    problems.append(f"R3 方向鍵翻頁異常：→ 後在第 {a + 1} 頁、← 後在第 {c + 1} 頁")
            for e in errs:
                problems.append(f"R4 {label} JavaScript 錯誤：{e}")
            await pg.close()
        await b.close()
    for line in problems:
        print("✗", line)
    print(f"── 成品檢查：{total} 頁，問題 {len(problems)} 個")
    sys.exit(1 if problems else 0)


asyncio.run(main())
