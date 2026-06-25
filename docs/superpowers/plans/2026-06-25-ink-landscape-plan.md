---
archived-with: 2026-06-25-redesign-index-ink-wash
status: final
---
# 全页水墨山水动画 — 实施计划

> **For agentic workers:** 單檔案 HTML（index.html），無 git，無外部依賴。直接在當前工作目錄修改。

**Goal:** 將「之間」品牌首頁的 Hero 區 SVG 水墨濾鏡改為全頁 Canvas 水墨山水動畫，覆蓋整個頁面。

**Architecture:** 一個全屏 fixed `<canvas>` 作為山水渲染層，內容 section 改為半透明背景讓山水透出。Perlin noise 生成山巒，粒子系統渲染雲霧，定時墨暈點綴，滾動驅動景觀演變。

**Tech Stack:** 純 Canvas 2D API、CSS backdrop-filter、vanilla JS。零外部依賴。

---

## 文件結構

唯一文件：`index.html`

| 區域 | 行數範圍（約） | 內容 |
|------|--------------|------|
| `<style>` Canvas 區 | 新插入 ~50 行 | Canvas 固定定位、section 半透明背景、backdrop-filter |
| `<body>` 頂部 | 新插入 `<canvas>` | 全屏 fixed canvas，替換 SVG ink filter |
| `<script>` 渲染引擎 | ~250 行 | Perlin noise、山巒繪製、雲霧粒子、墨暈散落、滾動聯動 |

---

### Task 1: Canvas 元素與基礎 CSS 設置

**Files:**
- Modify: `index.html` — 在 `<style>` 加入 Canvas CSS，在 `<body>` 開頭插入 `<canvas>`

- [x] **Step 1: 在 CSS 中新增 Canvas 與半透明背景規則**

在 `<style>` 中「SVG Ink Filter」區塊後新增：

```css
/* ============================================
   3a. Canvas 山水背景
   ============================================ */
#landscape-canvas {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 0;
  pointer-events: none;
}

/* Content sections — translucent for landscape visibility */
.timeline-section,
.gallery-section {
  background: rgba(250, 247, 243, 0.85) !important;
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
}

.pillars-section,
.contact-section {
  background: rgba(245, 240, 235, 0.80) !important;
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
}

.site-footer {
  background: rgba(245, 240, 235, 0.90) !important;
}

.hero {
  background: transparent !important;
}
```

- [x] **Step 2: 在 `<body>` 開頭插入 Canvas 元素（替換 SVG filter）**

移除現有 SVG ink filter block（`.ink-filter`），在 `<body>` 開頭插入：

```html
<!-- 水墨山水 Canvas 背景 -->
<canvas id="landscape-canvas" aria-hidden="true"></canvas>
```

同時移除 `#mouse-glow` div 和 `.hero-ink-bg` div。

---

### Task 2: Perlin Noise 與山巒生成引擎

**Files:**
- Modify: `index.html` — 在 `<script>` 中新增顏色和 Perlin noise 實作

- [x] **Step 1: 實作 Perlin Noise（Simplex 變體）**

在 `<script>` 中新增 Perlin noise 實現：

```javascript
// Perlin Noise — simplified simplex variant
class PerlinNoise {
  constructor(seed) {
    this.p = [];
    const perm = Array.from({length: 256}, (_, i) => i);
    for (let i = 255; i > 0; i--) {
      const j = Math.floor(seededRandom(seed + i) * (i + 1));
      [perm[i], perm[j]] = [perm[j], perm[i]];
    }
    this.p = new Array(512);
    for (let i = 0; i < 512; i++) this.p[i] = perm[i & 255];
  }
  noise(x, y) {
    const X = Math.floor(x) & 255, Y = Math.floor(y) & 255;
    const xf = x - Math.floor(x), yf = y - Math.floor(y);
    const u = fade(xf), v = fade(yf);
    const aa = this.p[this.p[X] + Y], ab = this.p[this.p[X] + Y + 1];
    const ba = this.p[this.p[X + 1] + Y], bb = this.p[this.p[X + 1] + Y + 1];
    return lerp(v, lerp(u, grad(aa, xf, yf), grad(ba, xf - 1, yf)),
                   lerp(u, grad(ab, xf, yf - 1), grad(bb, xf - 1, yf - 1)));
  }
}
function fade(t) { return t * t * t * (t * (t * 6 - 15) + 10); }
function lerp(t, a, b) { return a + t * (b - a); }
function grad(hash, x, y) { const h = hash & 3; const u = h < 2 ? x : y; const v = h < 2 ? y : x; return ((h & 1) === 0 ? u : -u) + ((h & 2) === 0 ? v : -v); }
function seededRandom(seed) { const x = Math.sin(seed + 0.1) * 43758.5453; return x - Math.floor(x); }
```

