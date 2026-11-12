# MultiServerZh

Minecraft 伺服器英語 → 繁體中文翻譯模組。翻譯系統訊息、NPC 對話、物品說明、計分板與浮空文字，讓你用熟悉的語言遊玩。

**只需在自己的遊戲客戶端安裝，伺服器不需加裝插件。**

[模組網站](https://multiserverzh.pages.dev/) · [下載最新版](https://github.com/starekingz/MultiServerZh-Translations/releases/latest) · [回報問題](https://github.com/starekingz/MultiServerZh-Translations/issues)

## 安裝

需要 Minecraft Java **1.21.11**、**Fabric Loader 0.19.2 以上**、Fabric API 與 **Java 21 以上**。下載前請確認 Release 的相容版本說明。

1. 從 [GitHub Releases](https://github.com/starekingz/MultiServerZh-Translations/releases/latest) 下載 `multiserverzh-版本.jar`。
2. 將 JAR 放入遊戲實例的 `mods` 資料夾。更新時移除舊版，避免同時安裝兩份。
3. 啟動遊戲，進入支援的伺服器。
4. 在聊天欄輸入 `/mszh import`，等待詞庫匯入成功。
5. 按 **F9** 調整翻譯開關與顯示方式。

模組與完整原始碼均由 GitHub Releases 提供。一般玩家只需下載 JAR，不需下載詞庫 JSON 或原始碼壓縮檔。

## 支援的伺服器

| 伺服器 | 連線位址 |
| --- | --- |
| OPLegends | `play.oplegends.com` |
| PikaNetwork | `mcslr.pika.host` |

請使用上表的連線位址。模組依實際連線位址辨識詞庫；修改多人遊戲清單中的伺服器名稱不影響辨識，其他網域別名可能無法自動取得翻譯。

翻譯範圍取決於目前已收錄的內容，尚未收錄的句子可能保留英文。

## 顯示與設定

按 **F9** 或執行 `/mszh config` 開啟設定，可分別調整聊天、物品、浮空文字、計分板、Boss Bar 與 Action Bar 等翻譯。

- **物品說明：**可使用獨立翻譯面板，或直接在原提示框取代。
- **計分板：**使用原地取代。
- **玩家聊天與機器翻譯：**預設關閉。使用人工詞庫不需要架設翻譯服務。
- **詞庫：**各伺服器分開保存，下載後可離線使用。

## 更新

### 更新詞庫

進服時可檢查詞庫更新。點擊更新提示，或執行：

```text
/mszh import
```

匯入會保留本地人工修改。檢查或下載失敗時，仍可使用既有的本地詞庫。單純更新翻譯內容通常不需要更換模組。

### 更新模組

執行 `/mszh modupdate` 手動檢查版本，或直接查看 [最新 Release](https://github.com/starekingz/MultiServerZh-Translations/releases/latest)。

依遊戲中的提示下載更新後，需重新啟動遊戲才能使用新版。也可以正常關閉遊戲，手動將 `mods` 內的舊 JAR 替換為新版。請先確認新版支援你的 Minecraft 版本。

## 常用操作

| 操作 | 功能 |
| --- | --- |
| **F9** 或 `/mszh config` | 開啟設定 |
| **F8** | 在物品提示框顯示時擷取原文與格式 |
| `/mszh import` | 更新目前伺服器詞庫 |
| `/mszh modupdate` | 檢查模組版本 |
| `/mszh toggle` | 開關翻譯 |
| `/mszh reload` | 重新載入本地設定與詞庫 |
| `/mszh status` | 查看目前伺服器、詞庫路徑與狀態 |
| `/mszh items panel` | 使用獨立物品翻譯面板 |
| `/mszh items replace` | 在物品提示框原地取代 |
| `/mszh missing export` | 匯出未翻譯原文與來源資料 |
| `/mszh missing clear` | 清除本服未翻譯紀錄 |
| `/mszh export state` | 匯出浮空文字的原文與顯示狀態 |

設定與資料位於遊戲實例的 `config/multiserverzh/`。

## 常見問題

### 已匯入詞庫，為什麼仍有英文？

1. 執行 `/mszh status`，確認伺服器與詞庫是否正確。
2. 執行 `/mszh import` 取得最新詞庫。
3. 按 F9，確認對應位置的翻譯開關已啟用。
4. 確認已安裝相容的新版模組。
5. 若仍未翻譯，可能是缺詞，或文字的換行、狀態、字型與已收錄範例不同。

同一句話在聊天、物品或浮空文字中可能需要分別收錄。特殊動畫或混淆文字也可能保留原文。

### 更新後版本沒有改變？

模組更新需重新啟動遊戲才會生效。若手動安裝，請確認替換的是目前啟動實例的 `mods` 資料夾，並移除舊版 JAR。

### 詞庫下載失敗怎麼辦？

確認網路能連線 GitHub，稍後再執行 `/mszh import`。若已有本地詞庫，可以繼續使用；若沒有，請附上錯誤訊息回報。

### 如何回報缺詞或顯示錯誤？

請至 [Issues](https://github.com/starekingz/MultiServerZh-Translations/issues) 提供模組版本、伺服器連線位址、重現方式及畫面，並視問題附上：

- **缺少翻譯：**執行 `/mszh missing export`，附上原文 JSON 與配對的 `.sources.json`；若有多個分檔，請一併附上。
- **物品文字或格式：**顯示物品提示框時按 F8 擷取。
- **浮空文字：**執行 `/mszh export state`。
- **聊天格式或點擊問題：**在 F9 將聊天右鍵功能設為完整擷取，再擷取該訊息。

上傳前請移除不相關的玩家聊天、私訊與個人資料。

## 授權與來源

MultiServerZh 採用 **AGPL-3.0-only**，設定介面改作自 [WynnChaYuan](https://github.com/LyuChaCha/WynnChaYuan)。完整對應原始碼與授權說明請見各版本的 [Release 附件](https://github.com/starekingz/MultiServerZh-Translations/releases)。

本專案為獨立社群專案，非 Mojang 或 Microsoft 官方產品。
