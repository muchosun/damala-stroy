# Contact Polish Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add restrained desktop messenger actions, a mobile floating contact capsule, and a mobile dropdown menu while preserving the current landing-page concept and publishing each milestone.

**Architecture:** Keep the site as a single static HTML document. Extend the existing header with new contact controls, add mobile-only fixed UI elements, and use a tiny inline script for menu and scroll state. Git remains the only rollback system, with milestone commits and tags.

**Tech Stack:** HTML, CSS, vanilla JavaScript, Git, GitHub Pages

---

## File Map

- Modify: `/Users/aleksandrsvistov/Documents/Damala/index.html`
  - Desktop contact icons
  - Mobile burger menu
  - Mobile floating contact capsule
  - Responsive and scroll-state styles
  - Inline JavaScript for menu state
- Keep as reference: `/Users/aleksandrsvistov/Documents/Damala/docs/superpowers/specs/2026-05-17-contact-polish-design.md`

### Task 1: Add desktop contact controls

**Files:**
- Modify: `/Users/aleksandrsvistov/Documents/Damala/index.html`

- [ ] **Step 1: Record current rollback point**

Run:
```bash
git status --short
git tag --list
```

Expected:
```text
clean working tree
v0-original-published
```

- [ ] **Step 2: Add desktop icon actions to the header**

Add a `.header-actions` container that holds Telegram, WhatsApp, and phone actions:

```html
<div class="header-actions">
  <a class="contact-icon" href="https://t.me/" aria-label="Telegram">...</a>
  <a class="contact-icon" href="https://wa.me/79181792703" aria-label="WhatsApp">...</a>
  <a class="phone" href="tel:+79181792703">+7 918 179-27-03</a>
</div>
```

Use inline SVG icons so the static page needs no extra assets.

- [ ] **Step 3: Add supporting desktop styles**

Add styles for:

```css
.header-actions { display:flex; align-items:center; gap:10px; }
.contact-icon { width:42px; height:42px; ... }
.contact-icon:hover { ... }
```

- [ ] **Step 4: Verify desktop rendering locally**

Run:
```bash
python3 -m http.server 8000
```

Expected:
- page loads at `http://localhost:8000`
- Telegram and WhatsApp icons appear beside the phone number
- hero layout remains unchanged

- [ ] **Step 5: Commit checkpoint**

```bash
git add index.html
git commit -m "Add desktop contact actions"
```

### Task 2: Add mobile navigation and floating contact capsule

**Files:**
- Modify: `/Users/aleksandrsvistov/Documents/Damala/index.html`

- [ ] **Step 1: Add mobile-only markup**

Add:

```html
<button class="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-menu">...</button>
<div class="mobile-menu" id="mobile-menu">...</div>
<div class="mobile-contact-bar">...</div>
```

The mobile menu contains links to:

```html
<a href="#tariffs">Пакеты</a>
<a href="#portfolio">Работы</a>
<a href="#process">Процесс</a>
<a href="#contact">Расчёт</a>
```

The floating bar contains Telegram, WhatsApp, and phone icons.

- [ ] **Step 2: Add responsive CSS**

At mobile breakpoints:

```css
.nav,
.header-actions .phone { display:none; }
.menu-toggle { display:grid; }
.mobile-contact-bar { display:flex; }
```

Add a bottom safe-area aware floating capsule:

```css
.mobile-contact-bar {
  position: fixed;
  left: 50%;
  bottom: max(16px, env(safe-area-inset-bottom));
  transform: translateX(-50%);
}
```

- [ ] **Step 3: Add scroll and menu behavior**

Add inline JavaScript:

```js
const header = document.querySelector('.topbar');
const toggle = document.querySelector('.menu-toggle');
const mobileMenu = document.querySelector('.mobile-menu');

window.addEventListener('scroll', () => {
  header.classList.toggle('is-scrolled', window.scrollY > 24);
});

toggle.addEventListener('click', () => {
  const open = mobileMenu.classList.toggle('is-open');
  toggle.setAttribute('aria-expanded', String(open));
});

mobileMenu.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    mobileMenu.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
  });
});
```

- [ ] **Step 4: Verify mobile behavior**

Use browser responsive mode or resize the page below 560 px.

Expected:
- burger visible in header
- desktop nav hidden
- lower floating bar visible
- menu opens and closes
- menu closes after clicking an anchor
- scrolling compacts the header subtly without breaking layout

- [ ] **Step 5: Commit checkpoint**

```bash
git add index.html
git commit -m "Add mobile menu and floating contact bar"
```

### Task 3: Verify, tag, and publish

**Files:**
- Modify: `/Users/aleksandrsvistov/Documents/Damala/index.html`

- [ ] **Step 1: Run final local verification**

Run:
```bash
python3 -m http.server 8000
```

Verify:
- desktop header contains Telegram, WhatsApp, and phone
- mobile header contains logo and burger
- mobile lower capsule contains Telegram, WhatsApp, and phone
- anchors scroll to the correct sections
- no visible breakage in hero, tariffs, portfolio, process, or contact sections

- [ ] **Step 2: Tag the polished milestone**

```bash
git tag v1-contact-polish
```

- [ ] **Step 3: Push and publish**

```bash
git push origin main
git push origin v1-contact-polish
```

Expected:
- GitHub Pages rebuilds from `main`
- public site updates at `https://muchosun.github.io/damala-stroy/`

- [ ] **Step 4: Verify production**

Run:
```bash
curl -L -s https://muchosun.github.io/damala-stroy/ | grep -q 'mobile-contact-bar'
curl -I https://muchosun.github.io/damala-stroy/
```

Expected:
- HTML contains the new mobile contact markup
- HTTP status is `200`

- [ ] **Step 5: Commit plan state if needed**

If any final adjustments were required during verification:

```bash
git add index.html
git commit -m "Polish contact interactions after verification"
git push origin main
git tag -f v1-contact-polish
git push -f origin v1-contact-polish
```
