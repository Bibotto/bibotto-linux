# Bibotto Linux — Architecture

**Status:** Initial architecture baseline  
**Release:** No verified ISO release yet

## 1. Project Overview

Bibotto is a Debian 13 (Trixie)-based, amd64 Linux distribution using KDE Plasma 6. Its goals are a modern, premium, minimal desktop experience, a carefully selected default software set, and optional software choices during installation.

## 2. Design Principles

- Modern, premium, minimal desktop experience.
- Prefer reliable Debian packages and established upstream components.
- Keep the default installation focused.
- Provide optional software through the installer.
- Prioritize security, recoverability, and maintainability.
- Clearly distinguish implemented features from plans and unverified assumptions.

## 3. Platform

| Component | Decision |
|---|---|
| Base | Debian 13 Trixie |
| Architecture | amd64 / x86_64 |
| Desktop | KDE Plasma 6 |
| Display manager | SDDM |
| Primary session | Wayland |
| Compatibility goal | X11 |
| Image | Hybrid ISO |
| Build system | Debian live-build |
| Installer | Calamares 3.3.14 |
| Init system | systemd |
| Live environment | Debian live-boot |
| Preferred filesystem | Btrfs |
| Encryption goal | LUKS2 |

These are project decisions, not proof of successful implementation.

## 4. Build Architecture

The project uses Debian live-build.

- `config/` contains build configuration.
- `config/package-lists/` contains active package lists.
- `config/includes.chroot/` contains files copied into the live filesystem.
- `config/hooks/` contains build hooks and may include system-provided hook symlinks.
- Root-level package planning files are not automatically active live-build package lists.

The current configuration targets Debian Trixie repositories: `main`, `contrib`, and `non-free-firmware`.

The reviewed active package lists contain 111 unique package names. An APT dependency simulation completed without visible resolver errors.

The optional-package payload has also been assembled as an ISO-contained local APT repository. It contains 1,059 `.deb` archives and occupies approximately 678 MB. Its package index was generated with `apt-ftparchive`. A separate isolated APT test successfully loaded the local repository and resolved all dependencies for the Development and Email package groups. This was a simulation, not an actual package installation.

A complete ISO build has not been verified.

## 5. Live System and Installed System

The live environment and installed system have different responsibilities.

1. The ISO boots the live environment.
2. Calamares partitions and mounts the target disk.
3. `unpackfs` transfers the live filesystem to the target.
4. Calamares configures the installed system.
5. Live-only components are removed where appropriate.

Optional applications must not be installed into the live root if that root is copied to the target. They are delivered through a separate ISO-contained local APT repository and are intended to be installed only when selected.

The repository is stored at `config/includes.binary/bibotto-repo`, so its contents are intended to appear in the ISO root. Calamares shellprocess configurations prepare the target system to use this repository before the package installation step and restore the original APT sources afterward.

The repository and shellprocess integration are configured. Their behavior during a real Calamares installation remains unverified.

## 6. Optional Installer Packages

The intended optional groups are:

- Development: `build-essential`, `docker.io`, `docker-compose`.
- Email: KMail and Thunderbird.

LibreOffice is part of the standard desktop installation and is installed by default.

All package archives and required dependencies should be included in the ISO. The installer should allow the user to select none, one, or multiple groups.

The packagechooser configuration and offline repository integration are present. The local repository has passed an isolated APT index and dependency-resolution simulation. Real installation behavior remains untested.

## 7. Desktop Identity

Visual direction: modern, premium, minimal, and original.

- Breeze Light and Breeze Dark remain core theme options.
- Viola-Dark-Plasma, Vivid Dark Plasma, and Slot Dark Plasma are planned optional themes.
- Desktop concept: clean panel, restrained translucent bottom dock, search-first launcher.
- Graphite: `#171B22`
- Off-white: `#F4F5F7`
- Turquoise: `#20A9B5`
- Blue-purple: `#6674D9`
- Typography direction: Inter and JetBrains Mono.
- Logo direction: original geometric eagle head, strong and elegant without a military or heraldic appearance.

