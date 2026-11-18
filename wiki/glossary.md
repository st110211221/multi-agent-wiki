# 名詞表（Glossary）

> v2 新增。簡報第一次出現的術語，解釋一律從這裡拿。有來源的標出處；常識性的說明標「整理者註」。

## 代理人（agent）
能自己決定下一步、使用工具、一步步完成任務的 AI。多代理人系統就是好幾個代理人一起合作，見 [多代理人系統](concepts/multi-agent-system.md)。（整理者註）

## 提示（prompt）／系統提示（system prompt）
提示是給 AI 的指令或問題；系統提示是事先寫好、用來設定 AI 身分與規則的提示。CAMEL 用兩段系統提示分別指定助理與使用者的角色〔camel §3.1〕。

## token
AI 計算文字量的單位，一段文字會被切成很多個 token；用量越多，花費和時間通常越多。（整理者註）Anthropic 的多代理人系統約用聊天 15 倍的 token〔anthropic-research §Benefits〕。

## 上下文視窗（context window）
AI 一次能讀進來的內容上限，超過就讀不下或被截斷。（整理者註）Anthropic 的主代理人在 context 超過 200,000 tokens 時會被截斷，所以先把計畫存到外部記憶〔anthropic-research §Architecture〕。

## 可執行率（executability）
產生的程式能直接編譯、執行的比例〔chatdev §4〕。
