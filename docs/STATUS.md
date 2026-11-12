# Bibotto Linux — Project Status

**Last reviewed:** 2026-11-12
**Overall state:** KDE default scheme correction prepared; fresh ISO rebuild pending
**Release state:** No ISO release

## Summary

Bibotto is being developed as a Debian 13 Trixie-based amd64 distribution with KDE Plasma 6 and Calamares.

An initial live-build configuration and package baseline exist. The Calamares packagechooser and ISO-contained offline APT repository are configured. The local repository has passed an isolated index and dependency-resolution simulation. The latest built ISO passed Hyper-V BIOS and UEFI live-boot tests. Both Bibotto color schemes were verified and manually applied. The KDE default scheme identifier has since been corrected in the source overlays; a fresh ISO rebuild and automatic startup verification are pending.

## Confirmed Decisions

- Debian 13 Trixie.
- amd64 / x86_64.
- KDE Plasma 6.
- SDDM.
- Wayland as primary session goal.
- Hybrid ISO.
- Debian live-build.
- Calamares 3.3.14.
- Btrfs preferred filesystem direction.
- LUKS2 encryption support as a goal.
- Breeze Light and Breeze Dark retained.
- Optional themes: Viola-Dark-Plasma, Vivid Dark Plasma, Slot Dark Plasma.
- Optional installer groups: development tools, KMail and Thunderbird.
- LibreOffice is included in the standard desktop package set and installed by default.
- Windows and Debian share one project directory through WSL.

## Implementation Inventory

| Area | Evidence | Status |
|---|---|---|
| Project structure | Existing `config/` tree | Present |
| live-build configuration | Main configuration files reviewed | Configured; build unverified |
| Package lists | 10 active lists; 111 unique names | Present |
| APT simulation | Completed without visible resolver errors | Simulated only |
| Debian base | Trixie repositories configured | Configured |
| KDE desktop | Plasma 6 packages listed | Runtime unverified |
| Calamares | 3.3.14 package available | Runtime unverified |
| Calamares settings | Custom settings, module files, and two shellprocess instances | Configured; runtime unverified |
| Branding | `branding.desc` and two package-choice SVGs | Partial; referenced assets missing |
| Optional package UI | Development and Email groups in `packagechooser.conf` | Configured; runtime unverified |
| Offline package source | 1,059 `.deb` files, `Packages`, and `Packages.gz` | Assembled; isolated APT simulation passed |
| Offline dependency resolution | Isolated APT state and local file repository | Simulated successfully; installation unverified |
| Calamares offline integration | Setup before packages; cleanup afterward | Configured; runtime unverified |
| ISO build | Passed | Multiple hybrid ISO builds completed; latest built ISO approximately 2.4 GB. Source changes after the latest build require a fresh rebuild |
| Live boot | Passed | BIOS Gen 1 and UEFI Gen 2; KDE desktop verified |
| Installation | No successful installation recorded | Not tested |
| Hardware | No real-hardware results recorded | Not tested |

## Package Baseline

The active live-build package lists contain 111 unique package names.

An APT simulation was run in WSL using `--no-install-recommends`. Separately, the local offline repository was tested with an isolated APT state directory and an empty package status file. The repository index loaded successfully, and the dependency-resolution simulation for all five optional package roots completed with 1,059 packages and no reported missing dependencies or conflicts.

The repository contains 1,059 `.deb` archives and occupies approximately 678 MB. These tests do not prove actual package installation, clean live-build behavior, final ISO contents, or successful boot.

**LibreOffice status:** `libreoffice` is correctly present in the active desktop package list and is intended to remain part of the default installation.

Root-level developer and email package planning files do not automatically include their packages in the ISO.

## Immediate Priorities

1. Resolve the remaining Calamares branding asset references.
2. Launch Calamares from the live desktop and verify installer startup.
3. Test automatic and manual partitioning in a disposable VM.
4. Test a complete installation and first boot.
5. Test offline installation options: default, Development, Email, and both optional groups.
6. Validate installed-system BIOS/UEFI boot and Secure Boot separately.

## Evidence Policy

"Configured" means configuration files or package lists exist. It does not mean the feature has passed a build or runtime test.

Do not mark a feature as tested without recording the environment and result.

## ISO Identity

The live-build ISO metadata now uses Bibotto branding. The image
basename is `bibotto-linux`; the ISO application, preparer, publisher,
volume ID, and disk label are also branded.

The live boot command line no longer disables the SDDM live-config
component. The component configures SDDM autologin in the live session.
This does not establish the login policy of the installed system.

