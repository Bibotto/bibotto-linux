# Bibotto Plasma Theme — Research and Technical Decisions

**Last updated:** 2026-11-14  
**Project:** Bibotto Linux  
**Scope:** KDE Plasma 6 desktop theme architecture and color integration  
**Status:** Research completed; implementation not started

---

## 1. Purpose

This document records the research, technical findings, design decisions,
and next steps for developing the original Bibotto desktop theme family
for KDE Plasma 6.

It is intended to be a self-contained continuation reference. It should
allow development to resume without repeating the initial research.

This document distinguishes between:

- Verified findings from the existing local system and source files.
- Current Bibotto design decisions.
- Proposed implementation details that still require testing.

No Plasma theme implementation has been created or tested as part of
this research stage.

## 2. Project Design Direction

Bibotto will use an original desktop identity rather than exposing an
existing third-party theme as its primary visual identity.

Design principles:

- Modern, premium, minimal technology aesthetic.
- Consistent visual language across the desktop.
- Original Bibotto visual assets.
- Light and Dark variants.
- Readability and accessibility.
- KDE Plasma 6 compatibility.
- Wayland as the primary session, X11 as fallback.

The Manjaro Breath theme was examined as a technical reference only.
Bibotto will not distribute Manjaro branding or simply adopt Breath
unchanged.

Breeze assets and technical dependencies may remain installed when
required by KDE or Plasma. This does not mean Breeze should be the
user-facing Bibotto theme.

## 3. Existing Project Environment

### 3.1 Platform

- Distribution base: Debian 13 Trixie.
- Architecture: amd64.
- Desktop: KDE Plasma 6.
- Inspected Plasma desktop theme package version: `6.3.5-1`.
- Development environment: Debian 13 under WSL2.
- Project root: `~/Bibotto`.

### 3.2 Existing Bibotto color assets

The current color source of truth is:

`branding/colors.json`

Existing KDE color scheme sources:

- `branding/themes/light/Bibotto-Light.colors`
- `branding/themes/dark/Bibotto-Dark.colors`

Existing installed-image overlays:

- `config/includes.chroot/usr/share/color-schemes/Bibotto-Light.colors`
- `config/includes.chroot/usr/share/color-schemes/Bibotto-Dark.colors`

The existing `kdeglobals` overlays select `Bibotto-Light`:

- `config/includes.chroot/etc/xdg/kdeglobals`
- `config/includes.chroot/etc/skel/.config/kdeglobals`

The ISO build validation script also checks these selections.

The existing KDE color scheme files must be preserved and used as
the foundation for Plasma color integration.

## 4. Important Architectural Distinction

There are two related but separate KDE theming layers.

### 4.1 KDE Color Scheme

The `.colors` files control application and desktop color roles,
including window, view, button, selection, tooltip, and text colors.

Existing Bibotto files:

- `Bibotto-Light.colors`
- `Bibotto-Dark.colors`

These remain the authoritative Light and Dark color definitions.

### 4.2 Plasma Desktop Theme

The Plasma desktop theme controls the visual assets used by Plasma
components, including panels, widgets, tooltips, and desktop elements.

Typical theme assets include:

- `metadata.json`
- `plasmarc`
- `widgets/`
- `dialogs/`
- Optional `opaque/`, `solid/`, and `translucent/` assets.

Plasma SVG assets can use dynamic `ColorScheme-*` roles. This allows
the theme artwork to follow the currently selected system color scheme.

### 4.3 Bibotto architectural decision

The intended architecture is:

1. Maintain one Bibotto Plasma visual theme.
2. Maintain separate Bibotto Light and Dark KDE color schemes.
3. Use dynamic color roles in Plasma SVG assets wherever supported.
4. Avoid duplicating the complete Plasma theme solely to change colors.
5. Do not add a separate Plasma theme `colors` file unless testing
   demonstrates a specific technical requirement.

This is the selected design direction. Runtime behavior still needs
to be verified in the actual Plasma session.

## 5. Breeze Theme Inspection Findings

The local Breeze desktop theme was inspected under:

`chroot/usr/share/plasma/desktoptheme/`

### 5.1 Directory structure

The `default` theme contains the main SVG asset tree, including:

- `dialogs/`
- `icons/`
- `opaque/`
- `solid/`
- `translucent/`
- `widgets/`
- `metadata.json`
- `plasmarc`

The `breeze-light` and `breeze-dark` directories contain color,
metadata, and configuration files, but do not contain independent
copies of the complete SVG asset tree.

This indicates that the main asset tree and the color variants are
separated in the inspected installation.

### 5.2 Metadata observations

Inspected metadata:

- `default`: KPlugin ID `default`, Name `Breeze`.
- `breeze-light`: KPlugin ID `default`, Name `Breeze Light`.
- `breeze-dark`: KPlugin ID `breeze-dark`, Name `Breeze Dark`.

