# Brainstorm Summary

- Change: redesign-index-ink-wash
- Date: 2026-06-25

## 确认的技术方案

方案 **A+C 融合**：单一 Canvas 全页固定背景 + 按滚动分区的叙事式景观演化。

- 架构：一个 `<canvas>`，`position: fixed; z-index: 0`，覆盖全页
- 内容层：各 section 背景改为 `rgba(245, 240, 235, 0.85)` + `backdrop-filter: blur(12px)`
- Canvas 2D API（非 WebGL），无外部依赖

## 关键取舍与风险

| 决策 | 取舍 |
|------|------|
| 单一 Canvas fixed | 整页都需要背景透明化，section 颜色调整 |
| 滚动分区叙事 | 4 个分区对应页面内容，景观变化驱动视觉节奏 |
| `backdrop-filter` | 现代浏览器支持好，但低端机可能性能问题 |
| 透过内容看到山水 | 需要密切注意文字可读性，对比度足够 |

## 测试策略

- 手动确认山水逐层渲染
- 各 partition 滚动景观变化流畅
- 跨 section 内容可读性
- prefers-reduced-motion 静态降级
- 移动端 <768px 降级测试

## Spec Patch

无 — 现有 specs 已覆盖需求。补充说明：从 Hero-only 扩展为全页覆盖。