- [x] **Step 2: 實作山巒繪製函數**

```javascript
function drawMountains(ctx, w, h, scrollRatio, time, quality) {
  const layers = quality.layers; // 3–5
  const mountains = [];

  for (let i = 0; i < layers; i++) {
    const depth = i / layers; // 0=遠, 1=近
    const baseY = h * (0.55 + depth * 0.25);
    const amplitude = 40 + depth * 80;
    const frequency = 0.003 + depth * 0.002;
    const opacity = lerp(depth, 0.08, 0.80);
    const vOffset = -scrollRatio * depth * 200; // 視差: 近山移動更多

    const points = [];
    const step = Math.max(4, Math.floor(w / 120));
    for (let x = -20; x <= w + 20; x += step) {
      const noiseVal = perlin.noise(x * frequency + time * 0.00005 * (1 - depth), depth * 100);
      const y = baseY + noiseVal * amplitude + vOffset;
      points.push({x, y});
    }

    ctx.beginPath();
    ctx.moveTo(0, h);
    for (let p = 0; p < points.length - 1; p++) {
      const xc = (points[p].x + points[p + 1].x) / 2;
      const yc = (points[p].y + points[p + 1].y) / 2;
      ctx.quadraticCurveTo(points[p].x, points[p].y, xc, yc);
    }
    ctx.lineTo(w, h);
    ctx.closePath();

    // Ink wash gradient fill
    const grad = ctx.createLinearGradient(0, baseY - amplitude, 0, h);
    grad.addColorStop(0, `rgba(44, 40, 36, ${opacity})`);
    grad.addColorStop(0.4, `rgba(44, 40, 36, ${opacity * 0.5})`);
    grad.addColorStop(1, `rgba(44, 40, 36, 0)`);
    ctx.fillStyle = grad;
    ctx.globalCompositeOperation = 'multiply';
    ctx.fill();
    ctx.globalCompositeOperation = 'source-over';
  }
}
```

- [x] **Step 3: 新增墨暈渲染函數**

```javascript
function drawInkSplash(ctx, w, h, splash) {
  const progress = splash.elapsed / splash.duration; // 0→1
  const radius = splash.maxRadius * Math.min(progress * 2, 1);
  const opacity = splash.maxOpacity * (1 - progress);

  ctx.save();
  ctx.globalAlpha = opacity;
  const grad = ctx.createRadialGradient(splash.x, splash.y, 0, splash.x, splash.y, radius);
  grad.addColorStop(0, 'rgba(44, 40, 36, 0.3)');
  grad.addColorStop(0.3, 'rgba(44, 40, 36, 0.15)');
  grad.addColorStop(0.7, 'rgba(44, 40, 36, 0.05)');
  grad.addColorStop(1, 'rgba(44, 40, 36, 0)');
  ctx.fillStyle = grad;
  ctx.beginPath();
  ctx.arc(splash.x, splash.y, radius, 0, Math.PI * 2);
  ctx.fill();
  ctx.restore();
}
```

---

### Task 3: 雲霧粒子系統

**Files:**
- Modify: `index.html` — 在 `<script>` 中新增雲霧粒子系統

- [x] **Step 1: 實作雲霧粒子系統**

