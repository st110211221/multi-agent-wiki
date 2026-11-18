---
type: source
title: "CAMEL: Communicative Agents for \"Mind\" Exploration of Large Language Model Society"
authors: Guohao Li et al.
year: 2023
url: https://arxiv.org/abs/2303.17760
ingested: 2026-11-18
---
# CAMEL：讓兩個 AI 用角色扮演合作（CAMEL）

## 一句話摘要
給兩個 AI 各自一個角色（下指令的「使用者」和動手做的「助理」），只在開頭寫好 prompt，之後讓它們自己一來一往對話，把任務做完。

## 它想解決什麼問題
- 聊天 AI 很會解題，但很依賴人類一步一步引導；非專家常常不知道該怎麼下 prompt〔camel §1〕。
- 研究問題：能不能讓 AI 自己把對話帶向完成任務，只需要最少的人類監督〔camel §1〕。

## 怎麼做
- **角色扮演框架（role-playing）**：人只提供一個點子和兩個角色，例如「開發股票交易機器人」，角色是 Python 程式設計師（助理）和股票交易員（使用者）〔camel §3.1〕。
- **任務指定代理人（task specifier）**：先把模糊的點子改寫成具體任務，像一個「想像力增強器」〔camel §3.1〕。
- **AI 使用者負責規劃、一次給一個指令；AI 助理負責執行並回覆解法**，直到使用者宣布完成〔camel §3.1〕。
- **起始提示（inception prompting）**：只在開頭寫好三個 prompt（任務指定、助理、使用者），之後代理人自動互相 prompt〔camel §3.2〕。
- prompt 裡寫明規矩：不准互換角色、回覆要以「Solution:」開頭並以「Next request.」結尾、完成時輸出結束標記〔camel §3.2〕。

## 主要發現
- 用 50 個助理角色 × 50 個使用者角色 × 每組 10 個任務，產生 25,000 段對話〔camel §4.1〕。
- 觀察到四種合作失敗：角色反轉、助理重複指令、空頭回覆（說「我會做」卻沒做）、訊息無限迴圈〔camel §4.1〕。
- 設了五種終止條件，包括使用者連 3 輪沒下指令、出現結束標記、訊息上限 40 則（成本隨對話長度呈平方成長）〔camel §4.1〕。
- 和 gpt-3.5-turbo 單次回答相比，人類評審在 AI Society 任務中有 76.3% 選 CAMEL；GPT-4 評審在 AI Society 選 CAMEL 73.0%、在 Code 任務選 CAMEL 76.0%〔camel §5.1〕。

## 限制與注意
- 作者在結論承認：對話偏離、角色反轉、何時停止，都讓自主合作很困難〔camel §6〕。
- 附錄的「壞心智」例子顯示：沒有對齊好的自主代理人系統，可能自己生出有害的計畫〔camel §Appendix B〕。
- 人類評估只做了 AI Society；Code 等資料集由 GPT-4 產生〔camel §5.1〕。

## 相關概念
- [多代理人系統](../concepts/multi-agent-system.md)
- [角色扮演](../concepts/role-playing.md)
- [多代理人的常見失敗](../concepts/failure-modes.md)
- [停止條件](../concepts/termination.md)
