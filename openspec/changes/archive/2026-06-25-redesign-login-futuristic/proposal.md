## Why

当前登录页采用 glassmorphism + 紫色渐变风格，视觉上偏向柔和梦幻。需要重新设计为「极简未来」风格——暗黑背景 + 霓虹点缀 + 流畅过渡动效，以提升产品的科技感和现代感，同时保持所有现有功能不变。

## What Changes

- 完整重新设计 `login.html` 的 HTML 结构、CSS 样式和 JS 交互
- 配色方案：纯黑/深黑背景 + 单一霓虹色（电光蓝 #00d4ff）点缀
- 布局重构：更简洁的几何构型，大量留白，精确线条
- 动效升级：输入框聚焦光效、按钮悬停过渡、页面载入动画
- 保留所有现有功能：邮箱/密码登录、记住我、忘记密码、密码可见切换、Google/Apple 社交登录、注册链接

## Capabilities

### New Capabilities

- `futuristic-login-ui`: 极简未来风格登录页面的视觉设计、交互效果和响应式布局

### Modified Capabilities

（无）

## Impact

- **文件**：`login.html`（单文件全量修改）
- **依赖**：无新增依赖，仍使用 Google Fonts (Inter) 和原生 JS
- **兼容性**：需保持移动端（<480px）响应式支持
