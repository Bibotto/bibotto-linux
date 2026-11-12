# Bibotto Linux — Installer

**Installer:** Calamares 3.3.14  
**Status:** Configuration exists; complete installation has not been tested.

## 1. Goals

Provide a clear and predictable installation experience, support the declared boot modes, and allow optional software installation without internet access.

## 2. Current Configuration

The current `settings.conf` defines:

- Local module configuration search.
- Branding identifier `bibotto`.
- Two shellprocess instances: `offline-repo-setup` and `offline-repo-cleanup`.
- Welcome, locale, keyboard, partition, users, and summary pages.
- Execution modules for partitioning, mounting, filesystem unpacking, machine ID, fstab, locale, keyboard, users, display manager, network, clock, services, packages, initramfs, GRUB, and unmounting.
- Custom configurations for bootloader, display manager, fstab, GRUB, mount, packages, partition, services, unmount, and users.

The Bibotto branding directory contains `branding.desc` and the `development.svg` and `email.svg` illustrations. It is not complete: `branding.desc` still references logo, welcome-image, and slideshow assets that have not been supplied. Debian branding was inspected only as a reference and must not replace Bibotto branding.

## 3. Intended User Flow

1. Welcome and language.
2. Keyboard layout.
3. Disk and partitioning.
4. User account.
5. Optional software selection.
6. Installation summary.
7. Copy live filesystem to target.
8. Configure installed system.
9. Prepare the target system's temporary local APT source from the ISO-contained repository.
10. Install selected optional packages through the Calamares packages module.
11. Remove the temporary repository configuration and restore the target's original APT sources.
12. Generate initramfs and install bootloader.
13. Finish and reboot.

The exact page order must be validated against Calamares 3.3.14.

## 4. Optional Software

| Choice | Packages |
|---|---|
| Development | `build-essential`, `docker.io`, `docker-compose` |
| Email | KMail and Thunderbird |

LibreOffice is installed by default as part of the standard desktop package set; it is not an optional installer choice.

The packagechooser configuration is present at `modules/packagechooser.conf`, using `mode: optionalmultiple` and `method: packages`. It defines Development and Email groups. Users can select none, one, or both groups. LibreOffice remains a default desktop application and is not an optional choice.

The local repository is stored at `config/includes.binary/bibotto-repo`. It contains 1,059 `.deb` files and is approximately 678 MB. `Packages` and `Packages.gz` indexes are present. An isolated APT test successfully loaded this repository and simulated dependency resolution for all five optional package roots.

Two Calamares shellprocess configurations are present:

- `shellprocess-offline-repo-setup.conf`: copies the repository from the live medium into the target, temporarily configures a local APT source, and updates the target APT index.
- `shellprocess-offline-repo-cleanup.conf`: removes the temporary source and repository copy and restores the original APT source files.

The settings sequence places repository setup before the `packages` job and cleanup after it. This integration is configured but has not yet been tested in a real Calamares installation.

### Critical Constraint

`unpackfs` copies the live filesystem to the target. Adding optional packages to normal live-build chroot lists can therefore make them present regardless of installer selection.

The implemented design uses a separate ISO-contained local APT repository. The repository is copied to the target during installation, used through a temporary APT source, and scheduled for cleanup after optional package operations. The original APT source files are backed up and restored by the cleanup script.

The local repository has passed an isolated APT index and dependency-resolution simulation. The complete Calamares workflow, actual package installation, cleanup, and restoration still require runtime testing.

## 5. Storage Design

The current configuration describes:

- EFI system partition mounted at `/boot/efi`.
- Btrfs as the preferred filesystem.
- Btrfs subvolumes `@` and `@home`.
- `noatime` and `compress=zstd` mount options.
- LUKS2 encryption support.
- Automatic layout with ext4 `/boot` and Btrfs root.
- Manual partitioning enabled.

Test firmware mode, EFI handling, encrypted root, initramfs unlock, GRUB, and recovery after interrupted installation.

## 6. User Configuration

Current settings intend to provide:

- Regular user with `sudo` privileges.
- No root password.
- Automatic login disabled.
- Password length between 8 and 64 characters.
- `libpwquality` integration.
- Weak passwords disallowed.
- Bash shell.
- Home directory permissions `0700`.
- Hostname template based on CPU information.

