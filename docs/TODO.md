# Bibotto Linux — TODO

## P0 — Before First Meaningful ISO Test

- [x] Create initial Calamares settings and module configuration for Debian 13 / version 3.3.14.
- [ ] Verify every module referenced by `settings.conf` is available in the final live image.
- [x] Complete module configuration schema and execution-order audit.
- [x] Assemble the ISO-contained offline APT repository with optional package archives and dependency closure.
- [x] Keep optional packages out of the normal live-build package lists.
- [x] Verify LibreOffice remains in the default desktop package set.
- [x] Add packagechooser configuration for Development and Email.
- [x] Generate local repository indexes and pass isolated APT dependency-resolution simulation.
- [ ] Test actual offline package installation through Calamares.
- [ ] Verify none, either, and both optional-group selections in the installer.
- [x] Audit offline repository setup and cleanup scripts (isolated integration tests passed).
- [ ] Complete Bibotto Calamares branding and resolve missing asset references.
- [ ] Review active package lists for unnecessary or misplaced packages.

## P1 — First ISO and Installer Validation

- [ ] Build from a clean documented environment.
- [ ] Record build logs and ISO size.
- [ ] Verify SHA-256 checksum.
- [x] Boot in a UEFI virtual machine.
- [x] Verify live Plasma session.
- [ ] Launch Calamares.
- [ ] Test automatic partitioning.
- [ ] Test manual partitioning.
- [ ] Test Btrfs subvolumes and mount options.
- [ ] Test LUKS2 encryption.
- [ ] Test user creation and first login.
- [ ] Test GRUB installation and reboot.
- [ ] Confirm the installed system boots without the ISO attached.

## P2 — Desktop and Hardware

- [ ] Validate SDDM and Wayland.
- [ ] Decide and test X11 fallback.
- [ ] Test AMDGPU and Mesa.
- [ ] Test Intel/NVIDIA paths as applicable.
- [ ] Test Wi-Fi, Bluetooth, audio, suspend/resume, and external displays.
- [ ] Integrate panel, dock, launcher, icons, and themes.
- [ ] Add optional Plasma themes.
- [ ] Check fonts and accessibility contrast.

## P3 — Security and Maintenance

- [ ] Define update channels and package policy.
- [ ] Validate AppArmor profiles and service state.
- [ ] Validate firewalld defaults.
- [ ] Validate unattended-upgrades.
- [ ] Define kernel update and fallback policy.
- [ ] Define backup and recovery recommendations.
- [ ] Define release signing and checksum publication.

## Documentation Maintenance

- [ ] Keep STATUS.md aligned with test evidence.
- [ ] Update CHANGELOG.md for meaningful changes.
- [ ] Record package changes in PACKAGE-MANIFEST.md.
- [ ] Record installer changes in INSTALLER.md.
- [ ] Keep offline repository archive count, size, and test evidence current.
- [ ] Record test environment and results in TESTING.md.
- [ ] Add exact build commands after they are validated.

## Tamamlanan Geliştirme Ortamı İşleri
- [x] [2026-11-10] Debian 13 üzerinde SVG -> PNG dönüştürme altyapısını kur ve doğrula (librsvg2-bin).

### Calamares Branding Follow-up

- [x] Centralize the existing `branding.desc`, `development.svg`, and `email.svg`
  files under `branding/calamares/bibotto/`.
- [x] Add automatic source-to-ISO-target synchronization to the build workflow (`auto/build`; sync-only test passed).
- [ ] Create original Bibotto logo artwork and configure Calamares product images.
- [ ] Verify branding in a built ISO and live installer.

### Offline Repository Cleanup
- [x] Verify that only the offline repository cleanup instance is marked as a Calamares emergency module.

- [x] Add Calamares emergency metadata to the shellprocess descriptor overlay and cleanup instance.
- [x] Harden cleanup against APT cache-cleaning failure.
- [x] Pass isolated cleanup success and failure-path tests.
- [ ] Validate emergency cleanup in a real Calamares installation.
- [ ] Complete the setup-script audit and end-to-end offline repository audit.
- [x] Verify all 24 configured Calamares modules and their package load targets.

## Calamares Unpackfs Follow-up