The inspected metadata reports API version `5.0`. This value must not
be confused with the installed Plasma package version.

### 5.3 plasmarc observations

The inspected `default/plasmarc` includes:

```ini
[Wallpaper]
defaultWallpaperTheme=Next
defaultFileSuffix=.png
defaultWidth=1920
defaultHeight=1080

[ContrastEffect]
enabled=true
contrast=0.2
saturation=10

[AdaptiveTransparency]
enabled=true
```

The Light and Dark variants use different contrast and intensity
settings.

These values are reference material, not final Bibotto settings.

### 5.4 SVG color-role inspection

The compressed SVG files in:

`chroot/usr/share/plasma/desktoptheme/default/widgets/`

were scanned for dynamic color-role names.

Observed occurrence counts:

| Color role | Occurrences |
|---|---:|
| ColorScheme-Text | 236 |
| ColorScheme-ButtonFocus | 195 |
| ColorScheme-ButtonText | 170 |
| ColorScheme-Highlight | 169 |
| ColorScheme-Background | 152 |
| ColorScheme-ButtonBackground | 147 |
| ColorScheme-ButtonHover | 83 |
| ColorScheme-ViewBackground | 72 |
| ColorScheme-NeutralText | 57 |
| ColorScheme-PositiveText | 56 |
| ColorScheme-ViewFocus | 55 |
| ColorScheme-ViewHover | 28 |
| ColorScheme-ViewText | 25 |
| ColorScheme-NegativeText | 3 |

These counts describe the inspected widget SVG files only. They are
not a complete inventory of every Plasma SVG asset.

The inspected SVGs use CSS classes such as:

- `.ColorScheme-Text`
- `.ColorScheme-Background`
- `.ColorScheme-Highlight`
- `.ColorScheme-ViewText`
- `.ColorScheme-ViewBackground`
- `.ColorScheme-ButtonText`
- `.ColorScheme-ButtonBackground`

Some SVGs also contain fallback color declarations.

The actual supported role names and their behavior must be checked
against the relevant KDE/Plasma implementation before finalizing
Bibotto SVG assets.

## 6. Bibotto Color System

The source of truth is `branding/colors.json`.

### 6.1 Brand palette

| Token | Value |
|---|---|
| Graphite | `#171B22` |
| Off-white | `#F4F5F7` |
| Turquoise | `#20A9B5` |
| Blue-purple | `#6674D9` |

### 6.2 Light palette

| Token | Value |
|---|---|
| Background | `#F4F5F7` |
| Surface | `#FFFFFF` |
| Surface elevated | `#FFFFFF` |
| Primary text | `#202630` |
| Secondary text | `#66717E` |
| Border | `#DCE1E7` |
| Accent | `#087780` |
| Accent hover | `#06636A` |
| Accent subtle | `#E5F6F7` |
| Secondary accent | `#5967C8` |
| Surface alternate | `#E9EDF1` |
| Selection background | `#087780` |
| Selection foreground | `#FFFFFF` |
| Focus | `#087780` |
| Hover | `#06636A` |
| Link | `#087780` |
| Visited link | `#5967C8` |
| Header | `#E9EDF1` |
| Tooltip | `#FFFFFF` |
| Complementary background | `#202630` |
| Complementary surface | `#29323D` |

### 6.3 Dark palette

| Token | Value |
|---|---|
| Background | `#171B22` |
| Surface | `#202630` |
| Surface elevated | `#29323D` |
| Primary text | `#F4F5F7` |
| Secondary text | `#AAB4C0` |
| Border | `#343E4A` |
| Accent | `#35BAC5` |
| Accent hover | `#4BC7D1` |
| Accent subtle | `#16383D` |
| Secondary accent | `#AAB4FF` |
| Surface alternate | `#202630` |
| Selection background | `#35BAC5` |
| Selection foreground | `#171B22` |
| Focus | `#35BAC5` |
| Hover | `#4BC7D1` |
| Link | `#35BAC5` |
| Visited link | `#AAB4FF` |
| Header | `#202630` |
| Tooltip | `#29323D` |
| Complementary background | `#11151B` |
| Complementary surface | `#202630` |

### 6.4 Status colors

| Status | Light | Dark |
|---|---|---|
| Success | `#237A59` | `#2E9D72` |
| Warning | `#956000` | `#D99A32` |
| Error | `#B33A43` | `#D85B63` |
| Info | `#286A9B` | `#4A91C7` |

### 6.5 Accessibility

The project target is WCAG AA:

- Normal text contrast: at least 4.5:1.
- Large text contrast: at least 3:1.
- The signature brand turquoise `#20A9B5` must not be used
  indiscriminately for small text on light backgrounds.
- Every final color-role pairing must be contrast-tested.

## 7. Proposed Plasma Color-Role Mapping

The following is a working proposal, not a finalized mapping.

