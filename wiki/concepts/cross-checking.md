---
type: concept
sources: [chatdev, debate, anthropic-research, mas-failures]
---
# 互相檢查（Cross-checking）

## 一句話定義
讓一個 AI 的成果由另一個 AI 審查、追問或測試，抓出單一 AI 自己看不到的錯。

## 白話說明
自己寫的報告自己校對，常常看不出錯；交給同學看，一眼就抓到。讓 AI 互相檢查也是同樣的道理。

## 例子
- 審查員 AI 讀程式碼，最常指出「這個方法沒有實作」；測試員 AI 實際執行，最常回報「找不到模組」〔chatdev §4.3〕。

## 各來源怎麼說
- **ChatDev**：測試階段分成程式碼審查和實際執行測試〔chatdev §3.1〕。助理在回答前先反過來追問細節，叫做溝通式去幻覺〔chatdev §3.2〕。實驗顯示測試階段對可執行率特別關鍵，拿掉去幻覺機制四項指標都下降〔chatdev §4.2〕。審查時最常抓到的是「方法沒實作」，佔 34.85%〔chatdev §4.3〕。
- **多代理人辯論**：同一個模型的多個分身互相看答案、互相批評再修正，在推理和事實任務上都比單一代理人好〔debate §3.1〕。單一代理人自我反省（reflection）只有小幅幫助，在 MMLU 上甚至從 63.9 掉到 57.7〔debate §3.2〕。
- **Anthropic 研究系統**：最後由專門的引用代理人替每個說法找出處〔anthropic-research §Architecture〕。評估時用另一個 LLM 當評審，依事實正確、引用正確、完整度、來源品質、工具效率打分〔anthropic-research §Evaluation〕。但人工檢查仍抓到自動評審漏掉的問題，例如偏好內容農場而不是權威來源〔anthropic-research §Evaluation〕。
- **多代理人為何失敗**：驗證錯誤或不完整佔所有失敗的 13.48%〔mas-failures §4.3〕。有驗證者的系統失敗較少，但驗證者常只做表面檢查，例如井字遊戲判錯贏家也沒抓到〔mas-failures §4.3〕。在 ChatDev 加一個檢查整體目標的步驟，成功率提升 15.6%；作者認為需要多層次的驗證〔mas-failures §4.3〕。

## 說法不同
> ⚠️ **說法不同**
> - ChatDev 自己的實驗中，加入審查與測試後可執行率達 0.88，作者認為測試對可執行率很關鍵（條件：SRDD 1,200 個需求，指標是「能不能直接執行」）〔chatdev §4.1〕。
> - 多代理人為何失敗指出，即使有驗證者，ChatDev 在 ProgramDev 測驗只有 33.33% 正確率（條件：指標是「功能是否正確」）〔mas-failures §4.3〕。

## 相關概念
- [分工流水線](division-of-labor.md)
- [多代理人的常見失敗](failure-modes.md)
- [辯論](debate.md)