```javascript
function createMistParticles(count, w, h) {
  const particles = [];
  for (let i = 0; i < count; i++) {
    particles.push({
      x: Math.random() * w,
      y: h * (0.3 + Math.random() * 0.5),
      size: 80 + Math.random() * 200,
      speed: 0.2 + Math.random() * 0.6,
      phase: Math.random() * Math.PI * 2,
      depth: Math.random(),
    });
  }
  return particles;
}

function drawMist(ctx, w, h, particles, dt, scrollRatio) {
  const mistOpacity = lerp(scrollRatio, 0.35, 0.10);

  particles.forEach(p => {
    p.x += p.speed * dt * 0.06;
    if (p.x > w + p.size) p.x = -p.size;

    const alpha = (0.15 + Math.sin(p.phase + Date.now() * 0.0003 * (1 - p.depth)) * 0.15) * mistOpacity;

    ctx.save();
    ctx.globalAlpha = Math.max(0, alpha);
    ctx.fillStyle = 'rgba(220, 215, 205, 0.8)';
    ctx.shadowColor = 'rgba(220, 215, 205, 0.3)';
    ctx.shadowBlur = 40;
    ctx.beginPath();
    ctx.ellipse(p.x, p.y, p.size * 0.5, p.size * 0.25, 0, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();
  });
}
```

---

### Task 4: 動畫循環與初始化

**Files:**
- Modify: `index.html` — 主動畫迴圈、Canvas 初始化

- [x] **Step 1: Canvas 初始化函數**

```javascript
function initCanvas() {
  const canvas = document.getElementById('landscape-canvas');
  const ctx = canvas.getContext('2d');
  const dpr = window.devicePixelRatio || 1;
  const w = window.innerWidth;
  const h = window.innerHeight;

  const isMobile = w < 768;
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const quality = {
    layers: prefersReduced ? 3 : (isMobile ? 3 : 5),
    particles: prefersReduced ? 0 : (isMobile ? 25 : 60),
    inkSplashes: !prefersReduced && !isMobile,
    dpr: prefersReduced ? 1 : (isMobile ? 1 : dpr),
  };

  // iPad / mid-range
  if (w >= 768 && w < 1024) {
    quality.layers = 4;
    quality.particles = 35;
    quality.inkSplashes = true;
  }

  canvas.width = w * quality.dpr;
  canvas.height = h * quality.dpr;
  ctx.scale(quality.dpr, quality.dpr);

  return { canvas, ctx, w, h, quality, isMobile, prefersReduced };
}
```

- [x] **Step 2: 主動畫迴圈**

```javascript
const perlin = new PerlinNoise(42);
let splashTimer = 0;
let splashes = [];
let lastTime = 0;

function animate(time, state, scrollRatio) {
  const dt = Math.min(time - lastTime, 33);
  lastTime = time;
  const { ctx, w, h, quality } = state;

  ctx.clearRect(0, 0, w, h);

  // 1. Draw mountains
  drawMountains(ctx, w, h, scrollRatio, time, quality);

  // 2. Draw mist particles
  if (state.mistParticles && state.mistParticles.length) {
    drawMist(ctx, w, h, state.mistParticles, dt, scrollRatio);
  }

  // 3. Draw ink splashes
  if (quality.inkSplashes) {
    splashTimer += dt;
    if (splashTimer > 3000 + Math.random() * 5000) {
      splashes.push({
        x: Math.random() * w,
        y: h * (0.3 + Math.random() * 0.4),
        maxRadius: 60 + Math.random() * 90,
        maxOpacity: 0.08 + Math.random() * 0.12,
        elapsed: 0,
        duration: 2000 + Math.random() * 2000,
      });
      splashTimer = 0;
    }
    splashes = splashes.filter(s => s.elapsed < s.duration);
    splashes.forEach(s => { s.elapsed += dt; drawInkSplash(ctx, w, h, s); });
  }

  if (!state.paused) {
    state.rafId = requestAnimationFrame(t => animate(t, state, scrollRatio));
  }
}
```

---

### Task 5: 滾動聯動與分區敘事

**Files:**
- Modify: `index.html` — 滾動事件綁定與分區參數

- [x] **Step 1: 滾動事件與分區計算**

