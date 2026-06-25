## Context

「之間」品牌首頁目前使用 SVG ink filter + CSS 動畫營造水墨氛圍，但缺乏動態山水元素。用戶要求在 Hero 區加入 Canvas 繪製的山水水墨動效，使山巒、雲霧、墨暈在頁面加載後持續流動變化，呼應品牌「在傳統與現代之間」的哲學。

## Goals / Non-Goals

**Goals:**
- 以 Canvas 2D 繪製動態水墨山水作為 Hero 背景
- 山巒具備墨水暈染效果（毛筆觸感 + 墨汁擴散）
- 雲霧粒子緩慢飄移，製造深遠意境
- 頁面滾動時 Canvas 產生視差響應（山巒淡出、墨色加深）
- 保留「之間」大字、品牌 slogan、導航欄等核心品牌元素
- 單檔案內聯（維持現有專案結構），無外部依賴
- 支援 `prefers-reduced-motion` 降級

**Non-Goals:**
- 不引入 WebGL / Three.js（保持輕量，Canvas 2D 足矣）
- 不做 interactivity（點擊/拖拽等互動不在本次範圍）
- 不對 timeline/pillars/gallery 等下方區塊做結構改動

## Decisions

### 1. Canvas 2D 而非 WebGL

**選擇**：Canvas 2D API
**理由**：水墨效果的核心是「擴散」和「隨機筆觸」，Canvas 2D 的 pixel-level 操作和漸變繪製更自然。WebGL 對於 fluid simulation 更高效但對於本案的藝術風格過度設計。Canvas 2D 在所有現代瀏覽器上支援完善。

### 2. 山巒生成：Perlin Noise + 隨機頂點偏移

**選擇**：改進的 Perlin Noise 生成山形輪廓 + 隨機頂點偏移製造不規則感
**理由**：使用 Simplex noise 演算法生成山脊線，加上二次貝塞爾曲線繪製山形。每座山由 3-5 層疊加（由深到淺），形成傳統山水畫的「遠近」層次。

### 3. 墨暈效果：徑向漸變 + 隨機擴散

**選擇**：自訂 `drawInkSplash` 函數，使用 `createRadialGradient` 疊加隨機擴散
**理由**：在 Canvas 上繪製多層半透明徑向漸變，配合 `globalCompositeOperation` 的 `multiply` 模式，模擬墨水在宣紙上的暈染效果。

### 4. 雲霧系統：粒子陣列

**選擇**：數十個半透明圓形粒子，隨機遊走 + 淡入淡出
**理由**：雲霧在山間縹緲是山水畫的核心元素。粒子方式效能開銷低，視覺效果好。

### 5. 動畫循環：requestAnimationFrame + 時間增量

**選擇**：標準 rAF 循環，計算 deltaTime 驅動動畫
**理由**：確保 60fps 且在不同刷新率螢幕上行為一致。

### 6. 色彩策略

**選擇**：墨色五層次（焦濃重淡清），以 `rgba` 控制透明度
**理由**：中國水墨畫的墨分五色概念，從黑到極淡灰，搭配現有品牌的 `#3B5E5C` 墨綠作為點睛色。

### 7. 滾動聯動

**選擇**：`IntersectionObserver` + `scroll` event 驅動 Canvas 參數變化
**理由**：與現有頁面的 scroll-reveal 機制一致，不需引入新框架。

## Risks / Trade-offs

| 風險 | 緩解措施 |
|------|---------|
| Canvas 效能在低階行動裝置上不足 | 根據 `window.innerWidth` 和硬體並行度降低山巒層數和粒子數；`prefers-reduced-motion` 時靜止 Canvas |
| 水墨效果在不同螢幕上呈現不一致 | 使用 devicePixelRatio 確保 retina 清晰度；responsive 設計以 viewport 尺寸為基準 |
| 與現有 Hero CSS 動畫衝突 | 新 Canvas 覆蓋原 `.hero-ink-bg` 區域；浮字 / divider 動畫簡化或移除 |
| Canvas 在 iOS Safari 上的 memory 問題 | 限制 Canvas 尺寸不超過 2048px；移除離屏 canvas 快取 |

## Open Questions

- 是否需要支援 dark mode？目前 `var(--color-bg: #F5F0EB)` 暖灰已接近宣紙色，dark mode 下效果需評估
