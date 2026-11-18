# CLAUDE.md｜多代理人 AI 的 LLM Wiki＋教學簡報

> 給 AI：開工前依序讀 ① 本檔 ② `wiki/index.md` ③ `wiki/log.md` 最後幾筆。
> 本檔是由使用者訪談整理而成（見 `docs/01-discussion.md`）。規則與使用者當下指示衝突時，先問使用者。
> 規則有改動時，同步更新本檔並在 `wiki/log.md` 記一筆 `rule`。

---

## 1. 專案目的

- **主題**：多代理人 AI（multi-agent LLM systems）——多個 LLM 代理人分工、對話、互相檢查來完成任務。
- **兩個產出**：
  1. `wiki/`：由 AI 持續維護、互相連結的知識庫（LLM Wiki）。
  2. `slides/index.html`：以 Wiki 為**唯一知識來源**的教學 HTML 簡報。
- **簡報讀者**：用過 ChatGPT 的大學生——會用聊天 AI，但不知道 agent、多代理人是什麼。
- **學習目標**（簡報看完要會）：
  1. 說得出多代理人是什麼、和單一 AI 有什麼不同
  2. 看得懂常見的合作方式
  3. 知道它會在哪裡出錯

---

## 2. 三層架構

| 層 | 位置 | 誰寫 | 規則 |
|---|---|---|---|
| 原始資料 | `raw/` | 人放進來 | AI **只讀不改**，是事實的來源 |
| 知識頁 | `wiki/` | AI | 摘要、概念、互相連結，隨收錄更新 |
| 規則手冊 | `CLAUDE.md` | 人＋AI | 就是本檔 |

**著作權**：`raw/sources.md` 只放書目、連結、取得日期；原文內容只存在本機 `raw/_fulltext/`（已列入 `.gitignore`，不上傳）。Wiki 一律用自己的話改寫，引用原文單次不超過 15 字。

**原文怎麼取得**（2026-11-18 起）：工作環境無法直接下載論文 PDF，改用網頁擷取工具逐節讀原文，存成「逐節擷取筆記」`raw/_fulltext/<代號>.md`：保留原文章節號、所有數字與作者用語，不加外部知識。檔頭要註明擷取網址、日期與**未涵蓋的範圍**（例如被截斷的附錄）。擷取筆記不是逐字原文，寫 Wiki 時遇到擷取筆記沒寫清楚的地方，要標「（擷取未涵蓋）」而不是自己補。

---

## 3. 資料夾結構

```
multi-agent-wiki/
├── CLAUDE.md / AGENTS.md / README.md
├── index.html                  ← GitHub Pages 首頁（連到簡報與 Wiki）
├── raw/
│   ├── sources.md              ← 資料清單（代號、書目、連結）
│   └── _fulltext/              ← 全文（本機，不上傳）
├── wiki/
│   ├── index.md                ← 所有頁面目錄（AI 找頁面從這裡開始）
│   ├── log.md                  ← 只增不刪的工作紀錄
│   ├── sources/<代號>.md       ← 來源頁：一篇資料一頁
│   └── concepts/<slug>.md      ← 概念頁：一個概念一頁
├── docs/
│   ├── 01-discussion.md        ← 訪談紀錄
│   ├── workflow.md             ← 簡報的 loop／graph 設計
│   ├── run-*.md                ← 每次執行紀錄
│   └── reflection.md           ← 反思
├── slides/
│   ├── outline.md              ← 大綱（每頁要列出引用的 Wiki 頁）
│   ├── drafts/NN.md            ← 逐頁內容稿
│   └── index.html              ← 成品簡報
└── tools/                      ← 自動檢查腳本
```

---

## 4. 頁面種類與格式

### 來源頁 `wiki/sources/<代號>.md`
代號固定為：`camel`、`chatdev`、`debate`、`generative-agents`、`anthropic-research`、`mas-failures`。