`LB_NET_TARBALL` remains true. The installed live-build source confirms
that netboot tarball creation is gated by `LB_IMAGE_TYPE=netboot`, so
it does not create an additional tarball for the current `iso-hybrid`
configuration.

Shell syntax and metadata length checks passed. The first ISO has not
yet been built or boot-tested.

## 2026-11-10 — Calamares Configuration Audit Update

The six remaining module configurations have been reviewed.
`plasma-workspace` is included in the default desktop package list;
its absence from the optional offline repository is expected.
The configuration review was complete at the time of this audit.
Subsequent ISO-level verification and BIOS/UEFI live boots have passed.
Installed-system testing and Calamares runtime validation remain pending.

## SVG Görsel Üretim Altyapısı
- [2026-11-10] Debian 13 WSL geliştirme ortamına librsvg2-bin kuruldu. rsvg-convert ile 128x128 SVG -> PNG testi başarılı.

## Calamares Branding Source Structure

- [2026-11-10] Created `branding/calamares/bibotto/` as the authoritative source directory.
- Copied `branding.desc`, `development.svg`, and `email.svg` from the existing ISO include directory.
- Verified all three source files match their ISO target copies using `diff -r`.
- Automatic source-to-target synchronization is implemented in `auto/build`; sync-only test passed on 2026-11-10.
- Original logo and Calamares product images remain pending.

## Calamares Branding Synchronization

- `auto/build` now synchronizes the authoritative branding source directory
  into the live-build Calamares branding target before starting the ISO build.
- The `BIBOTTO_BRANDING_SYNC_ONLY=1` mode allows synchronization without
  starting an ISO build.
- Shell syntax validation passed.
- The synchronization-only run completed successfully.
- Source and target directories matched (`diff -r`, exit code 0).
- ISO build and Calamares runtime rendering remain unverified.

## Offline APT Repository Emergency Cleanup

- Calamares shellprocess module descriptor is overridden through the live-build chroot overlay.
- The shellprocess descriptor and offline cleanup configuration both declare `emergency: true`.
- Cleanup continues when `apt-get clean` fails and reports errors.
- Original APT source files are restored independently of APT cache-cleaning success.
- Unrestored source backups are preserved.
- Shell syntax and isolated success/failure tests passed.
- Real Calamares execution and ISO validation remain pending.

## Offline APT Repository Setup and Cleanup Audit

- Added a transaction marker to distinguish active Bibotto repository setup from unrelated APT state.
- Setup validates target paths and rejects existing backup, repository-cache, and offline-source collisions before modifying APT sources.
- Repository setup uses an atomic rename to publish the temporary APT source.
- Emergency cleanup does nothing when no Bibotto transaction marker exists.
- Cleanup restores original APT sources and removes transaction-owned temporary repository data.
- YAML, shell syntax, and three isolated setup/cleanup integration scenarios passed.
- Real Calamares execution and ISO validation remain pending.

### Calamares Emergency Module Selection

- Verified the shellprocess module descriptor declares `emergency: true`.
- Verified `offline-repo-setup` has `emergency: false`.
- Verified `crypttab-luks-fix` has `emergency: false`.
- Verified `offline-repo-cleanup` has `emergency: true`.
- Configuration-level emergency selection audit: PASS.
- Real installer failure-path execution: PENDING.

### Calamares Module Availability and Load Targets

- Audited all 24 modules referenced by `settings.conf`.
- All module descriptors were found in the Calamares 3.3.14 core package.
- All Python `main.py` and native shared-library load targets were present.
- Project shellprocess overlay exists and retains the core package load target.
- Shellprocess emergency capability is enabled in the project overlay.
- Static module load-target audit: 24/24 PASS.
- Actual Calamares runtime and ISO tests remain pending.

## Calamares Unpackfs and rsync Integration

- Added Bibotto's own `unpackfs.conf`.
- Configured the live squashfs source as `/run/live/medium/live/filesystem.squashfs`.
- Added `rsync` to `bibotto-installer.list.chroot`; Calamares unpackfs uses it for copying.
- Static YAML, source configuration, and package-list checks passed.
- ISO build and real Calamares installation remain unverified.

## Calamares Mount and Fstab Audit

- Reviewed the Calamares 3.3.14 mount and fstab implementations and schemas.
- Confirmed the configured Btrfs subvolume creation and fstab propagation.
- Confirmed mount options are passed from mount to fstab.
- Confirmed EFI, LUKS mapper, and tmpfs configuration behavior.
- Static review only; installation and generated fstab remain untested in a VM.

## Calamares Users Module Audit

