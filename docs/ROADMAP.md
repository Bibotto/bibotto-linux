# Bibotto Linux — Roadmap

**Status:** Initial roadmap. No release dates are committed.

## Phase 1 — Project Foundation

- [x] Select Debian 13 Trixie.
- [x] Select amd64 as initial architecture.
- [x] Select KDE Plasma 6 and SDDM.
- [x] Establish live-build configuration structure.
- [x] Establish initial package-list baseline.
- [ ] Document reproducible build procedure.
- [ ] Define project versioning.

**Exit criteria:** A clean environment can produce an ISO from documented configuration.

## Phase 2 — Bootable Live Image

- [x] Resolve live-build configuration and hook issues.
- [x] Build the first complete hybrid ISO.
- [x] Generate and record the ISO SHA-256 checksum.
- [x] Boot the live ISO in a Hyper-V Generation 2 UEFI virtual machine.
- [x] Test legacy BIOS boot in Hyper-V Generation 1.
- [ ] Verify desktop, networking, audio, display, and installer startup.

## Phase 3 — Calamares Installation

- [x] Create initial Calamares 3.3.14 settings and module configuration.
- [x] Complete static Calamares configuration audit.
- [ ] Validate Calamares configuration at runtime.
- [ ] Complete Bibotto branding.
- [ ] Test automatic and manual partitioning.
- [ ] Test Btrfs and any retained ext4 path.
- [ ] Test LUKS2 encryption.
- [ ] Test users, locale, keyboard, services, initramfs, and GRUB.
- [ ] Verify live-only package cleanup.

## Phase 4 — Offline Optional Software

- [x] Design and assemble an ISO-contained local APT repository.
- [x] Include optional package archives and simulated dependency closure.
- [x] Add Calamares packagechooser configuration.
- [x] Add optional Development group.
- [x] Add optional Email group.
- [x] Add shellprocess configuration for temporary repository setup and cleanup.
- [ ] Validate the complete workflow through a real Calamares installation.
- [ ] Verify unselected packages remain absent.
- [ ] Test installation without network access.
- [ ] Clean temporary repository configuration after installation.

## Phase 5 — Desktop Identity

- [ ] Complete original Bibotto logo and visual identity.
- [ ] Populate Calamares branding.
- [ ] Integrate approved panel, dock, and launcher layout.
- [ ] Retain Breeze Light and Breeze Dark.
- [ ] Package optional Plasma themes.
- [ ] Validate fonts, icons, portals, scaling, and accessibility.
- [ ] Check WCAG AA contrast for project-controlled UI assets.

## Phase 6 — Hardware and Reliability

- [ ] Test AMD graphics.
- [ ] Test Intel and NVIDIA paths where applicable.
- [ ] Test Wi-Fi, Bluetooth, audio, suspend/resume, and external displays.
- [ ] Test upgrades and recovery.
- [ ] Validate kernel fallback and initramfs regeneration.
- [ ] Test different disk layouts.

## Phase 7 — Release Engineering

- [ ] Define versions and release channels.
- [ ] Define security and update policy.
- [ ] Establish ISO signing and checksum publication.
- [ ] Create release notes and build records.
- [ ] Run the complete release test matrix.

## Current Focus

The first hybrid ISO has been built and structurally verified. BIOS Generation 1 and UEFI Generation 2 live boots both reached KDE Plasma. Current focus: Calamares installation testing and offline package validation; Secure Boot remains a separate test.

The first ISO build and structural inspection succeeded. BIOS and UEFI live boots have been verified in Hyper-V. Calamares installation and installed-system boot remain untested.

### Calamares Configuration Audit — 2026-11-10

The configuration/source review of the remaining six Calamares module
files is complete. Runtime validation is still pending and belongs to
the first ISO build and virtual-machine test phase.


### First Hybrid ISO — 2026-11-11

- [x] Build `bibotto-linux-amd64.hybrid.iso` successfully.
- [x] Record SHA-256 checksum.
- [x] Verify BIOS El Torito boot entry.
- [x] Verify UEFI El Torito boot entry.
- [x] Verify live SquashFS, kernel, and initrd inside the ISO.
- [x] Boot and test the live ISO in a BIOS virtual machine.
- [x] Boot and test the live ISO in a UEFI virtual machine.
- [ ] Validate Calamares installation and offline package selection.
