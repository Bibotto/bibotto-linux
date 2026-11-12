# Bibotto Linux — Package Manifest

**Status:** Initial inventory based on reviewed project package lists.  
**Note:** This is not a resolved dependency manifest and does not prove ISO contents.

## 1. Package Policy

Packages are classified as:

1. Default: required for the live environment or base installation.
2. Optional: delivered in the ISO and installed only when selected.
3. Build/runtime dependency: required by build or installer infrastructure.

Optional applications must not be installed into the live root if that root is copied to the target system.

## 2. Intended Optional Groups

| Optional installer choice | Intended packages |
|---|---|
| Development | `build-essential`, `docker.io`, `docker-compose` |
| Email | `kmail`, `thunderbird` |

`libreoffice` is part of the standard desktop package set and is installed by default.

The ISO-contained local APT repository has been assembled with the dependency closure for both groups. It contains 1,059 `.deb` archives and is approximately 678 MB. The repository index files `Packages` and `Packages.gz` were generated with `apt-ftparchive`.

An isolated APT test loaded the local repository and simulated installation of all five package roots. The simulation resolved 1,059 packages without reported missing dependencies or conflicts. This does not yet prove actual installation through Calamares.

**Current state:** `libreoffice` is correctly included in the active desktop package list and remains a default installation package. The optional Development and Email groups are configured separately in the Calamares packagechooser.

## 3. Active Package Lists

### Bootloader — `bibotto-bootloader.list.chroot`

- `grub-common`
- `grub2-common`
- `grub-pc-bin`
- `grub-efi-amd64-bin`
- `efibootmgr`

### Desktop — `bibotto-desktop.list.chroot`

- `sddm`
- `sddm-theme-breeze`
- `plasma-workspace`
- `plasma-desktop`
- `kwin-x11`
- `kwin-wayland`
- `xserver-xorg`
- `xserver-xorg-core`
- `xserver-xorg-input-libinput`
- `xserver-xorg-video-amdgpu`
- `xserver-xorg-video-nouveau`
- `xwayland`
- `systemsettings`
- `dolphin`
- `konsole`
- `ark`
- `kinfocenter`
- `kde-spectacle`
- `kscreen`
- `powerdevil`
- `plasma-pa`
- `plasma-nm`
- `plasma-discover`
- `plasma-discover-backend-flatpak`
- `plasma-discover-backend-fwupd`
- `kio-extras`
- `ffmpegthumbs`
- `kdegraphics-thumbnailers`
- `okular`
- `flatpak`
- `packagekit`
- `fwupd`
- `vlc`
- `vlc-l10n`
- `vlc-plugin-access-extra`
- `libreoffice` — standard desktop package; installed by default
- `xdg-desktop-portal`
- `xdg-desktop-portal-kde`
- `xdg-desktop-portal-gtk`
- `xdg-user-dirs`
- `xdg-utils`
- `breeze`
- `breeze-gtk-theme`
- `breeze-icon-theme`
- `fonts-inter`
- `fonts-noto-core`
- `fonts-noto-color-emoji`

### Filesystem — `bibotto-filesystem.list.chroot`

- `btrfs-progs`
- `cryptsetup`
- `cryptsetup-initramfs`

### Firmware — `bibotto-firmware.list.chroot`

- `firmware-linux`
- `firmware-intel-graphics`
- `firmware-nvidia-graphics`
- `firmware-realtek`
- `firmware-iwlwifi`
- `amd64-microcode`
- `intel-microcode`

### Hardware — `bibotto-hardware.list.chroot`

- `network-manager`
- `wpasupplicant`
- `wireless-regdb`
- `bluez`
- `bluez-obexd`
- `bluedevil`
- `pipewire-audio`
- `alsa-utils`
- `dbus-user-session`
- `libpam-systemd`
- `udisks2`
- `upower`
- `polkitd`
- `mesa-vulkan-drivers`
- `libgl1-mesa-dri`
- `va-driver-all`
- `exfatprogs`
- `ntfs-3g`
- `usbutils`
- `pciutils`
- `sudo`

### Installer — `bibotto-installer.list.chroot`

- `calamares`
- `squashfs-tools`
- `rsync`

### Kernel — `bibotto-kernel.list.chroot`

- `linux-image-amd64`
- `initramfs-tools`

### Productivity — `bibotto-productivity.list.chroot`

- `zip`
- `unzip`
- `tar`
- `gzip`
- `bzip2`
- `7zip`
- `unrar-free`
- `git`
- `snapper`
- `btrfs-assistant`
- `btrfsmaintenance`
- `zram-tools`

### Security — `bibotto-security.list.chroot`

- `apparmor`
- `apparmor-utils`
- `firewalld`
- `plasma-firewall`
- `nftables`
- `unattended-upgrades`
- `libpam-pwquality`

### Live system — `live.list.chroot`

- `live-boot`
- `live-config`
- `live-config-systemd`
- `systemd-sysv`
- `user-setup`

## 4. Other Planning Files

Root-level planning files reviewed:

- `packages-desktop.txt`
- `packages-developer.txt`
- `packages-email.txt`

The developer list includes `build-essential`, `docker.io`, and `docker-compose`. The email list includes `kmail` and `thunderbird`.

These files are planning inventories. Their presence does not automatically make packages active live-build lists or include their archives in the ISO.

## 5. Package Count and Dependency Check

The active lists contained 111 unique package names.

An APT simulation with `--no-install-recommends` completed without visible resolver errors in WSL. Separately, the ISO-contained local repository was tested using an isolated APT state directory and an empty package status file. The local index loaded successfully, and the dependency-resolution simulation for `build-essential`, `docker.io`, `docker-compose`, `kmail`, and `thunderbird` ended with `0 upgraded, 1059 newly installed, 0 to remove, and 0 not upgraded`.

This confirms repository index readability and simulated dependency resolution. It does not prove actual package installation, a clean live-build chroot, final ISO contents, or runtime behavior.

## 6. Validation Required

- [x] Verify package availability and simulated dependency resolution for the optional package roots against the local Debian Trixie amd64 repository.
- [x] Resolve dependency closure for both optional groups in the local repository and simulate offline dependency resolution.
- Decide Docker package source and repository policy.
- Verify package sizes and ISO size.
- Review firmware licensing and inclusion.
- Review redundant or conflicting packages.
- Generate a resolved manifest from the actual build.