Verify actual installed-system behavior.

## 7. Services

The current service configuration includes AppArmor, firewalld, NetworkManager, and SDDM as non-mandatory services. Verify installation, enablement, and successful startup.

## 8. Acceptance Criteria

- [ ] Calamares launches from the live session.
- [ ] All pages render correctly.
- [ ] Configured modules load without errors.
- [ ] Automatic and manual partitioning work.
- [ ] Btrfs subvolumes are created correctly.
- [ ] LUKS2 unlock works at boot.
- [ ] User and hostname settings are correct.
- [ ] GRUB works in every supported firmware mode.
- [ ] Optional packages install offline.
- [ ] Unselected optional groups remain absent.
- [ ] Live-only packages are removed.
- [ ] Installed system boots without the ISO attached.

<!-- bibotto-calamares-3.3.14-audit -->
## Calamares 3.3.14-1 yapılandırma denetimi

- Debian Trixie Calamares sürümü: `3.3.14-1`.
- `fstab.schema.yaml`, `grubcfg.schema.yaml` ve `mount.schema.yaml` incelendi; mevcut yapılandırmalarımız bu şemaların alan ve tip kurallarına uyuyor.
- Paket içinde `partition.schema.yaml` bulunmadı. `partition.conf` ayrıca modülün gerçek varsayılan yapılandırması ve kaynak koduyla doğrulanmalı.
- `fstab/main.py`, şifrelenmiş `/` ile şifrelenmemiş ayrı `/boot` düzeninde kök `crypttab` kaydının seçeneklerini boşaltıyor.
- `initramfscfg/main.py`, bu düzen için `encrypt_hook_nokey` kullanıyor. Hook, `/etc/crypttab` dosyasını initramfs içine kopyalıyor; anahtar dosyası kopyalamıyor.
- Bu nedenle Bibotto'nun parola ile açılan LUKS2 kök tasarımında `luksbootkeyfile` kullanılmayacak.
- Debian Trixie cryptsetup `2:2.7.5-2` belgelerine göre crypttab seçenek alanında şifreleme türü belirtilmeli; belirtilmediğinde `plain` varsayılıyor. Kök eşlemesine `luks` eklenmesi gerekiyor.
- Çözüm: `fstab` sonrasında ve `initramfscfg` öncesinde çalışan bir işlemle yalnızca şifreli kök eşlemesinin crypttab seçeneklerini `luks` olarak düzeltmek. Bu işlem henüz uygulanıp test edilmiş sayılmaz.

Kaynaklar:
- https://github.com/calamares/calamares/blob/calamares/src/modules/fstab/main.py
- https://github.com/calamares/calamares/blob/calamares/src/modules/initramfscfg/main.py
- https://sources.debian.org/src/cryptsetup/2%3A2.7.5-2/debian/doc/crypttab.xml

## LUKS crypttab düzeltmesi

Calamares `fstab` işleminden hemen sonra `crypttab-luks-fix` shellprocess çalışır.
Şifrelenmiş kök `/dev/mapper/<eşleme_adı>` üzerinden bağlanıyorsa, aynı eşleme
adına ait `/etc/crypttab` kaydının seçenek alanında `luks` bulunmasını sağlar.
Şifresiz kökte değişiklik yapmaz; eşleşen kayıt yoksa hata verir. Anahtar dosyası
kullanılmaz. İşlem `initramfscfg` öncesinde çalışır.

## BIOS / UEFI kurulum kararı

Bibotto ISO hem Legacy BIOS hem UEFI modunda açılacak. Kurulu sistemin
önyükleyicisi, kurulumun başlatıldığı firmware moduna göre kurulacak.
Tek bir kurulumun aynı diskte iki modda da açılması hedeflenmiyor.
Calamares 3.3.14'te desteklenmeyen `createHybridBootloaderLayout` ve
`defaultPartitionTableType` ayarları kullanılmayacak.
Debian'ın standart GRUB EFI paketiyle uyumluluk için `efiBootloaderId`
değeri `debian`; dağıtım markası Bibotto olarak kalacak.

### Live paketlerinin kurulu sistemden temizlenmesi

