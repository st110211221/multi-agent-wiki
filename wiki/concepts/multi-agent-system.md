---
type: concept
sources: [camel, chatdev, debate, generative-agents, anthropic-research, mas-failures]
---
# 多代理人系統（Multi-Agent System）

## 一句話定義
讓多個 AI 代理人（agent）各自負責一部分，靠彼此傳訊息合作完成同一個任務的系統。

## 白話說明
平常用 ChatGPT，是你跟一個「萬能助理」來回聊天，每一步都要你來引導。多代理人系統比較像一個「專案小組」：有人負責規劃、有人負責動手做，它們自己互相交代工作，你只要在一開始交代清楚目標。

## 例子
- 讓一個 AI 扮演「股票交易員」下需求、另一個 AI 扮演「Python 程式設計師」寫程式，兩個 AI 自己對話到把交易機器人做完〔camel §3.1〕。

## 各來源怎麼說
- **CAMEL**：動機是聊天 AI 太依賴人類一步一步引導；讓兩個角色不同的 AI 自己對話，可以在最少人類監督下完成任務〔camel §1〕。它們的對話歷史會一輪一輪累積，下一個指令和解法都根據歷史產生〔camel §3.1〕。框架也可以延伸到多於兩個代理人〔camel §3.1〕。
- **ChatDev**：把軟體開發交給 CEO、CTO、程式設計師、審查員、測試員等 AI 角色，用語言當作不同階段之間的共同橋樑〔chatdev §Abstract〕。在 1,200 個軟體需求上，它的四項指標都贏過單代理人的 GPT-Engineer〔chatdev §4.1〕。
- **多代理人辯論**：多個代理人也可以是**同一個模型的多個分身**，靠互相辯論提升正確性；只需要呼叫 API 就能用〔debate §Abstract〕。
- **Generative Agents**：多代理人不一定是為了完成一件工作，也可以用來模擬社會：25 個 AI 居民住在虛擬小鎮，各自生活、互相對話〔generative-agents §3.1〕。
- **Anthropic 研究系統**：用多代理人的理由是研究工作無法事先決定步驟，而且多個子代理人可以平行探索、各用自己的 context window〔anthropic-research §Benefits〕。在內部研究評測中，多代理人系統比單一代理人好 90.2%〔anthropic-research §Benefits〕。
- **多代理人為何失敗**：多代理人在常見測驗上相對單一代理人的進步常常很小〔mas-failures §Abstract〕。作者主張很多失敗來自組織和協調的設計，而不只是模型能力〔mas-failures §1〕。

## 說法不同
> ⚠️ **說法不同**：多代理人到底比單一 AI 強多少？
> - Anthropic 的內部研究評測中，多代理人比單一代理人好 90.2%（條件：需要同時追多個方向的研究型問題）〔anthropic-research §Benefits〕。
> - 多代理人辯論在算術、數學題、事實問答上都贏過單一代理人（條件：3 個代理人辯論 2 輪）〔debate §3.1〕。
> - 多代理人為何失敗指出，在常見測驗上相對單一代理人的進步常常很小（條件：7 個開源框架、多種測驗）〔mas-failures §Abstract〕。

## 相關概念
- [角色扮演](role-playing.md)
- [多代理人的常見失敗](failure-modes.md)
- [停止條件](termination.md)
- [辯論](debate.md)
- [湧現的社會行為](emergent-behavior.md)
- [主管－助手架構](orchestrator-worker.md)
