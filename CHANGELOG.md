# Changelog

All notable changes to this project will be documented in this file.

## 2026-06-10

### Bug Fixes
- ***(lynis)*** Create crontab if absent before setting permissions [file-7524] ([db4894b](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/db4894b))
- ***(config)*** Remove allow_broken_conditionals flag ([7cc60f5](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/7cc60f5))

### Documentation
- ***(readme)*** Mention rocky linux in opening description ([8ad68a5](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/8ad68a5))
- Added cloud-init removal section ([22c3c57](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/22c3c57))

## 2026-06-09

### Features
- Make public web ports optional and disabled by default ([1239dae](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/1239dae))
- ***(ci)*** Automate changelog generation ([09b75eb](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/09b75eb))
- Add molecule test scenarios for ubuntu and rocky linux ([685bcc2](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/685bcc2))
- Added molecule tests for ubuntu and rocky linux with github actions ci ([0dd7f0e](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/0dd7f0e))

### Bug Fixes
- ***(tailscale,vars)*** Correct registration typo, fix debug logic & update default vars ([685954f](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/685954f))
- ***(handlers)*** Correct module and state for firewalld reload task ([f6c2f4d](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/f6c2f4d))
- ***(base)*** Resolve ansible-lint package-latest violation for redhat upgrades ([7bff31c](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/7bff31c))
- 403 error on generating changelog and pushing it ([3eb1479](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/3eb1479))
- Trailing spaces ([5590d1b](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/5590d1b))
- Skip tailscale installation in ci environments ([0fa239a](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/0fa239a))
- Add error handling to tailscale installer task ([06c37cf](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/06c37cf))
- Use lowercase filter for os-specific variable loading ([e6b54b9](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/e6b54b9))

### Documentation
- ***(readme)*** Remove zero-window security from the title itself ([74b5421](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/74b5421))
- ***(readme)*** Remove zero-window security from the title itself ([433c9f7](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/433c9f7))
- Add ansible_user to inventory to shortened the playbook run command ([b568da6](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/b568da6))
- Fixed minor list formatting ([41c98f0](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/41c98f0))
- Fix critical sudoers security flaw and harden ssh setup in readme ([f67f5fe](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/f67f5fe))
- Marked molecule tests and distro-agnostic support as done ([273e0ee](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/273e0ee))
- Marked molecule tests and distro-agnostic support as done ([f6b6386](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/f6b6386))

### Refactoring
- ***(vars)*** Extract ssh service name to distro-specific variables ([8dced53](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/8dced53))
- ***(playbook)*** Remove redundant vars_files import for baseline role ([2420f72](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/2420f72))
- ***(handlers)*** Remove failure masking from ssh restart task ([c47f7dd](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/c47f7dd))
- ***(base)*** Use native dnf module for redhat package upgrades ([18a98e7](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/18a98e7))

### CI/CD Framework
- Automated changelog to only update at 12am ([f8e5187](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/f8e5187))
- Removed -v flag and used env flag instead ([f369c6e](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/f369c6e))

### Other Changes
- ***(molecule)*** Add ssh service state assertion in verify.yml ([a57fe1b](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/a57fe1b))
- Revert "docs: marked molecule tests and distro-agnostic support as done" ([07b84f8](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/07b84f8))
- Complexity to enabled pubkey only authentication ([528b4cb](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/528b4cb))
- Verify.yml with relevant tests ([e05b1ae](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/e05b1ae))
- -v flag to the molecule tests to see the error (temp) ([acaa65a](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/acaa65a))
- Merge pull request #1 from Tanvir101cmd/refactor/distro-agnostic ([cec9ecd](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/cec9ecd))

## 2026-06-08

### Bug Fixes
- Make fail2ban.yml distro-agnostic ([49eeaa1](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/49eeaa1))

### Documentation
- Updated prerequisites to include rocky linux support ([ec5f1ed](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/ec5f1ed))
- Updated readme with current variables and repository structure ([2209a83](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/2209a83))
- Revamped and condensed each instructions ([13a43af](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/13a43af))

