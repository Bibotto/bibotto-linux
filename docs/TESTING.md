# Bibotto Linux — Testing Plan

**Status:** Test plan only. Results must be recorded after tests are run.

## 1. Testing Principles

Every test record should include:

- Date and tester.
- Project revision or source identifier.
- Build environment and host details.
- ISO filename, size, and SHA-256 checksum.
- Exact steps and expected result.
- Actual result and relevant logs.
- Pass, fail, or blocked status.

A successful package simulation is not a substitute for a built ISO or installed-system test.

## 2. Current Evidence

| Test | Result | Notes |
|---|---|---|
| Active package inventory | Passed | 111 unique package names |
| APT dependency simulation | Passed with limitations | WSL, `--no-install-recommends` |
| Calamares availability | Confirmed | Debian Trixie candidate 3.3.14-1 |
| Full ISO build | Passed | First hybrid ISO built successfully |
| ISO checksum | Passed | SHA-256 generated and verified |
| UEFI boot | Passed | Hyper-V Generation 2; Secure Boot disabled |
| BIOS boot | Passed | Hyper-V Generation 1 |
| Calamares installation | Not tested | No completed installation |
| Offline repository index | Passed | Isolated APT state; local `file:` repository index loaded |
| Offline dependency simulation | Passed with limitations | Five optional package roots; 1,059 packages resolved; no actual installation |
| Optional packagechooser | Configuration present | Runtime UI and selection behavior untested |
| Calamares offline integration | Configuration present | Shellprocess setup and cleanup not tested in a real installation |
| Real hardware | Not tested | No validation evidence |

## 3. Build Tests

- [ ] Build from a clean documented Debian environment.
- [ ] Confirm repository access and package resolution.
- [ ] Confirm hooks resolve and execute.
- [ ] Check unexpected package removals and dependency errors.
- [ ] Record build duration and peak disk usage.
- [ ] Confirm ISO artifact exists and is non-empty.
- [ ] Generate and verify SHA-256.
- [ ] Inspect ISO boot files and optional package payloads.

## 4. Virtual Machine Boot Matrix

| Environment | Result | Notes |
|---|---|---|
| UEFI, Secure Boot off | Passed | ISO booted; KDE desktop interaction verified; installer not tested |
| UEFI, Secure Boot on | Pending | Separate Secure Boot test |
| Legacy BIOS | Passed | Hyper-V Generation 1 live desktop |
| Low-memory VM | Pending | Boot stability and memory use not tested |
| No network | Live desktop and installer behavior |
| Multiple virtual disks | Safe disk selection |

## 5. Installer Tests

- [ ] Automatic partitioning on empty disk.
- [ ] Manual partitioning.
- [ ] EFI partition creation and reuse.
- [ ] Btrfs root and `@home`.
- [ ] ext4 path, if retained.
- [ ] LUKS2 encrypted installation.
- [ ] User creation and password validation.
- [ ] Locale and keyboard configuration.
- [ ] Hostname configuration.
- [ ] GRUB installation and boot.
- [ ] Cancellation and error handling.
- [ ] Reboot after removing ISO.

## 6. Optional Package Tests

### Completed repository checks

- [x] Download the optional package dependency closure into the repository payload.
- [x] Generate `Packages` and `Packages.gz` indexes.
- [x] Load the local repository using an isolated APT configuration.
- [x] Simulate dependency resolution for `build-essential`, `docker.io`, `docker-compose`, `kmail`, and `thunderbird`.

The repository contains 1,059 `.deb` files and occupies approximately 678 MB. The simulation ended with 1,059 newly installed packages and no reported missing dependencies or conflicts. It did not install packages and did not exercise Calamares.

### Remaining runtime tests

Run the installer without network access.

- [ ] Select no optional groups; confirm none are installed.
- [ ] Verify LibreOffice is installed in the default desktop installation.
- [ ] Select Development only; verify requested tools.
- [ ] Select Email only; verify KMail and Thunderbird.
- [ ] Select all groups; verify dependency resolution.
- [ ] Verify choices reach the Calamares package module.
- [ ] Verify the setup shellprocess finds the repository on the booted ISO.
- [ ] Verify the target APT index is updated from the local repository.
- [ ] Verify cleanup restores the original APT sources and removes temporary files.
- [ ] Verify local package source cleanup.
- [ ] Confirm optional packages are absent by default.