| Plasma role | Proposed Bibotto token |
|---|---|
| ColorScheme-Text | `text_primary` |
| ColorScheme-Background | `background` |
| ColorScheme-Highlight | `selection_background` |
| ColorScheme-ViewBackground | `surface` |
| ColorScheme-ViewText | `text_primary` |
| ColorScheme-ButtonBackground | `surface` |
| ColorScheme-ButtonText | `text_primary` |
| ColorScheme-ButtonHover | `accent_subtle` |
| ColorScheme-ButtonFocus | `focus` |
| ColorScheme-ViewHover | `hover` |
| ColorScheme-ViewFocus | `focus` |

Important:

- This mapping must be validated against actual Plasma SVG usage.
- Hover and focus behavior may require refinement.
- Button text and background combinations must be contrast-tested.
- Status roles must not be assumed to be supported simply because
  their names appear in some inspected SVG files.
- The role list and semantics must be checked against KDE's
  implementation and documentation before production use.

## 8. Proposed Source and Installation Layout

The final source layout has not yet been created.

The intended installation location for the Plasma desktop theme is:

`/usr/share/plasma/desktoptheme/bibotto/`

Expected theme components:

- `metadata.json`
- `plasmarc`
- `widgets/`
- `dialogs/`
- Optional asset directories when required.

The exact source directory inside the Bibotto repository is still
to be decided after checking the existing project structure and
build conventions.

The existing KDE color scheme source files remain:

- `branding/themes/light/Bibotto-Light.colors`
- `branding/themes/dark/Bibotto-Dark.colors`

No duplicate color scheme source should be introduced.

## 9. Build Integration Findings

The existing `auto/build` script synchronizes Calamares branding
assets before running live-build.

It currently does not synchronize Plasma desktop theme assets.

The existing `scripts/build-iso.py` validates KDE color scheme
selection and ISO contents, but does not yet validate a Bibotto
Plasma desktop theme.

When implementation begins, build integration will need to:

1. Copy or install the Plasma theme into the correct chroot path.
2. Validate required metadata and assets.
3. Verify the theme is present in the generated ISO.
4. Avoid overwriting unrelated KDE system assets.
5. Preserve the existing KDE color scheme installation and selection.

These are future implementation tasks, not completed changes.

## 10. Initial Prototype Scope

The first prototype should be deliberately small.

Initial components:

1. Panel background.
2. Widget background.
3. Tooltip.
4. Button.

The prototype should use original Bibotto visual styling and dynamic
color roles wherever supported.

Breeze assets may be inspected as technical references, but the
prototype must not simply be a renamed copy of Breeze.

Missing assets and fallback behavior must be tested in Plasma.

## 11. Testing Plan

No runtime test has been completed yet for the proposed Bibotto
Plasma theme.

Testing should proceed in this order:

1. Validate `metadata.json` and theme directory structure.
2. Validate SVG syntax and referenced assets.
3. Install the prototype in the test Plasma environment.
4. Test with Bibotto Light color scheme.
5. Test with Bibotto Dark color scheme.
6. Test panel, widget, tooltip, and button rendering.
7. Test transparency and contrast behavior.
8. Test Wayland session.
9. Test X11 fallback if available.
10. Check Plasma logs for missing assets or theme errors.

Only after successful testing should the project documentation,
roadmap, and package/build configuration be updated.

## 12. Outstanding Decisions and Risks

The following are not finalized:

- Exact source directory for the Plasma theme.
- Final theme metadata and plugin identifiers.
- Final SVG artwork and element naming.
- Final `plasmarc` values.
- Final color-role mapping.
- Whether any additional Plasma asset directories are required.
- Runtime fallback behavior for missing assets.
- Build integration and ISO validation changes.

Compatibility must be tested against the actual Debian Trixie
Plasma version used by Bibotto. Findings from a newer Plasma release
must not be assumed to apply unchanged.

Third-party assets must not be incorporated without checking their
licenses and attribution requirements.

## 13. Next Development Steps

The next work session should continue from this sequence:

1. Confirm the existing repository source layout and build conventions.
2. Select the source location for the Bibotto Plasma theme.
3. Inspect the four initial reference SVG assets in detail.
4. Confirm supported SVG elements and dynamic color roles.
5. Create the minimal original Bibotto theme prototype.
6. Install and test it in the Plasma environment.
7. Refine Light and Dark rendering.
8. Integrate the tested theme into the live-build configuration.
9. Update project documentation after successful testing and approval.
10. Commit locally and push to GitHub after explicit approval.

---

## 14. Current Checkpoint

**Research stage:** Completed for the initial architecture investigation.

**Implementation stage:** Not started.

**Files changed during this research:** None.

**Existing color schemes:** Preserved.

**Plasma theme source:** Not yet created.

**Build integration:** Not yet implemented.

**Runtime testing:** Pending.

**Next action:** Begin detailed inspection of the Breeze reference SVGs
for the panel background, widget background, tooltip, and button.
