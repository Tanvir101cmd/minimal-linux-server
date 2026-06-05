# Changelog

## 2026-06-04

### Added
- **Documentation:** Added a Table of Contents (ToC) to the main manual for better navigation.
- **Documentation:** Added a dedicated License section and project banner.
- **Documentation:** Added steps for safely removing `swap.img` when setting up `zram`.

### Changed
- **Documentation:** Rearranged manual sections for improved readability and logical flow.
- **Documentation:** Clarified that the SSH port is fully configurable rather than being hardcoded.
- **Legal:** Updated the copyright owner details in the `LICENSE` file.

### Fixed
- **Tailscale:** Resolved conflicting action statements within the Tailscale installer task.
- **Ansible:** Added the missing command task required to properly execute `/tmp/install.sh`.

## 2026-06-03
### Added
- `roles/linux_baseline/vars/main.yml` for user-configurable values (username, SSH key path, SSH port, NTFS options)
- Ansible tags for selective task execution (`packages`, `ssh`, `security`, `system`)
- CI workflow with separate `lint` and `dry-run` jobs via GitHub Actions
- Troubleshooting section in README

### Changed
- Refactored flat `playbook.yml` into organised roles with dedicated task files (`base.yml`, `ssh.yml`, `security.yml`, `system.yml`)
- Migrated `become_method` to FQCN (`ansible.builtin.sudo`)
- Migrated all `import_tasks` to FQCN (`ansible.builtin.import_tasks`)
- Tailscale install task split into `get_url` + `shell` to resolve ansible-lint violations
- Rewrote README with requirements, repo structure, tags reference table and troubleshooting
- Installed Ansible via `pip` in CI to fix version mismatch execution

### Removed
- Hardcoded personal values (`tanvir`, `~/.ssh/hp.pub`, drive UUID) from `playbook.yml`
- Laptop lid-close task (out of scope for a server baseline)

### Fixed
- Missing file permissions on SSH backup and fail2ban config tasks
- Trailing spaces and missing newlines across task files
- `community.general.ufw` collection not found in CI environment

## 2026-05-01
### Added
- Initial playbook with SSH, UFW, fail2ban, Tailscale, zram