## 7. Installed System Tests

- [ ] First boot reaches SDDM.
- [ ] Wayland session starts.
- [ ] X11 fallback starts, if shipped.
- [ ] User can log in and use `sudo`.
- [ ] NetworkManager connects to wired and wireless networks.
- [ ] Audio input and output work.
- [ ] Bluetooth works.
- [ ] Display scaling and multi-monitor behavior work.
- [ ] Suspend and resume work.
- [ ] AppArmor has expected active profiles.
- [ ] Firewall has expected policy.
- [ ] Updates can be applied.
- [ ] Kernel/initramfs update and fallback work.
- [ ] Btrfs snapshots and recovery work, if advertised.

## 8. Hardware Validation

Test representative AMD, Intel, and NVIDIA graphics configurations as applicable, plus networking, Bluetooth, audio, storage controllers, and UEFI firmware.

Record exact hardware identifiers and driver/firmware versions. Do not claim broad compatibility from one machine.

## 9. Release Gate

Do not publish a release until:

1. A clean ISO build succeeds.
2. The checksum is verified.
3. Live boot works in all declared supported firmware modes.
4. Calamares completes installation on a clean test disk.
5. Installed system boots without the ISO.
6. Offline optional package selection works correctly.
7. Security and update behavior are checked.
8. Known issues are documented.

<!-- bibotto-calamares-3.3.14-audit-tests -->
## Calamares 3.3.14-1 denetim sonuçları

Tamamlanan incelemeler:
- [x] Calamares Debian Trixie sürümü doğrulandı: `3.3.14-1`.
- [x] Fstab, GRUB ve Mount YAML şemaları incelendi.
- [x] Mevcut üç yapılandırmanın şema alanları ve veri tipleri kontrol edildi.
- [x] Fstab modülünün açık `/boot` + LUKS kök için crypttab seçeneklerini boşalttığı kaynak kodundan doğrulandı.
- [x] Initramfs yapılandırmasının `encrypt_hook_nokey` kullandığı ve crypttab dosyasını initramfs'e kopyaladığı doğrulandı.
- [x] Debian Trixie crypttab belgesinde seçenek belirtilmediğinde varsayılan türün `plain` olduğu doğrulandı.

Henüz yapılmayan testler:
- [ ] Kök crypttab kaydına `luks` ekleyen düzeltmenin uygulanması ve sentetik dosyalarla test edilmesi.
- [ ] `partition.conf` anahtarlarının Calamares 3.3.14-1 ile ayrıca doğrulanması.
- [ ] Gerçek ISO oluşturma ve sanal makinede UEFI/BIOS açılış testi.
- [ ] LUKS2 parola istemi, kök dosya sistemi açılması ve kurulum sonrası ilk açılış testi.

YAML şema kontrolü veya kaynak kod incelemesi, gerçek ISO/kurulum testi yerine geçmez.

## LUKS crypttab düzeltmesi — sentetik testler

`crypttab-luks-fix` shellprocess için YAML ve Bash sözdizimi doğrulandı.
Sentetik hedef sistemlerde şu senaryolar başarılı: boş seçenek alanına `luks`
ekleme, şifresiz kökte değişiklik yapmama, mevcut seçenekleri koruma,
başka şifreli bölüm kaydını koruma ve eşleşmeyen kayıt durumunda hata verme.
Bunlar gerçek Calamares kurulumu veya ISO açılış testi değildir.

## BIOS / UEFI yapılandırma denetimi

Calamares 3.3.14 kaynak şemasıyla mevcut partition ayarları karşılaştırıldı.
EFI ayarlarının desteklendiği doğrulandı. Debian GRUB EFI paketinin sabit
`debian` EFI dizin gereksinimine uygun bootloader kimliği ayarlandı.
Gerçek BIOS/UEFI sanal makine açılış ve kurulum testleri henüz yapılmadı.

### 2026-11-10 — Calamares live paket temizliği

