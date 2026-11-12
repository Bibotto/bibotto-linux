#!/usr/bin/env python3

import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ISO = ROOT / "bibotto-linux-amd64.hybrid.iso"

CHECKS = {
    "etc/xdg/kdeglobals": "Bibotto-Light",
    "etc/skel/.config/kdeglobals": "Bibotto-Light",
}


def run(command, env=None):
    print("\n>>>", " ".join(map(str, command)), flush=True)
    subprocess.run(command, cwd=ROOT, env=env, check=True)


def read_squashfs_file(squashfs, internal_path):
    result = subprocess.run(
        ["unsquashfs", "-cat", str(squashfs), internal_path],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def main():
    if os.geteuid() != 0:
        sys.exit("HATA: Betiği sudo ile çalıştır: sudo python3 scripts/build-iso.py")

    if not (ROOT / "config").is_dir():
        sys.exit("HATA: Bibotto proje kökü veya config dizini bulunamadı.")

    for relative_path, expected in CHECKS.items():
        source = ROOT / "config/includes.chroot" / relative_path
        if not source.is_file():
            sys.exit(f"HATA: Overlay dosyası bulunamadı: {source}")
        if f"ColorScheme={expected}" not in source.read_text():
            sys.exit(f"HATA: {source} içinde ColorScheme={expected} bulunamadı.")

    sync_env = os.environ.copy()
    sync_env["BIBOTTO_BRANDING_SYNC_ONLY"] = "1"
    run(["./auto/build"], env=sync_env)

    run(["lb", "chroot_includes_after_packages", "--force"])
    run(["lb", "installer", "--force"])
    run(["lb", "binary", "--force"])

    if not ISO.is_file():
        sys.exit(f"HATA: ISO oluşturulamadı: {ISO}")

    with tempfile.TemporaryDirectory(prefix="bibotto-iso-") as temp:
        squashfs = Path(temp) / "filesystem.squashfs"

        run([
            "xorriso", "-osirrox", "on",
            "-indev", str(ISO),
            "-extract", "/live/filesystem.squashfs", str(squashfs),
        ])

        if not squashfs.is_file():
            sys.exit("HATA: ISO içinde filesystem.squashfs bulunamadı.")

        for internal_path, expected in CHECKS.items():
            content = read_squashfs_file(squashfs, internal_path)
            if f"ColorScheme={expected}" not in content:
                sys.exit(
                    f"HATA: ISO içindeki {internal_path} "
                    f"beklenen ColorScheme={expected} değerini taşımıyor."
                )
            print(f"DOĞRULANDI: {internal_path} -> {expected}")

    hasher = hashlib.sha256()
    with ISO.open("rb") as image_file:
        for chunk in iter(lambda: image_file.read(8 * 1024 * 1024), b""):
            hasher.update(chunk)
    digest = hasher.hexdigest()

    print("\n========================================")
    print("BIBOTTO ISO BAŞARIYLA OLUŞTURULDU")
    print(f"Dosya: {ISO}")
    print(f"Boyut: {ISO.stat().st_size:,} bayt")
    print(f"SHA256: {digest}")
    print("========================================")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as error:
        sys.exit(f"\nHATA: Komut başarısız oldu (kod {error.returncode}).")
