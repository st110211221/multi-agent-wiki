---
title: 從一個人到一個團隊：多代理人 AI 入門
audience: 用過 ChatGPT 的大學生
length: 12 頁、約 10 分鐘
---
# 大綱 v2

> v2：每頁加上「事實」（附 Wiki 原句片段，程式會確認真的在 Wiki 裡）與「術語」（必須在名詞表裡）。

> 目標代號：1＝說得出多代理人是什麼、和單一 AI 有什麼不同；2＝看得懂常見的合作方式；3＝知道它會在哪裡出錯。0＝不對應（封面、總結）。

## 01｜從一個人到一個團隊：多代理人 AI 入門
- 類型：封面
- 重點：當 AI 不只一個，它們怎麼分工、合作，又會怎麼出包？
- 目標：0
- 出處：concepts/multi-agent-system

## 02｜你現在用的 AI：一個萬能助理
- 類型：內容
- 重點：用 ChatGPT 時，每一步都要你來引導
- 目標：1
- 出處：concepts/multi-agent-system
- 事實：「聊天 AI 很會解題，但很依賴人類一步一步引導」〔wiki: sources/camel〕
- 事實：「非專家常常不知道該怎麼下 prompt」〔wiki: sources/camel〕
- 術語：prompt

## 03｜多代理人系統是什麼？
- 類型：內容
- 重點：多個 AI 各負責一部分，互相傳訊息完成同一件事
- 目標：1
- 出處：concepts/multi-agent-system, concepts/role-playing
- 事實：「讓多個 AI 代理人（agent）各自負責一部分」〔wiki: concepts/multi-agent-system〕
- 事實：「同一個模型的多個分身」〔wiki: concepts/multi-agent-system〕
- 術語：代理人

## 04｜第一步：先發角色卡
- 類型：內容
- 重點：用 prompt 替每個 AI 指定身分和職責
- 目標：2
- 出處：concepts/role-playing
- 事實：「不准互換角色」〔wiki: concepts/role-playing〕
- 事實：「可執行率從 0.88 掉到 0.58」〔wiki: concepts/role-playing〕
- 事實：「MMLU 正確率從 71.1 升到 74.2」〔wiki: concepts/role-playing〕
- 術語：可執行率

## 05｜合作方式①：分工接力
- 類型：內容
- 重點：把大任務切成小任務，一棒交給下一棒
- 目標：2
- 出處：concepts/division-of-labor, concepts/memory
- 事實：「照瀑布模型分成設計、寫程式、測試三個階段」〔wiki: concepts/division-of-labor〕
- 事實：「長期記憶只把前面階段的」〔wiki: concepts/memory〕
- 事實：「代理人自己討論目標使用者、資料管理、使用者介面」〔wiki: concepts/division-of-labor〕

## 06｜合作方式②：互相辯論
- 類型：內容
- 重點：各自作答、互相挑錯，來回幾輪後更正確
- 目標：2
- 出處：concepts/debate, concepts/cross-checking
- 事實：「GSM8K 數學題上單一代理人 77.0%、多數決 81.0%、辯論 85.0%」〔wiki: concepts/debate〕
- 事實：「實驗預設用 3 個代理人、辯論 2 輪」〔wiki: sources/debate〕
- 事實：「模型會自信地附和錯的答案」〔wiki: sources/debate〕

## 07｜合作方式③：主管帶助手
- 類型：內容
- 重點：主管拆解分派，助手平行執行，主管整合
- 目標：2
- 出處：concepts/orchestrator-worker, concepts/memory
- 事實：「主代理人分析問題、擬定策略、產生子代理人平行工作，再整合結果」〔wiki: concepts/orchestrator-worker〕
- 事實：「否則會重複做同一件事」〔wiki: concepts/orchestrator-worker〕
- 事實：「這個系統比單一代理人好 90.2%」〔wiki: concepts/orchestrator-worker〕

## 08｜番外：一群 AI 自己形成小社會
- 類型：內容
- 重點：沒寫劇本，互動中自己長出傳消息、辦派對等行為
- 目標：2
- 出處：concepts/emergent-behavior
- 事實：「25 個 AI 居民住在虛擬小鎮」〔wiki: concepts/multi-agent-system〕
- 事實：「研究者只設定了兩件事」〔wiki: sources/generative-agents〕
- 事實：「知道派對的居民從 4% 增加到 52%」〔wiki: concepts/emergent-behavior〕
- 事實：「12 位受邀者中有 5 位真的到場」〔wiki: sources/generative-agents〕

## 09｜它真的比單一 AI 強嗎？
- 類型：內容
- 重點：看任務而定，而且一定比較貴
- 目標：1, 3
- 出處：concepts/multi-agent-system, concepts/cost-and-fit
- 事實：「多代理人比單一代理人好 90.2%」〔wiki: concepts/multi-agent-system〕
- 事實：「在常見測驗上相對單一代理人的進步常常很小」〔wiki: concepts/multi-agent-system〕
- 事實：「多代理人約 15 倍」〔wiki: concepts/cost-and-fit〕
- 術語：token

## 10｜多代理人會在哪裡出錯？
- 類型：內容
- 重點：規格不清、彼此沒對齊、沒檢查好，是三大類原因
- 目標：3
- 出處：concepts/failure-modes
- 事實：「分析 7 個開源多代理人框架的 200 條執行紀錄」〔wiki: sources/mas-failures〕
- 事實：「規格問題（41.77%）」〔wiki: concepts/failure-modes〕
- 事實：「最常見的單一模式是重複步驟，佔 17.14%」〔wiki: concepts/failure-modes〕

## 11｜怎麼讓 AI 團隊少出錯？
- 類型：內容
- 重點：角色寫清楚、加上檢查關卡、設好停止條件
- 目標：3
- 出處：concepts/role-playing, concepts/cross-checking, concepts/termination
- 事實：「把角色規格寫得更清楚，成功率提升 9.4%」〔wiki: concepts/role-playing〕
- 事實：「在 ChatDev 加一個檢查整體目標的步驟，成功率提升 15.6%」〔wiki: concepts/cross-checking〕
- 事實：「訊息達到 40 則上限」〔wiki: concepts/termination〕
- 事實：「這些改進有幫助，但沒有消除所有失敗」〔wiki: sources/mas-failures〕

## 12｜總結：從一個人到一個團隊
- 類型：總結
- 重點：分工合作能變強，但要付出成本，也要防出錯
- 目標：1, 2, 3
- 出處：concepts/multi-agent-system, concepts/failure-modes