- Calamares 3.3.14 APT backend kaynak kodu incelendi.
- `remove` işleminin purge ve autoremove uyguladığı doğrulandı.
- `casper` paketinin Debian Trixie APT kaynaklarında bulunmadığı doğrulandı.
- `packages.conf` listesinden `casper` çıkarıldı.
- YAML ve beklenen paket listesi doğrulandı.
- Gerçek Calamares kurulumu henüz çalıştırılmadı.

### 2026-11-10 — Live paketlerinin doğrudan kurulum kontrolü

Tüm `config/package-lists/*.list.chroot` dosyaları tarandı.
`live-boot`, `live-config` ve `live-config-systemd` yalnızca
`live.list.chroot` içinde doğrudan tanımlı. `live-boot-initramfs-tools`
hiçbir paket listesinde doğrudan tanımlı değil. APT autoremove davranışının
gerçek live-build ortamında doğrulanması ISO testine bırakıldı.

### 2026-11-10 — Offline APT deposu bütünlük testi

- `Packages.gz` açılarak `Packages` ile byte düzeyinde karşılaştırıldı.
- İndeks kaydı: 1.059 paket.
- Fiziksel `.deb` dosyası: 1.059.
- Eksik veya indekste bulunmayan dosya: 0.
- SHA256 doğrulaması başarılı: 1.059/1.059.
- Sonuç: Offline depo dosya ve indeks bütünlüğü doğrulandı.
- Gerçek ISO açılışı ve Calamares kurulumu henüz test edilmedi.

### 2026-11-10 — Live açılış parametreleri ve ISO metadata

- Debian Trixie `live-config` 11.0.5 paketindeki `0085-sddm`
  bileşeni incelendi.
- `nocomponents=sddm` parametresinin SDDM live-config bileşenini
  devre dışı bıraktığı doğrulandı.
- Parametre kaldırıldı; live açılış komut satırı sadeleştirildi.
- ISO metadata ve dosya adı Bibotto markasına göre güncellendi.
- `config/binary` ve `config/common` için `bash -n` başarılı.
- ISO metadata alanlarının uzunluk sınırları kontrol edildi; tümü PASS.
- `LB_NET_TARBALL` varsayılanı true olarak bırakıldı. Kaynak koduna
  göre netboot tarball üretimi yalnızca `LB_IMAGE_TYPE=netboot`
  olduğunda çalışır; mevcut ISO-hybrid yapılandırmasında etkisizdir.
- Gerçek ISO üretimi ve açılış testi henüz yapılmadı.

## 2026-11-10 — Calamares Module Configuration Review

- Reviewed `displaymanager.conf`, `users.conf`,
  `services-systemd.conf`, `umount.conf`, `welcome.conf`,
  and `packagechooser.conf`.
- Confirmed `plasma-workspace` is in the default desktop package list.
- Confirmed its absence from the optional offline repository is
  consistent with the repository's intended scope.
- This is a configuration and package-list review only.
- Pending: verify the Wayland executable and session desktop file
  inside the built ISO/live filesystem; test SDDM and Plasma startup.

## SVG Dönüştürme Testi
- [2026-11-10] Debian 13 üzerinde rsvg-convert doğrulandı; 128x128 SVG dosyası geçerli PNG çıktısına dönüştürüldü.

## Calamares Branding Source Verification

- [2026-11-10] Compared `branding/calamares/bibotto/` with
  `config/includes.chroot/etc/calamares/branding/bibotto/` using `diff -r`.
- Result: no differences; all three files matched.
- This verifies file synchronization at this point only; it does not verify
  Calamares runtime rendering or an installed ISO.

## Calamares Branding Build Synchronization Test

- [2026-11-10] `sh -n auto/build` passed.
- [2026-11-10] `BIBOTTO_BRANDING_SYNC_ONLY=1 ./auto/build` passed.
- Source and ISO target branding directories were compared with `diff -r`;
  no differences were reported.
- This test does not run or validate a complete live-build ISO build.

## Calamares Branding Synchronization Test

- Date: 2026-11-10
- `sh -n auto/build`: PASS.
- `BIBOTTO_BRANDING_SYNC_ONLY=1 ./auto/build`: PASS.
- `diff -r branding/calamares/bibotto config/includes.chroot/etc/calamares/branding/bibotto`: exit code 0.
- Result: source and target branding files match.
- Scope: synchronization only; no ISO build or installer runtime test was performed.