Calamares `packages` modülünün APT backend'i, `remove` işlemi sırasında
`apt-get --purge remove` ve ardından `apt-get --purge autoremove` çalıştırır.
Bu nedenle live-boot kaldırıldığında otomatik kurulmuş
live-boot-initramfs-tools bağımlılığı da gereksiz hâle gelirse temizlenir.

Debian Trixie depolarında bulunmayan Ubuntu paketi casper, kaldırma listesinden
çıkarılmıştır.

## Calamares Module Configuration Audit

Reviewed: 2026-11-10

- Reviewed the six module configurations: `displaymanager.conf`,
  `users.conf`, `services-systemd.conf`, `umount.conf`,
  `welcome.conf`, and `packagechooser.conf`.
- The SDDM display-manager configuration selects the Plasma Wayland
  session (`/usr/bin/startplasma-wayland`, desktop file `plasma`).
- `plasma-workspace` is included in the default
  `bibotto-desktop.list.chroot` package list.
- The optional offline repository does not contain `plasma-workspace`;
  this is expected because it contains the optional package groups and
  their dependencies, not the default desktop package set.
- User defaults, system services, emergency unmount, storage
  requirement, and optional package chooser settings were reviewed.
- Configuration/source review completed. Actual ISO file presence,
  live-session startup, and installed-system behavior remain untested.

## Calamares Branding Asset Locations

Authoritative branding sources are stored in `branding/calamares/bibotto/`.
The live-build include target is `config/includes.chroot/etc/calamares/branding/bibotto/`.

Current assets are `branding.desc`, `development.svg`, and `email.svg`.
The source and target copies were compared successfully on 2026-11-10.
The `auto/build` entry point synchronizes this directory before invoking `lb build noauto`. Its sync-only mode has been tested; a full ISO build has not.

## Automated Calamares Branding Synchronization

`auto/build` copies the authoritative files from
`branding/calamares/bibotto/` into
`config/includes.chroot/etc/calamares/branding/bibotto/` before invoking
`lb build noauto`.

Set `BIBOTTO_BRANDING_SYNC_ONLY=1` to run the synchronization step and exit
without starting the ISO build.

## Offline Repository Emergency Cleanup

The shellprocess module descriptor is overridden at:

`config/includes.chroot/usr/lib/x86_64-linux-gnu/calamares/modules/shellprocess/module.desc`

The descriptor and `shellprocess-offline-repo-cleanup.conf` both enable `emergency: true`.

The cleanup script attempts source restoration and temporary repository removal even if `apt-get clean` fails. It preserves source backups that could not be restored and returns a failure status when cleanup operations fail.

This behavior has passed isolated shell tests. Actual Calamares execution and ISO validation are still pending.

## Offline APT Repository Transaction Safety

The offline repository setup and cleanup scripts use a transaction marker at:

`/var/tmp/bibotto-apt-sources-backup/.bibotto-transaction`

Setup validates existing paths before modifying APT sources, rejects collisions, backs up the original source configuration, and atomically publishes the temporary offline source.

Emergency cleanup checks for the marker before changing anything. Without an active marker it exits without touching APT sources or repository data. With a marker it attempts to restore the original sources and remove transaction-owned temporary files. Unrestored backups are preserved.

Isolated integration tests cover normal setup/cleanup, an existing repository collision, and an `apt-get update` failure. Real Calamares and ISO validation remain pending.

### Emergency Module Selection

The shellprocess module descriptor supports emergency execution. Emergency behavior is enabled only on the `offline-repo-cleanup` instance. The `offline-repo-setup` and `crypttab-luks-fix` instances remain ordinary modules.

The project configuration audit confirmed these three settings. Runtime failure handling still requires validation in a built installer.

### Calamares Module Package Compatibility

The configured installer sequence references 24 Calamares modules. A static audit against the extracted Calamares 3.3.14 core package confirmed that every referenced module has a descriptor and its declared Python or native load target.

The project shellprocess descriptor overlay was also checked against the core package: its native load target matches, and emergency capability is enabled.

This confirms package-file availability only. It does not replace runtime testing of Calamares or an installed ISO.

## Unpackfs Configuration

Bibotto provides its own `unpackfs.conf`. It instructs Calamares to unpack
`/run/live/medium/live/filesystem.squashfs` into the target root.

