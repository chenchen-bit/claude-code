# Comet Design Handoff

- Change: redesign-index-ink-wash
- Phase: design
- Mode: compact
- Context hash: 100f2cdc98782cd3fee1ec840d2d3c8b9ae6ba2b0e3fbb44ba8b0bb8db6b14b2

Generated-by: comet-handoff.sh

OpenSpec remains the canonical capability spec. This handoff is a deterministic, source-traceable context pack, not an agent-authored summary.

## openspec/changes/redesign-index-ink-wash/proposal.md

- Source: openspec/changes/redesign-index-ink-wash/proposal.md
- Lines: 1-28
- SHA256: c922b97de28a31bfcb3805633b4afb86d5c9873d0b29a36850f1132a207e8fb4

```md
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
```

## openspec/changes/redesign-index-ink-wash/design.md

- Source: openspec/changes/redesign-index-ink-wash/design.md
- Lines: 1-69
- SHA256: 72c75b5fa775678a33ae650775a4f4b68e42fce457083e792c693f8813127d91

```md
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
```

## openspec/changes/redesign-index-ink-wash/tasks.md

- Source: openspec/changes/redesign-index-ink-wash/tasks.md
- Lines: 1-25
- SHA256: 4226f195fe30c556ac881d7576679ab3941c2aadbcef1bf7781d7a96d44ac1e1

```md
## 1. Canvas 山水引擎

- [ ] 1.1 在 Hero 區加入 `<canvas>` 元素，設定全屏尺寸與 `devicePixelRatio` 處理
- [ ] 1.2 實現 Perlin-noise 山巒生成函數（3-5 層山形，由近到遠）
- [ ] 1.3 實現墨暈渲染（`globalCompositeOperation: multiply` + 徑向漸變）
- [ ] 1.4 實現雲霧粒子系統（20-60 個半透明粒子隨機飄移）

## 2. 動畫與互動

- [ ] 2.1 建立 `requestAnimationFrame` 動畫循環（deltaTime 驅動）
- [ ] 2.2 實現墨滴飛濺動畫（定時隨機位置擴散淡出）
- [ ] 2.3 實現滾動視差聯動（山巒淡出 + 墨色加深）
- [ ] 2.4 實現 `prefers-reduced-motion` 降級（靜止畫面）

## 3. 效能與相容性

- [ ] 3.1 行動端適配（<768px 降低山巒層數與粒子數）
- [ ] 3.2 iOS Safari 相容性測試與 Canvas memory 優化
- [ ] 3.3 滾出視口時暫停動畫循環

## 4. 頁面整合

- [ ] 4.1 調整 Hero CSS 與 Canvas 疊層順序（z-index）
- [ ] 4.2 簡化或移除與山水動畫衝突的舊效果（mouse-glow、floating-chars）
- [ ] 4.3 確認導航欄、品牌字標、slogan 在所有 breakpoint 正常顯示
```

## openspec/changes/redesign-index-ink-wash/specs/ink-landscape-canvas/spec.md

- Source: openspec/changes/redesign-index-ink-wash/specs/ink-landscape-canvas/spec.md
- Lines: 1-45
- SHA256: a9481ff2f586ed4d20029ec26ab568be89669dc550fd32deedb65d1c4f878114

```md
## ADDED Requirements

### Requirement: Landscape generation
The system SHALL generate mountain landscape shapes using layered noise-based terrain curves.

#### Scenario: Mountains render in layers
- **WHEN** the Canvas initializes
- **THEN** it SHALL draw 3–5 mountain layers with decreasing opacity from foreground to background

#### Scenario: Mountain shapes appear organic
- **WHEN** a mountain layer is drawn
- **THEN** its contour SHALL use bezier curves with Perlin-noise vertex offsets for irregular, hand-painted appearance

#### Scenario: Ink wash texture
- **WHEN** a mountain layer is rendered
- **THEN** it SHALL use `globalCompositeOperation: 'multiply'` and radial gradients to simulate ink bleeding on rice paper

### Requirement: Mist particle system
The system SHALL render slow-moving mist particles that drift across mountain layers.

#### Scenario: Mist particles float
- **WHEN** the animation loop runs
- **THEN** 20–60 particles SHALL move horizontally at random speeds between 0.1–0.5 px/frame and fade in/out with sine-wave opacity

#### Scenario: Mist respects layer depth
- **WHEN** particles are rendered
- **THEN** particles behind mountain layers SHALL draw with lower opacity than those in front

### Requirement: Ink splash accent
The system SHALL periodically render ink-splash accents at random positions for organic texture.

#### Scenario: Random ink drops
- **WHEN** the animation timer reaches a random interval (3–8 seconds)
- **THEN** the system SHALL draw an expanding radial ink blotch that fades out over 2–4 seconds

### Requirement: Performance adaptation
The system SHALL degrade gracefully on low-power devices.

#### Scenario: Reduced quality on mobile
- **WHEN** `window.innerWidth < 768`
- **THEN** the system SHALL reduce mountain layers to 3 and particle count to 20

#### Scenario: No animation for reduced motion
- **WHEN** the user has `prefers-reduced-motion: reduce`
- **THEN** the system SHALL render a static frame and skip the animation loop
```

## openspec/changes/redesign-index-ink-wash/specs/scroll-reactive-animation/spec.md

- Source: openspec/changes/redesign-index-ink-wash/specs/scroll-reactive-animation/spec.md
- Lines: 1-34
- SHA256: 0c3cbe8e9bf8bf40c4f1d05ae80313035ac7e8c2dc35b5b25aac325195307a92

```md
## ADDED Requirements

### Requirement: Scroll-reactive parallax
The system SHALL adjust Canvas rendering parameters in response to page scroll position.

#### Scenario: Foreground mountains fade on scroll
- **WHEN** the page is scrolled past 50vh
- **THEN** the opacity of the foreground mountain SHALL decrease proportionally to scroll distance, reaching 0 at 100vh

#### Scenario: Ink density increases
- **WHEN** the page is scrolled past 30vh
- **THEN** the ink saturation of the background mountain layers SHALL increase by up to 30% at 80vh

#### Scenario: Scroll resets on top
- **WHEN** the page is scrolled back to the top
- **THEN** all Canvas parameters SHALL return to their initial values within 300ms

### Requirement: Hero content layer integration
The Canvas SHALL render behind brand typography as a background layer.

#### Scenario: Canvas behind text
- **WHEN** the Hero section is visible
- **THEN** the Canvas SHALL be positioned with `z-index: 0` and the text/content SHALL be above it with `z-index: 2`

#### Scenario: Divider line reacts to landscape
- **WHEN** the hero divider line is visible
- **THEN** its accent color SHALL be extended by a subtle ink spread animation drawn on the Canvas

### Requirement: Memory management
The system SHALL clean up resources when the Hero section is out of view or the component unmounts.

#### Scenario: Animation stops when hidden
- **WHEN** the Hero section scrolls out of view (past 150vh from top)
- **THEN** the animation loop SHALL pause and resume when the Hero re-enters the viewport
```