## Offline APT Repository Emergency Cleanup Test — 2026-11-10

- Shell syntax validation: PASS (`sh -n`).
- YAML parsing of module descriptor: PASS.
- YAML parsing of cleanup configuration: PASS.
- Emergency metadata detected in both files: PASS.
- Isolated successful cleanup and APT source restoration: PASS.
- Isolated `apt-get clean` failure handling: PASS.
- APT source restoration after simulated failure: PASS.
- Real Calamares emergency execution: NOT TESTED.
- ISO build and installer runtime: NOT TESTED.

## Offline APT Repository Setup/Cleanup Integration — 2026-11-10

- Setup YAML parsing: PASS.
- Cleanup YAML parsing: PASS.
- Shell syntax for setup and cleanup scripts: PASS.
- Shellprocess emergency metadata: PASS.
- Normal setup followed by cleanup: PASS.
- Existing repository-cache collision preserves existing data: PASS.
- APT update failure followed by emergency source restoration: PASS.
- Tests used temporary target roots and a mocked `chroot` command.
- Real APT operations, Calamares runtime, and ISO boot: NOT TESTED.

### Calamares Emergency Module Selection Test — 2026-11-10

- Shellprocess descriptor emergency capability: PASS.
- Offline repository setup instance is not emergency: PASS.
- Crypttab fix instance is not emergency: PASS.
- Offline repository cleanup instance is emergency: PASS.
- This test validates configuration metadata only; Calamares runtime behavior remains untested.

### Calamares Module Load Target Audit — 2026-11-10

- Modules referenced by settings: 24.
- Python module entry points: all present.
- Native module libraries: all present.
- Missing module descriptors: 0.
- Missing load targets: 0.
- Shellprocess overlay descriptor: PASS.
- Overlay load target matches core package: PASS.
- Overlay emergency capability: PASS.
- Result: 24/24 modules passed static load-target checks.
- Runtime module loading and installer execution: NOT TESTED.

## Calamares Unpackfs Static Validation

- Parsed `unpackfs.conf` successfully with PyYAML.
- Verified the squashfs source, filesystem type, and empty destination.
- Verified that `rsync` executes in the Debian build environment.
- Verified that `rsync` is listed in the installer live-system package list.
- A built ISO and a real installation test are still pending.

## Calamares Mount and Fstab Static Review

- Reviewed both module implementations and their configuration schemas.
- Confirmed Btrfs subvolume handling and mount-option propagation.
- Confirmed `tmpOptions.default.tmpfs: false`.
- Confirmed the configured EFI and LUKS handling paths.
- No real disk partitioning or installation was performed.

## Calamares Users Configuration Review

- Confirmed sudo group exists with GID 27 in the development environment.
- `visudo -c` passed for the Debian sudoers configuration.
- Confirmed the `%sudo ALL=(ALL:ALL) ALL` rule.
- Reviewed defaultGroups map syntax against the Calamares 3.3 implementation.
- VM user creation and installed-system sudo validation remain pending.

## Calamares LUKS and Crypttab Tests

- Verified the Calamares initramfscfg module implementation and encryption hook files.
- Verified the cryptsetup package list and initramfs-tools package list.
- Verified the live-build cryptsetup hook symlink target exists.
- Isolated crypttab tests:
  - Encrypted root adds the luks option: PASS.
  - Existing crypttab options are preserved: PASS.
  - Existing luks option is not duplicated: PASS.
  - Unencrypted root is a no-op: PASS.
  - Missing mapper entry fails: PASS.
  - Duplicate mapper entries fail: PASS.
- All six isolated tests passed.
- No real disk encryption, ISO boot or VM installation test has been performed.

## Calamares GRUB and UEFI Configuration Review

- Bootloader YAML parsed successfully.
- Confirmed efiBootLoader=grub, efiBootloaderId=Bibotto and installEFIFallback=true.
- Reviewed Calamares grubcfg kernel parameter generation and bootloader installation flow.
- Confirmed the five required bootloader package names are present in bibotto-bootloader.list.chroot.
- Confirmed their absence from the separate offline APT repository; no offline package installation is configured for these packages.
- No actual BIOS/UEFI boot test has been performed.

