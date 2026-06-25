## Why

現有的「之間」首頁已具備基礎水墨視覺風格（SVG ink filter、浮字動效），但缺乏沉浸式的動態山水體驗。中國山水畫的核心在於「氣韻生動」——靜態的佈局和簡單的模糊濾鏡無法傳達水墨在紙上暈染、山巒在雲霧中浮沉的動態美感。本次改版旨在以 **Canvas 繪製的動態山水中墨動畫**作為 Hero 區的背景，將品牌「在傳統與現代之間」的哲學以最直觀的視覺語言呈現。

## What Changes

- **Hero 區徹底重構**：以 Canvas 全屏動畫取代現有 SVG ink filter 背景，繪製動態水墨山水（遠山、近巒、雲霧、墨暈）
- **保留品牌核心元素**：保留「之間」大字標題、品牌 slogan、滾動提示，但整合進新的動畫語境
- **色彩體系微調**：保留現有暖灰/墨綠基調，融入更豐富的墨色層次（焦、濃、重、淡、清）
- **導航欄保持不變**：現有 fixed nav 設計已成熟，只做相容性調整
- **滾動觸發動畫**：頁面滾動時 Canvas 山水產生「墨色加深」「山巒淡出」等動態響應
- **移除冗餘效果**：合併/簡化 mouse-glow 和 floating-chars 這些與新視覺衝突的效果

## Capabilities

### New Capabilities
- `ink-landscape-canvas`: 基於 Canvas 的實時水墨山水渲染引擎，包含遠山生成、雲霧粒子、墨暈擴散算法
- `scroll-reactive-animation`: 頁面滾動與 Canvas 動畫的聯動系統（視差滾動、墨色濃度變化）

### Modified Capabilities
- *(無現有 spec 需要修改)*

## Impact

- 僅改寫 `index.html` 一個檔案（單頁應用，CSS/JS 全部內聯）
- 增加 Canvas 渲染的 CPU/GPU 消耗，需要做移動端性能優化（降級方案或降低粒子數）
- 移除或簡化部分現有 JS 效果（mouse-glow 可能不再需要，floating-chars 可保留但減弱）
- 需要處理 `prefers-reduced-motion` 的無動畫降級