### Refactoring
- Extract fail2ban to separate role ([795f39d](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/795f39d))
- Make linux_baseline role fully distro-agnostic (debian & redhat) ([0639c92](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/0639c92))

## 2026-06-07

### Features
- Add lynis-recommended kernel sysctl parameters ([c669bb9](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/c669bb9))

### Documentation
- Minor polish to toc ([067941d](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/067941d))
- Fixed wrong arrangement of toc ([4c5328d](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/4c5328d))
- Removed sepearator ([b6d001c](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/b6d001c))
- Added roadmap section ([af728e5](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/af728e5))
- Updated with kernel parameter section ([94ae1fc](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/94ae1fc))
- Updated changelog of 2026-06-06 ([76001b9](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/76001b9))

### Refactoring
- Make linux_baseline role distro-agnostic ([ccabefb](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/ccabefb))

### Miscellaneous Tasks
- Enable task timer and profile_tasks in ansible.cfg ([b6133a7](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/b6133a7))

### CI/CD Framework
- Added -y apt flag to ensure it doesn't hang ([8267da1](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/8267da1))

## 2026-06-06

### Features
- Restrict system crontab permission [file-7524] ([afcbb82](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/afcbb82))
- Restricted access to compilers [bann-9130] ([1aeeb02](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/1aeeb02))
- Added auditd for kernel-level security logging ([932b723](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/932b723))

### Bug Fixes
- ***(ssh)*** Conditionally apply pubkey and password auth settings ([a8bfdcd](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/a8bfdcd))
- Scope sudo nopasswd to ansible commands only ([cdee9c9](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/cdee9c9))

### Documentation
- Fixed typo ([1acd2c9](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/1acd2c9))
- Fixed typo ([70abb33](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/70abb33))
- Formatted the #troubleshooting section ([962322d](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/962322d))
- Added minor separator ([b3418a9](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/b3418a9))
- Converted the banners to pure markdown ([8b2ec0e](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/8b2ec0e))
- Fixed toc broken link ([0c573bc](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/0c573bc))
- Fixed minor heading format for better visual ([4d02dd3](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/4d02dd3))
- Fixed heading of some elements ([c7d5e99](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/c7d5e99))

### Miscellaneous Tasks
- Updated changelog for 2026-06-05 ([bcb5283](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/bcb5283))
- Updated changelog for 2026-06-04 ([85184bb](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/85184bb))

### CI/CD Framework
- Fixed incorrct var names ([9821a52](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/9821a52))

### Other Changes
- All the warnings of ansible by ansible-lint --fix ([1d96cc4](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/1d96cc4))
- Restrict compilers to root-only mode ([0084e5d](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/0084e5d))
- Small typo in playbook ([8a66e1d](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/8a66e1d))
- updated lynis tasks with their respective TEST ID ([4525dd7](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/4525dd7))
- updated lynis tasks with their respective TEST ID ([022e150](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/022e150))

## 2026-06-05

### Features
- Ensuring fail2ban is installed before configuring ([332ec06](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/332ec06))
- Add lynis hardening tasks and configurations ([4db9be9](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/4db9be9))
- ***(system)*** Set system timezone to asia/dhaka ([9059efe](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/9059efe))
- Enable unattended-upgrades for automatic security patches ([b0c4aba](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/b0c4aba))

### Documentation
- Changed fail2ban bantime to 24h in manual ([d48f1e8](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/d48f1e8))
- Fixed minor formatting issue on references ([8e85ca0](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/8e85ca0))
- Added hardened ssh configuration in manual ([116488d](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/116488d))

### Refactoring
- Moved timezone configuration to vars/main.yml ([c785233](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/c785233))

### Miscellaneous Tasks
- Separated tailscale from security.yml ([a509e33](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/a509e33))