## SDDM and Plasma Static Configuration Review

- Reviewed displaymanager.conf, sddm.conf and services-systemd.conf.
- Confirmed SDDM and Plasma packages are listed and have Debian Trixie candidates.
- Confirmed live-config defines the live username as bibotto.
- Reviewed Calamares 3.3.14 SDDM implementation: it removes Autologin.User when no autoLoginUser exists and writes the configured desktop session.
- No graphical login, Wayland session, or X11 fallback runtime test has been performed.

## NetworkManager and networkcfg Static Review

- [x] Confirmed `networkcfg` is present in the Calamares execution sequence.
- [x] Confirmed `networkcfg` runs before `services-systemd`.
- [x] Confirmed `NetworkManager.service` is configured for enablement.
- [x] Confirmed `network-manager`, `wpasupplicant` and `wireless-regdb` are in the hardware package list.
- [x] Confirmed Debian Trixie has a `wireless-regdb` package candidate.
- [x] Confirmed no custom NetworkManager connection profiles are included.
- [ ] Test Ethernet and Wi-Fi connectivity in a booted live ISO.
- [ ] Verify NetworkManager service and connectivity after installation in a VM.

The static Python assertions passed. The WSL development environment's empty `systemctl cat NetworkManager.service` output is not treated as evidence about the built ISO.

## Calamares Installer Package Cleanup Review

- [x] Confirmed APT is the configured package backend.
- [x] Confirmed database and system updates are disabled.
- [x] Confirmed offline repository setup precedes the packages module.
- [x] Confirmed offline repository cleanup follows the packages module.
- [x] Confirmed the removal list contains `calamares`, `squashfs-tools`, `live-boot`, `live-config` and `live-config-systemd`.
- [x] Confirmed `rsync` remains in the installer package list.
- [ ] Verify APT package removal and autoremove behavior in a VM.
- [ ] Verify the installed system retains required desktop, network, filesystem and boot packages.

Static YAML and package-list assertions passed. No real APT removal or ISO installation has been tested.

### APT Autoremove Dependency Review

- [x] Reviewed direct dependencies of Calamares and squashfs-tools.
- [x] Confirmed rsync is not in the removal list.
- [ ] Simulate APT removal and autoremove against the built target system.
- [ ] Verify Plasma, networking, Btrfs, encryption and boot functionality afterward.

The current apt-cache output is from the Debian development environment, not the installed Bibotto target.

## Initramfs and LUKS Static Validation

- [x] Reviewed Calamares `initramfscfg` source and both encryption hooks.
- [x] Confirmed separate unencrypted `/boot` selects `encrypt_hook_nokey`.
- [x] Confirmed the no-key hook copies `/etc/crypttab` into initramfs.
- [x] Confirmed no project keyfile is generated or included in the active sequence.
- [x] Confirmed cryptsetup packages and live-build hook are configured.
- [x] Confirmed crypttab correction precedes initramfs generation.
- [x] Confirmed GRUB configuration and bootloader follow initramfs.
- [ ] Verify password prompt and encrypted-root boot in BIOS and UEFI VMs.
- [ ] Test supported manual partitioning layouts.

Static source and configuration checks passed. No actual ISO or VM boot test has been performed.

## BIOS and UEFI Bootloader Static Validation

- [x] Verified Calamares GRUB selection for BIOS and UEFI.
- [x] Verified BIOS `i386-pc` installation path.
- [x] Verified x86_64 UEFI target and EFI fallback file handling.
- [x] Verified EFI System Partition mount point `/boot/efi`.
- [x] Verified `Bibotto` EFI bootloader ID and branding input.
- [x] Verified GRUB timeout and default entry settings.
- [x] Verified LUKS root kernel parameters and separate `/boot` behavior.
- [ ] Test BIOS installation and boot in a VM.
- [ ] Test UEFI installation, EFI fallback and boot in a VM.
- [ ] Test encrypted-root password prompt and successful boot.

These are static source/configuration checks. No ISO installation or VM boot test has been performed.

## Finished Module Static Validation

