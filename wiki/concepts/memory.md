---
type: concept
sources: [chatdev, debate, generative-agents, anthropic-research]
---
# 記憶（Memory）

## 一句話定義
決定每個 AI 能看到哪些過去的資訊：要記住什麼、要傳給誰、要丟掉什麼。

## 白話說明
AI 一次能讀的內容有上限（context window），塞太多它會分心或塞不下。所以要像交接一樣：只把重點交給下一個人，而不是把整本會議紀錄丟過去。

## 例子
- 下一階段的 AI 只拿到前一階段的「解法」，不用讀完前一階段的全部對話〔chatdev §3.1〕。

## 各來源怎麼說
- **ChatDev**：因為 context 長度有限，把記憶分成兩層：短期記憶保留目前階段的對話，長期記憶只把前面階段的「解法」帶進下一階段〔chatdev §3.1〕。作者說只分享解法可以避免資訊過載，又能保持前後連貫〔chatdev §3.1〕。
- **多代理人辯論**：辯論太長時，模型常只注意最近的回答〔debate §5〕。代理人有 5 個以上時，要先把其他人的回答摘要再傳過去，避免超過 context 長度〔debate §3.3〕。
- **Generative Agents**：每個居民有一條記憶流，用文字記下所有經歷；需要時依「多新、多重要、多相關」三個分數挑出記憶〔generative-agents §4.1〕。重要事件累積夠多就觸發「反思」，把零散觀察整理成更高層的想法〔generative-agents §4.2〕。拿掉記憶、規劃和反思，可信度評分從 29.89 掉到 21.21〔generative-agents §6.5〕。
- **Anthropic 研究系統**：主代理人先把研究計畫存到外部記憶，因為 context 超過 200,000 tokens 會被截斷〔anthropic-research §Architecture〕。子代理人把成果寫進檔案、只回傳位置，避免像「傳話遊戲」一樣越傳越失真〔anthropic-research §Appendix〕。

## 說法不同
目前沒有。

## 相關概念
- [分工流水線](division-of-labor.md)
- [多代理人系統](multi-agent-system.md)
- [湧現的社會行為](emergent-behavior.md)
