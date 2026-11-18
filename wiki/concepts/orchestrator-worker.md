---
type: concept
sources: [anthropic-research]
---
# 主管－助手架構（Orchestrator-worker）

## 一句話定義
一個「主管」AI 負責拆解問題和分派工作，多個「助手」AI 平行執行，最後由主管整合結果。

## 白話說明
像分組報告的組長：先想好要查哪幾個方向，分給組員同時去查，組員只交回重點，組長再拼成一份報告。好處是快、而且每個組員只要專心看自己那一塊。

## 例子
- 問「2025 年有哪些 AI agent 公司」：子代理人反覆搜尋後交回一份公司清單，主管再整合成答案〔anthropic-research §Architecture〕。

## 各來源怎麼說
- **Anthropic 研究系統**：主代理人分析問題、擬定策略、產生子代理人平行工作，再整合結果〔anthropic-research §Architecture〕。每個子代理人有自己的 context window，像過濾器一樣只交回濃縮後的發現〔anthropic-research §Benefits〕。分派時要給每個助手明確的目標、輸出格式、工具指引和任務邊界，否則會重複做同一件事〔anthropic-research §Prompting〕。這個系統比單一代理人好 90.2%，但用掉約 15 倍於聊天的 token〔anthropic-research §Benefits〕。

## 說法不同
目前沒有。

## 相關概念
- [多代理人系統](multi-agent-system.md)
- [分工流水線](division-of-labor.md)
- [成本與適用時機](cost-and-fit.md)