- [x] Confirmed `finished` is a Calamares Qt view module.
- [x] Confirmed `user-unchecked` is an accepted restart mode in Calamares 3.3.14.
- [x] Confirmed the checkbox starts unchecked and restarts only when selected.
- [x] Confirmed failed installation disables restarting.
- [x] Added the explicit Bibotto restart command.
- [ ] Verify the finished page visually in a VM.
- [ ] Test both checked and unchecked restart behavior in a VM.
- [ ] Verify the failure screen does not restart the system.

Static source/configuration validation only; no graphical runtime test has been performed.


## Calamares Log Upload Configuration Validation

- [x] Branding YAML parsed successfully.
- [x] `uploadServer.type` verified as `none`.
- [x] `uploadServer.sizeLimit` verified as `0`.
- [ ] Runtime behavior to be verified in an actual installer session.

## GRUB BIOS and UEFI Static Validation

- [x] Confirmed Calamares accepts the configured GRUB bootloader selection.
- [x] Confirmed BIOS installation uses `i386-pc`.
- [x] Confirmed 64-bit x86 UEFI installation uses `x86_64-efi`.
- [x] Confirmed EFI identity `Bibotto` and fallback installation setting.
- [x] Confirmed GRUB configuration generation follows installation.
- [x] Reviewed BIOS and UEFI GRUB package metadata.
- [ ] Test BIOS installation and boot in a VM.
- [ ] Test UEFI installation, NVRAM entry and fallback boot in a VM.
- [ ] Test encrypted-root boot in both firmware modes.

Static source/configuration checks only; no firmware or VM boot test has been performed.

## GRUB Boot Experience Static Validation

- [x] Verified GRUB timeout and default entry settings.
- [x] Verified Calamares distributor branding and kernel parameter generation.
- [x] Distinguished live ISO boot arguments from installed-system GRUB arguments.
- [x] Verified Plymouth is absent from target package lists.
- [x] Verified `os-prober` is absent from target package lists.
- [x] Verified Debian GRUB 2.12 initializes `GRUB_DISABLE_OS_PROBER=true`.
- [ ] Test the installed GRUB menu and kernel command line in a VM.
- [ ] Review the boot appearance after the first real ISO build.

Static source/configuration review only; no ISO or VM boot test has been performed.

## Live ISO BIOS/UEFI Static Validation

- Reviewed `config/binary` and the installed live-build scripts.
- Confirmed the `iso-hybrid` BIOS GRUB2 and UEFI boot paths in `binary_iso`, `binary_grub-pc`, and `binary_grub-efi`.
- Confirmed UEFI image creation uses a FAT filesystem and copies EFI boot files plus a GRUB configuration into `boot/grub/efi.img`.
- Confirmed live-build checks the required EFI GRUB modules, `grub-mkimage`, `mtools`, and `dosfstools`.
- `LB_UEFI_SECURE_BOOT=auto` is best effort, not proof of Secure Boot operation.
- Completed: ISO build and BIOS/UEFI live boot tests. Secure Boot validation remains pending.

## First ISO Build Preflight Validation

- Verified `sudo -v` succeeds.
- Verified `lb` version and required host commands.
- Verified installed packages: xorriso, squashfs-tools, grub-common, grub-pc-bin, grub-efi-amd64-bin, mtools, and dosfstools.
- Verified `mcopy` and `mkfs.msdos` are executable.
- Verified available disk space and empty output directory.
- No ISO build or boot test performed during this preflight.

## First Hybrid ISO — Structural Validation

- Build completed successfully using live-build.
- `xorriso -report_el_torito plain` reports both BIOS and UEFI boot images.
- BIOS image: `/boot/grub/grub_eltorito`.
- UEFI image: `/boot/grub/efi.img`.
- ISO reports MBR and GPT hybrid boot metadata.
- `/live` contains `filesystem.squashfs`, `vmlinuz`, and `initrd.img`.
- SHA-256: `06ed32e5e587989cdc34d44c2356e8a1a533803facca1fe0bc874113d92c83bb`.
- No VM boot or installer runtime test has been performed yet.

### BIOS Live ISO Boot — 2026-11-11

Environment: Hyper-V Generation 1, 4096 MB RAM, 2 virtual CPUs, network disconnected.

