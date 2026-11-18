---
type: source
title: Why Do Multi-Agent LLM Systems Fail?
authors: Mert Cemri et al.
year: 2025
url: https://arxiv.org/abs/2503.13657
ingested: 2026-11-18
---
# 多代理人為何失敗：14 種失敗模式（Why Do Multi-Agent LLM Systems Fail?）

## 一句話摘要
研究者仔細讀了多個開源多代理人系統的執行紀錄，整理出 14 種失敗模式、分成 3 大類，並指出很多問題出在系統設計，而不是模型不夠聰明。

## 它想解決什麼問題
- 大家對多代理人很期待，但它在常見測驗上相對單一代理人的進步常常很小〔mas-failures §Abstract〕。
- 想系統性地回答：多代理人系統到底為什麼會失敗〔mas-failures §Abstract〕。

## 怎麼做
- 分析 7 個開源多代理人框架的 200 條執行紀錄，每條平均超過 15,000 行〔mas-failures §1〕。
- 由專家標註，經過三輪修正定義，標註一致性 Cohen's Kappa 從 0.24 提升到 0.92 和 0.84〔mas-failures §3〕。
- 做出一個 LLM 自動標註器，few-shot 版本準確率 0.94〔mas-failures §3〕。

## 主要發現
- **14 種失敗模式、3 大類**〔mas-failures §4.1〕：
  - 規格問題 41.77%：例如重複步驟 17.14%、不遵守任務規格 10.98%、不知道什麼時候該停 9.82%〔mas-failures §4.1〕。
  - 代理人之間不對齊 36.94%：例如推理和行動不一致 13.98%、沒有要求釐清 11.65%、任務偏離 7.15%〔mas-failures §4.1〕。
  - 任務驗證 21.30%：過早結束 7.82%、沒有或不完整的驗證 6.82%、錯誤的驗證 6.66%〔mas-failures §4.1〕。
- 有驗證者的系統（MetaGPT、ChatDev）失敗較少，但 ChatDev 在 ProgramDev 測驗上仍只有 33.33% 正確率；驗證者常只做表面檢查〔mas-failures §4.3〕。
- 在 ChatDev 加入一個檢查整體目標的驗證步驟，成功率提升 15.6%〔mas-failures §4.3〕；把角色規格寫清楚，成功率提升 9.4%〔mas-failures §5〕。

## 限制與注意
- 這些改進有幫助，但沒有消除所有失敗，完成率仍偏低〔mas-failures §5〕。
- 不包含效率問題；例如有系統用了 10 輪才拿到本來 1 個動作就能拿的 10 首歌，成本可能因此變成 10 倍以上〔mas-failures §4.4〕。
- 「只靠模型進步不夠」是作者的主張，沒有直接驗證〔mas-failures §1〕。
- （擷取未涵蓋）部分附錄與 AG2 的介入數字。

## 相關概念
- [多代理人的常見失敗](../concepts/failure-modes.md)
- [互相檢查](../concepts/cross-checking.md)
- [多代理人系統](../concepts/multi-agent-system.md)
- [停止條件](../concepts/termination.md)
- [角色扮演](../concepts/role-playing.md)
- [成本與適用時機](../concepts/cost-and-fit.md)
