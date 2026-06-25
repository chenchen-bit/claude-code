---
change: redesign-index
design-doc: docs/superpowers/specs/2026-06-25-zhijian-redesign-design.md
base-ref: no-git
---

# 之間 品牌概念页 — 重新设计实施计划

## 概述

基于 Design Doc 中确认的「东方意境 · 沉浸叙事」方向，对 `index.html` 进行完整视觉重构。所有代码保留单文件内联。

## 实施步骤

### 第一阶段：基础框架
1. HTML 结构重写 — 语义化标签、ARIA 标注、区块顺序
2. CSS 设计令牌更新 — 色彩系统、间距、字体配置
3. 全局样式 — Reset、排版系统、SVG filter 定义

### 第二阶段：核心区块
4. Hero 区 — SVG feTurbulence 水墨背景 + 汉字「之間」入场动画 + 浮动汉字
5. 品牌故事 — 纵向卷轴时间线（4 个节点）
6. 理念展示 — 水平滚动卡片（承/融/创 + scroll-snap）
7. 氛围画廊 — CSS column-count 瀑布流（字形占位）
8. 联系区 + 页脚 — 简洁版

### 第三阶段：交互与动画
9. 导航滚动效果 + 鼠标跟随光晕
10. IntersectionObserver 滚动触发 + 视差效果

### 第四阶段：打磨
11. 响应式适配（640/1024/1280px 断点）
12. prefers-reduced-motion + 无障碍完善
