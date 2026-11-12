# Bibotto Linux — Security Policy

**Status:** Initial policy baseline. Defaults require implementation and testing.

## 1. Objectives

Provide a secure-by-default desktop while preserving usability. Prefer maintained Debian components, minimal privilege, timely updates, and transparent configuration.

## 2. Base and Repositories

- Debian 13 Trixie is the initial base.
- Prefer official Debian repositories.
- Keep `main`, `contrib`, and `non-free-firmware` explicit.
- Configure Debian security and stable update sources intentionally.
- Do not add third-party repositories without documenting ownership, signing keys, package provenance, and maintenance responsibilities.
- Package availability alone is not proof of suitability or security.

The final repository list, pinning policy, and update cadence remain open.

## 3. System Hardening

The package plan includes:

- AppArmor and utilities.
- firewalld.
- Plasma firewall integration.
- nftables.
- unattended-upgrades.
- PAM password quality controls.

Package presence alone does not guarantee enforcement. Profiles, service enablement, firewall zones, and update behavior must be tested.

## 4. Accounts and Privileges

Current installer configuration intends to:

- Create a regular user with `sudo` access.
- Avoid setting a root password.
- Disable automatic login by default.
- Require at least eight password characters.
- Reject weak passwords.
- Set home directory permissions to `0700`.

Validate the resulting PAM and account configuration after installation.

## 5. Encryption and Filesystems

LUKS2 is an intended installer capability. Test encrypted installation, initramfs integration, boot-time unlock, recovery guidance, and failure recovery.

Btrfs is preferred, with `@` and `@home` subvolumes planned. Snapper tools are in the package plan, but snapshot creation, retention, boot integration, and recovery policy are not established.

## 6. Updates and Kernel Maintenance

The project intends to use Debian security and update repositories.

Open policy decisions:

- Update cadence and release channels.
- Automatic versus user-approved updates.
- Kernel update and fallback strategy.
- Recovery from failed updates.
- Security advisory communication.
- Support lifetime for Bibotto releases.

Do not promise a support lifetime until it is formally defined.

## 7. Optional Software

The ISO-contained offline package source must preserve package integrity and dependency consistency.

- Verify package signatures and repository metadata.
- Document package origins.
- Keep unselected optional packages out of the installed system.
- Remove temporary local APT sources where appropriate.
- Rebuild the ISO when bundled security fixes are required.

## 8. Build and Release Security

Before publishing:

- Record build environment and source revision.
- Generate SHA-256 checksums.
- Define ISO signing and key management.
- Preserve build logs and package manifests.
- Verify source artifacts and package signatures.
- Document known vulnerabilities and release blockers.

## 9. Vulnerability Reporting

A public security contact and reporting process have not yet been established. Create a monitored reporting channel before public release. Do not publish response-time commitments until they are defined.
