---
archived-with: 2026-06-25-redesign-login-futuristic
status: final
---
# Login Page Minimalist Futuristic Redesign - Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Redesign login.html from glassmorphism to minimalist futuristic style with dark background, neon accents, and smooth transitions.

**Architecture:** Single-file CSS/HTML/JS rewrite. Replace all visual styles while preserving HTML structure and JS logic. Use CSS variables for theming.

**Tech Stack:** HTML5, CSS3 (variables, transitions, keyframes), Vanilla JS, Google Fonts (Inter)

## Global Constraints

- Single file: `login.html` only
- No new dependencies
- Must maintain all existing functionality
- Mobile responsive (<480px)
- Inter font from Google Fonts
- localStorage authentication logic unchanged

---

### Task 1: CSS Reset & Variable System

**Files:**
- Modify: `login.html` (lines 7-64, replace entire `<style>` block)

**Interfaces:**
- Consumes: None (first task)
- Produces: CSS variable system used by all subsequent tasks

- [x] **Step 1: Replace CSS reset and body styles**

Replace the entire `<style>` content starting from the reset through body styles:

```css
*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

@import url('https://fonts.googleapis.com/css2?family=Inter:opsz@14..32&display=swap');

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

body {
  font-family: var(--font-family);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--bg-primary);
  overflow: hidden;
}
```

- [x] **Step 2: Verify in browser**

Open `login.html` in browser. Expected: black background, no visible content styling yet.

---

### Task 2: Background Effects

**Files:**
- Modify: `login.html` (remove .particle CSS, .bg::before, .bg::after; update .bg .grid)

**Interfaces:**
- Consumes: CSS variables from Task 1
- Produces: Clean background with subtle grid

- [x] **Step 1: Remove particle and gradient animations**

Delete the following CSS blocks entirely:
- `.bg::before` and its `@keyframes floatA`
- `.bg::after` and its `@keyframes floatB`
- All `.particle` styles and `@keyframes rise`

- [x] **Step 2: Update grid overlay**

Replace `.bg .grid` with:

```css
.bg .grid {
  position: absolute; inset: 0;
  background-image:
    linear-gradient(rgba(0,212,255,.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,212,255,.03) 1px, transparent 1px);
  background-size: 80px 80px;
}
```

- [x] **Step 3: Remove particle HTML elements**

In the `<body>`, remove all `<div class="particle"></div>` elements from the `.particles` container. Keep the `.particles` div itself or remove it entirely.

- [x] **Step 4: Verify in browser**

Expected: Clean black background with very subtle blue-tinted grid lines.

---

### Task 3: Card Container

**Files:**
- Modify: `login.html` (.card CSS)

**Interfaces:**
- Consumes: CSS variables from Task 1
- Produces: Styled card container for form elements

- [x] **Step 1: Replace .card styles**

Replace the `.card` CSS block with:

```css
.card {
  position: relative; z-index: 1;
  width: 420px;
  background: var(--bg-card);
  border-radius: var(--radius);
  border: 1px solid var(--border);
  box-shadow: 0 4px 24px rgba(0,0,0,0.5);
  padding: 44px 40px 40px;
  animation: cardIn var(--transition-slow) both;
}
```

- [x] **Step 2: Update cardIn animation**

Replace `@keyframes cardIn` with:

```css
@keyframes cardIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
```

- [x] **Step 3: Verify in browser**

Expected: Dark card with thin border, centered on black background, fades in on load.

---

### Task 4: Brand Header

**Files:**
- Modify: `login.html` (.brand CSS)

**Interfaces:**
- Consumes: CSS variables from Task 1
- Produces: Styled brand logo and title

- [x] **Step 1: Replace .brand styles**

Replace the brand-related CSS:

```css
.brand {
  text-align: center;
  margin-bottom: 32px;
}
.brand .logo {
  display: inline-flex;
  align-items: center; justify-content: center;
  width: 52px; height: 52px;
  border-radius: var(--radius);
  border: 1px solid var(--accent);
  box-shadow: 0 0 16px var(--accent-dim);
  margin-bottom: 12px;
}
.brand .logo svg {
  width: 26px; height: 26px;
  fill: var(--accent);
}
.brand h1 {
  color: var(--text-primary);
  font-size: 22px;
  font-weight: 600;
  letter-spacing: -.3px;
}
```

