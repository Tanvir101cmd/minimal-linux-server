# Ansible-linux-baseline

A minimal, opinionated Ansible playbook for hardening a fresh ubuntu server. Run it once and the server comes out with SSH locked down, a default deny firewall, brute-force protection, tailscale mesh VPN and zram, creating a baseline to run anything on it. 

<p align="center">
  <img src="https://img.shields.io/badge/Ansible-EE0000?style=flat-square&logo=ansible&logoColor=white" alt="Ansible">
  <img src="https://img.shields.io/badge/Ubuntu-E95420?style=flat-square&logo=ubuntu&logoColor=white" alt="Ubuntu">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License">
  <img src="https://img.shields.io/badge/Security-Hardened-brightgreen?style=flat-square&logo=linuxfoundation&logoColor=white" alt="Security Hardened">
  <img src="https://img.shields.io/badge/Tailscale-Integrated-5B49E9?style=flat-square&logo=tailscale&logoColor=white" alt="Tailscale">
  <img src="https://img.shields.io/badge/Firewall-UFW%20%2B%20Fail2Ban-blue?style=flat-square&logo=shautomatik&logoColor=white" alt="Firewall">
  <img src="https://github.com/Tanvir101cmd/ansible-linux-baseline/actions/workflows/test-playbook.yml/badge.svg" alt="CI">
</p>

## Table of Contents

- [Core Features](#core-features)
- [Repository Structure](#repository-structure)
- [Usage](#usage)
  - [Prerequisites](#prerequisites) 
  - [1. Server Pre-configuration](#1-server-pre-configuration)
  - [2. Install ansible and collections](#2-install-ansible-and-collections)
  - [3. Create inventory file](#3-create-inventory-file)
  - [4. Configure your variables](#4-configure-your-variables)
  - [5. Run the Ansible playbook](#5-run-the-ansible-playbook)
- [Troubleshooting](#troubleshooting)
- [References and Acknowledgments](#references-and-acknowledgments)
- [License](#license)

## Core Features

After a successful run the server will have:

- SSH restricted to key-based authentication only on port `2222`, root login disabled 
- UFW enabled with default-deny incomin, and rate limited SSH port
- Fail2ban automatically banning after 5 failed attemps for 24 hour
- Tailscale installed and running for remote access
- Automatic security updates applied via unattended-upgrades
- Zram swap active, default `swap.img` removed

---

## Repository Structure

```bash
├── CHANGELOG.md
├── docs
│   └── MANUAL_SETUP.md
├── LICENSE
├── playbook.yml
├── README.md
└── roles
    └── linux_baseline
        ├── handlers
        │   └── main.yml
        ├── tasks
        │   ├── base.yml
        │   ├── lynis.yml
        │   ├── main.yml
        │   ├── security.yml
        │   ├── ssh.yml
        │   ├── system.yml
        │   └── tailscale.yml
        └── vars
            └── main.yml
```

## Usage

### Prerequisites

- Server running **Ubuntu 22.04+**
- A user with `sudo` access on the target server
- SSH access to the target server from the host machine
- Ansible installed on **host machine** (the machine you run the playbook from)
- `ansible.posix` and `community.general` collections

### 1. Server Pre-configuration

Ansible can hit a 12 second SSH timeout on Ubuntu due to interactive TTY environment checks. Rather than granting full passwordless sudo (`NOPASSWD: ALL`), we can scope it to only the packges/tools Ansible uses in the playbook (e.g. apt, cp, mkdir etc) and increase the sudo timeout from 15m to 60m so that the playbook doesn't lose its escalated privilege mid-way in its execution:

Create a sudoers file in /etc/sudoers.d/

``` bash 
sudo visudo -f /etc/sudoers.d/your_username-ansible
```

```ini
Defaults:your_username timestamp_timeout=60
your_username ALL=(ALL) NOPASSWD: /bin/sh, /usr/bin/apt-get, /usr/bin/apt, /usr/bin/systemctl, /usr/bin/ufw, /usr/bin/tee, /usr/bin/chmod, /usr/bin/chown, /usr/bin/cp, /usr/bin/mkdir, /usr/bin/python3, /usr/bin/python3.14
```

---

### 2. Install ansible and collections

Install Ansible on your host machine:
```bash
# Ubuntu / Debian
sudo apt update && sudo apt install ansible -y

# Fedora / RHEL
sudo dnf install ansible -y

# Arch Linux
sudo pacman -S --noconfirm ansible

# macOS
brew install ansible
```

Then install the required collections:

```bash
ansible-galaxy collection install ansible.posix community.general
```

---

### 3. Create inventory & ansible.cfg file

Create a hosts.ini file in the project root:

`hosts.ini`

```ini
[homelab]
192.168.0.150 ansible_port=22
```

---

### 4. Configure your variables

Open `roles/linux_baseline/vars/main.yml` and set your values:

```yaml
linux_baseline_username: "your_username"             # Primary user on the server
linux_baseline_pub_key: "~/.ssh/id_ed25519.pub"      # Path to ssh public key
linux_baseline_ssh_port: "2222"                      # Set your custom ssh port   
linux_baseline_mount_ntfs: false                     # Set to true only if mounting a NTFS drive
linux_baseline_ntfs_drive_uuid: "XXXXXXXXXXXXXXXX"   # Set to your drive_uuid, check via lsblk -f
linux_baseline_ntfs_mount_path: "/mnt/XXX"           # Set the mount path
```

---

### 5. Run the Ansible playbook

Execute the playbook with the following command:

```bash
ansible-playbook -i hosts.ini playbook.yml --user <your_username>
```

 Or run specific sections:

| Tag       | What it does                   |
| -----------| --------------------------------|
| packages  | System update + base packages  |
| ssh       | SSH hardening + key deployment |
| security  | ufw + fail2ban                 |
| tailscale | Mesh VPN service               |
| lynis     | Lynis audit suggestions        |
| system    | zram + swapfile removal        |

``` bash
# Security hardening only
ansible-playbook -i hosts.ini playbook.yml --user <your_username> --tags security

# SSH setup only
ansible-playbook -i hosts.ini playbook.yml --user <your_username> --tags ssh

# Everything except the system
ansible-playbook -i hosts.ini playbook.yml --user <your_username> --skip-tags system
```

---

## Troubleshooting

### **Playbook hangs at the start**

This is a TTY timeout issue. Make sure to ran the sudoers pre-configuration step on the target server before running the playbook.

---

### **UFW locked me out of SSH**

If the playbook fails mid-run and UFW is left in a broken state, access your server via your hosting provider's console and run `sudo ufw disable` to recover access, then re-run the playbook from the beginning.

---

### **Tailscale task fails**

The Tailscale installer requires internet access from the target server. If your server is behind a restrictive firewall, allow outbound traffic on port `443` before running.

### For a full list of changes, see [CHANGELOG.md](./CHANGELOG.md).

### For manual step-by-step setup without Ansible, see [Manual Setup](./docs/MANUAL_SETUP.md).

---

## References and Acknowledgments

### [Lynis by Cisofy](https://github.com/cisofy/lynis) - The open-source security auditing tool to benchmark and guide these hardening configurations

### [Linux Audit Blog](https://linux-audit.com) - A valuable resource website for in-depth technical guide for standard Linux system hardening practices.  

---

## License

This project is licensed under the **MIT License** - see the [LICENSE](./LICENSE) file for details.

Copyright (c) 2026 [@Tanvir101cmd](https://github.com/Tanvir101cmd)