- Reviewed the Bibotto users.conf configuration against Calamares 3.3 users module behavior.
- Confirmed that defaultGroups supports named entries with must_exist and system fields.
- Confirmed the Debian sudo group and `%sudo ALL=(ALL:ALL) ALL` policy.
- Kept sudoersGroup unset to avoid generating a duplicate sudoers policy.
- Password policy, disabled autologin, disabled root password, and home permissions reviewed.
- Static review only; real user creation and sudo access remain untested in a VM.

## Calamares LUKS and Initramfs Audit

- Reviewed the Calamares 3.3.14 initramfscfg implementation and both encryption hooks.
- Confirmed that encrypted root with a separate unencrypted /boot selects encrypt_hook_nokey.
- Confirmed that encrypt_hook_nokey copies the target crypttab into initramfs without copying a keyfile.
- Confirmed cryptsetup, cryptsetup-initramfs and initramfs-tools are included in the relevant package lists.
- Verified that the live-build cryptsetup hook is a valid symlink to the installed live-build hook.
- Reviewed the custom crypttab-luks-fix shellprocess script.
- All six isolated crypttab fix tests passed.
- Static and isolated tests only; real ISO boot, LUKS unlock and installed-system initramfs behavior remain pending.

## Calamares GRUB and UEFI Bootloader Audit

- Reviewed Calamares 3.3.14 grubcfg and bootloader implementations.
- Set efiBootloaderId to Bibotto; YAML validation passed.
- Confirmed GRUB_DISTRIBUTOR is derived from branding.desc bootloaderEntryName.
- Confirmed installEFIFallback is enabled.
- Confirmed BIOS and UEFI GRUB packages and efibootmgr are listed for the live-build chroot.
- The five bootloader packages are not in the separate offline APT repository. This is intentional: they are installed in the live filesystem and copied to the target by unpackfs; the Calamares packages module does not install them.
- Static review only; BIOS and UEFI installation and boot tests remain pending.

## Calamares SDDM and Plasma Session Audit

- SDDM, Breeze theme, Plasma Workspace, Plasma Desktop, KWin X11 and KWin Wayland are included in the desktop package list.
- Calamares displaymanager is configured to use SDDM and the Plasma Wayland session.
- The live session uses the bibotto account through live-config.
- Live SDDM autologin is configured for bibotto.
- Calamares displaymanager source removes the target SDDM Autologin.User when no autoLoginUser is configured, while setting the configured desktop session.
- This separates live-session autologin from the installed system's user login.
- Static review only; graphical login and session startup have not been tested in an ISO or VM.

## Calamares NetworkManager and Network Configuration Audit

- NetworkManager, `wpasupplicant` and `wireless-regdb` are included in the hardware package list.
- Calamares `networkcfg` runs before `services-systemd`.
- `NetworkManager.service` is configured to be enabled.
- No custom NetworkManager connection profiles are currently included in the live filesystem.
- Debian Trixie provides a candidate for `wireless-regdb`.
- Static configuration checks passed.
- Actual Ethernet/Wi-Fi connectivity and installed-system service behavior remain untested in a VM.

## Calamares Installer Package Cleanup

- Calamares is installed in the live system for installation.
- `packages.conf` removes `calamares`, `squashfs-tools`, `live-boot`, `live-config` and `live-config-systemd` from the installed system.
- `rsync` remains installed.
- YAML parsing and package-list assertions passed.
- Actual APT removal and installed-system package state remain pending VM testing.

### APT Autoremove Dependency Review

- Static dependency review found no immediate reason to retain Calamares or squashfs-tools in the installed system.
- APT should preserve dependencies still required by other installed packages.
- Actual target-system dependency state and autoremove results remain subject to VM testing.

## Calamares Initramfs and LUKS Boot Audit

- Confirmed automatic layout uses a separate unencrypted ext4 `/boot` and LUKS2-encrypted Btrfs `/`.
- Confirmed Calamares initramfscfg selects `encrypt_hook_nokey` for this layout.
- Confirmed the hook copies target `/etc/crypttab` into initramfs without copying a keyfile.
- Confirmed the active sequence corrects crypttab before initramfs generation and configures GRUB afterward.
- Confirmed the cryptsetup live-build hook symlink resolves to an executable target.
- Manual partitioning remains available; equivalent LUKS boot behavior is only established for the documented separate `/boot` layout.
- BIOS and UEFI live ISO boots passed; installed-system LUKS boot remains untested.

## Calamares BIOS and UEFI Bootloader Audit

