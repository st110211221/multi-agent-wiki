---
type: source
title: Improving Factuality and Reasoning in Language Models through Multiagent Debate
authors: Yilun Du et al.
year: 2023
url: https://arxiv.org/abs/2305.14325
ingested: 2026-11-18
---
# 多代理人辯論：讓 AI 互相吵出更好的答案（Multiagent Debate）

## 一句話摘要
讓同一個模型的好幾個分身先各自作答，再互相看對方的答案、修正自己的答案，來回幾輪，最後得到更正確的共同答案。

## 它想解決什麼問題
- 語言模型會自信地捏造事實，或在推理中做出不合理的跳躍〔debate §1〕。
- 過去的改進方法都只在單一個模型身上做〔debate §1〕。

## 怎麼做
- 受《心智社會》（The Society of Mind）啟發〔debate §1〕。
- 三步驟：每個代理人先獨立解題 → 把其他代理人的答案給它看並要求更新 → 重複好幾輪〔debate §2.1〕。
- 只需要呼叫模型的 API，不需要模型內部資訊〔debate §Abstract〕。
- 實驗預設用 3 個代理人、辯論 2 輪，是考量運算成本〔debate §3〕。

## 主要發現
- 推理任務上，辯論都贏過單一代理人：算術正確率 81.8% 對 67.0%、GSM8K 數學題 85.0% 對 77.0%〔debate §3.1〕。
- 事實任務上也贏：電腦科學家傳記 73.8 對 66.0、MMLU 71.1 對 63.9〔debate §3.2〕。
- 有時所有代理人一開始都答錯，辯論後卻得到正確答案〔debate §1〕。
- 代理人越多、輪數越多，算術正確率越高；但超過 4 輪和 4 輪差不多〔debate §3.3〕。
- 給代理人不同人設（教授、醫生、數學家），MMLU 從 71.1 升到 74.2〔debate §3.3〕。
- 不同模型也能辯論：20 題數學題中 Bard 解出 11 題、ChatGPT 14 題，一起辯論解出 17 題〔debate §3.3〕。

## 限制與注意
- 比其他提示方法貴，因為要生成很多次、跑很多輪〔debate §5〕。
- 辯論太長時，模型常只注意最近的回答〔debate §5〕。
- 辯論通常會收斂，但不一定收斂到正確答案；模型會自信地附和錯的答案〔debate §5〕。
- 代理人普遍太「好說話」，可能是 instruction tuning 或 RLHF 造成的〔debate §2.2〕。

## 相關概念
- [辯論](../concepts/debate.md)
- [互相檢查](../concepts/cross-checking.md)
- [多代理人系統](../concepts/multi-agent-system.md)
- [角色扮演](../concepts/role-playing.md)
- [多代理人的常見失敗](../concepts/failure-modes.md)
- [停止條件](../concepts/termination.md)
- [記憶](../concepts/memory.md)
- [成本與適用時機](../concepts/cost-and-fit.md)
