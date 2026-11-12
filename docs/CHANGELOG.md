# Bibotto Linux — Changelog

All notable project changes should be recorded here. Version numbers will be assigned when the release policy is defined.

## [Unreleased]

### Added

- Initial project documentation baseline.
- Architecture, roadmap, status, and TODO documentation.
- Package manifest and installer design documentation.
- Initial security policy and testing plan.
- Calamares packagechooser configuration for Development and Email groups.
- ISO-contained local APT repository with 1,059 package archives.
- Local APT repository index generated with `apt-ftparchive`.
- Calamares shellprocess configurations for temporary offline repository setup and cleanup.
- Development and Email package-choice SVG illustrations.

### Changed

- Updated Calamares settings to run offline repository setup before package operations and cleanup afterward.
- Confirmed LibreOffice remains part of the default desktop package set.

### Validated

- Local APT repository index successfully loaded in an isolated test.
- Offline dependency-resolution simulation completed for all five optional package roots, resolving 1,059 packages without reported missing dependencies or conflicts.

### Remaining

- Audit shellprocess configuration and Calamares integration.
- Build and inspect the first hybrid ISO.
- Test real offline installation through Calamares.
- Complete Bibotto installer branding.

### Notes

No successful ISO build, live boot, or installation is claimed by this entry.

### 2026-11-10 — ISO identity

- Replaced Debian-default ISO application, preparer, publisher,
  volume ID, disk label, and image filename with Bibotto branding.
- Removed the `nocomponents=sddm` live boot parameter so the SDDM
  live-config component can configure live-session autologin.
- Kept `LB_NET_TARBALL=true`; it is inactive for the configured
  `iso-hybrid` image type.
- Validated shell syntax and metadata length limits.
- No ISO build or boot test is claimed.

## 2026-11-10

### Installer configuration review

- Completed review of the remaining six Calamares module configurations.
- Confirmed Plasma Workspace is part of the default desktop package list.
- Recorded that ISO-level and runtime validation remain pending.

## Development Environment
- [2026-11-10] Debian 13 WSL ortamına SVG rasterleştirme için librsvg2-bin (rsvg-convert) eklendi.

## 2026-11-10 — Calamares Branding Source Structure

- Added `branding/calamares/bibotto/` as the authoritative source directory.
- Added source copies of `branding.desc`, `development.svg`, and `email.svg`.
- Verified source and ISO include copies are identical.
- Automatic synchronization and original logo artwork remain pending.

## 2026-11-10 — Branding Build Synchronization

- Added executable `auto/build` using the Debian live-build `noauto` pattern.
- The build entry point validates and synchronizes Calamares branding sources
  before invoking `lb build noauto`.
- Added `BIBOTTO_BRANDING_SYNC_ONLY=1` to test synchronization without starting
  an ISO build.
- Shell syntax and sync-only tests passed. Full ISO build remains unverified.

## 2026-11-10 — Calamares Branding Build Synchronization

- Added automatic branding asset synchronization to `auto/build`.
- Added a synchronization-only test mode using
  `BIBOTTO_BRANDING_SYNC_ONLY=1`.
- Verified shell syntax, successful synchronization, and matching source/target
  directories.
- No ISO build was performed.

## 2026-11-10 — Offline Repository Emergency Cleanup

- Added a live-build overlay for the Calamares shellprocess module descriptor.
- Enabled emergency execution for the offline repository cleanup instance.
- Hardened cleanup so APT cache-cleaning failure does not prevent source restoration.
- Preserved backups when source restoration is incomplete.
- Added isolated success and failure-path tests.

## 2026-11-10 — Offline APT Repository Transaction Safety

- Added transaction-marker protection to offline repository setup and emergency cleanup.
- Added preflight collision checks for existing repository and APT source paths.
- Published the temporary APT source using an atomic rename.
- Made emergency cleanup a no-op when no active Bibotto transaction exists.
- Passed three isolated setup/cleanup integration scenarios.

## 2026-11-10 — Calamares Emergency Module Selection Audit

- Verified that only the offline repository cleanup shellprocess instance is marked for emergency execution.
- Confirmed setup and crypttab shellprocess instances remain non-emergency.

## 2026-11-10 — Calamares Module Availability Audit

- Audited all 24 modules referenced by the installer settings.
- Confirmed all Python entry points and native module libraries are present.
- Verified the project shellprocess overlay load target and emergency capability.
- Static module load-target audit passed with zero failures.

