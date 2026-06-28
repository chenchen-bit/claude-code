# Login Page Redesign: Minimalist Futuristic

## Change: `redesign-login-futuristic`

### Status
- OpenSpec change created: `openspec/changes/redesign-login-futuristic/`
- Comet state initialized: `.comet.yaml` (phase: open, workflow: full)
- Proposal: ❌ pending
- Design: ❌ pending
- Tasks: ❌ pending

---

## Design Direction

**Style**: 极简未来 (Minimalist Futuristic)
- **Background**: Pure black `#050505` + subtle grid texture
- **Accent**: Single neon color `#00d4ff` (electric blue)
- **Typography**: Inter, clean sans-serif, generous whitespace
- **Card**: Borderless or ultra-thin border, subtle shadow
- **Inputs**: Underline style, neon glow on focus
- **Button**: Neon border + glow expansion on hover

---

## Execution Plan

### Phase 1: Open (Create Artifacts)

1. **Create `proposal.md`**
   - Why: Current glassmorphism style → minimalist futuristic for tech feel
   - What: Full redesign of login.html, keep all features
   - Capabilities: `futuristic-login-ui`
   - Impact: login.html only

2. **Create `design.md`**
   - Color system: CSS variables for dark theme + neon accent
   - Typography: Inter font, size scale
   - Spacing: 4px grid system
   - Components: Input, button, card, social buttons
   - Animation: Timing functions, durations

3. **Create `tasks.md`**
   - Task list with checkboxes for each implementation step

### Phase 2: Design (Deep Design)

- Detailed CSS design system
- Animation specifications
- Layout grid and component dimensions

### Phase 3: Build (Implementation)

Execute tasks from tasks.md:

1. **Base & Reset** — CSS reset, body background, CSS variables
2. **Background Effects** — Grid texture, subtle particle animation
3. **Card Container** — Borderless card, centering, shadow
4. **Brand Header** — Logo with neon glow, title
5. **Input Fields** — Underline style, neon focus glow, icons
6. **Password Toggle** — Visibility toggle button
7. **Options Row** — Remember me checkbox, forgot password link
8. **Primary Button** — Neon border, hover glow, active state
9. **Divider** — Minimal "或" divider
10. **Social Buttons** — Google/Apple with consistent style
11. **Footer** — Register link
12. **Animations** — Page load fade-in, input focus transitions
13. **Responsive** — Mobile adaptation (<480px)
14. **JS Interactions** — Password toggle, form submit, pre-fill

### Phase 4: Verify

- Open in browser, test all interactions
- Check mobile responsive
- Verify neon effects render correctly

### Phase 5: Archive

- Run archive script
- Move change to archive directory

---

## File Structure After Completion

```
login.html (modified)
openspec/changes/redesign-login-futuristic/
├── .openspec.yaml
├── .comet.yaml
├── proposal.md ✅
├── design.md ✅
└── tasks.md ✅
```

---

## How to Resume

In a new opencode session, run:
```
/comet
```

The system will detect the active change `redesign-login-futuristic` and resume from the current phase.
