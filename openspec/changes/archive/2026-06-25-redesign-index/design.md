# 高层设计决策

## 架构

- 单文件 HTML，所有 CSS/JS 内联
- 零外部依赖（除 Google Fonts）
- 渐进增强：JS 增强动画，无 JS 时内容仍可读

## 视觉系统

### 色彩（方向 A）
- 背景：宣纸白/米白渐变 → `#F5F0EB` 至 `#EAE3DA`
- 文字：墨黑 `#1C1815`、灰 `#7A736C`
- 强调色：保留原有墨绿 `#3B5E5C`，增加朱红 `#C23B22` 作为点缀
- 水墨元素：半透明 `rgba(28, 24, 21, 0.03-0.12)`

### 排版
- 保留 Noto Serif SC 和 Playfair Display
- 增大 hero 汉字，引入竖排文字实验
- 行间留白更充分

### 区块设计
1. **Hero**：汉字渐显 + 浮动水墨粒子（CSS 实现）
2. **品牌故事**：卷轴式展开时间线（JS 控制 IntersectionObserver）
3. **理念展示**：保留「承融创」但改为水平滚动卡片
4. **氛围画廊**：竖向瀑布流布局（CSS columns）
5. **联系方式**：保留但更简洁

### 动画
- 所有动画遵循 `prefers-reduced-motion`
- 新增：视差滚动、水墨晕染效果（CSS mask-image 动画）
- 过渡曲线保持 `cubic-bezier(0.22, 1, 0.36, 1)`

## 响应式策略

- Mobile-first：320px 起
- 断点：640px（mobile landscape）、1024px（tablet）、1280px（desktop）
- 移动端：单列布局、增大触控目标、简化动画
