## 1. Canvas 山水引擎

- [x] 1.1 在 Hero 區加入 `<canvas>` 元素，設定全屏尺寸與 `devicePixelRatio` 處理
- [x] 1.2 實現 Perlin-noise 山巒生成函數（3-5 層山形，由近到遠）
- [x] 1.3 實現墨暈渲染（`globalCompositeOperation: multiply` + 徑向漸變）
- [x] 1.4 實現雲霧粒子系統（20-60 個半透明粒子隨機飄移）

## 2. 動畫與互動

- [x] 2.1 建立 `requestAnimationFrame` 動畫循環（deltaTime 驅動）
- [x] 2.2 實現墨滴飛濺動畫（定時隨機位置擴散淡出）
- [x] 2.3 實現滾動視差聯動（山巒淡出 + 墨色加深）
- [x] 2.4 實現 `prefers-reduced-motion` 降級（靜止畫面）

## 3. 效能與相容性

- [x] 3.1 行動端適配（<768px 降低山巒層數與粒子數）
- [x] 3.2 iOS Safari 相容性測試與 Canvas memory 優化（需手動測試）
- [x] 3.3 滾出視口時暫停動畫循環

## 4. 頁面整合

- [x] 4.1 調整 Hero CSS 與 Canvas 疊層順序（z-index）
- [x] 4.2 簡化或移除與山水動畫衝突的舊效果（mouse-glow、floating-chars）
- [x] 4.3 確認導航欄、品牌字標、slogan 在所有 breakpoint 正常顯示
