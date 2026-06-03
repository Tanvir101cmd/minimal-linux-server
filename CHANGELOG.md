# Changelog

## [1.1.0] - 2026-06-03
### Added
- `vars/config.yml` for user-configurable values (username, SSH key path, SSH port, NTFS options)
- Ansible tags for selective task execution (`packages`, `ssh`, `security`, `system`)
- CI workflow with separate `lint` and `dry-run` jobs via GitHub Actions
- Troubleshooting section in README

### Changed
- Refactored flat `playbook.yml` into organised roles with dedicated task files (`base.yml`, `ssh.yml`, `security.yml`, `system.yml`)
- Migrated `become_method` to FQCN (`ansible.builtin.sudo`)
- Migrated all `import_tasks` to FQCN (`ansible.builtin.import_tasks`)
- Tailscale install task split into `get_url` + `shell` to resolve ansible-lint violations
- Switched SSH key standard from RSA to ed25519
- Rewrote README with requirements, repo structure, tags reference table and troubleshooting
- Installed Ansible via `pip` in CI to fix version mismatch execution

### Removed
- Hardcoded personal values (`tanvir`, `~/.ssh/hp.pub`, drive UUID) from `playbook.yml`
- Laptop lid-close task (out of scope for a server baseline)

### Fixed
- Missing file permissions on SSH backup and fail2ban config tasks
- Trailing spaces and missing newlines across task files
- `community.general.ufw` collection not found in CI environment

## [1.0.0] - 2026-05-01
### Added
- Initial playbook with SSH, UFW, fail2ban, Tailscale, zram