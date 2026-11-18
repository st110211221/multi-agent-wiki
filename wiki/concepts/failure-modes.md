---
type: concept
sources: [camel, chatdev, debate, generative-agents, anthropic-research, mas-failures]
---
# 多代理人的常見失敗（Failure modes）

## 一句話定義
多個 AI 合作時反覆出現、會讓任務做不完或做錯的典型問題。

## 白話說明
專案小組會出的包，AI 小組也會出：有人搶著當主管、有人一直重複別人的話、有人說「我來處理」卻沒動、大家互相道謝卻沒人收尾。

## 例子
- 兩個 AI 不停互說「謝謝」「再見」，有時明明知道卡住了卻出不去〔camel §4.1〕。

## 各來源怎麼說
- **CAMEL**：在 25,000 段角色扮演對話中歸納出四種問題〔camel §4.1〕：
  - 角色反轉（role flipping）：助理開始對使用者下指令〔camel §4.1〕。
  - 助理重複指令：只把使用者的指令照抄回去〔camel §4.1〕。
  - 空頭回覆（flake replies）：說「我會…」卻沒有真的做〔camel §4.1〕。
  - 訊息無限迴圈：重複道謝、道別而沒有進展〔camel §4.1〕。
- **ChatDev**：代理人直接交談也會出現角色反轉、重複指令、假回覆〔chatdev §3.1〕。寫程式時另有「程式幻覺」：不完整、無法執行或和需求不一致，常發生在指令模糊的時候〔chatdev §3.2〕。
- **多代理人辯論**：辯論不一定收斂到正確答案，模型會自信地附和錯的答案〔debate §5〕。代理人普遍太「好說話」，作者推測和 instruction tuning 或 RLHF 有關〔debate §2.2〕。
- **Generative Agents**：會加油添醋，說出沒發生過的事〔generative-agents §6.5〕。記憶越多越難找到對的記憶〔generative-agents §7.2〕。難用文字表達的規範沒傳到，例如商店關門後還進去〔generative-agents §7.2〕。太有禮貌、太配合，很少拒絕別人〔generative-agents §7.2〕。
- **Anthropic 研究系統**：早期會為簡單問題派出 50 個子代理人、一直搜尋不存在的來源、彼此過度更新〔anthropic-research §Prompting〕。錯誤會累積：一個步驟失敗，代理人可能走上完全不同的路〔anthropic-research §Conclusion〕。
- **多代理人為何失敗**：分析 7 個框架的執行紀錄，整理出 14 種失敗模式、3 大類〔mas-failures §4.1〕：
  - 規格問題（41.77%）：代理人不照任務或角色要求做、重複步驟、忘記對話、不知道何時該停〔mas-failures §4.1〕。
  - 代理人之間不對齊（36.94%）：沒問清楚就做、任務偏離、隱瞞資訊、說的和做的不一致〔mas-failures §4.1〕。
  - 任務驗證（21.30%）：太早結束、沒檢查或檢查錯〔mas-failures §4.1〕。
  - 最常見的單一模式是重複步驟，佔 17.14%〔mas-failures §4.1〕。
  - 作者認為很多失敗是組織和協調的設計問題，不只是單一代理人能力不足〔mas-failures §1〕。

## 說法不同
> ⚠️ **說法不同**
> - CAMEL 把「角色反轉」列為角色扮演對話的主要挑戰之一，並為此在 prompt 裡寫明禁止互換角色（條件：兩個 gpt-3.5-turbo 直接對話的初步觀察）〔camel §4.1〕。
> - 多代理人為何失敗的統計中，「不遵守角色規格」只佔所有失敗的 0.5%（條件：7 個已設計好角色的開源框架、200 條紀錄）〔mas-failures §4.1〕。

## 相關概念
- [停止條件](termination.md)
- [角色扮演](role-playing.md)