### CI/CD Framework
- Manually installing fail2ban via apt ([65f1c52](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/65f1c52))

### Other Changes
- Incorrect variable names ([d7afbdb](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/d7afbdb))
- Timezone section altogether ([1f3da42](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/1f3da42))
- Indentation and quotation ([d1cb1e4](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/d1cb1e4))
- Revert "fixed: indentation on tags" ([dfddb15](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/dfddb15))
- Indentation on tags ([98a7d4d](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/98a7d4d))
- Hardened ssh configuration per lynis [ssh-7408] ([02aebc1](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/02aebc1))
- Changed bantime to 24h ([3a89a12](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/3a89a12))

## 2026-06-04

### Bug Fixes
- Resolve conflicting action statements in tailscale installer task ([811e86c](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/811e86c))
- Add ansible command task to run /tmp/install.sh ([792e143](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/792e143))

### Documentation
- Added license section & banner ([d075d4f](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/d075d4f))
- Added license section & banner ([cc15497](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/cc15497))
- Added toc and rearranged sections ([cb00a1b](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/cb00a1b))
- Add swap.img removal steps alongside zram setup ([5da6550](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/5da6550))
- Clarify ssh port is configurable, not hardcoded ([7b78deb](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/7b78deb))

### Other Changes
- Update copyright owner in LICENSE file ([014d720](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/014d720))

## 2026-06-03

### Features
- Add ansible tags for selective task exec ([6a19e71](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/6a19e71))

### Bug Fixes
- Install ansible via pip to fix version mismatch ([8cd9b0d](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/8cd9b0d))

### Documentation
- Mismatch path for vars/main.yml ([bb5dd45](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/bb5dd45))
- Link changelog.md in readme ([e6fe19c](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/e6fe19c))
- Added changelog.md ([c165093](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/c165093))
- Add changelog.md ([3e2bc38](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/3e2bc38))
- Fixed troubleshooting section formatting ([eeadf3d](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/eeadf3d))
- Fixed troubleshooting section formatting ([4192485](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/4192485))
- Fixed troubleshooting section formatting ([04cf54b](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/04cf54b))
- Fixed bash formatting ([ed96c4e](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/ed96c4e))
- Revamped with sections ([01b3db4](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/01b3db4))
- Generalize python binary path in sudoers instruction ([3aee43b](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/3aee43b))
- Removed zram tag as it inside system tag now ([a90657b](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/a90657b))
- Added banner & improved explanation ([c1faae3](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/c1faae3))

### Refactoring
- Update root playbook to execute role ([ed77586](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/ed77586))
- Split playbook into task files using import_tasks ([a8483a5](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/a8483a5))
- Moved hardcoded personal values into vars/config.yml ([51b3fee](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/51b3fee))

### Miscellaneous Tasks
- Implemented github actions pipeline for linting ([a1285f2](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/a1285f2))

### CI/CD Framework
- Renamed config.yml to main.yml for handlers ([e4f2b5c](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/e4f2b5c))
- Renamed config.yml to main.yml for handlers ([c5ddf00](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/c5ddf00))
- Fixed ssh-keygen hanging ([0a93771](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/0a93771))
- Fixed ssh-keygen hanging ([1839837](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/1839837))
- Split into lint and dry-run jobs, remove hardcoded values ([bad3c17](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/bad3c17))
- Handlers failed when false, swap path swap.img ([1705b7e](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/1705b7e))
- Mock systemd service manager in github actions workflow ([f7adfa3](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/f7adfa3))
- Removed mock tailscale and added ci bypass in zram section ([e2f66e1](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/e2f66e1))
- Removed mock tailscale and added ci bypass ([fd8c125](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/fd8c125))
- Fixed daemon-reload typo ([4ed98de](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/4ed98de))
- Added mock tailscale service ([351770b](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/351770b))
- Removed some pkgs to avoid error ([149e3fa](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/149e3fa))

