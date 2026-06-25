---
comet_change: redesign-index-ink-wash
role: technical-design
canonical_spec: openspec
archived-with: 2026-06-25-redesign-index-ink-wash
status: final
---

# 全页水墨山水动画 — 技术设计

## 1. 架构总览

```
┌──────────────────────────────────┐
│  <canvas> (fixed, z-index: 0)    │  ← 山水渲染层
│  ├─ 远山  (5层, perlin noise)    │
│  ├─ 云雾  (40-80 粒子)          │
│  └─ 墨晕  (定时随机扩散)        │
├──────────────────────────────────┤
│  内容层 (半透明, backdrop-filter) │  ← 各 section 叠加
│  ├─ .site-nav (fixed, z-index:100)│
│  ├─ .hero (z-index: 2)           │
│  ├─ timeline / pillars / gallery  │
│  └─ contact / footer             │
└──────────────────────────────────┘
```

**关键设计**：`<canvas>` 在 DOM 中紧贴 `<body>` 开头，固定定位。所有现有内容 position 层级高于 canvas。各 section 背景改为半透明白/暖灰，让山水透出。

## 2. 渲染引擎

### 2.1 山峦生成

依赖：纯数学函数，无外部库。

```
Perlin Noise → 山脊线顶点数组
    ↓
二次贝塞尔曲线 → 平滑山形轮廓
    ↓
渐变 fill (黑到透明) → 墨色填充
    ↓
globalCompositeOperation = 'multiply' → 层叠混合
    ↓
5 层, 从远到近, opacity: 0.08 → 0.8
```

- 使用经典 Perlin noise 实现（simplex 变体，~30 行 JS）
- 每层由 60–120 个顶点构成
- 颜色：远山 `rgba(44,40,36,0.08)` → 近山 `rgba(44,40,36,0.80)`
- 层间距为 viewport 高度的 15–25%

### 2.2 云雾粒子系统

- 粒子数量：40–80（移动端 25）
- 每粒子属性：x, y, size, speed, phase, depth
- 动画：x 以 speed 速度右移（循环），opacity = sin(phase + time) 映射到 [0, 0.4]
- 形状：`arc()` 绘制，`shadowBlur` 制造朦胧感

### 2.3 墨滴晕染

- 每 3–8 秒随机触发
- 以随机位置为中心，用 `createRadialGradient` 绘制多层半透明圆
- 半径从 0 扩展到 60–150px，透明度随之衰减
- 生命周期 2–4 秒

### 2.4 动画循环

```javascript
let lastTime = 0;
function animate(time) {
  const dt = Math.min(time - lastTime, 33); // cap at ~30fps delta
  lastTime = time;
  ctx.clearRect(...);
  drawMountains(dt, scrollRatio);
  drawMist(dt);
  drawInkSplashes(dt);
  requestAnimationFrame(animate);
}
```

- `scrollRatio`: 0 → 1，由 `window.scrollY / (documentHeight - viewportHeight)` 计算

## 3. 滚动叙事分区

使用 IntersectionObserver + scroll event 驱动 `renderState`：

```javascript
const PARTITIONS = [
  { name: 'hero',     range: [0, 0.15] },
  { name: 'story',    range: [0.15, 0.40] },
  { name: 'gallery',  range: [0.40, 0.65] },
  { name: 'ending',   range: [0.65, 1.0] },
];
```

**各分区景观参数**：

| 分区 | 山前景 opacity | 云密度 | 墨色基调 | 特殊效果 |
|------|---------------|--------|---------|---------|
| hero (0–0.15) | 1.0 | 高 | 淡墨 + 留白 | 山峦从水面升起 |
| story (0.15–0.40) | 0.7 | 中 | 浓墨 | 山形丰富，云雾在山间 |
| gallery (0.40–0.65) | 0.3 | 中 | 重墨 | 山下水面波光 |
| ending (0.65–1.0) | 0 | 低 | 焦墨渐收 | 墨晕归寂 |

## 4. Section 背景调整

| 原 class | 原 background | 改为 |
|---------|-------------|------|
| `body` | `--color-bg (#F5F0EB)` | 不变（Canvas 在 body 下） |
| `.timeline-section` | `--color-surface (#FAF7F3)` | `rgba(250, 247, 243, 0.85)` + `backdrop-filter: blur(16px)` |
| `.pillars-section` | 无（继承 body） | `rgba(245, 240, 235, 0.80)` |
| `.gallery-section` | `--color-surface` | 同上半透明 |
| `.contact-section` | 无 | `rgba(245, 240, 235, 0.85)` |
| `.site-footer` | 无 | `rgba(245, 240, 235, 0.90)` |
| `.site-nav.scrolled` | `rgba(245,240,235,0.85)` + blur | 保留不变 |

## 5. 文字可读性保障

- 所有文字色维持现有 `--color-text (#1C1815)` 和 `--color-text-muted (#7A736C)`
- 关键区（hero 大字、timeline、gallery）在 Canvas 上方测试对比度
- `backdrop-filter: blur(16px)` 确保背景杂讯不会干扰阅读
- `prefers-reduced-motion` 时：Canvas 渲染静态帧，动画循环跳过

## 6. 移动端与效能

**检测顺序**：

```javascript
const isMobile = window.innerWidth < 768;
const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
let lowPower = isMobile || prefersReduced;
```

**降级层级**：

| 级别 | 条件 | 山层 | 粒子 | 墨晕 | 分辨率 |
|------|------|------|------|------|--------|
| 高 | Desktop | 5 | 80 | 启用 | devicePixelRatio |
| 中 | <1024px | 4 | 40 | 启用 | 1x |
| 低 | <768px | 3 | 25 | 禁用 | 1x |
| 零 | reduced-motion | 3 (静态) | 0 | 禁用 | 1x |

**已排除的问题**：
- iOS Safari Canvas memory：限制 Canvas 尺寸 ≤2048px
- 滚动性能：`requestAnimationFrame` 在不可见时暂停（使用 IntersectionObserver）
- 电池寿命：移动端帧率 cap 到 30fps

## 7. 旧效果处理

| 效果 | 处理 |
|------|------|
| `.hero-ink-bg` SVG filter | 移除（全面被 Canvas 取代） |
| `#mouse-glow` | 移除 |
| `.floating-chars` | 保留，opacity 降低到 0.15，不与山水争抢视觉 |
| `.hero-char` 动画 | 保留，动画延迟缩短 |
| `.hero-divider` | 保留，但 canvas 追加墨痕扩散 |
| `.hero-content` fade-in | 保留 |
| `#ink-wash` filter SVG | 移除（不再需要） |

## 8. 文件变更清单

唯一变更文件：`index.html`

变更范围：
- `<head>`：新增 `<style>` 中 Canvas 样式
- `<body>`：顶部插入 `<canvas>`，移除 SVG ink filter
- `<style>`：新增 Canvas 相关 CSS + 各 section 背景改为半透明
- `<script>`：新增 ~200–300 行渲染引擎 JS
- 移除：SVG filter defs、mouse-glow div

无新依赖，无新文件，单文件自包含。