```javascript
const PARTITIONS = [
  { name: 'hero',    range: [0, 0.15], fgOpacity: [1.0, 0.8], mistDensity: [1.0, 0.8], inkTone: 'light' },
  { name: 'story',   range: [0.15, 0.40], fgOpacity: [0.8, 0.5], mistDensity: [0.8, 0.6], inkTone: 'medium' },
  { name: 'gallery', range: [0.40, 0.65], fgOpacity: [0.5, 0.2], mistDensity: [0.6, 0.4], inkTone: 'heavy' },
  { name: 'ending',  range: [0.65, 1.0], fgOpacity: [0.2, 0], mistDensity: [0.4, 0.1], inkTone: 'dark' },
];

function getScrollRatio() {
  const docEl = document.documentElement;
  const scrollTop = window.scrollY;
  const scrollHeight = Math.max(
    document.body.scrollHeight, docEl.scrollHeight,
    document.body.offsetHeight, docEl.offsetHeight,
    document.body.clientHeight, docEl.clientHeight
  );
  return Math.min(scrollTop / (scrollHeight - window.innerHeight), 1);
}

function getPartitionParams(scrollRatio) {
  const p = PARTITIONS.find(p => scrollRatio >= p.range[0] && scrollRatio < p.range[1])
    || PARTITIONS[PARTITIONS.length - 1];
  const t = (scrollRatio - p.range[0]) / (p.range[1] - p.range[0]);
  return {
    fgOpacity: lerp(t, p.fgOpacity[0], p.fgOpacity[1]),
    mistDensity: lerp(t, p.mistDensity[0], p.mistDensity[1]),
    inkTone: p.inkTone,
  };
}
```

- [x] **Step 2: 整合啟動和 resize**

```javascript
function startLandscape() {
  const state = initCanvas();
  if (state.prefersReduced) {
    // Draw one static frame
    drawMountains(state.ctx, state.w, state.h, 0, 0, state.quality);
    return;
  }
  state.mistParticles = createMistParticles(state.quality.particles, state.w, state.h);
  state.paused = false;

  function onScroll() {
    state.scrollRatio = getScrollRatio();
  }
  window.addEventListener('scroll', onScroll, { passive: true });

  function onResize() {
    const prevPaused = state.paused;
    if (state.rafId) cancelAnimationFrame(state.rafId);
    Object.assign(state, initCanvas());
    state.mistParticles = createMistParticles(state.quality.particles, state.w, state.h);
    state.paused = prevPaused;
    if (!state.paused) {
      state.rafId = requestAnimationFrame(t => animate(t, state, state.scrollRatio || 0));
    }
  }
  window.addEventListener('resize', onResize, { passive: true });

  state.rafId = requestAnimationFrame(t => animate(t, state, 0));
}
```

---

### Task 6: 頁面整合與啟動

**Files:**
- Modify: `index.html` — 更新現有 JS，接入山水動畫

- [x] **Step 1: 在 DOMContentLoaded 中啟動山水動畫**

```javascript
// 取代現有 Hero 入口動畫，整合到啟動流程
document.addEventListener('DOMContentLoaded', () => {
  startLandscape();

  // 原 Hero 入場動畫（保留，動畫延遲縮短）
  const heroChars = document.querySelectorAll('.hero-char');
  const heroDivider = document.querySelector('.hero-divider');
  const heroContent = document.querySelector('.hero-content');
  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      heroChars.forEach(c => c.classList.add('is-visible'));
      heroDivider.classList.add('is-visible');
      heroContent.classList.add('is-visible');
    });
  });
});
```

- [x] **Step 2: 清理無用的舊程式碼**

移除或註解掉以下內容：
- `#mouse-glow` 相關 JS（mouse move listener）
- `.hero-ink-bg` 相關程式碼已移除（Task 1 Step 2）
- 確保 scrolling 仍然保留 timeline progress 等既有功能
- 浮動字符 `.floating-chars` CSS 中的 `opacity` 從原本值降低到 0.15

---

### Task 7: 滾出視口暫停動畫

- [x] **Step 1: 使用 IntersectionObserver 暫停/恢復動畫**

```javascript
// Pause animation when hero is far out of view
const heroSection = document.querySelector('.hero');
if (heroSection && 'IntersectionObserver' in window) {
  const heroObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      state.paused = !entry.isIntersecting;
      if (state.paused && state.rafId) {
        cancelAnimationFrame(state.rafId);
        state.rafId = null;
      } else if (!state.paused && !state.rafId) {
        state.rafId = requestAnimationFrame(t => animate(t, state, state.scrollRatio || 0));
      }
    });
  }, { threshold: 0, rootMargin: '0px 0px 100% 0px' });
  heroObserver.observe(heroSection);
}
```

注意：這需要在 `state` 變數可訪問的位置執行（在 `startLandscape` 內或之後）。
