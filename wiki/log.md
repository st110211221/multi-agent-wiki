# Wiki 工作紀錄（只增不刪）

> 格式：`## [日期] 動作 | 對象 | 摘要`。動作：discuss、rule、ingest、lint、query、slides。

## [2026-11-18] discuss | 建 Wiki 前訪談 | 9 題，結果見 docs/01-discussion.md，整理成 CLAUDE.md

## [2026-11-18] rule | 原文取得方式 | 工作環境無法下載 PDF，改存「逐節擷取筆記」；新增 tools/lint_wiki.py 與 tools/check_numbers.py

## [2026-11-18] ingest | camel | 新增 5 頁（來源 1、概念 4：multi-agent-system、role-playing、failure-modes、termination）、更新 0 頁

## [2026-11-18] ingest | chatdev | 新增 5 頁（來源 1、概念 4：division-of-labor、cross-checking、memory、cost-and-fit）、更新 4 頁（multi-agent-system、role-playing、failure-modes、termination）

## [2026-11-18] ingest | debate | 新增 2 頁（來源 1、概念 1：debate）、更新 7 頁（cross-checking、multi-agent-system、role-playing、failure-modes、termination、memory、cost-and-fit）

## [2026-11-18] ingest | generative-agents | 新增 2 頁（來源 1、概念 1：emergent-behavior）、更新 5 頁（memory、multi-agent-system、role-playing、failure-modes、cost-and-fit）

## [2026-11-18] ingest | anthropic-research | 新增 2 頁（來源 1、概念 1：orchestrator-worker）、更新 7 頁（multi-agent-system、division-of-labor、memory、cross-checking、failure-modes、termination、cost-and-fit）

## [2026-11-18] ingest | mas-failures | 新增 1 頁（來源）、更新 6 頁（failure-modes、cross-checking、multi-agent-system、termination、role-playing、cost-and-fit）；新增 3 個「說法不同」

## [2026-11-18] lint | 全部 17 頁 | 自動：錯誤 1（「擷取未涵蓋」被當成缺出處 → 工具與規則不一致，修正 lint_wiki.py）；數字核對 190 個全部吻合。人工：generative-agents 來源頁一句比較語意不清（看起來像「拿掉記憶後比真人還高」），已改寫；確認 3 處「說法不同」都寫了各自條件。

## [2026-11-18] fix | generative-agents、emergent-behavior、division-of-labor | 簡報審稿時發現：① 派對實驗其實設定了兩件事，Wiki 只寫一件（「只」字造成錯誤）；② division-of-labor 的「例子」是整理時自己編的（原文沒說 CTO 負責什麼），改成原文有的五子棋例子並標出處。原因：「例子」區塊不受出處檢查。

## [2026-11-18] rule | lint v2 | 「例子」區塊也要有出處，或標（整理者舉例）
## [2026-11-18] lint | 概念頁的例子 | lint v2 抓到 9 個例子沒出處：5 個原文有→補出處；1 個是示意→標（整理者舉例）；3 個有自己加的細節→改寫（cost-and-fit 把 1,200 個需求的平均說成「寫一個小遊戲」、memory 自編「決定用什麼技術」、orchestrator-worker 自編「派三個助手」）

## [2026-11-18] rule | 新增 wiki/glossary.md 名詞表 | 簡報的術語解釋要能追到 Wiki；有來源標出處，常識性說明標（整理者註）

## [2026-11-18] ingest | chatdev（補收錄）| run-2 大綱檢查發現 Wiki 缺「設計階段做什麼」→ 回原文重新擷取 §4.3（原本擷取時漏掉）→ 更新 2 頁（sources/chatdev、concepts/division-of-labor）

## [2026-11-18] slides | run-1（流程 v1）| 12 頁完成；審稿回頭修 Wiki 3 頁（見上方 fix）。紀錄：docs/run-1.md
## [2026-11-18] slides | run-2（流程 v2）| Wiki 健檢、大綱事實檢查、警告審稿；回 Wiki 補 1 處、重做 8 頁次。紀錄：docs/run-2.md
