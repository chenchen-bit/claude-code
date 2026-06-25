# Comet Design Handoff

- Change: redesign-index
- Phase: design
- Mode: compact
- Context hash: f76bd9f6ec7757f528c8d5bea61bafe37d42585c0c4daf999afc85b14768d8a9

Generated-by: comet-handoff.sh

OpenSpec remains the canonical capability spec. This handoff is a deterministic, source-traceable context pack, not an agent-authored summary.

## openspec/changes/redesign-index/proposal.md

- Source: openspec/changes/redesign-index/proposal.md
- Lines: 1-58
- SHA256: c0e453ba32e88c753b810267d9dd4bad4fcf4f1fd83cc849f1cf56880288bbfd

```md
# 重新设计 index.html — 提案

## 背景

`index.html` 是「之間」品牌概念页。当前版本采用暖色调侘寂风格，以「之间」哲学为核心，展示品牌理念。页面功能是静态品牌展示，无交互式商业功能。

## 当前问题

1. **视觉层次单一** — 当前 Hero 只有两个大字+一条线，缺少视觉锚点
2. **内容深度不足** — 页面只有约 4 个区块，作为品牌落地页信息量偏低
3. **缺少产品展示** — 作为 lifestyle 品牌概念页，没有视觉化的产品/氛围呈现
4. **交互局限** — 仅有 scroll reveal，缺少沉浸式体验
5. **响应式细节** — 移动端布局过于简单地改为纵向排列，缺少针对性设计
6. **品牌叙事** — 「承融创」三个理念很好，但呈现方式较平铺直叙

## 设计方向

### 方向 A：东方意境 · 沉浸叙事（推荐）

强化品牌哲学与东方美学的沉浸感，以「留白、水墨、光影变化」为视觉语言。

- 新 Hero：水墨渐变背景 + 动态粒子/浮动汉字
- 增加「品牌故事」区块：时间线或卷轴式展开
- 产品/氛围展示：竖向瀑布流或横向滚动画廊
- 动画升级：视差滚动、文本渐显、鼠标跟随
- 保留核心品牌色，增加水墨黑与宣纸白

### 方向 B：现代极简 · 国际视野

偏向国际品牌官网风格，以西式 grid 布局呈现东方内容。

- 全屏 Hero：大幅背景图/视频 + 精简文案
- 卡片式布局展示品牌理念
- 干净利落的动画过渡
- 更多留白，更少的装饰性元素

### 方向 C：复古融合 · 工艺质感

以手工感、印刷质感为特色，模拟纸张/印刷品体验。

- 纹理背景（纸纹、印刷网点）
- 手写风格标题字
- 复古排版：竖排文字、印章元素
- 加载动画模拟纸张展开

## 范围

- 仅修改 `index.html` 一个文件
- 保持零依赖、零构建工具、纯前端
- 保持 Google Fonts 在线字体
- 不引入 JavaScript 框架或库

## 不包含

- 多页面路由
- 后端或数据库
- 购物车/电商功能
- 用户登录
```

## openspec/changes/redesign-index/design.md

- Source: openspec/changes/redesign-index/design.md
- Lines: 1-38
- SHA256: b468763166437d4790f99e12a750c9a740335ed2db1a6a4db73f424e0da7a280

```md
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
```

## openspec/changes/redesign-index/tasks.md

- Source: openspec/changes/redesign-index/tasks.md
- Lines: 1-27
- SHA256: a091ed5b2ceb43f26c867fde1642f384d83378cfff67717fd6d767c64d6d62c9

```md
# 任务清单

## 阶段 1：基础框架
- [ ] HTML 结构重写（语义化标签、ARIA 标注）
- [ ] CSS 设计令牌与配色系统更新
- [ ] 全局样式（Reset、排版系统）

## 阶段 2：区块实现
- [ ] Hero 区：水墨效果 + 汉字渐显动画
- [ ] 品牌故事：卷轴式时间线
- [ ] 理念展示：水平滚动卡片（承/融/创）
- [ ] 氛围画廊：竖向瀑布流
- [ ] 联系区 + 页脚

## 阶段 3：交互与动画
- [ ] 导航栏滚动效果
- [ ] IntersectionObserver 滚动触发动画
- [ ] 视差滚动效果
- [ ] 水墨/浮动粒子 CSS 动画
- [ ] 鼠标跟随效果（可选）

## 阶段 4：打磨
- [ ] 响应式适配（320px-1280px+）
- [ ] prefers-reduced-motion 支持
- [ ] 无障碍 (a11y) 完善
- [ ] 性能优化
- [ ] 浏览器兼容性检查
```