## 2026-11-10 — Calamares Unpackfs

- Added the Bibotto `unpackfs.conf` configuration.
- Added `rsync` to the installer live-system package list.
- Recorded static configuration checks; ISO and VM validation remain pending.

## 2026-11-10 — Mount and Fstab Audit

- Reviewed Calamares mount/fstab source code and schemas.
- Verified Btrfs subvolume and mount-option propagation paths.
- Documented static findings; runtime validation remains pending.

## 2026-11-10 — Calamares Users Audit

- Reviewed user account, password, autologin, and group settings.
- Verified the Debian sudo policy and Calamares defaultGroups syntax.
- No users.conf changes were required.

## 2026-11-10 — Calamares LUKS and Initramfs Audit

- Audited Calamares encrypted-root initramfs hook selection.
- Verified the cryptsetup live-build hook target and relevant package lists.
- Reviewed the custom crypttab LUKS option correction.
- Added six isolated crypttab behavior tests; all passed.

## 2026-11-10 — GRUB and UEFI Branding

- Changed the Calamares UEFI bootloader identity from debian to Bibotto.
- Validated the bootloader YAML configuration.
- Reviewed Calamares GRUB kernel parameter and installation behavior.
- Documented the live filesystem package path for BIOS and UEFI GRUB components.

## 2026-11-11 — SDDM and Plasma Audit

- Reviewed SDDM, Plasma session, live-user and systemd service configuration.
- Verified Calamares SDDM autologin handling against the packaged module source.
- Documented the separation between live-session autologin and installed-system login.

## 2026-11-11 — Network Configuration Audit

- Audited Calamares `networkcfg` placement and NetworkManager service configuration.
- Confirmed NetworkManager, WPA supplicant and wireless regulatory database packages are included.
- Confirmed no custom connection profiles are bundled.
- Static assertions passed; VM network testing remains pending.

## 2026-11-11 — Installer Package Cleanup

- Added `calamares` and `squashfs-tools` to the installed-system removal list.
- Kept `rsync` in the installed-system package set.
- Verified the package configuration and package-list assertions.
- APT runtime and VM installation tests remain pending.

### APT Autoremove Dependency Review

- Reviewed direct dependencies of Calamares and squashfs-tools.
- No static dependency finding changed the package cleanup decision.
- Target-system APT simulation and VM verification remain pending.

## 2026-11-11 — Initramfs and LUKS Audit

- Reviewed Calamares initramfscfg, encryption hooks, fstab, GRUB and bootloader logic.
- Verified the automatic separate `/boot` and encrypted Btrfs root layout.
- Verified crypttab correction and initramfs/GRUB execution order.
- Recorded manual partitioning limitations and pending VM boot tests.

## 2026-11-11 — BIOS and UEFI Bootloader Audit

- Audited Calamares GRUB installation paths for BIOS and UEFI.
- Verified x86_64 EFI target selection, EFI fallback handling and `Bibotto` bootloader ID.
- Verified ESP mount point and GRUB defaults.
- Confirmed LUKS root kernel parameters align with the separate unencrypted `/boot` design.
- Recorded BIOS and UEFI VM tests as pending.

## 2026-11-11 — Finished Module Configuration

- Added an explicit Calamares finished-page configuration.
- Replaced Debian's deprecated restart booleans with `restartNowMode: user-unchecked`.
- Configured `systemctl -i reboot` as the user-selected restart command.
- Recorded graphical and runtime restart tests as pending.


## 2026-11-11 — Calamares Log Upload Privacy

- Explicitly disabled external Calamares log uploads in Bibotto branding.

## 2026-11-11 — GRUB BIOS and UEFI Audit

- Verified Calamares GRUB selection and BIOS/UEFI installation branches.
- Verified BIOS `i386-pc` and x86_64 UEFI `x86_64-efi` targets.
- Verified Bibotto EFI identity and fallback loader configuration.
- Recorded pending BIOS and UEFI VM boot tests.

## 2026-11-11 — GRUB Boot Experience Audit

- Reviewed GRUB timeout, default entry, distributor branding and kernel parameters.
- Confirmed live ISO boot arguments are separate from installed-system GRUB arguments.
- Deferred Plymouth until Bibotto boot artwork is ready.
- Confirmed `os-prober` is excluded and Debian GRUB defaults to disabling its execution.
- No configuration changes were required.

