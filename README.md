# 多代理人 AI：LLM Wiki＋教學 HTML 簡報

生成式 AI 第十週作業。先用「先討論、後生成」建立一個 **多代理人 AI** 主題的 LLM Wiki（收錄 6 篇資料），再只用這個 Wiki 當知識來源，透過有檢查關卡的 loop／graph 流程，做出一份教學 HTML 簡報。

- **教學簡報**：https://st110211221.github.io/multi-agent-wiki/slides/
- **專案首頁**：https://st110211221.github.io/multi-agent-wiki/

## 專案導覽

| 想看什麼 | 檔案 |
|---|---|
| 建 Wiki 前的訪談（先討論） | [docs/01-discussion.md](docs/01-discussion.md) |
| Wiki 規則（由訪談整理） | [CLAUDE.md](CLAUDE.md) |
| Wiki 目錄 | [wiki/index.md](wiki/index.md) |
| Wiki 工作紀錄（收錄、健檢、修正） | [wiki/log.md](wiki/log.md) |
| 簡報流程設計 v2（含流程圖） | [docs/workflow.md](docs/workflow.md)（v1：[workflow-v1.md](docs/workflow-v1.md)） |
| 執行紀錄 | [docs/run-1.md](docs/run-1.md)、[docs/run-2.md](docs/run-2.md) |
| 反思 | [docs/reflection.md](docs/reflection.md) |
| 簡報大綱與逐頁內容稿 | [slides/outline.md](slides/outline.md)、[slides/drafts/](slides/drafts/) |
| 自動檢查工具 | [tools/](tools/) |

## 收錄的資料

| 代號 | 資料 |
|---|---|
| camel | Li et al. (2023). CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society |
| chatdev | Qian et al. (2023). ChatDev: Communicative Agents for Software Development |
| debate | Du et al. (2023). Improving Factuality and Reasoning in Language Models through Multiagent Debate |
| generative-agents | Park et al. (2023). Generative Agents: Interactive Simulacra of Human Behavior |
| anthropic-research | Anthropic (2025). How we built our multi-agent research system |
| mas-failures | Cemri et al. (2025). Why Do Multi-Agent LLM Systems Fail? |

原文有著作權，repo 只放書目與連結（[raw/sources.md](raw/sources.md)）；逐節擷取筆記只留在本機。

## 檢查工具

```bash
python3 tools/lint_wiki.py      # Wiki 健檢：格式、出處、連結、例子
python3 tools/check_numbers.py  # Wiki 數字和原文擷取筆記一致（需本機 raw/_fulltext）
python3 tools/check_outline.py  # 大綱：頁數、目標、事實片段在 Wiki 裡、術語在名詞表
python3 tools/check_slides.py   # 逐頁：要點數與字數、出處、數字、絕對用語、過度概括
python3 tools/build_slides.py   # 內容稿 → slides/index.html
python3 tools/check_render.py   # 無頭瀏覽器檢查跑版、翻頁、JS 錯誤（需 playwright）
```
