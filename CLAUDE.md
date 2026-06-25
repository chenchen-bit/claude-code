# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This workspace contains standalone front-end projects and utility scripts. No build systems, package managers, or test frameworks are used — everything runs directly in the browser or via the Python interpreter.

## Projects

- **index.html** — "之間" (Zhijian), a Chinese lifestyle brand concept page. Pure HTML+CSS+JS, open by double-clicking or `open index.html`.
- **login.html** — "创客" (Maker) login page with glassmorphism UI. Open directly in browser.
- **pomodoro.py** — CLI Pomodoro timer. Run with `python3 pomodoro.py`.

## Architecture Notes

- All projects are self-contained single files — no imports, no build step, no dependencies.
- CSS is inlined in `<style>` blocks (no external stylesheets).
- JavaScript uses vanilla JS with no frameworks. IE11 is not targeted.
- `index.html` uses Google Fonts (`Noto Serif SC`, `Noto Sans SC`, `Playfair Display`) loaded via `@import` in the HTML — offline development needs internet for first load.
- `login.html` uses the Inter font from Google Fonts via `@import` in `<style>`.

## Commands

```bash
# Open a page in browser
open index.html
open login.html

# Run the Pomodoro timer
python3 pomodoro.py

# Run Pomodoro with custom durations (in minutes)
python3 pomodoro.py -w 25 -s 5 -l 15

# Run N cycles then exit
python3 pomodoro.py -c 4

# Disable macOS notifications
python3 pomodoro.py --no-notify
```
