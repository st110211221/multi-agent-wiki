---
type: source
title: "Generative Agents: Interactive Simulacra of Human Behavior"
authors: Joon Sung Park et al.
year: 2023
url: https://arxiv.org/abs/2304.03442
ingested: 2026-11-18
---
# Generative Agents：25 個 AI 居民的虛擬小鎮（Generative Agents）

## 一句話摘要
在一個像《模擬市民》的小鎮放進 25 個 AI 居民，每個都會記憶、反思、規劃，結果它們自己傳消息、交朋友、一起辦派對。

## 它想解決什麼問題
- 想做出行為「像真人」的 AI 角色，用在社會模擬、遊戲 NPC、設計原型等地方〔generative-agents §1〕。
- 過去的做法只看當下情境，沒辦法長期保持一致，因為過去經驗會超過模型能讀的長度〔generative-agents §2.3〕。

## 怎麼做
- 25 個代理人，每個只有一段種子描述（身分、職業、人際關係）〔generative-agents §3.1〕。
- **記憶流（memory stream）**：用文字記下所有經歷；需要時依「多新、多重要、多相關」三個分數挑出記憶〔generative-agents §4.1〕。重要性由模型打 1–10 分，例如打掃房間 2 分、約暗戀對象出去 8 分〔generative-agents §4.1〕。
- **反思（reflection）**：近期事件的重要性加總超過 150 就觸發，把觀察整理成更高層的想法，約每天 2–3 次〔generative-agents §4.2〕。
- **規劃（planning）**：先排一天的大綱，再拆成每小時、每 5–15 分鐘的行動，遇到事情可以改計畫〔generative-agents §4.3〕。

## 主要發現
- 社交行為是自己「湧現」的，不是寫好的：研究者只設定了兩件事——Isabella 想辦情人節派對、Maria 暗戀 Klaus；邀請、布置、Maria 邀 Klaus 一起去，都是代理人自己做的〔generative-agents §3.4〕。
- 兩個遊戲日內，知道派對的居民從 1 位（4%）增加到 13 位（52%），知道 Sam 參選鎮長的從 1 位增加到 8 位（32%）〔generative-agents §7.1〕。
- 居民之間的關係網密度從 0.167 增加到 0.74〔generative-agents §7.1〕。
- 12 位受邀者中有 5 位真的到場〔generative-agents §7.1〕。
- 完整架構的可信度評分 29.89，比真人照劇本扮演的 22.95 還高；拿掉記憶、規劃、反思後只剩 21.21〔generative-agents §6.5〕。

## 限制與注意
- 會加油添醋：例如說 Sam「明天會宣布」，但那件事從沒發生〔generative-agents §6.5〕。
- 記憶越多越難找到對的記憶，也越難選對地點〔generative-agents §7.2〕。
- 文字很難表達的規範沒傳到：有人走進有人在用的單人浴室、商店 5 點關門後還進去〔generative-agents §7.2〕。
- 太有禮貌、太配合：Isabella 幾乎不拒絕別人的派對點子，興趣還被別人改變〔generative-agents §7.2〕。
- 模擬 25 個代理人 2 天花了數千美元、跑了好幾天〔generative-agents §8.2〕。
- 倫理：要避免使用者把 AI 當真人依賴，代理人應揭露自己是電腦程式〔generative-agents §8.3〕。

## 相關概念
- [湧現的社會行為](../concepts/emergent-behavior.md)
- [記憶](../concepts/memory.md)
- [多代理人系統](../concepts/multi-agent-system.md)
- [角色扮演](../concepts/role-playing.md)
- [多代理人的常見失敗](../concepts/failure-modes.md)
- [成本與適用時機](../concepts/cost-and-fit.md)
