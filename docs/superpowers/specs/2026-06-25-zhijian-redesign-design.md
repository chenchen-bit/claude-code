---
comet_change: redesign-index
role: technical-design
canonical_spec: openspec
---

# 之間 — 品牌概念页重新设计 · 技术设计

## 1. 视觉架构

### 1.1 色彩系统

| Token | 颜色 | 用途 |
|-------|------|------|
| `--color-bg` | `#F5F0EB` | 主背景（宣纸白） |
| `--color-bg-alt` | `#EAE3DA` | 交替背景 |
| `--color-text` | `#1C1815` | 主文字（墨黑） |
| `--color-text-muted` | `#7A736C` | 次级文字 |
| `--color-text-light` | `#A69F98` | 弱化文字 |
| `--color-accent` | `#3B5E5C` | 主强调（墨绿） |
| `--color-accent-warm` | `#C23B22` | 暖强调（朱红点缀） |
| `--color-border` | `#D6D0C9` | 边框 |
| `--color-ink` | `rgba(28,24,21,0.06)` | 水墨半透明层 |

### 1.2 排版

- 标题：`Noto Serif SC` (weight: 200/300/400/600)
- 正文：`Noto Sans SC` (weight: 300/400/500)
- 西文：`Playfair Display` (italic)
- 竖排文字: `writing-mode: vertical-rl` 在引文区块使用

### 1.3 间距

保留原有 spacing scale，新增 `--space-3xl: 16rem` 用于大幅留白区域。

## 2. 区块设计

### 2.1 Hero

```
┌──────────────────────────────────┐
│   浮动汉字背景 (CSS animation)    │
│                                  │
│   SVG filter 水墨晕染背景层       │
│                                  │
│       之          間              │
│       ← 动画滑入 →              │
│                                  │
│   ──── 分隔线渐显 ────           │
│   介于传统与现代之间的生活美学    │
│   概念店 · 生活选品 · 文化空间    │
│                                  │
│           滚 动 (竖排)           │
└──────────────────────────────────┘
```

实现：
- SVG `<filter id="ink-wash">` 定义水墨纹理
- 汉字分左右动画入场（`transform: translateX` → `translateX(0)`）
- 浮动汉字用 `position: absolute` + `animation: drift` 随机路径（多个 `@keyframes`）
- 背景水墨层用 `mix-blend-mode: multiply`

### 2.2 品牌故事（卷轴时间线）

```
┌──────────────────────────────────┐
│          Philosophy              │
│                                  │
│    ● ──── 2018 │ 缘起            │
│                │ 品牌概念萌芽    │
│    ────────────┼────             │
│                │ 2020 ●          │
│            立 | 首场展览         │
│                │                 │
│    ● ──── 2023 │ 成长            │
│                │ 空间落成        │
│    ────────────┼────             │
│                │ 2025 ●          │
│            融 | 走向国际         │
└──────────────────────────────────┘
```

实现：
- 左侧竖线 (`::before` with `height` animation)
- 节点圆点 (`border-radius: 50%` + scale-in animation)
- 文字左右交替：`nth-child(odd)` 左文右线，`nth-child(even)` 右文左线
- 每个 `.timeline-item` 由 IntersectionObserver 触发入场

### 2.3 理念展示（水平滚动）

```
┌──────────────────────────────────────────┐
│  ← [承] │ [融] │ [创] →                │
│      Inheritance │ Fusion │ Creation     │
│      尊重传统     │ 差异和谐 │ 创造新可能  │
└──────────────────────────────────────────┘
```

实现：
- `overflow-x: auto` + `scroll-snap-type: x mandatory`
- 卡片 `scroll-snap-align: center`
- 左右箭头按钮（桌面端），触摸滑动（移动端）
- 每个卡片 hover 时：背景水墨扩散动画（`clip-path` 或 `mask-image` 动画）
- 当前卡片居中放大效果

### 2.4 氛围画廊

```
┌──────┬──────┬──────┐
│  ✦   │  ◈   │  ❋   │
│      │      │      │
│  ──  │  ──  │  ──  │
│  ～   │  庭  │  器  │
│  茶  │      │      │
├──────┼──────┼──────┤
│  花  │   ✦  │  ～   │
│      │      │      │
└──────┴──────┴──────┘
```

实现：
- `column-count: 3`（桌面）`column-count: 2`（平板）`column-count: 1`（移动）
- 每项为 `display: inline-block; break-inside: avoid`
- 内容使用 unicode 符号和汉字组合成诗意网格
- 悬停时背景水墨晕染

### 2.5 联系区

- 简化为：一句问候 + email 链接 + 社交媒体
- 保留原有设计 DNA 但更简洁

## 3. 动画系统

| 动画 | 实现 | 触发 |
|------|------|------|
| 水墨晕染 | SVG feTurbulence + feColorMatrix | 页面加载 |
| 汉字入场 | CSS `@keyframes` translateX | 页面加载 (rAF) |
| 浮动汉字 | CSS `@keyframes drift` 多路径 | 页面加载 |
| 时间线展开 | CSS height 动画 + IntersectionObserver | 滚动触发 |
| 卡片高亮 | CSS `scroll-snap` + IntersectionObserver | 滚动对齐 |
| 鼠标光晕 | `mousemove` JS → CSS `radial-gradient` 位置 | 鼠标移动 |
| 晕染 hover | CSS `mask-image` 动画 | hover |

### 3.1 性能

- SVG filter 动画限制在 30fps 范围内（使用 `will-change: filter`）
- IntersectionObserver `rootMargin` 提前 100px 加载
- 浮动汉字使用 `transform` + `opacity`（GPU 合成）
- `prefers-reduced-motion: reduce` 禁用全部动画

## 4. 文件结构

所有代码保留在 `index.html` 一个文件中：
- CSS：约 600-800 行，按区块划分
- HTML：语义化标签 + ARIA
- JS：约 150 行，IIFE 模式

## 5. 响应式断点

| 断点 | 布局 |
|------|------|
| < 640px | 单列，简化动画 |
| 640-1024px | 两列画廊，时间线单侧 |
| 1024-1280px | 三列画廊，理想布局 |
| > 1280px | 最大宽度限制 1280px |

## 6. 无障碍

- 所有 ARIA labels 标注
- 键盘导航支持水平滚动卡片
- `prefers-reduced-motion` 完整支持
- 颜色对比度 WCAG AA
- Focus visible 样式

## 7. 风险与缓解

| 风险 | 缓解 |
|------|------|
| SVG filter 性能 | 限制动画区域大小，`will-change` |
| 水平滚动可发现性 | 显示箭头提示，`scroll-snap` 明确对齐 |
| 无真实产品图效果 | 使用 unicode 符号 + 汉字组合，保持风格统一 |
| 移动端触摸 | 确保滚动容器 touch 事件正常穿透 |
