#!/usr/bin/env python3
"""節點 ⑦：把 slides/drafts/*.md 組成 slides/index.html（不經過 AI，成品＝內容稿）。

視覺元件（內容稿的 ```visual 區塊）：
  compare  兩欄對照：- 欄名 | 說明
  flow     流程箭頭：- 步驟 | 說明
  hub      主管＋助手：第一行是主管，其餘是助手
  debate   多個代理人互相討論：- 名稱 | 說明
  pair     兩個角色對話：- 角色 | 說明
  bars     長條圖：- 標籤 | 數值（百分比）
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DRAFTS = ROOT / "slides" / "drafts"
OUT = ROOT / "slides" / "index.html"
REPO = "https://github.com/st110211221/multi-agent-wiki/blob/main/wiki/"
TAG = re.compile(r"〔(wiki: [^〕]+|比喻)〕")
DECK_TITLE = "從一個人到一個團隊：多代理人 AI 入門"


def esc(s):
    return html.escape(s, quote=True)


def inline(s):
    """去掉出處標記、處理 **粗體**。"""
    s = esc(TAG.sub("", s).strip())
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)


def refs_of(text):
    out = []
    for t in TAG.findall(text):
        if t.startswith("wiki:"):
            for r in t[5:].split(","):
                r = r.strip()
                if r and r not in out:
                    out.append(r)
    return out


def wiki_title(ref):
    p = ROOT / "wiki" / f"{ref}.md"
    m = re.search(r"^# (.+)$", p.read_text(encoding="utf-8"), re.M)
    return re.split(r"[（(]", m.group(1))[0].strip() if m else ref


def section(text, name):
    m = re.search(rf"^## {name}\n(.*?)(?=^## |^```visual|\Z)", text, re.S | re.M)
    return m.group(1).strip() if m else ""


def parse(path):
    text = path.read_text(encoding="utf-8")
    fm = dict(re.findall(r"^(\w+):\s*(.+)$", text.split("---")[1], re.M))
    vis = re.search(r"```visual\n(.*?)```", text, re.S)
    visual = None
    if vis:
        vtype = re.search(r"^type:\s*(\w+)", vis.group(1), re.M).group(1)
        items = []
        for l in vis.group(1).splitlines():
            if l.startswith("- "):
                label, _, desc = l[2:].partition("|")
                items.append((label.strip(), desc.strip()))
        vtitle = re.search(r"^title:\s*(.+)$", vis.group(1), re.M)
        visual = {"type": vtype, "items": items, "title": vtitle.group(1).strip() if vtitle else ""}
    return {
        "no": path.stem,
        "title": fm.get("title", ""),
        "type": fm.get("type", "content"),
        "key": section(text, "重點"),
        "points": [l[2:] for l in section(text, "要點").splitlines() if l.startswith("- ")],
        "notes": section(text, "講者備註"),
        "visual": visual,
        "refs": refs_of(text),
    }


# ---------- 視覺元件 ----------
def v_compare(v):
    cols = "".join(
        f'<div class="cmp-col cmp-{i}"><div class="cmp-head">{inline(a)}</div><p>{inline(b)}</p></div>'
        for i, (a, b) in enumerate(v["items"])
    )
    return f'<div class="v-compare">{cols}</div>'


def v_flow(v):
    parts = []
    for i, (a, b) in enumerate(v["items"]):
        if i:
            parts.append('<div class="flow-arrow" aria-hidden="true">→</div>')
        parts.append(f'<div class="flow-step"><span class="flow-no">{i + 1}</span><b>{inline(a)}</b><small>{inline(b)}</small></div>')
    return f'<div class="v-flow">{"".join(parts)}</div>'


def v_hub(v):
    (boss, bdesc), workers = v["items"][0], v["items"][1:]
    ws = "".join(f'<div class="hub-worker"><b>{inline(a)}</b><small>{inline(b)}</small></div>' for a, b in workers)
    return (f'<div class="v-hub"><div class="hub-boss"><b>{inline(boss)}</b><small>{inline(bdesc)}</small></div>'
            f'<div class="hub-lines" aria-hidden="true">{"<span></span>" * len(workers)}</div>'
            f'<div class="hub-workers">{ws}</div></div>')


def v_debate(v):
    agents = "".join(f'<div class="deb-agent"><span class="deb-face">{i + 1}</span><b>{inline(a)}</b><small>{inline(b)}</small></div>'
                     for i, (a, b) in enumerate(v["items"]))
    return f'<div class="v-debate"><div class="deb-agents">{agents}</div><div class="deb-loop">⇄ 互相看答案、挑錯、修正，來回幾輪</div></div>'


def v_pair(v):
    (a1, d1), (a2, d2) = v["items"][:2]
    return (f'<div class="v-pair"><div class="pair-role"><b>{inline(a1)}</b><small>{inline(d1)}</small></div>'
            f'<div class="pair-talk" aria-hidden="true"><span>指令 →</span><span>← 解法</span></div>'
            f'<div class="pair-role"><b>{inline(a2)}</b><small>{inline(d2)}</small></div></div>')


def v_bars(v):
    rows = []
    for a, b in v["items"]:
        num = re.search(r"\d+(?:\.\d+)?", TAG.sub("", b))
        val = float(num.group()) if num else 0
        rows.append(f'<div class="bar-row"><span class="bar-label">{inline(a)}</span>'
                    f'<span class="bar-track"><span class="bar-fill" style="--w:{val:.2f}%"></span></span>'
                    f'<span class="bar-val">{inline(b)}</span></div>')
    title = f'<div class="bar-title">{esc(v["title"])}</div>' if v["title"] else ""
    return f'<div class="v-bars">{title}{"".join(rows)}</div>'


VISUALS = {"compare": v_compare, "flow": v_flow, "hub": v_hub, "debate": v_debate, "pair": v_pair, "bars": v_bars}


def render_slide(s, total):
    refs = "".join(f'<a href="{REPO}{esc(r)}.md" target="_blank" rel="noopener">{esc(wiki_title(r))}</a>' for r in s["refs"])
    footer = f'<footer class="refs">Wiki 出處：{refs}</footer>' if refs else ""
    notes = f'<aside class="notes">{inline(s["notes"])}</aside>' if s["notes"] else ""
    if s["type"] == "cover":
        sub = "".join(f"<li>{inline(p)}</li>" for p in s["points"])
        return (f'<section class="slide cover" data-no="{s["no"]}"><div class="slide-inner">'
                f'<div class="cover-tag">教學簡報・以 LLM Wiki 為知識來源</div>'
                f'<h1>{esc(s["title"])}</h1><p class="key">{inline(s["key"])}</p>'
                f'<ul class="cover-meta">{sub}</ul>{footer}{notes}</div></section>')
    pts = "".join(f"<li>{inline(p)}</li>" for p in s["points"])
    vis = VISUALS[s["visual"]["type"]](s["visual"]) if s["visual"] and s["visual"]["type"] in VISUALS else ""
    layout = "with-visual" if vis else "text-only"
    return (f'<section class="slide {s["type"]}" data-no="{s["no"]}"><div class="slide-inner">'
            f'<div class="slide-top"><span class="slide-no">{int(s["no"]):02d} / {total:02d}</span></div>'
            f'<h2>{esc(s["title"])}</h2><p class="key">{inline(s["key"])}</p>'
            f'<div class="body {layout}"><ul class="points">{pts}</ul>{f"<div class=visual>{vis}</div>" if vis else ""}</div>'
            f'{footer}{notes}</div></section>')


CSS = r"""
:root{--bg:#F6F8FB;--surface:#FFFFFF;--navy:#1E3A5F;--ink:#2A3441;--muted:#6A7686;--line:#E2E8F0;--accent:#2F6FED;
--accent-bg:#EEF4FF;--green:#23935A;--green-bg:#ECF8F1;--amber:#D99000;--amber-bg:#FFF7E6;--violet:#7C5CD6;--violet-bg:#F5F2FD;
--font:"Noto Sans TC","PingFang TC","Microsoft JhengHei",sans-serif;--shadow:0 1px 2px rgba(30,58,95,.06),0 6px 20px rgba(30,58,95,.08)}
*{box-sizing:border-box}html,body{margin:0;height:100%;background:var(--bg);color:var(--ink);font-family:var(--font)}
.deck{position:fixed;inset:0;overflow:hidden}
.slide{position:absolute;left:50%;top:50%;width:1280px;height:720px;margin:-360px 0 0 -640px;display:none}
.slide.active{display:block}
.slide-inner{position:relative;width:100%;height:100%;overflow:hidden;background:var(--surface);border-radius:20px;box-shadow:var(--shadow);padding:44px 68px 76px}
.slide-top{font-size:18px;color:var(--muted);margin-bottom:6px}
h1,h2{color:var(--navy);margin:0;line-height:1.3}h2{font-size:48px;padding-left:18px;border-left:9px solid var(--accent)}
.key{font-size:30px;line-height:1.5;color:var(--ink);background:var(--accent-bg);border-radius:14px;padding:14px 24px;margin:22px 0 26px}
.body{display:flex;gap:36px;align-items:flex-start}.body.with-visual .points{flex:0 0 55%}.body .visual{flex:1;min-width:0}
.points{margin:0;padding:0;list-style:none}.points li{position:relative;font-size:28px;line-height:1.5;padding:8px 0 8px 34px}
.points li::before{content:"";position:absolute;left:4px;top:23px;width:14px;height:14px;border-radius:50%;background:var(--accent)}
.points strong{color:var(--navy)}
.refs{position:absolute;left:68px;right:68px;bottom:22px;font-size:17px;color:var(--muted);border-top:1px solid var(--line);padding-top:10px}
.refs a{color:var(--accent);text-decoration:none;margin-right:14px}.refs a:hover{text-decoration:underline}
.notes{display:none}.show-notes .notes{display:block;position:absolute;right:20px;bottom:56px;max-width:520px;background:#FFFBEA;border:1px solid #F1D98A;border-radius:10px;padding:10px 14px;font-size:15px;line-height:1.6}
/* 封面 */
.cover .slide-inner{display:flex;flex-direction:column;justify-content:center;padding:64px 96px 80px;background:linear-gradient(135deg,#fff 60%,var(--accent-bg))}
.cover h1{font-size:60px}.cover .key{font-size:28px;background:none;padding:0;color:var(--muted)}
.cover-tag{display:inline-block;align-self:flex-start;background:var(--accent);color:#fff;border-radius:999px;padding:6px 18px;font-size:18px;margin-bottom:22px}
.cover-meta{list-style:none;padding:0;margin:8px 0 0;font-size:24px;color:var(--ink);line-height:1.8}
/* 總結 */
.summary .points li{font-size:30px}
/* 視覺：compare */
.v-compare{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.cmp-col{border-radius:14px;padding:18px 20px;background:var(--bg);border:2px solid var(--line)}
.cmp-col.cmp-1{background:var(--accent-bg);border-color:var(--accent)}
.cmp-head{font-size:27px;font-weight:700;color:var(--navy);margin-bottom:10px}.cmp-col p{margin:0;font-size:23px;line-height:1.55}
/* flow */
.v-flow{display:flex;align-items:stretch;gap:8px;flex-wrap:wrap}
.flow-step{flex:1 1 120px;background:var(--green-bg);border:2px solid var(--green);border-radius:14px;padding:14px 12px;text-align:center;display:flex;flex-direction:column;gap:6px}
.flow-step b{font-size:25px;color:var(--navy)}.flow-step small{font-size:19px;color:var(--muted);line-height:1.45}
.flow-no{display:inline-block;margin:0 auto;width:30px;height:30px;line-height:30px;border-radius:50%;background:var(--green);color:#fff;font-weight:700}
.flow-arrow{align-self:center;font-size:28px;color:var(--green);font-weight:700}
/* hub */
.v-hub{display:flex;flex-direction:column;align-items:center}
.hub-boss{background:var(--navy);color:#fff;border-radius:14px;padding:12px 26px;text-align:center}
.hub-boss b{font-size:26px;display:block}.hub-boss small{font-size:19px;opacity:.85}
.hub-lines{display:flex;justify-content:space-around;width:90%;height:34px}.hub-lines span{width:2px;background:var(--accent);opacity:.6}
.hub-workers{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;width:100%}
.hub-worker{background:var(--accent-bg);border:2px solid var(--accent);border-radius:12px;padding:10px;text-align:center}
.hub-worker b{display:block;font-size:23px;color:var(--navy)}.hub-worker small{font-size:18px;color:var(--muted)}
/* debate */
.deb-agents{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.deb-agent{background:var(--violet-bg);border:2px solid var(--violet);border-radius:14px;padding:12px;text-align:center}
.deb-face{display:inline-block;width:36px;height:36px;line-height:36px;border-radius:50%;background:var(--violet);color:#fff;font-weight:700;margin-bottom:6px}
.deb-agent b{display:block;font-size:23px;color:var(--navy)}.deb-agent small{font-size:18px;color:var(--muted);line-height:1.4}
.deb-loop{margin-top:16px;text-align:center;font-size:22px;color:var(--violet);font-weight:700;border:2px dashed var(--violet);border-radius:999px;padding:8px}
/* pair */
.v-pair{display:flex;align-items:center;gap:10px}
.pair-role{flex:1;background:var(--amber-bg);border:2px solid var(--amber);border-radius:14px;padding:16px;text-align:center}
.pair-role b{display:block;font-size:24px;color:var(--navy)}.pair-role small{font-size:19px;color:var(--muted);line-height:1.45}
.pair-talk{display:flex;flex-direction:column;gap:8px;font-size:20px;color:var(--amber);font-weight:700;white-space:nowrap}
/* bars */
.v-bars{background:var(--bg);border-radius:14px;padding:20px 22px}.bar-title{font-size:21px;color:var(--muted);margin-bottom:12px}
.bar-row{display:grid;grid-template-columns:150px 1fr 96px;gap:12px;align-items:center;margin:14px 0}
.bar-label{font-size:22px;color:var(--navy);font-weight:700}.bar-val{font-size:22px;text-align:right;font-variant-numeric:tabular-nums}
.bar-track{height:28px;background:#fff;border-radius:999px;overflow:hidden;border:1px solid var(--line)}
.bar-fill{display:block;height:100%;width:var(--w);background:var(--accent);border-radius:999px}
/* 控制列 */
.controls{position:fixed;right:18px;bottom:8px;display:flex;gap:8px;z-index:5}
.controls button{border:1px solid var(--line);background:#fff;border-radius:10px;padding:4px 14px;font-size:16px;cursor:pointer;color:var(--navy)}
.progress{position:fixed;left:0;top:0;height:4px;background:var(--accent);transition:width .2s;z-index:5}
.hint{position:fixed;left:18px;bottom:12px;font-size:13px;color:var(--muted)}
/* 窄螢幕：改成可上下捲動的卡片 */
.narrow .deck{overflow-y:auto;-webkit-overflow-scrolling:touch}
.narrow .slide{position:static;width:auto;height:auto;margin:12px}
.narrow .slide-inner{height:auto;min-height:calc(100vh - 80px);padding:22px 18px 70px;border-radius:14px}
.narrow h2{font-size:26px;border-left-width:6px;padding-left:10px}.narrow .cover h1{font-size:32px}
.narrow .key{font-size:18px;padding:10px 14px;margin:14px 0}.narrow .cover .key{font-size:18px}
.narrow .body{flex-direction:column;gap:16px}.narrow .body.with-visual .points{flex:none}
.narrow .points li{font-size:17px;padding-left:24px}.narrow .points li::before{top:15px;width:10px;height:10px}
.narrow .cmp-head{font-size:19px}.narrow .cmp-col p,.narrow .flow-step small,.narrow .pair-role small{font-size:15px}.narrow .flow-step b,.narrow .pair-role b,.narrow .hub-worker b,.narrow .deb-agent b{font-size:18px}.narrow .hub-boss b{font-size:19px}.narrow .deb-loop{font-size:16px}
.narrow .refs{position:static;margin-top:20px;font-size:13px}.narrow .slide-inner{padding-bottom:24px}.narrow .cover .slide-inner{padding:30px 22px 70px}
.narrow .cover-meta{font-size:16px}.narrow .cover-tag{font-size:14px}
.narrow .v-compare,.narrow .deb-agents,.narrow .hub-workers{grid-template-columns:1fr}
.narrow .v-flow{flex-direction:column}.narrow .flow-arrow{transform:rotate(90deg)}
.narrow .v-pair{flex-direction:column}.narrow .bar-row{grid-template-columns:96px 1fr 60px}.narrow .bar-label,.narrow .bar-val{font-size:14px}
.narrow .hint{display:none}
"""

JS = r"""
(function(){
  var slides=[].slice.call(document.querySelectorAll('.slide')),cur=0,bar=document.querySelector('.progress');
  function mode(){var n=innerWidth<760||innerWidth<innerHeight;document.body.classList.toggle('narrow',n);
    slides.forEach(function(s){s.style.transform=n?'':'scale('+Math.min((innerWidth-32)/1280,(innerHeight-88)/720)+')';s.style.marginTop=n?'':'-388px';});}
  function show(i){cur=Math.max(0,Math.min(slides.length-1,i));slides.forEach(function(s,k){s.classList.toggle('active',k===cur);});
    bar.style.width=((cur+1)/slides.length*100)+'%';if(location.hash!=='#'+(cur+1))history.replaceState(null,'','#'+(cur+1));
    var d=document.querySelector('.deck');if(d)d.scrollTop=0;}
  window.deck={show:show,get index(){return cur},get total(){return slides.length}};
  document.addEventListener('keydown',function(e){
    if(['ArrowRight','PageDown',' '].indexOf(e.key)>=0){e.preventDefault();show(cur+1);}
    else if(['ArrowLeft','PageUp'].indexOf(e.key)>=0){e.preventDefault();show(cur-1);}
    else if(e.key==='n'||e.key==='N'){document.body.classList.toggle('show-notes');}});
  document.getElementById('prev').onclick=function(){show(cur-1)};document.getElementById('next').onclick=function(){show(cur+1)};
  var x0=null;document.addEventListener('touchstart',function(e){x0=e.touches[0].clientX},{passive:true});
  document.addEventListener('touchend',function(e){if(x0===null)return;var dx=e.changedTouches[0].clientX-x0;
    if(Math.abs(dx)>60)show(cur+(dx<0?1:-1));x0=null;},{passive:true});
  addEventListener('resize',mode);mode();show((parseInt(location.hash.slice(1),10)||1)-1);
})();
"""


def main():
    drafts = [parse(p) for p in sorted(DRAFTS.glob("*.md"))]
    total = len(drafts)
    body = "\n".join(render_slide(s, total) for s in drafts)
    page = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(DECK_TITLE)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700&display=swap">
<style>{CSS}</style>
</head>
<body>
<!-- 本檔由 tools/build_slides.py 從 slides/drafts/*.md 產生，請勿手改 -->
<div class="progress"></div>
<main class="deck">
{body}
</main>
<div class="controls"><button id="prev" aria-label="上一頁">←</button><button id="next" aria-label="下一頁">→</button></div>
<div class="hint">← → 翻頁・N 顯示講者備註</div>
<script>{JS}</script>
</body>
</html>
"""
    OUT.write_text(page, encoding="utf-8")
    print(f"── 組成 HTML：{total} 頁 → {OUT.relative_to(ROOT)}")
    print(json.dumps({s['no']: s['refs'] for s in drafts}, ensure_ascii=False))


if __name__ == "__main__":
    main()
