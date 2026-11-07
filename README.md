# MultiServerZh Translations

MultiServerZh 的英翻繁體中文詞庫。OPLegends 詞庫目前包含 530 條，涵蓋聊天、物品名稱、Lore、附魔與選單提示。

## 手動匯入

使用支援 GitHub 詞庫的新版模組，連線到 OPLegends 後執行：

```text
/mszh import oplegends
/mszh items on
```

只有執行匯入指令時才會下載；不在啟動、登入、重繪或背景排程自動更新。匯入後的本地副本可離線使用。未下載成功時保留本地譯文。

詞庫位置：[packs/oplegends.zh-TW.json](packs/oplegends.zh-TW.json)

原始下載網址：

```text
https://raw.githubusercontent.com/starekingz/MultiServerZh-Translations/main/packs/oplegends.zh-TW.json
```

## 維護詞庫

直接編輯 JSON 並提交至 main。使用者下次執行匯入指令時才取得新版，不需為純譯文更新重新發布模組。

- JSON 鍵為完整英文來源，值為繁體中文；換行使用 `\n`。
- `{0}`、`{1}` 等佔位符的集合必須一致，可重排或重複使用。重複的來源編號必須匹配同一個值。
- 佔位符不能跨行，不能漏掉數值、網址、指令與圖示。
- 不接受空譯文；未完成的條目請先不要提交到正式詞庫。
- 已存在的本地人工修改保留；上次匯入後未修改的條目可更新。匯入前會自動備份本地詞庫。
- 此倉庫不包含機器翻譯服務、不存放使用者的 missing 或機翻快取。

對新 Minecraft 版本、自訂字型或其他模組的相容性，仍需遊戲內驗證。
