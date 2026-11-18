---
type: concept
sources: [chatdev, anthropic-research]
---
# 分工流水線（Division of labor / Chat chain）

## 一句話定義
把大任務切成有先後順序的小任務，每個小任務交給專門的角色，前一棒的成果交給下一棒。

## 白話說明
像工廠的生產線，或分組報告時「有人找資料、有人寫稿、有人做投影片、最後有人校對」。每一站只管自己那一段，交接的是成品，不是整段聊天紀錄。

## 例子
- 開發五子棋遊戲：照設計 → 寫程式 → 測試的順序，每一站由兩個角色對話完成，再把成果交給下一站〔chatdev §3.1〕。

## 各來源怎麼說
- **ChatDev**：照瀑布模型分成設計、寫程式、測試三個階段，每個階段再切成子任務，每個子任務只讓兩個代理人對話〔chatdev §3.1〕。作者說兩人一組可以避免複雜的多代理人連線、比較容易達成共識〔chatdev §3.1〕。前一個子任務的解法會接到下一個，而且每個中間成果都看得到〔chatdev §3.1〕。在設計階段，代理人自己討論目標使用者、資料管理、使用者介面等面向〔chatdev §4.3〕。
- **Anthropic 研究系統**：分工不一定是排隊接力，也可以讓子代理人**平行**做不同方向〔anthropic-research §Architecture〕。分派指示太短，子代理人會重複工作：一個查 2021 年車用晶片危機，另外兩個重複查 2025 年供應鏈〔anthropic-research §Prompting〕。

## 說法不同
目前沒有。

## 相關概念
- [多代理人系統](multi-agent-system.md)
- [角色扮演](role-playing.md)
- [互相檢查](cross-checking.md)
- [記憶](memory.md)
- [主管－助手架構](orchestrator-worker.md)