- ISO: `bibotto-linux-amd64.hybrid.iso`
- Windows-host SHA-256 matched the Debian build artifact.
- BIOS boot reached the KDE Plasma live desktop.
- Mouse, application launcher, desktop context menu, and `Ctrl+Alt+T` terminal launch were checked successfully.
- Installed-system boot, GRUB installation, networking, audio, and display scaling were not part of this test.

### UEFI Live ISO Boot — 2026-11-11

Environment: Hyper-V Generation 2, 4096 MB RAM, 2 virtual CPUs, network disconnected, Secure Boot disabled.

- ISO: `bibotto-linux-amd64.hybrid.iso`
- DVD drive was first in the UEFI boot order.
- Boot reached the KDE Plasma live desktop successfully.
- Mouse, application launcher, desktop context menu, and `Ctrl+Alt+T` terminal launch were checked successfully.
- Secure Boot, Calamares installation, installed-system boot, and UEFI NVRAM/fallback installation behavior were not tested.


## Latest ISO Artifact — 2026-11-12

| Field | Result |
|---|---|
| ISO | `bibotto-linux-amd64.hybrid.iso` |
| Build tool | live-build `20250505+deb13u1` |
| Build | Passed |
| Size | `2,514,907,136` bytes |
| SHA-256 | `0af6ff5d5bdc7003ddc18ed3e600db7fd973c28a2ffded4221ef56e82ef21799` |
| SquashFS | `/live/filesystem.squashfs`, 1,654,091,776 bytes |
| Bibotto Light scheme | Present in extracted SquashFS |
| Bibotto Dark scheme | Present in extracted SquashFS |
| System KDE default | `ColorScheme=BibottoLight` |
| New-user KDE default | `ColorScheme=BibottoLight` |
| Latest ISO Hyper-V Generation 1 BIOS boot | Passed — live KDE desktop reached |
| KDE visual/runtime test | Pending |
| Calamares installation | Pending |

The first ISO is preserved at
`releases/archive/bibotto-linux-amd64-first.iso`.
Its SHA-256 remains
`06ed32e5e587989cdc34d44c2356e8a1a533803facca1fe0bc874113d92c83bb`.

These checks confirm the ISO artifact and selected SquashFS contents;
they do not replace VM boot, graphical-session, installer, or
installed-system testing.

## Windows ISO Transfer Verification — 2026-11-12

- Destination: `C:\\Hyper-V\\Bibotto\\bibotto-linux-amd64.hybrid.iso`
- Source and destination SHA-256 values match.
- Verified SHA-256: `0af6ff5d5bdc7003ddc18ed3e600db7fd973c28a2ffded4221ef56e82ef21799`.
- Hyper-V boot testing of this latest ISO: pending.


## Latest ISO — Hyper-V Generation 1 BIOS Boot — 2026-11-12

- ISO: `bibotto-linux-amd64.hybrid.iso`
- Virtual machine firmware generation: Hyper-V Generation 1 (BIOS).
- Result: Passed.
- Evidence: The live KDE Plasma desktop opened successfully.
- Hyper-V Generation 2 (UEFI): Pending.


## Latest ISO — Hyper-V Generation 2 UEFI Boot — 2026-11-12

- ISO: `bibotto-linux-amd64.hybrid.iso`
- Virtual machine firmware generation: Hyper-V Generation 2 (UEFI).
- Result: Passed.
- Evidence: KDE live environment and application menu opened successfully.
- Secure Boot remains a separate pending test.



## Latest ISO — KDE Color Scheme Runtime Test — 2026-11-12

- Environment: Hyper-V live KDE session.
- Bibotto Light visible in Colors settings: Passed.
- Bibotto Dark visible in Colors settings: Passed.
- Bibotto Light manually applied: Passed.
- Bibotto Dark manually applied: Passed.
- Automatic application of `Bibotto-Light` at session startup: Pending.

## KDE Default Scheme Identifier Correction — 2026-11-12

- System-wide configuration: `ColorScheme=Bibotto-Light`.
- New-user configuration: `ColorScheme=Bibotto-Light`.
- Both values were checked in the chroot.
- Fresh ISO rebuild and automatic live-session application test: Pending.
