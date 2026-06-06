# Changelog

## 2026-06-06

### Features

- **auditd:** Added auditd for kernel-level security logging
- **cron:** Restricted system crontab permissions [FILE-7524]
- **compilers:** Restricted access to compilers [BANN-9130]

### Fixes

- **ssh:** Conditionally apply public key and password authentication hardening — skips PubkeyAuthentication and PasswordAuthentication changes when no authorized_keys are found on the host, preventing accidental lockout
- **sudo:** Scoped NOPASSWD to Ansible commands only
- **ci:** Fixed incorrect variable names

### Removed

- Restrict-compilers-to-root-only mode

### Chores

- Updated Lynis tasks with their respective Test IDs
- Fixed ansible-lint warnings (resolved via ansible-lint --fix)

### Documentation

- Converted banners to pure Markdown
- Fixed broken Table of Contents link
- Formatted the #Troubleshooting section
- Fixed minor heading formats for better visual hierarchy
- Added minor separator
- Fixed small typo in playbook
- Fixed multiple minor typos

## 2026-06-05

### Added
- **Security:** Added Lynis hardening tasks and configurations.
- **Security:** Hardened SSH configuration per Lynis auditing guidelines `[SSH-7408]`.
- **Security:** Enabled `unattended-upgrades` for automatic background security patches.
- **Fail2ban:** Added manual installation step via `apt` in CI pipeline.
- **Fail2ban:** Ensured the service is fully installed before configuration tasks run.

### Changed
- **Structure:** Separated Tailscale tasks out of `security.yml` into its own dedicated scope.
- **Fail2ban:** Updated default `bantime` to 24 hours.
- **Documentation:** Added hardened SSH configuration details to the manual.
- **Documentation:** Documented the updated 24h Fail2ban ban time in the manual.

### Fixed
- Fixed incorrect variable names.
- Fixed YAML indentation and quotation issues across tasks.
- Fixed a minor formatting issue in the documentation references.
- *Reverted an experimental indentation fix on tags.*

### Removed
- Removed the timezone configuration section entirely from the main task runner.

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