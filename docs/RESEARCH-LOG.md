

<!-- bibotto-calamares-audit-log -->
# Bibotto araştırma ve denetim kayıtları

## 2026-11-10 — Calamares 3.3.14-1 ve LUKS

İncelenen yerel paket:
`/tmp/bibotto-calamares-inspect/extracted/`

Calamares paketinin yeniden indirilmesi veya WSL ortamına kurulması gerekmiyor; açılmış paket mevcut.

İncelenen dosyalar:
- `fstab/fstab.schema.yaml`
- `grubcfg/grubcfg.schema.yaml`
- `mount/mount.schema.yaml`
- `fstab/main.py`
- `initramfscfg/main.py`
- `initramfscfg/encrypt_hook_nokey`
- `initramfscfg/encrypt_hook`
- `grubcfg/main.py`
- `partition/module.desc`
- `luksbootkeyfile/module.desc`

Bulgular:
1. Fstab, GRUB ve Mount yapılandırma şemaları incelendi.
2. Paket içinde partition şeması bulunmadı; yalnızca partition modül tanımı ve ikili modülü bulundu.
3. Fstab modülü, şifrelenmiş kök + şifrelenmemiş ayrı `/boot` düzeninde kök crypttab seçeneklerini boşaltıyor.
4. Initramfs yapılandırması bu düzende `encrypt_hook_nokey` kancasını seçiyor.
5. GRUB yapılandırması kök LUKS eşlemesi için kernel parametreleri üretiyor.
6. Debian Trixie cryptsetup sürümü `2:2.7.5-2`; crypttab belgesinde seçenek alanı boş bırakılırsa şifreleme türünün `plain` varsayıldığı belirtiliyor.
7. Kök crypttab kaydına `luks` eklenmesi gerekiyor. Düzeltme henüz uygulanmış veya ISO üzerinde test edilmiş değil.

Referanslar:
- https://github.com/calamares/calamares/blob/calamares/src/modules/fstab/main.py
- https://github.com/calamares/calamares/blob/calamares/src/modules/initramfscfg/main.py
- https://github.com/calamares/calamares/blob/calamares/src/modules/grubcfg/main.py
- https://sources.debian.org/src/cryptsetup/2%3A2.7.5-2/debian/doc/crypttab.xml
- https://mail-archive.com/ubuntu-bugs%40lists.ubuntu.com/msg6326786.html

Not: Son hata raporu Ubuntu 26.04.1 ortamındandır. Debian Trixie için kararımız Debian'ın kendi crypttab belgesine dayanmaktadır; gerçek açılış testi ayrıca yapılacaktır.

## 2026-11-10 — LUKS crypttab düzeltmesi

Calamares 3.3.14 `fstab/main.py` incelendi. Şifrelenmiş kök cihazının
`/dev/mapper/<luksMapperName>` olarak yazıldığı doğrulandı. Bu nedenle
`fstab` sonrasına, `initramfscfg` öncesine `crypttab-luks-fix` shellprocess
eklendi. İşlem yalnızca kök mapper kaydını hedefler ve seçenek alanına
`luks` ekler. Sentetik testler ve YAML/Bash sözdizimi kontrolleri geçti.
Gerçek ISO ve kurulum testi henüz yapılmadı.

## 2026-11-10 — Calamares 3.3.14 bölümleme ve EFI denetimi

Debian kaynak paketindeki `partition.schema.yaml` ve `partition.conf`
incelendi. Mevcut `partition.conf` anahtarlarının desteklendiği doğrulandı.
Bu sürümün şemasında `createHybridBootloaderLayout` ve
`defaultPartitionTableType` bulunmadığından kullanılmayacak.
Debian `bootloader.conf` kaynağı, değiştirilmemiş Debian GRUB EFI
paketleri için `efiBootloaderId: debian` gerektiğini belirtiyor.

## 2026-11-10 — live-build BIOS/UEFI ayarlarının sadeleştirilmesi

`live-build` kaynak kodunda `LB_BOOTLOADERS` değişkeninin eski uyumluluk
yolu olduğu ve tanımlandığında ayrı BIOS/EFI değişkenlerini yeniden
oluşturduğu doğrulandı. Projede açık `LB_BOOTLOADER_BIOS=grub-pc` ve
`LB_BOOTLOADER_EFI=grub-efi` ayarları korundu; eski `LB_BOOTLOADERS`
satırı kaldırıldı.

## 2026-11-10 — Calamares live paket temizliği

Calamares 3.3.14 APT backend kodu incelendi. `remove` işlemi paketleri
`apt-get --purge remove` ile kaldırıyor ve ardından `apt-get --purge
autoremove` çalıştırıyor. Debian Trixie depolarında bulunmayan `casper`
paketi temizleme listesinden çıkarıldı. `live-boot` bağımlılığı olan
`live-boot-initramfs-tools` için ayrıca satır eklenmedi; APT autoremove
davranışıyla temizlenmesi bekleniyor. Gerçek kurulum testi henüz yapılmadı.

## 2026-11-10 — Live paketlerinin doğrudan kurulum kontrolü

Paket listeleri tarandı. Live paketleri yalnızca `live.list.chroot`
dosyasında doğrudan tanımlı; `live-boot-initramfs-tools` doğrudan
kurulmuyor. Bağımlılığın APT tarafından otomatik işaretlenip
autoremove ile kaldırıldığı gerçek ISO testinde doğrulanacak.

## 2026-11-10 — Offline APT deposu bütünlük doğrulaması

Offline depodaki `Packages.gz` ve `Packages` indeksleri byte düzeyinde
karşılaştırıldı. İndekste 1.059 kayıt ve depoda 1.059 fiziksel `.deb`
dosyası bulundu. Tüm dosyaların SHA256 değerleri indeksle eşleşti.
Eksik, fazladan veya hash uyuşmazlığı olan paket bulunmadı.
Gerçek ISO çalışma testi henüz yapılmadı.

## 2026-11-10 — SDDM live-config ve ISO kimliği

Debian Trixie `live-config` 11.0.5 paketinin `0085-sddm` bileşeni
incelendi. Bileşen, canlı oturumdaki kullanıcı için SDDM otomatik
giriş ayarını oluşturuyor. `nocomponents=sddm` bu bileşeni devre
dışı bıraktığından `LB_BOOTAPPEND_LIVE` içinden kaldırıldı.

`live-build` 20250505+deb13u1 kaynak kodunda `LB_NET_TARBALL`
varsayılanının true olduğu doğrulandı. Ancak `binary_netboot`
betiği önce `LB_IMAGE_TYPE=netboot` koşulunu kontrol ediyor;
mevcut `iso-hybrid` yapılandırmasında netboot tarball üretilmiyor.
Bu nedenle değer değiştirilmedi.

ISO kimliği Bibotto olarak düzenlendi:
- `LB_IMAGE_NAME`: `bibotto-linux`
- `LB_HDD_LABEL`: `BIBOTTO_LIVE`
- `LB_ISO_APPLICATION`: `Bibotto Linux`
- `LB_ISO_PREPARER`: `Bibotto Linux Build System`
- `LB_ISO_PUBLISHER`: `Bibotto Linux`
- `LB_ISO_VOLUME`: `BIBOTTO_LINUX_0_1`

`config/binary` ve `config/common` sözdizimi ile metadata uzunluk
kontrolleri başarılı. Gerçek ISO üretimi henüz yapılmadı.