- Confirmed Calamares selects GRUB for BIOS and UEFI.
- Confirmed BIOS installation uses the `i386-pc` target and Calamares-selected boot device.
- Confirmed UEFI installation uses the x86_64 EFI target and `Bibotto` bootloader ID.
- Confirmed EFI fallback installation is enabled and the ESP mount point is `/boot/efi`.
- Confirmed GRUB configuration uses Bibotto branding, timeout 5 and default entry 0.
- Confirmed encrypted-root kernel parameters are generated for the LUKS mapper.
- Confirmed the automatic separate `/boot` layout does not enable GRUB cryptodisk unnecessarily.
- Static source and configuration audit completed; BIOS/UEFI live boots passed. Calamares installation and installed-system boot remain pending.

## Calamares Finished Module Configuration

- Added the Calamares `finished.conf` configuration.
- Restart mode is `user-unchecked`: the restart checkbox is visible and initially unchecked.
- Restart command is `systemctl -i reboot`.
- Calamares 3.3.14 source confirms failed installations force restart mode to `never`.
- Static configuration recorded; graphical and runtime behavior still requires VM testing.


## Calamares Log Upload Privacy

- [x] External Calamares log upload explicitly disabled with `uploadServer.type: none`.

## Calamares GRUB BIOS and UEFI Audit

- Confirmed `efiBootLoader: grub` is supported by Calamares 3.3.14.
- BIOS installation uses the `i386-pc` GRUB target.
- 64-bit x86 UEFI installation uses the `x86_64-efi` target.
- EFI bootloader identity is configured as `Bibotto`.
- EFI fallback installation is enabled; Calamares copies the fallback boot file.
- GRUB configuration generation runs after installation in both paths.
- BIOS and UEFI package configuration passed static review.
- Actual firmware boot tests remain pending.

## GRUB Boot Experience Audit

- GRUB timeout is configured to 5 seconds.
- The first GRUB entry is the default.
- Calamares generates `GRUB_DISTRIBUTOR` from the Bibotto bootloader entry name.
- Installed-system kernel parameters default to `quiet`; LUKS parameters are added by Calamares.
- The live ISO uses its separate `quiet splash` boot arguments.
- Plymouth is not included; graphical boot splash work is deferred.
- `os-prober` is not included in the target package lists.
- Debian GRUB 2.12 defaults `GRUB_DISABLE_OS_PROBER` to true in `grub-mkconfig`.
- No GRUB configuration change was required by this audit.

## Live ISO BIOS/UEFI Boot Infrastructure Audit

- Static source audit completed for the Debian live-build ISO boot pipeline.
- ISO type: `iso-hybrid`.
- BIOS bootloader: `grub-pc`; GRUB2 El Torito image and hybrid MBR path verified in live-build source.
- UEFI bootloader: `grub-efi`; FAT EFI image creation and inclusion path verified.
- Secure Boot remains `auto` (best effort); actual signed-boot behavior must be checked in the build log.
- No ISO build or BIOS/UEFI runtime test has been completed yet.

## First ISO Build Preflight

- Host build prerequisites verified: live-build, xorriso, squashfs-tools, GRUB BIOS/UEFI tools, mtools, and dosfstools are installed.
- `sudo` access verified for privileged live-build operations.
- EFI image utilities `mcopy` and `mkfs.msdos` are available.
- Project filesystem has approximately 955 GB free.
- Output directory contains no previous build artifact.
- Preflight passed; ISO build has not started.

## First Hybrid ISO Build — Successful

- Built `bibotto-linux-amd64.hybrid.iso` successfully.
- ISO size: approximately 2.4 GB.
- SHA-256: `06ed32e5e587989cdc34d44c2356e8a1a533803facca1fe0bc874113d92c83bb`.
- Inspected ISO with xorriso: BIOS and UEFI El Torito entries are both present.
- Confirmed BIOS image `/boot/grub/grub_eltorito` and UEFI image `/boot/grub/efi.img`.
- Confirmed `/live/filesystem.squashfs`, kernel, and initrd are present.
- BIOS and UEFI live boots are verified; Calamares installation and installed-system boot remain pending.

### BIOS Live ISO Boot — 2026-11-11

- Successfully booted the first hybrid ISO in a Hyper-V Generation 1 (BIOS) virtual machine.
- Verified KDE Plasma desktop startup, mouse interaction, application launcher, desktop context menu, and terminal launch.
- This confirms live ISO BIOS boot only; installed-system boot and GRUB installation remain unverified.

### UEFI Live ISO Boot — 2026-11-11

