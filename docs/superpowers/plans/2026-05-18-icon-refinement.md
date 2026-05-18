# Icon Refinement Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the custom contact SVGs with cleaner Bootstrap Icons-style SVGs and slightly enlarge the mobile floating contact capsule.

**Architecture:** Keep the landing as one static HTML file. Update only the icon SVG markup and contact-control sizing CSS, then verify through existing structural tests plus icon-specific assertions.

**Tech Stack:** HTML, CSS, inline SVG, Python unittest, Git, GitHub Pages

---

### Task 1: Test icon refinement requirements

**Files:**
- Modify: `/Users/aleksandrsvistov/Documents/Damala/tests/test_contact_polish.py`

- [ ] Add assertions that the page contains Bootstrap Icons class markers for Telegram, WhatsApp, and telephone.
- [ ] Add assertions that mobile contact icons are enlarged beyond the previous 44px size.
- [ ] Run `python3 -m unittest discover -s tests -p 'test_*.py'` and confirm the new tests fail before implementation.

### Task 2: Replace SVGs and enlarge mobile contact controls

**Files:**
- Modify: `/Users/aleksandrsvistov/Documents/Damala/index.html`

- [ ] Replace Telegram SVGs with Bootstrap Icons-compatible `bi bi-telegram` markup.
- [ ] Replace WhatsApp SVGs with Bootstrap Icons-compatible `bi bi-whatsapp` markup.
- [ ] Replace phone SVG with Bootstrap Icons-compatible `bi bi-telephone-fill` markup.
- [ ] Increase mobile floating contact icon size from `44px` to `52px`.
- [ ] Increase mobile SVG size slightly so the icons read clearly.
- [ ] Run tests and confirm they pass.
- [ ] Commit the change.

### Task 3: Publish final icon polish

**Files:**
- Modify: Git state only.

- [ ] Tag the milestone as `v2-icon-refinement`.
- [ ] Push `main` and the tag.
- [ ] Verify production contains `bi bi-telegram` and `mobile-contact-bar`.