The Calamares branding directory contains `branding.desc` and the Development and Email package-choice SVG illustrations. Branding is incomplete: referenced logo, welcome image, and slideshow assets still need to be supplied or their references removed.

## 8. Storage and Boot

The current configuration describes EFI/GRUB settings, Btrfs subvolumes `@` and `@home`, `noatime`, `compress=zstd`, and LUKS2 support.

The automatic partitioning configuration also describes an ext4 `/boot` partition and Btrfs root partition.

BIOS/UEFI boot, encryption, partitioning, and recovery behavior require virtual-machine testing.

## 9. Security and Updates

The package plan includes AppArmor, firewalld, unattended-upgrades, password quality controls, and NetworkManager.

The exact update cadence, repository policy, signing process, and kernel support policy remain to be finalized.

## 10. Development Environment

Development takes place in Debian under WSL2 on Windows 11. Both environments access the same project directory. There must be one authoritative project tree, not separate copies.

WSL development is not a substitute for testing the ISO on real firmware and hardware.

## 11. Open Architecture Decisions

- Real Calamares installation test of the offline optional-package repository.
- Final Calamares branding and missing asset references.
- Supported boot modes and partitioning combinations.
- Update and release policy.
- X11 fallback scope.
- Kernel support and rollback policy.

<!-- bibotto-luks-boot-design -->
## LUKS açılış mimarisi

Bibotto'nun hedef otomatik bölüm düzeni:
- EFI System Partition: FAT32, şifrelenmemiş.
- `/boot`: ext4, şifrelenmemiş.
- `/`: LUKS2 içinde Btrfs.
- Btrfs alt birimleri: `@` ve `@home`.
- Açılışta initramfs üzerinden kullanıcıdan LUKS parolası istenir.

GRUB'un kernel ve initramfs dosyalarına erişebilmesi için `/boot` açık kalır. LUKS anahtar dosyası initramfs içine yerleştirilmez. Calamares'in `luksbootkeyfile` modülü bu tasarımda kullanılmaz.

Calamares 3.3.14-1'in `fstab` modülü, şifrelenmiş kök + açık `/boot` düzeninde crypttab seçeneklerini boşalttığından, kök crypttab kaydına `luks` seçeneği eklenmelidir. Bu düzeltme `fstab` sonrasında, initramfs oluşturulmadan önce yapılacaktır.

## 2026-11-10 — Build Entry Point

`auto/build` is the project build entry point. It validates and synchronizes
`branding/calamares/bibotto/` into the Calamares live filesystem include
directory, then invokes `lb build noauto`. Set
`BIBOTTO_BRANDING_SYNC_ONLY=1` to test branding synchronization without
starting a full ISO build.

## Build Entry Point and Branding Synchronization

The build entry point is `auto/build`. Before invoking live-build, it validates
and synchronizes the authoritative Calamares branding assets from
`branding/calamares/bibotto/` into
`config/includes.chroot/etc/calamares/branding/bibotto/`.

For synchronization-only testing, set `BIBOTTO_BRANDING_SYNC_ONLY=1`.
This exits after copying the assets and does not invoke the ISO build.

## BIOS and UEFI Bootloader Design

- Target architecture: amd64 / x86_64.
- Calamares uses GRUB for both BIOS and UEFI installations.
- BIOS installation uses `grub-install --target=i386-pc` and the boot device selected by Calamares.
- UEFI installation uses the x86_64 EFI GRUB target, with the EFI System Partition mounted at `/boot/efi`.
- EFI bootloader ID is `Bibotto`; EFI fallback installation is enabled.
- GRUB configuration uses Bibotto branding, a five-second timeout and default entry zero.
- The automatic encrypted-root layout keeps `/boot` unencrypted and uses a LUKS2 Btrfs root.
- 32-bit UEFI and non-x86_64 architectures are outside the current project target.
- Actual BIOS and UEFI installation and boot tests remain pending until an ISO is available.