```markdown
---
type: source
title: 原文標題
authors: 第一作者 et al.
year: 2023
url: https://…
ingested: YYYY-MM-DD
---
# 中文短標題（原文標題）
## 一句話摘要
## 它想解決什麼問題
## 怎麼做
## 主要發現
## 限制與注意
## 相關概念        ← 連到 concepts/ 的頁面
```

### 概念頁 `wiki/concepts/<slug>.md`
slug 用英文小寫＋連字號（例：`role-playing`、`orchestrator-worker`）。

```markdown
---
type: concept
sources: [camel, chatdev]      ← 有提到這個概念的來源代號
---
# 中文名稱（English name）
## 一句話定義
## 白話說明              ← 寫給「用過 ChatGPT 的大學生」，先比喻再細節
## 例子
## 各來源怎麼說          ← 每個來源一小段，都要標出處
## 說法不同              ← 沒有就寫「目前沒有」
## 相關概念
```

---

## 5. 出處規則（每個重點句都標）

- 格式：句尾加 `〔代號 §節〕`，例如 `〔camel §3〕`、`〔mas-failures §4.2〕`。`§` 後面寫原文的章節號或章節名。
- 概念頁引用來源，也用同樣格式（代號對應 `wiki/sources/<代號>.md`）。
- 數字（百分比、倍數、個數）必須和原文一致，並標出處；不確定就不寫。
- 「重點句」＝任何事實、數字、結論、作法描述。純轉場或比喻句不用標。
- 只寫原文有的內容；AI 自己的推論要寫成「（整理者註：…）」且不能當成來源說法。

---

## 6. 說法不同

不同來源說法不一致時，**兩邊都記**，用這個區塊，不替讀者下結論：

```markdown
> ⚠️ **說法不同**
> - A 的說法…（條件：什麼任務、怎麼量）〔代號 §節〕
> - B 的說法…（條件：…）〔代號 §節〕
```

---

## 7. 三個操作

### 收錄（ingest）——一次一篇
1. 讀 `raw/_fulltext/<代號>.md`（沒有全文就停下來問使用者）。
2. 寫來源頁。
3. 對這篇提到的每個重要概念：已有概念頁就**更新**（在「各來源怎麼說」加一段），沒有就新建。
4. 和既有頁面比對，有矛盾就加「說法不同」。
5. 更新 `wiki/index.md`；在 `wiki/log.md` 追加 `## [YYYY-MM-DD] ingest | 代號 | 新增 N 頁、更新 M 頁`。
6. 跑 `python3 tools/lint_wiki.py`，有錯先修再收下一篇。

### 提問（query）
- 只根據 Wiki 回答，引用 Wiki 頁面；Wiki 沒有的就說「Wiki 沒有」，不得用外部知識補。
- 好的回答可以存成概念頁，並記一筆 `query` 到 log。

### 健檢（lint）
- 自動：`python3 tools/lint_wiki.py`（壞連結、孤兒頁、缺出處、未知代號、front matter 缺欄位）。
- 人工：找互相矛盾但沒標「說法不同」的地方、太難懂的段落。
- 結果記一筆 `lint` 到 log。

---

## 8. 簡報規則

- 流程依 `docs/workflow.md`（loop／graph），每次執行都要寫 `docs/run-*.md`。
- **只能用 Wiki 的內容**；每頁內容稿要標引用的 Wiki 頁 `〔wiki: concepts/xxx〕`。
- 主線：從「一個人」到「一個團隊」（萬能助理 vs. 專案小組）。
- 10～12 頁；每頁一個重點、最多 5 個要點、每個要點 40 字以內。
- 風格：清爽筆記風（白底、深藍標題、圓角卡片、淡陰影；色票同第九週筆記站）。
- 單一 HTML 檔，鍵盤左右鍵翻頁、手機可滑動；只用原生 HTML／CSS／JS，外部資源只允許 Google Fonts。

---

## 9. 寫作規範

- 繁體中文、全形標點；中文與英文、數字之間加半形空格。
- 專有名詞第一次出現附英文：多代理人系統（multi-agent system）。
- 寫給用過 ChatGPT 的大學生：先講直覺或比喻，再講細節；避免沒解釋的術語。