- [x] Add Bibotto's `unpackfs.conf`.
- [x] Add `rsync` to the installer package list.
- [ ] Verify the squashfs source path in the built ISO.
- [ ] Test unpackfs and installation in a virtual machine.

## Mount and Fstab Follow-up

- [x] Review mount and fstab module implementations and schemas.
- [ ] Verify generated fstab and Btrfs subvolumes in a VM installation.

## Calamares Users Follow-up

- [x] Audit users.conf and verify the sudo group policy.
- [ ] Test user creation, password enforcement, and sudo access in a VM.

## Calamares LUKS Follow-up

- [x] Review Calamares initramfscfg encryption hook selection.
- [x] Verify cryptsetup, cryptsetup-initramfs and initramfs-tools package-list entries.
- [x] Verify the live-build cryptsetup hook symlink target.
- [x] Test crypttab correction behavior in isolated temporary roots.
- [ ] Build the ISO and inspect the generated target initramfs configuration.
- [ ] Test encrypted-root boot and password unlock in a VM.
- [ ] Verify the installed system can regenerate initramfs successfully.

## GRUB and Bootloader Follow-up

- [x] Review Calamares GRUB configuration and bootloader implementation.
- [x] Set and validate the Bibotto UEFI bootloader identity.
- [x] Verify BIOS and UEFI GRUB package-list entries.
- [ ] Verify GRUB installation in a BIOS virtual machine.
- [ ] Verify GRUB installation and fallback boot in a UEFI virtual machine.
- [ ] Verify encrypted Btrfs root boot through GRUB.

## SDDM and Plasma Follow-up

- [x] Review SDDM and Plasma package-list entries.
- [x] Review live-session user and SDDM autologin configuration.
- [x] Verify Calamares removes target autologin when no autoLoginUser is configured.
- [ ] Verify Plasma Wayland session starts successfully in a VM.
- [ ] Verify installed-system login screen and user authentication.
- [ ] Test X11 session availability as a fallback.

## NetworkManager Follow-up

- [x] Include NetworkManager, WPA supplicant and wireless regulatory database packages.
- [x] Place Calamares `networkcfg` before service enablement.
- [x] Configure `NetworkManager.service` for enablement.
- [x] Confirm no personal connection profiles are bundled.
- [ ] Test Ethernet and Wi-Fi in a live ISO.
- [ ] Verify NetworkManager startup and connectivity in the installed VM.
- [ ] Test migration of a temporary NetworkManager profile, if profile migration is part of the intended live-session workflow.

## Installer Package Cleanup Follow-up

- [x] Remove Calamares from the installed system after installation.
- [x] Remove squashfs-tools from the installed system after installation.
- [x] Remove live-boot, live-config and live-config-systemd from the installed system.
- [x] Retain rsync.
- [ ] Verify APT removal and autoremove behavior in a VM.
- [ ] Confirm no required desktop, network, filesystem or boot dependencies are removed.

### APT Autoremove Verification

- [x] Perform static review of Calamares and squashfs-tools dependencies.
- [ ] Run APT simulation on the built target before confirming autoremove effects.
- [ ] Verify desktop, networking, Btrfs, LUKS and boot packages remain installed.

## Initramfs and LUKS Follow-up

- [x] Verify automatic separate unencrypted `/boot` and LUKS2 root configuration.
- [x] Verify Calamares selects the no-key initramfs hook for this layout.
- [x] Verify crypttab correction and initramfs/GRUB execution order.
- [ ] Test password-based boot in BIOS and UEFI VMs.
- [ ] Validate alternative manual partitioning layouts or document their restrictions.

## BIOS and UEFI Boot Verification

- [x] Audit Calamares BIOS and UEFI GRUB installation logic.
- [x] Verify x86_64 EFI target, ESP path and fallback configuration.
- [x] Verify Bibotto GRUB branding and default settings.
- [ ] Verify BIOS installation and boot in a VM.
- [ ] Verify UEFI installation and fallback boot in a VM.
- [ ] Verify LUKS2 password-based boot in both firmware modes.

## Finished Module Runtime Verification

- [x] Configure the restart checkbox as visible and unchecked by default.
- [x] Configure the explicit systemd reboot command.
- [x] Confirm failed installations disable restart.
- [ ] Inspect the finished page in a VM.
- [ ] Test completion with restart unchecked.
- [ ] Test completion with restart checked.
- [ ] Test the failed-installation screen.


