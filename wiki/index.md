# Wiki 目錄｜多代理人 AI

> AI 找頁面從這裡開始。每收錄一篇資料就更新。規則見 [`CLAUDE.md`](../CLAUDE.md)，工作紀錄見 [`log.md`](log.md)。

## 名詞表

- [名詞表](glossary.md)：代理人、prompt、token、上下文視窗、可執行率

## 來源頁（一篇資料一頁）

| 代號 | 頁面 | 一句話 |
|---|---|---|
| `camel` | [CAMEL：讓兩個 AI 用角色扮演合作](sources/camel.md) | 兩個角色不同的 AI 自己對話完成任務 |
| `chatdev` | [ChatDev：一間全是 AI 的軟體公司](sources/chatdev.md) | 照設計→寫程式→測試分工，兩兩對話完成 |
| `debate` | [多代理人辯論：讓 AI 互相吵出更好的答案](sources/debate.md) | 多個分身各自作答、互相修正 |
| `generative-agents` | [Generative Agents：25 個 AI 居民的虛擬小鎮](sources/generative-agents.md) | 會記憶、反思、規劃的 AI 居民自己發展出社交行為 |
| `anthropic-research` | [Anthropic 多代理人研究系統](sources/anthropic-research.md) | 主管 AI 帶多個助手平行搜尋、整合、補出處 |
| `mas-failures` | [多代理人為何失敗：14 種失敗模式](sources/mas-failures.md) | 分析執行紀錄，整理出 3 大類 14 種失敗 |

## 概念頁

| 頁面 | 一句話 | 來源 |
|---|---|---|
| [多代理人系統](concepts/multi-agent-system.md) | 多個 AI 分工、互傳訊息合作完成任務 | camel, chatdev, debate, generative-agents, anthropic-research, mas-failures |
| [角色扮演](concepts/role-playing.md) | 用 system prompt 替每個 AI 指定身分與職責 | camel, chatdev, debate, generative-agents, mas-failures |
| [多代理人的常見失敗](concepts/failure-modes.md) | AI 小組反覆出現的典型問題 | camel, chatdev, debate, generative-agents, anthropic-research, mas-failures |
| [停止條件](concepts/termination.md) | 事先規定合作何時結束 | camel, chatdev, debate, anthropic-research, mas-failures |
| [分工流水線](concepts/division-of-labor.md) | 大任務切成小任務、一棒接一棒 | chatdev, anthropic-research |
| [互相檢查](concepts/cross-checking.md) | 由另一個 AI 審查、追問、測試 | chatdev, debate, anthropic-research, mas-failures |
| [記憶](concepts/memory.md) | 決定每個 AI 看得到哪些過去資訊 | chatdev, debate, generative-agents, anthropic-research |
| [成本與適用時機](concepts/cost-and-fit.md) | 多代理人更花時間與錢，要看值不值得 | chatdev, debate, generative-agents, anthropic-research, mas-failures |
| [辯論](concepts/debate.md) | 多個 AI 互相看答案、挑錯、修正 | debate |
| [湧現的社會行為](concepts/emergent-behavior.md) | 沒有劇本、互動中自己長出群體行為 | generative-agents |
| [主管－助手架構](concepts/orchestrator-worker.md) | 主管拆解分派、助手平行執行、主管整合 | anthropic-research |

## 有「說法不同」的頁面

- [多代理人系統](concepts/multi-agent-system.md)：多代理人到底比單一 AI 強多少
- [互相檢查](concepts/cross-checking.md)：ChatDev 的驗證到底有多有效
- [多代理人的常見失敗](concepts/failure-modes.md)：角色反轉是主要問題還是很少見
