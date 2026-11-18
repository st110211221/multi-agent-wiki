---
type: source
title: How we built our multi-agent research system
authors: Anthropic Engineering
year: 2025
url: https://www.anthropic.com/engineering/multi-agent-research-system
ingested: 2026-11-18
---
# Anthropic 多代理人研究系統：一個主管帶一群助手（How we built our multi-agent research system）

> 章節代號：§Benefits＝多代理人的好處、§Architecture＝架構、§Prompting＝提示設計、§Evaluation＝評估、§Reliability＝上線的可靠度、§Appendix＝附錄。

## 一句話摘要
Claude 的「研究」功能由一個主代理人規劃問題，同時派出多個子代理人平行上網搜尋，再整合答案並補上出處。

## 它想解決什麼問題
- 研究是開放式的工作，事前無法知道要走哪些步驟，會依中間的發現改變方向〔anthropic-research §Benefits〕。
- 一次跑完的固定流程，處理不了這種邊做邊調整的工作〔anthropic-research §Benefits〕。

## 怎麼做
- **主管－助手架構（orchestrator-worker）**：主代理人分析問題、擬定策略、產生子代理人，最後整合結果〔anthropic-research §Architecture〕。
- 子代理人各自有獨立的 context window，平行探索不同面向，只把濃縮後的結果交回〔anthropic-research §Benefits〕。
- 主代理人先把計畫存進外部記憶，因為 context 超過 200,000 tokens 會被截斷〔anthropic-research §Architecture〕。
- 最後由一個專門的引用代理人（CitationAgent）替每個說法找出處〔anthropic-research §Architecture〕。
- 依問題難度決定派多少人：簡單查詢 1 個代理人、3–10 次工具呼叫；比較型問題 2–4 個子代理人；複雜研究 10 個以上〔anthropic-research §Prompting〕。

## 主要發現
- 在內部研究評測中，多代理人系統比單一代理人好 90.2%〔anthropic-research §Benefits〕。
- 特別擅長要同時追很多獨立方向的「廣度型」問題〔anthropic-research §Benefits〕。
- 表現差異有 80% 可以用 token 用量解釋〔anthropic-research §Benefits〕。
- 代價是很耗 token：一般 agent 約是聊天的 4 倍，多代理人約是聊天的 15 倍〔anthropic-research §Benefits〕。
- 讓主代理人同時開 3–5 個子代理人、子代理人同時用多個工具，複雜問題的研究時間最多縮短 90%〔anthropic-research §Prompting〕。

## 限制與注意
- 早期常出錯：簡單問題也派出 50 個子代理人、一直搜尋不存在的來源〔anthropic-research §Prompting〕。
- 分派指示太短，子代理人會重複做同一件事〔anthropic-research §Prompting〕。
- 錯誤會累積：一個步驟失敗，整個代理人可能走上完全不同的路〔anthropic-research §Conclusion〕。
- 主代理人要等所有子代理人做完，一個慢的會拖住整體〔anthropic-research §Reliability〕。
- 適用條件：任務價值要高到付得起額外成本〔anthropic-research §Benefits〕。

## 相關概念
- [主管－助手架構](../concepts/orchestrator-worker.md)
- [多代理人系統](../concepts/multi-agent-system.md)
- [分工流水線](../concepts/division-of-labor.md)
- [記憶](../concepts/memory.md)
- [互相檢查](../concepts/cross-checking.md)
- [多代理人的常見失敗](../concepts/failure-modes.md)
- [停止條件](../concepts/termination.md)
- [成本與適用時機](../concepts/cost-and-fit.md)