The installer package list explicitly includes `rsync`, which the unpackfs
module invokes for filesystem copying, and `squashfs-tools`, which provides
squashfs utilities. The source path must be confirmed against the built ISO
before declaring the installer runtime validated.

## Mount and Fstab Behavior

The mount module creates the configured Btrfs root and home subvolumes
when the selected root filesystem is Btrfs. The fstab module consumes
the resulting subvolume list and mount options. The current configuration
uses no swap by default and does not create a tmpfs mount for `/tmp`.
These behaviors have been statically reviewed against Calamares 3.3.14;
VM validation is pending.

## User Account and Privilege Configuration

The Calamares users module assigns the sudo group to the created user.
The target system's Debian sudoers policy grants administrative privileges
to members of that group. `sudoersGroup` is intentionally omitted to avoid
generating a duplicate installer-managed sudoers file.

Root password setup and automatic login are disabled. Weak passwords are
not allowed, the configured minimum password length is eight characters,
and user home directories use 0700 permissions.

The configuration has been statically reviewed. Runtime validation in a VM
is still required.

## LUKS and Initramfs Configuration

- Automated partitioning uses LUKS2 for the encrypted root and a separate unencrypted /boot.
- The installer package list includes cryptsetup and cryptsetup-initramfs; the kernel package list includes initramfs-tools.
- Calamares initramfscfg detects encrypted root and copies encrypt_hook_nokey when /boot is separate and unencrypted.
- encrypt_hook_nokey copies the generated /etc/crypttab into the target initramfs without copying a keyfile.
- The crypttab-luks-fix shellprocess runs immediately after fstab generation and ensures the encrypted root mapper entry has the luks option.
- The fix is tested in isolated temporary roots; real boot-time unlock behavior still requires VM validation.

## GRUB BIOS and UEFI Bootloader

- Calamares uses GRUB for UEFI and BIOS installations.
- UEFI bootloader identity is Bibotto.
- UEFI fallback installation is enabled.
- GRUB distributor branding comes from branding.desc bootloaderEntryName.
- grub-common, grub2-common, grub-pc-bin, grub-efi-amd64-bin and efibootmgr are included in the live-build bootloader package list.
- These packages are carried into the installed system through unpackfs; they are not sourced from the separate offline APT repository.

## SDDM and Plasma Session Configuration

- SDDM is the configured display manager and is enabled through services-systemd.conf.
- Plasma Wayland is the configured default desktop session.
- The live environment uses the bibotto account and SDDM autologin.
- Calamares disables target-system autologin when no autoLoginUser is supplied, preventing the live username from being forced onto the installed system.
- The configured desktop session is written to the target SDDM configuration.

## Network Configuration

- The live system includes `network-manager`, `wpasupplicant` and `wireless-regdb`.
- Calamares runs `networkcfg` after user creation and display-manager configuration, before service enablement.
- `networkcfg` can migrate applicable live NetworkManager profiles and adjust live-user profile permissions for the installed user.
- No custom Wi-Fi profiles or credentials are bundled in the current project configuration.
- `NetworkManager.service` is configured for enablement through `services-systemd.conf`.
- Runtime connectivity and profile migration must still be verified in a VM.

## Installer Package Cleanup

The Calamares `packages` module uses the APT backend with database and system updates disabled. After the offline repository is prepared, it removes these live-installer packages from the target system:

- `calamares`
- `squashfs-tools`
- `live-boot`
- `live-config`
- `live-config-systemd`

`rsync` is intentionally retained as a general-purpose system utility. The offline repository cleanup runs after the package operation. Actual package removal and dependency effects require VM verification.

### APT Autoremove Behavior

The APT backend purges the explicitly listed packages and then invokes autoremove. Dependencies still required by other installed packages should be retained. This behavior must be verified against the actual installed Bibotto target in a VM.

## Initramfs and Encrypted Root

The automatic partition layout uses an unencrypted ext4 `/boot` and a LUKS2-encrypted Btrfs root filesystem.

Calamares `initramfscfg` detects the separate unencrypted `/boot` and selects `encrypt_hook_nokey`. This hook copies the target `/etc/crypttab` into initramfs without embedding a keyfile. The custom crypttab correction runs before initramfs generation. GRUB configuration and bootloader installation follow afterward.