## Calamares Log Upload Runtime Verification

- [ ] Verify in a real installer session that external log upload is unavailable.

## GRUB BIOS and UEFI Follow-up

- [x] Verify Calamares GRUB selection and BIOS/UEFI installation logic.
- [x] Verify EFI identity and fallback loader configuration.
- [ ] Test BIOS installation and boot in a VM.
- [ ] Test UEFI installation, NVRAM registration and fallback boot in a VM.
- [ ] Test LUKS2 encrypted-root boot in BIOS and UEFI VMs.

## GRUB Boot Experience Follow-up

- [x] Review GRUB timeout and default entry.
- [x] Review installed-system kernel parameter generation.
- [x] Verify automatic OS probing remains disabled by default.
- [ ] Design Bibotto boot artwork and evaluate Plymouth integration.
- [ ] Review the GRUB menu and boot appearance after the first ISO build.
- [ ] Test the installed kernel command line and boot flow in BIOS and UEFI VMs.
- [ ] Consider optional multi-boot detection only if explicitly requested.

## Live ISO Boot Validation — Completed (Secure Boot pending)

- [x] Build the first Bibotto hybrid ISO.
- [x] Inspect the build log for successful BIOS and UEFI boot image generation.
- [x] Test BIOS boot in a virtual machine.
- [x] Test UEFI boot in a virtual machine.
- [ ] Check Secure Boot behavior separately; do not assume `auto` guarantees it.
- [ ] Test the resulting ISO from USB media after VM validation.

## First ISO Build

- [x] Verify host build tools and BIOS/UEFI utilities.
- [x] Verify sudo access for live-build.
- [x] Verify available disk space and output directory.
- [x] Run the first ISO build as root.
- [x] Review the complete build log and generated ISO.
- [x] Verify ISO contents and checksums.
- [x] Test BIOS and UEFI boot in virtual machines.

## First ISO — Validation Progress

- [x] Build the first Bibotto hybrid ISO.
- [x] Inspect the ISO build result and record its SHA-256.
- [x] Verify BIOS El Torito boot image is present.
- [x] Verify UEFI El Torito boot image is present.
- [x] Verify live SquashFS, kernel, and initrd are present.
- [x] Boot the ISO in a BIOS virtual machine.
- [x] Boot the ISO in a UEFI virtual machine.
- [ ] Test the Calamares installation workflow.
- [ ] Test Secure Boot separately.

## KDE Color Scheme Integration

- [x] Add Bibotto Light and Dark color schemes to the live-build chroot overlay.
- [x] Verify copied files against branding sources.
- [x] Configure Bibotto Light as the system-wide and new-user default color scheme.
- [x] Rebuild the ISO and verify both scheme files are embedded in the live SquashFS.
- [ ] Verify both schemes appear in KDE System Settings in the live session.
- [ ] Verify color schemes in the installed system.

## Local Version Control

- [x] Initialize the local Git repository.
- [x] Use `main` as the primary branch.
- [x] Exclude generated build artifacts with `.gitignore`.
- [ ] Review the remaining source files before the initial commit.
- [ ] Create the initial Git commit.


## Latest ISO — 2026-11-12

- [x] Complete a fresh live-build.
- [x] Confirm successful build completion.
- [x] Record ISO size and SHA-256.
- [x] Confirm `/live/filesystem.squashfs` is present.
- [x] Extract SquashFS and verify Bibotto Light and Dark scheme files.
- [x] Verify system-wide and new-user defaults select `BibottoLight`.
- [x] Preserve and recheck the archived first ISO.
- [x] Boot latest ISO in Hyper-V Generation 1 BIOS and reach the live KDE desktop.
- [x] Boot latest ISO in Hyper-V Generation 2 UEFI and open the KDE live environment.
- [x] Verify Bibotto Light and Dark appear in live KDE Colors settings.
- [x] Apply Bibotto Light successfully in the live session.
- [x] Apply and verify Bibotto Dark in the live session.
- [ ] Verify automatic Bibotto Light default selection at session startup.
- [ ] Test Calamares and complete an installation.
