---
comet_change: redesign-login-futuristic
role: technical-design
canonical_spec: openspec
archived-with: 2026-06-25-redesign-login-futuristic
status: final
---

# Login Page Redesign: Minimalist Futuristic

## Context

当前 `login.html` 是一个单文件登录页面，采用 glassmorphism 风格（半透明卡片 + backdrop-filter blur），紫色渐变主题。需要将其重新设计为「极简未来」风格——暗黑背景 + 霓虹点缀 + 流畅过渡动效。

## Goals / Non-Goals

**Goals:**
- 实现暗黑背景 + 霓虹点缀的极简未来视觉风格
- 保持所有现有功能完整可用
- 流畅的微交互动效（聚焦、悬停、点击反馈）
- 保持移动端响应式支持

**Non-Goals:**
- 不新增功能或修改认证逻辑
- 不引入新依赖或框架
- 不修改 `register.html` 或其他文件

## Design Decisions

### 1. CSS 变量系统

```css
:root {
  --bg-primary: #050505;
  --bg-card: #0a0a0a;
  --bg-input: transparent;
  --accent: #00d4ff;
  --accent-glow: rgba(0, 212, 255, 0.4);
  --accent-dim: rgba(0, 212, 255, 0.15);
  --text-primary: #ffffff;
  --text-secondary: #888888;
  --text-muted: #444444;
  --border: #1a1a1a;
  --border-focus: #00d4ff;
  --radius: 12px;
  --font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --transition-fast: 0.15s ease;
  --transition-normal: 0.3s ease;
  --transition-slow: 0.6s ease-out;
}
```

### 2. 卡片设计

纯色背景 `#0a0a0a`，1px `#1a1a1a` 边框，去掉 `backdrop-filter`。圆角 12px，微妙 `box-shadow: 0 4px 24px rgba(0,0,0,0.5)`。

### 3. 输入框

底线式设计：透明背景，底部 1px `#1a1a1a` 线条。聚焦时线条变为 `#00d4ff` 并添加 `box-shadow: 0 1px 8px rgba(0,212,255,0.3)`。图标在聚焦时同步变为霓虹色。

### 4. 主按钮

透明背景 + 1px `#00d4ff` 边框，文字 `#00d4ff`。悬停时 `box-shadow: 0 0 16px rgba(0,212,255,0.4)`。点击时 `transform: scale(0.98)`。

### 5. 动效规格

| 场景 | CSS 属性 | 时长 |
|------|---------|------|
| 页面载入 | opacity + translateY | 0.6s ease-out |
| 输入框聚焦 | border-color + box-shadow | 0.3s ease |
| 按钮悬停 | box-shadow | 0.3s ease |
| 按钮点击 | transform | 0.15s ease |

### 6. 背景

去掉浮动粒子和渐变光球，保留极简网格纹理（线条更细，透明度更低）。

## Risks / Trade-offs

- **对比度风险**：纯黑背景下弱化文字可能对比度不足 → 确保 text-secondary ≥ 4.5:1
- **视觉层次**：去掉 glassmorphism 后卡片层次感降低 → 用 box-shadow 补偿
- **兼容性**：box-shadow 和 CSS transitions 广泛支持，无兼容风险

## Implementation Plan

按 tasks.md 顺序执行，共 12 个任务组，约 30 个子任务。原地重写 login.html。
