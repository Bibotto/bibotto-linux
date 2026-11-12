# Bibotto — Brand Guidelines

## 1. Brand Identity

- Name: Bibotto
- Design direction: Modern, premium, minimal technology brand
- Design principles: Clarity, consistency, usability, originality

## 2. Logo Direction

- Concept: Original geometric eagle head
- Character: Sharp, strong, elegant and forward-looking
- Status: Approved concept; artwork postponed
- Avoid: Traditional heraldic or military emblem appearance

## 3. Brand Colors

| Color | Hex | Purpose |
|---|---|---|
| Graphite | #171B22 | Primary dark brand color |
| Off-white | #F4F5F7 | Primary light brand color |
| Signature Turquoise | #20A9B5 | Brand identity and decorative accents |
| Blue-purple | #6674D9 | Secondary brand identity |

Signature colors are preserved for branding and visual identity.
Functional UI colors may use adjusted shades for accessibility.

## 4. Light Theme

| Token | Hex |
|---|---|
| Background | #F4F5F7 |
| Surface | #FFFFFF |
| Alternate surface | #E9EDF1 |
| Primary text | #202630 |
| Secondary text | #66717E |
| Border | #DCE1E7 |
| Accent | #087780 |
| Accent hover | #06636A |
| Secondary accent | #5967C8 |
| Selection background | #087780 |
| Selection foreground | #FFFFFF |

### Light Status Colors

- Success: #237A59
- Warning: #956000
- Error: #B33A43
- Info: #286A9B

## 5. Dark Theme

| Token | Hex |
|---|---|
| Background | #171B22 |
| Surface | #202630 |
| Elevated surface | #29323D |
| Primary text | #F4F5F7 |
| Secondary text | #AAB4C0 |
| Border | #343E4A |
| Accent | #35BAC5 |
| Accent hover | #4BC7D1 |
| Secondary accent | #AAB4FF |
| Selection background | #35BAC5 |
| Selection foreground | #171B22 |

### Dark Status Colors

- Success: #2E9D72
- Warning: #D99A32
- Error: #D85B63
- Info: #4A91C7

## 6. Accessibility

- Target WCAG AA contrast for normal text: at least 4.5:1.
- Target WCAG AA contrast for large text: at least 3:1.
- Do not use signature turquoise #20A9B5 for small text on light backgrounds.
- Use theme-specific functional accent colors.
- Selection foreground and background must remain clearly distinguishable.
- Never communicate status using color alone; combine color with icons or labels.

## 7. Typography

- Interface: Inter
- Terminal and code: JetBrains Mono

## 8. Desktop Design

- KDE Plasma 6
- Wayland primary, X11 fallback
- Original light and dark themes
- Minimal translucent bottom dock
- Clean top system panel
- Search-first application launcher
- Consistent icons, spacing and window styling

## 9. Design Principles

- Original design, not a clone of another operating system
- Preserve Breeze as the foundational KDE theme infrastructure
- Include Breeze Light and Breeze Dark
- Include optional Viola-Dark-Plasma, Vivid Dark Plasma and Slot Dark Plasma themes
- Prefer native KDE functionality
- Avoid unnecessary desktop extensions
- Support high-DPI displays and accessibility
- Keep animations restrained and optional

## Calamares Asset Sources

- Authoritative source directory: `branding/calamares/bibotto/`
- ISO target directory: `config/includes.chroot/etc/calamares/branding/bibotto/`
- Current source assets: `branding.desc`, `development.svg`, `email.svg`
- The existing package chooser illustrations are preserved.
- Logo artwork and Calamares product images are not yet implemented.
- Keep source assets authoritative; `auto/build` synchronizes the ISO target from this directory before a build.