### Other Changes
- Revert "docs: add CHANGELOG.md" ([3035b5e](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/3035b5e))
- Revert "docs: fixed troubleshooting section formatting" ([1155a83](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/1155a83))
- Revert "docs: fixed troubleshooting section formatting" ([135708b](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/135708b))
- Revert "ci: renamed config.yml to main.yml for handlers" ([880b54e](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/880b54e))
- Revert "ci: fixed ssh-keygen hanging" ([6795d7e](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/6795d7e))
- Ansible-lint errors ([9d6229b](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/9d6229b))
- Laptop lid close tweaks ([f7a3512](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/f7a3512))
- Comments to hardcoded values ([201ef14](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/201ef14))

## 2026-06-02

### Features
- Added ansible blueprint for automation ([3fc33c7](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/3fc33c7))

### Documentation
- Rewrote the readme for ansible automation ([bf27271](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/bf27271))
- Separated automation and manual installtion doc ([7748c17](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/7748c17))

### Other Changes
- Formatting issue ([9f150cd](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/9f150cd))
- Revert "fixed: formatting issue" ([677c291](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/677c291))
- Formatting issue ([38a52c0](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/38a52c0))
- Revert "fixed formatting error" ([3913968](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/3913968))
- fixed formatting error ([17b3917](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/17b3917))
- .gitignore ([6832761](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/6832761))

## 2026-02-05

### Other Changes
- Update README.md ([316d3a2](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/316d3a2))

## 2026-01-23

### Other Changes
- Removed all the emojis ([856006d](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/856006d))

## 2026-01-21

### Other Changes
- Changed typo :) ([7749b62](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/7749b62))
- Updated to use ntfs3 instead of ntfs3g ([bd54cc2](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/bd54cc2))

## 2025-12-19

### Other Changes
- Update README.md ([af0432f](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/af0432f))

## 2025-12-08

### Other Changes
- Update README.md ([020fc23](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/020fc23))

## 2025-11-15

### Other Changes
- Update README.md ([8aad347](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/8aad347))

## 2025-11-10

### Other Changes
- Update README.md ([e2dd667](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/e2dd667))
- Update README.md ([67d65ab](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/67d65ab))
- Update README.md ([0ca1ecd](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/0ca1ecd))

## 2025-11-03

### Other Changes
- Update README.md ([f1cc1b4](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/f1cc1b4))
- Update README.md ([f06c955](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/f06c955))

## 2025-10-29

### Other Changes
- Update README.md ([ff2a543](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/ff2a543))

## 2025-10-28

### Other Changes
- Update README.md ([f549d3c](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/f549d3c))
- Update README.md ([4f09418](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/4f09418))
- Update README.md ([32b0167](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/32b0167))

## 2025-10-27

### Other Changes
- Update README.md ([f86cf54](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/f86cf54))
- Update README.md ([c14bd1b](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/c14bd1b))
- Update README.md ([7b222ec](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/7b222ec))
- Update README.md ([f4581b8](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/f4581b8))
- Update README.md ([624a395](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/624a395))
- Update README.md ([b71a315](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/b71a315))
- Update README.md ([073bb6c](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/073bb6c))
- Update README.md ([b34ac36](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/b34ac36))
- Update README.md ([d57c586](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/d57c586))
- Update README.md ([4efe8a6](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/4efe8a6))
- Update README.md ([a889fd0](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/a889fd0))
- Update README.md ([4a591e3](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/4a591e3))
- Update README.md ([fb0f5bf](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/fb0f5bf))
- Update README.md ([2569872](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/2569872))
- Update README.md ([1023a60](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/1023a60))
- Update README.md ([c8cb904](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/c8cb904))
- Update README.md ([3c1d6df](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/3c1d6df))
- Update README.md ([90ed44f](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/90ed44f))
- Update README.md ([5879071](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/5879071))
- Initial commit ([a46ac56](https://github.com/Tanvir101cmd/ansible-linux-baseline/commit/a46ac56))