- Successfully booted the hybrid ISO in a Hyper-V Generation 2 UEFI virtual machine.
- KDE Plasma desktop started successfully.
- Mouse, application launcher, desktop context menu, and terminal launch were verified.
- Secure Boot was disabled for this baseline test; Secure Boot validation remains pending.
- This verifies live ISO boot only, not Calamares installation or installed-system boot.

## Bibotto KDE Color Schemes

- Added `Bibotto-Light.colors` and `Bibotto-Dark.colors` to the live-build chroot overlay.
- ISO target: `/usr/share/color-schemes/`.
- Original source files remain under `branding/themes/`.
- Breeze Light and Breeze Dark are preserved.
- Source-to-target file comparison passed.
- Both color-scheme files were verified inside the latest built ISO.
- Installed-system availability remains pending verification.
- Automatic default selection at live-session startup remains pending.

## Bibotto Light Default Color Scheme

- The initial configuration used `BibottoLight` as the system-wide KDE color scheme default and for new users.
- This identifier was later corrected to `Bibotto-Light`; see the correction records below.
- Both schemes were manually applied and visually verified in the live session.
- Installed-system application remains pending verification.

## Local Git Repository

- Initialized a local Git repository in the Bibotto project root.
- Set the primary branch name to `main`.
- Added `.gitignore` rules for generated live-build output and downloaded root-level packages.
- GitHub connection is not required; the repository is local.
- Initial commit is pending source-file review.


## Latest Hybrid ISO Build — 2026-11-12

- Fresh live-build completed successfully using `sudo ./auto/build`.
- live-build version: `20250505+deb13u1`.
- ISO: `bibotto-linux-amd64.hybrid.iso`.
- Size: `2,514,907,136` bytes.
- SHA-256: `0af6ff5d5bdc7003ddc18ed3e600db7fd973c28a2ffded4221ef56e82ef21799`.
- xorriso confirmed `/live/filesystem.squashfs` is present (1,654,091,776 bytes).
- Extracted the SquashFS and verified both `/usr/share/color-schemes/Bibotto-Light.colors` and `Bibotto-Dark.colors`.
- Verified `/etc/xdg/kdeglobals` and `/etc/skel/.config/kdeglobals` both contain `ColorScheme=BibottoLight`.
- The first ISO remains archived at `releases/archive/bibotto-linux-amd64-first.iso`; its original SHA-256 remains unchanged.
- Latest ISO Hyper-V Generation 1 BIOS boot: passed; live KDE desktop reached.
- Latest ISO Hyper-V Generation 2 UEFI boot passed on 2026-11-12.
- Calamares runtime and installation tests remain pending.

## Windows Hyper-V ISO Copy — 2026-11-12

- Copied the latest ISO to `C:\\Hyper-V\\Bibotto\\bibotto-linux-amd64.hybrid.iso`.
- Compared source and destination SHA-256 values; they match.
- Verified SHA-256: `0af6ff5d5bdc7003ddc18ed3e600db7fd973c28a2ffded4221ef56e82ef21799`.


## Latest ISO — Hyper-V Generation 1 BIOS Test — 2026-11-12

- Result: Passed.
- The 2026-11-12 ISO booted in a Hyper-V Generation 1 virtual machine.
- The live KDE Plasma desktop opened successfully.
- Generation 2 UEFI and installer tests remain pending.


## Latest ISO — Hyper-V Generation 2 UEFI Test — 2026-11-12

- Result: Passed.
- The latest ISO booted in a Hyper-V Generation 2 virtual machine.
- The KDE live environment and application menu opened successfully.



## Latest ISO — KDE Color Scheme Runtime Test — 2026-11-12

- Bibotto Light and Bibotto Dark are both visible in KDE System Settings.
- Bibotto Light was manually selected and applied successfully in the live session.
- The applied Bibotto Light scheme was visually confirmed by the user.
- Bibotto Dark was also manually selected and applied successfully in the live session.
- Both Bibotto Light and Bibotto Dark were visually confirmed by the user.
- Automatic application of the configured default at live-session startup remains to be verified.

## KDE Default Color Scheme Identity Correction — 2026-11-12

- Corrected the system-wide and new-user KDE color scheme identifiers from `BibottoLight` to `Bibotto-Light`.
- The corrected identifier matches the color-scheme filename `Bibotto-Light.colors`.
- A fresh ISO rebuild and live-session startup verification are pending.

## Persistent KDE Scheme Configuration — 2026-11-12

- Corrected both KDE configuration files in `config/includes.chroot`.
- Verified system-wide and new-user defaults in both overlay and chroot.
- All four configurations now use `ColorScheme=Bibotto-Light`.
- Rebuild and fresh live-session verification are pending.