- [x] **Step 2: Verify in browser**

Expected: Logo with neon blue border and glow, white "创客" title.

---

### Task 5: Input Fields

**Files:**
- Modify: `login.html` (.form-group, .input-wrap, input CSS)

**Interfaces:**
- Consumes: CSS variables from Task 1
- Produces: Underline-style inputs with neon focus effect

- [x] **Step 1: Replace form group and input styles**

Replace all form-related CSS:

```css
.form-group {
  margin-bottom: 20px;
}
.form-group label {
  display: block;
  color: var(--text-secondary);
  font-size: 13px;
  font-weight: 500;
  margin-bottom: 8px;
}
.input-wrap {
  position: relative;
}
.input-wrap .icon {
  position: absolute;
  left: 0; top: 50%;
  transform: translateY(-50%);
  width: 18px; height: 18px;
  color: var(--text-muted);
  pointer-events: none;
  transition: color var(--transition-normal);
}
.input-wrap .icon svg { display: block; width: 100%; height: 100%; fill: currentColor; }
.input-wrap input {
  width: 100%;
  padding: 12px 12px 12px 30px;
  background: var(--bg-input);
  border: none;
  border-bottom: 1px solid var(--border);
  color: var(--text-primary);
  font-size: 15px;
  font-family: var(--font-family);
  outline: none;
  transition: border-color var(--transition-normal), box-shadow var(--transition-normal);
}
.input-wrap input::placeholder {
  color: var(--text-muted);
}
.input-wrap input:focus {
  border-bottom-color: var(--accent);
  box-shadow: 0 1px 8px var(--accent-dim);
}
.input-wrap:focus-within .icon {
  color: var(--accent);
}
```

- [x] **Step 2: Update password toggle button**

Replace `.toggle-pw` styles:

```css
.toggle-pw {
  position: absolute;
  right: 0; top: 50%;
  transform: translateY(-50%);
  background: none; border: none;
  color: var(--text-muted);
  cursor: pointer;
  padding: 4px;
  display: flex;
  transition: color var(--transition-normal);
}
.toggle-pw:hover { color: var(--text-secondary); }
.toggle-pw svg { width: 18px; height: 18px; fill: currentColor; display: block; }
```

- [x] **Step 3: Verify in browser**

Expected: Inputs show only bottom line, icons turn neon blue on focus, smooth transitions.

---

### Task 6: Options Row

**Files:**
- Modify: `login.html` (.options CSS)

**Interfaces:**
- Consumes: CSS variables from Task 1
- Produces: Styled checkbox and forgot password link

- [x] **Step 1: Replace .options styles**

```css
.options {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 20px 0 24px;
  font-size: 13px;
}
.options label {
  display: flex;
  align-items: center;
  gap: 8px;
  color: var(--text-secondary);
  cursor: pointer;
  user-select: none;
}
.options label input[type="checkbox"] {
  appearance: none;
  width: 16px; height: 16px;
  border: 1px solid var(--border);
  border-radius: 4px;
  background: transparent;
  cursor: pointer;
  flex-shrink: 0;
  transition: background var(--transition-normal), border-color var(--transition-normal);
  position: relative;
}
.options label input[type="checkbox"]:checked {
  background: var(--accent);
  border-color: var(--accent);
}
.options label input[type="checkbox"]:checked::after {
  content: '';
  position: absolute;
  left: 4px; top: 1px;
  width: 6px; height: 9px;
  border: solid var(--bg-primary);
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
}
.options a {
  color: var(--accent);
  text-decoration: none;
  font-weight: 500;
  opacity: 0.7;
  transition: opacity var(--transition-normal);
}
.options a:hover { opacity: 1; }
```

- [x] **Step 2: Verify in browser**

Expected: Neon blue checkbox when checked, subtle link hover effect.

---

### Task 7: Primary Button

**Files:**
- Modify: `login.html` (.btn-primary CSS)

**Interfaces:**
- Consumes: CSS variables from Task 1
- Produces: Neon border button with glow hover

- [x] **Step 1: Replace .btn-primary styles**

