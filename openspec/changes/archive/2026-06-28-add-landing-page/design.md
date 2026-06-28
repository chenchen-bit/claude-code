## Context

当前"创客"品牌系列只有 login.html 和 register.html，缺少一个给新访客看到的第一页。需要新建 landing.html，以全屏视频背景制造品牌冲击力，延续暗色 + 青色 (#00d4ff) 的视觉语言。

## Goals / Non-Goals

**Goals:**
- 新建 landing.html，全屏视频 hero + 下方内容区
- 视频使用 Pexels CDN 免费视频（直接 `<video>` 引用，不下载到本地）
- 视觉风格与 login/register 一致（暗色背景、Inter 字体、青色强调）

**Non-Goals:**
- 不涉及后端逻辑
- 不涉及用户认证
- 不改造现有页面

## Decisions

- **视频来源：Pexels CDN** — 选择 Pexels 而非 Coverr，因为 Pexels 视频 URL 返回 200 可直接引用，Coverr 有 hotlink 保护
- **视频文件：** `https://videos.pexels.com/video-files/11345330/11345330-hd_1920_1080_30fps.mp4` — 日落河面云霞，60s，温暖金色调与暗色 UI 形成反差，天空区域占比大适合放标题
- **遮罩方式：** 视频上方叠加从半透明黑到更暗的渐变层 + 青色氛围光，确保文字可读性
- **页面结构：** 单页 scroll 式，先全屏 hero，然后下方内容区折叠进入
- **性能策略：** `<video>` 设置 `preload="auto"` `muted` `playsinline`，手机端自动播放需要 muted。video 用 CSS `object-fit: cover` 铺满
- **无外部依赖：** 纯 HTML+CSS+JS，无框架

## Risks / Trade-offs

- **CDN 可用性** → Pexels 链接可能出现访问波动。备选：切换为其他 Pexels 视频 URL 或下载至本地
- **视频加载慢** → 28MB 在弱网环境可能延迟。通过 `poster` 属性设首帧截图兜底
- **移动端自动播放限制** → `muted` + `playsinline` 确保 iOS Safari 可以自动播放