## 2026-11-11 — Live ISO BIOS/UEFI Boot Audit

- Completed static review of the live-build hybrid ISO boot pipeline.
- Verified BIOS GRUB2 El Torito and hybrid MBR generation paths.
- Verified UEFI FAT image generation and ISO inclusion path.
- Retained best-effort Secure Boot configuration (`auto`).
- BIOS Generation 1 and UEFI Generation 2 live ISO boots were subsequently verified.

## 2026-11-11 — First ISO Build Preflight

- Verified sudo access and required live-build host tools.
- Verified BIOS/UEFI GRUB, xorriso, SquashFS, mtools, and dosfstools packages.
- Verified EFI image utilities and available disk space.
- First hybrid ISO build completed successfully; see the build and boot validation entries below.

## 2026-11-11 — First Bibotto Hybrid ISO Built

- First `bibotto-linux-amd64.hybrid.iso` build completed successfully.
- Verified BIOS and UEFI El Torito entries with xorriso.
- Verified hybrid MBR/GPT metadata and live filesystem, kernel, and initrd entries.
- Recorded the artifact SHA-256 in project status and testing documentation.
- BIOS and UEFI live desktop boots are verified; Calamares installation and installed-system boot remain pending.

### Testing — 2026-11-11

- Confirmed successful live ISO boot in a Hyper-V Generation 1 BIOS virtual machine.
- Verified basic KDE Plasma desktop interaction.
- No installer or installed-system boot result is claimed.


## 2026-11-11 — UEFI Live ISO Boot Verified

- Successfully booted the hybrid ISO in a Hyper-V Generation 2 UEFI virtual machine.
- Verified mouse input, Plasma application launcher, desktop context menu, and terminal launch.
- Secure Boot was disabled; Secure Boot validation remains pending.
- Calamares installation and installed-system boot have not yet been tested.

### Bibotto KDE color schemes

- Added Bibotto Light and Bibotto Dark color schemes to the live-build chroot overlay.
- Preserved the original branding source files and KDE Breeze themes.
- Verified both copied files against their sources.
- Runtime verification in a rebuilt ISO remains pending.

### Bibotto Light default

- Set Bibotto Light as the system-wide KDE color scheme default.
- Added the same initial preference to the new-user skeleton configuration.
- Runtime behavior remains to be verified.

### Local Git repository

- Initialized local version control for Bibotto.
- Added `.gitignore` for generated ISO, chroot, cache, binary and output artifacts.
- Renamed the initial branch to `main`.


## 2026-11-12 — Fresh hybrid ISO rebuild

- Rebuilt `bibotto-linux-amd64.hybrid.iso` successfully from a clean live-build state.
- ISO size: `2,514,907,136` bytes.
- SHA-256: `0af6ff5d5bdc7003ddc18ed3e600db7fd973c28a2ffded4221ef56e82ef21799`.
- Verified `/live/filesystem.squashfs` in the ISO.
- Extracted SquashFS and verified Bibotto Light and Dark color-scheme files.
- Verified system-wide and new-user KDE configuration both select `BibottoLight`.
- Confirmed the archived first ISO checksum remains unchanged.
- Latest ISO VM boot, KDE visual verification, Calamares, and installation tests remain pending.

## 2026-11-12 — ISO copied to Windows Hyper-V directory

- Copied the latest ISO to `C:\\Hyper-V\\Bibotto\\bibotto-linux-amd64.hybrid.iso`.
- Verified the copied file against the WSL source using SHA-256; values match.


## 2026-11-12 — Latest ISO Generation 1 BIOS boot passed

- Booted the freshly rebuilt ISO in a Hyper-V Generation 1 virtual machine.
- Confirmed that the live KDE desktop opened successfully.


## 2026-11-12 — Latest ISO Generation 2 UEFI boot passed

- Booted the latest ISO in a Hyper-V Generation 2 virtual machine.
- Confirmed that the KDE live environment and application menu opened.



## 2026-11-12 — Bibotto color schemes verified in live KDE

- Confirmed Bibotto Light and Bibotto Dark appear in KDE System Settings.
- Manually applied Bibotto Light and Bibotto Dark successfully in the live session.
- Automatic default selection at session startup remains to be checked.

## 2026-11-12 — Corrected KDE default color scheme identifier

- Changed both KDE default configurations to use `Bibotto-Light`, matching `Bibotto-Light.colors`.
- Fresh ISO rebuild and automatic startup verification remain pending.
