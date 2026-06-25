# Brainstorm Summary

- Change: redesign-index
- Date: 2026-06-25

## 确认的技术方案

### Hero 区
- SVG filter (feTurbulence) 水墨纹理背景 + CSS 动画晕染扩散
- 汉字「之間」入场动画（从两侧滑入 + 墨迹显现）
- 浮动汉字装饰（CSS animation 随机漂移）

### 品牌故事
- 纵向卷轴式时间线：一条竖线贯穿，节点 scroll reveal 入场，文字左右交替
- 纯 CSS + IntersectionObserver

### 理念卡片「承融创」
- 水平滚动容器，桌面端拖拽/箭头滚动，移动端触摸滑动
- 水墨晕染 hover 效果

### 氛围画廊
- CSS `column-count` 瀑布流，零 JS
- 使用字形/符号占位（无实际产品图情况）

### 新元素
- 浮动汉字（CSS animation 漂移）
- 竖排引文穿插区块
- 鼠标跟随光晕效果（可选）

## 关键取舍与风险

- SVG feTurbulence filter 可能在某些浏览器上性能开销大 — 限制动画频率，叠加 `will-change`
- 水平滚动卡片需要良好的触摸支持 — 用 CSS scroll-snap + 轻量 JS 拖拽
- `column-count` 在高度动态内容下顺序可能不符合预期 — 可接受，品牌展示页不要求严格排序

## 测试策略

- 浏览器直接打开验证，无需测试框架
- 手动测试：桌面 Chrome/Safari/Firefox + 移动端 Safari/Chrome
- `prefers-reduced-motion` 验证

## Spec Patch

无 — 本次不涉及 delta spec 变更
