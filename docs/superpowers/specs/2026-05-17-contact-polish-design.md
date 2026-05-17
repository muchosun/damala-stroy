# DAMALA STROY Landing — Contact Polish Design

## Goal

Polish the existing landing page without breaking its current premium visual concept. The client already likes the look, so the next iteration should improve contact accessibility and mobile usability rather than redesign the page.

## Agreed Direction

We will keep the current page structure and visual language, then add a restrained contact layer:

- **Desktop header**
  - Keep logo, navigation, and visible phone number.
  - Add compact Telegram and WhatsApp icon buttons beside the phone.

- **Mobile header**
  - Keep the header visually clean with logo plus burger menu.
  - Replace the hidden phone treatment with a lower fixed floating capsule containing:
    - Telegram
    - WhatsApp
    - Phone

- **Mobile menu behavior**
  - Burger menu reveals a refined dropdown / glass panel with anchors:
    - Пакеты
    - Работы
    - Процесс
    - Расчёт
  - Before scrolling, the page should remain especially clean.
  - After the user scrolls, the header may become slightly more compact and the menu interaction can feel subtly more dynamic, while staying restrained.

## UX Principles

1. **Do not disturb the first impression.** The hero section should remain visually dominant.
2. **Contacts should feel native, not bolted on.** They should look like part of the original design system.
3. **Mobile access beats visual cleverness.** The lower capsule exists because it is easier to reach with one hand.
4. **No extra CTA clutter yet.** We will not add new sticky sales messages until there is evidence the page needs them.

## Versioning and Rollback

All previous versions must remain recoverable.

Implementation will use:

- **Git history** for every meaningful stage.
- **Explicit checkpoint commits** before and after each notable change.
- **Named git tags** for important restore points:
  - `v0-original-published`
  - `v1-contact-polish`
  - future tags for later milestones
- **Snapshot files** in a dedicated archive directory when useful for quick visual reference.

Rollback requirement:

- It must always be possible to restore:
  1. the original published landing page,
  2. any tagged milestone,
  3. any intermediate commit if needed.

## Non-Goals

- No full redesign.
- No new content sections.
- No pricing or copy rewrite in this iteration.
- No new lead-capture logic beyond the current form and contact links.

## Expected Outcome

After this iteration, the site should:

- keep its current premium feel,
- make Telegram / WhatsApp / phone easier to access,
- feel more intentional on mobile,
- remain safely reversible at every stage.