```css
.btn-primary {
  width: 100%;
  padding: 14px;
  border: 1px solid var(--accent);
  border-radius: var(--radius);
  background: transparent;
  color: var(--accent);
  font-size: 15px;
  font-weight: 600;
  font-family: var(--font-family);
  cursor: pointer;
  transition: box-shadow var(--transition-normal), transform var(--transition-fast);
}
.btn-primary:hover {
  box-shadow: 0 0 16px var(--accent-glow);
}
.btn-primary:active {
  transform: scale(0.98);
}
```

- [x] **Step 2: Remove ::after pseudo-element**

Delete the `.btn-primary::after` block entirely.

- [x] **Step 3: Verify in browser**

Expected: Transparent button with neon blue border, glows on hover, scales on click.

---

### Task 8: Divider & Social Buttons

**Files:**
- Modify: `login.html` (.divider, .social-btn CSS)

**Interfaces:**
- Consumes: CSS variables from Task 1
- Produces: Consistent divider and social login buttons

- [x] **Step 1: Replace .divider styles**

```css
.divider {
  display: flex;
  align-items: center;
  gap: 16px;
  margin: 24px 0;
  color: var(--text-muted);
  font-size: 12px;
}
.divider::before,
.divider::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--border);
}
```

- [x] **Step 2: Replace .social-btn styles**

```css
.social-row {
  display: flex;
  gap: 10px;
}
.social-btn {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 11px;
  border-radius: var(--radius);
  border: 1px solid var(--border);
  background: transparent;
  color: var(--text-secondary);
  font-size: 13px;
  font-family: var(--font-family);
  cursor: pointer;
  transition: border-color var(--transition-normal), box-shadow var(--transition-normal), color var(--transition-normal);
  text-decoration: none;
}
.social-btn:hover {
  border-color: var(--accent);
  box-shadow: 0 0 8px var(--accent-dim);
  color: var(--text-primary);
}
.social-btn svg { width: 18px; height: 18px; }
```

- [x] **Step 3: Verify in browser**

Expected: Minimal divider, social buttons glow subtly on hover.

---

### Task 9: Footer

**Files:**
- Modify: `login.html` (.footer CSS)

**Interfaces:**
- Consumes: CSS variables from Task 1
- Produces: Styled footer with register link

- [x] **Step 1: Replace .footer styles**

```css
.footer {
  text-align: center;
  margin-top: 24px;
  color: var(--text-muted);
  font-size: 13px;
}
.footer a {
  color: var(--accent);
  text-decoration: none;
  font-weight: 500;
  opacity: 0.7;
  transition: opacity var(--transition-normal);
}
.footer a:hover { opacity: 1; }
```

- [x] **Step 2: Verify in browser**

Expected: Weak text with neon link that brightens on hover.

---

### Task 10: Responsive

**Files:**
- Modify: `login.html` (@media query)

**Interfaces:**
- Consumes: All previous CSS
- Produces: Mobile-friendly layout

- [x] **Step 1: Update responsive styles**

```css
@media (max-width: 480px) {
  .card { width: calc(100% - 24px); padding: 32px 24px 28px; }
  .brand h1 { font-size: 20px; }
}
```

- [x] **Step 2: Verify on mobile viewport**

Use browser dev tools to test at 375px width. Expected: Card fills width with proper padding.

---

### Task 11: Final Verification

**Files:**
- None (verification only)

**Interfaces:**
- Consumes: All previous tasks
- Produces: Confirmed working login page

- [x] **Step 1: Full functionality test**

1. Open `login.html` in browser
2. Verify page loads with fade-in animation
3. Test email input focus (neon glow appears)
4. Test password input focus (neon glow appears)
5. Test password visibility toggle
6. Test "记住我" checkbox
7. Test "忘记密码" link hover
8. Test login button hover glow
9. Test Google button hover
10. Test Apple button hover
11. Test "立即注册" link hover
12. Test form submission with valid/invalid credentials
13. Test mobile layout (375px width)

- [x] **Step 2: Commit changes**

```bash
git add login.html
git commit -m "feat: redesign login page with minimalist futuristic style

- Dark background (#050505) with subtle grid texture
- Neon accent color (#00d4ff) for interactive elements
- Underline-style inputs with focus glow effect
- Transparent button with neon border and hover glow
- Smooth CSS transitions for all interactions
- Removed glassmorphism, particles, and gradient animations
- Maintained all existing functionality"
```
