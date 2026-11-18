---
type: concept
sources: [chatdev, debate, generative-agents, anthropic-research, mas-failures]
---
# 成本與適用時機（Cost and fit）

## 一句話定義
多代理人通常比單一 AI 更花時間、更花錢，所以要看任務值不值得。

## 白話說明
找一整個小組來做事，比一個人做更周全，但開會、交接都要時間。簡單的事一個人做就好；大到一個人做不完、或需要多種專長的事，才值得組隊。

## 例子
- 同一批軟體需求：單一 AI 平均 15.6 秒交差，AI 小組平均 148.2 秒，但做出來的程式比較能直接執行〔chatdev §4.1〕。

## 各來源怎麼說
- **ChatDev**：ChatDev 平均花 148.2 秒、22,949.4 tokens，單代理人的 GPT-Engineer 只要 15.6 秒、7,182.5 tokens，但 ChatDev 產出更多檔案與程式碼〔chatdev §4.1〕。作者把成本列為限制，認為未來要減少代理人之間的互動〔chatdev §6〕。
- **多代理人辯論**：要多次生成、跑多輪，所以比其他提示方法貴〔debate §5〕。
- **Generative Agents**：模擬 25 個代理人 2 天，花了數千美元的 token 費用、跑了好幾天〔generative-agents §8.2〕。
- **Anthropic 研究系統**：一般 agent 約用聊天的 4 倍 token，多代理人約 15 倍，所以任務價值要高到付得起〔anthropic-research §Benefits〕。適合高度可平行、資訊量超過單一 context window、要用很多複雜工具的任務〔anthropic-research §Benefits〕。
- **多代理人為何失敗**：低效率的協調會讓成本和延遲變成 10 倍以上，例如用了 10 輪才拿到本來 1 個動作就能拿的資料〔mas-failures §4.4〕。

## 說法不同
目前沒有。

## 相關概念
- [多代理人系統](multi-agent-system.md)
- [主管－助手架構](orchestrator-worker.md)
