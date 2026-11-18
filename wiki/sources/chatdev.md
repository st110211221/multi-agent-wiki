---
type: source
title: "ChatDev: Communicative Agents for Software Development"
authors: Chen Qian et al.
year: 2023
url: https://arxiv.org/abs/2307.07924
ingested: 2026-11-18
---
# ChatDev：一間全是 AI 的軟體公司（ChatDev）

## 一句話摘要
把軟體開發照「設計 → 寫程式 → 測試」切成一串小任務，每個小任務由兩個不同角色的 AI 對話完成，像一間虛擬軟體公司。

## 它想解決什麼問題
- 過去的方法各自改善開發的某一個階段，彼此不連貫〔chatdev §Abstract〕。
- AI 寫的程式常有「程式幻覺」：不完整、無法執行或不正確〔chatdev §1〕。

## 怎麼做
- **聊天鏈（chat chain）**：照瀑布模型分成設計、寫程式、測試三個階段，再切成子任務；寫程式分成撰寫與補完，測試分成程式碼審查與實際執行測試〔chatdev §3.1〕。
- 每個子任務只有兩個代理人：一個下指令（instructor）、一個回覆解法（assistant），對話到有共識為止〔chatdev §3.1〕。
- 角色有 CEO、CTO、程式設計師、審查員、測試員〔chatdev §4〕。
- **記憶分兩層**：短期記憶保留目前階段的對話；長期記憶只把前一階段的「解法」帶到下一階段，不帶整段對話〔chatdev §3.1〕。
- **溝通式去幻覺（communicative dehallucination）**：助理先反過來追問細節（例如要用哪個套件），問清楚再寫〔chatdev §3.2〕。
- 子任務在程式碼連續兩次沒有變動、或溝通滿 10 輪時結束〔chatdev §4〕。

## 主要發現
- 在 1,200 個軟體需求上，ChatDev 四項指標都贏過單代理人的 GPT-Engineer 和多代理人的 MetaGPT；可執行率 0.88，綜合品質 0.3953〔chatdev §4.1〕。
- 但比單代理人慢很多、用更多 tokens：平均 148.2 秒、22,949.4 tokens，GPT-Engineer 只要 15.6 秒、7,182.5 tokens〔chatdev §4.1〕。
- 設計階段以自然語言溝通為主，代理人自己討論目標使用者、資料管理、使用者介面等面向；論文沒說設計階段由哪些角色負責〔chatdev §4.3〕。
- 拿掉「角色設定」傷害最大：可執行率掉到 0.58，品質掉到 0.2212；沒有「仔細的審查員」角色，回饋就變得空泛〔chatdev §4.2〕。
- 拿掉去幻覺機制，四項指標都下降〔chatdev §4.2〕。
- 審查時最常見的問題是「方法沒實作」，佔 34.85%；測試最常見的錯誤是找不到模組，佔 45.76%〔chatdev §4.3〕。

## 限制與注意
- 能力容易被高估：常只做出簡單邏輯，比較適合做原型，不適合複雜的真實應用〔chatdev §6〕。
- 一般軟體很難自動評估〔chatdev §6〕。
- 多代理人需要更多 tokens 與時間〔chatdev §6〕。

## 相關概念
- [多代理人系統](../concepts/multi-agent-system.md)
- [分工流水線](../concepts/division-of-labor.md)
- [互相檢查](../concepts/cross-checking.md)
- [角色扮演](../concepts/role-playing.md)
- [記憶](../concepts/memory.md)
- [多代理人的常見失敗](../concepts/failure-modes.md)
- [停止條件](../concepts/termination.md)
- [成本與適用時機](../concepts/cost-and-fit.md)