The `luksbootkeyfile` module is not in the active sequence. The documented password-based boot design is established for the automatic separate-`/boot` layout. Manual partitioning remains enabled, but other layouts require separate validation.

## BIOS and UEFI Bootloader Configuration

Calamares uses GRUB for both supported firmware modes.

- BIOS: GRUB is installed with target `i386-pc` on the boot device selected by Calamares.
- UEFI: GRUB uses the x86_64 EFI target. The EFI System Partition is mounted at `/boot/efi`.
- EFI bootloader ID: `Bibotto`.
- EFI fallback installation: enabled.
- GRUB defaults: timeout 5 seconds, default entry 0, Bibotto distributor branding.

The distribution target is amd64/x86_64. 32-bit UEFI and other CPU architectures are not supported project targets. BIOS and UEFI runtime validation remains pending until VM installation tests.

## Finished Installation Page

Bibotto configures Calamares' finished page through
`/etc/calamares/modules/finished.conf`.

- `restartNowMode: user-unchecked` displays a restart checkbox without selecting it by default.
- `restartNowCommand: "systemctl -i reboot"` is executed only when the user selects restart and confirms completion.
- A failed installation switches the restart mode to `never`.
- The finished page remains part of the final `show` sequence.


## Calamares Log Upload Privacy

Bibotto explicitly disables external Calamares log uploads using `uploadServer.type: none`. No external pastebin endpoint is configured.

## GRUB Bootloader Installation

Calamares is configured to use GRUB for both BIOS and UEFI installations.

- BIOS uses the `i386-pc` target.
- 64-bit x86 UEFI uses the `x86_64-efi` target.
- The EFI bootloader identity is `Bibotto`.
- EFI fallback installation is enabled, allowing the fallback loader to be copied to `EFI/BOOT/BOOTX64.EFI`.
- `grub-mkconfig` generates the final GRUB configuration after bootloader installation.

The live-build package list includes BIOS and UEFI GRUB modules and `efibootmgr`. These settings have passed static review; actual BIOS/UEFI installation and boot tests remain pending.

## Installed-System GRUB Defaults

Calamares currently configures:

- `GRUB_TIMEOUT=5`
- `GRUB_DEFAULT=0`
- `GRUB_DISTRIBUTOR=Bibotto`
- Kernel command-line default `quiet`, with LUKS parameters generated from the selected partition layout.

The live ISO's `quiet splash` arguments are separate from the installed system's GRUB configuration.

Plymouth is intentionally not installed yet. Its graphical boot splash is deferred until Bibotto's own boot artwork and theme are ready.

`os-prober` is not part of the target package lists. Debian GRUB 2.12 also initializes `GRUB_DISABLE_OS_PROBER=true` in `grub-mkconfig`, so automatic discovery of other operating systems remains disabled by default.

## Live ISO Boot Configuration

- The live image is configured as `iso-hybrid`.
- BIOS boot uses `grub-pc` with a GRUB2 El Torito image and hybrid MBR metadata.
- UEFI boot uses `grub-efi` and a separate FAT EFI image included in the ISO.
- The main ISO filesystem is not FAT32; the EFI boot image is FAT-formatted.
- `LB_UEFI_SECURE_BOOT` remains `auto`, allowing live-build to use signed shim/GRUB binaries when available and otherwise continue with a warning.
- Installed-system GRUB configuration and the live ISO bootloader are separate stages.

## ISO Build Host Requirements

- Run the build entrypoint with root privileges because live-build performs privileged mount and chroot operations.
- Build command: `sudo ./auto/build`.
- The build entrypoint synchronizes Calamares branding before invoking `lb build noauto`.
- Host-side ISO, SquashFS, GRUB, and EFI image utilities were verified before the first build.

## First ISO Artifact

- Artifact: `bibotto-linux-amd64.hybrid.iso`.
- Volume ID: `BIBOTTO_LINUX_0_1`.
- BIOS and UEFI El Torito entries are present.
- Live filesystem, kernel, and initrd are present in the ISO.
- Structural inspection does not replace BIOS/UEFI VM boot tests or a complete installation test.
