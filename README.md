# Server-Setup

This guide documents my personal setup process for setting up a baseline for a homelab or remote server, starting from mounting drives to configuring SSH and network protection tools like **fail2ban** and **ufw**.

<p align="center">
  <img src="https://img.shields.io/badge/Ansible-EE0000?style=flat-square&logo=ansible&logoColor=white" alt="Ansible">
  <img src="https://img.shields.io/badge/Ubuntu-E95420?style=flat-square&logo=ubuntu&logoColor=white" alt="Ubuntu">
  <img src="https://img.shields.io/badge/Security-Hardened-brightgreen?style=flat-square&logo=linuxfoundation&logoColor=white" alt="Security Hardened">
  <img src="https://img.shields.io/badge/Tailscale-Integrated-5B49E9?style=flat-square&logo=tailscale&logoColor=white" alt="Tailscale">
  <img src="https://img.shields.io/badge/Firewall-UFW%20%2B%20Fail2Ban-blue?style=flat-square&logo=shautomatik&logoColor=white" alt="Firewall">
</p>


## Infrastructure as Code (IaC)
Automated deployment using Ansible playbook. For step-by-step instructions, please refer to the [Manual Setup](./docs/MANUAL_SETUP.md)

### Core Features

| Tool | Purpose |
|---|---|
| SSH Hardening | Remote access, key-only auth on port 2222 |
| ufw | Default-deny firewall, rate-limited SSH |
| fail2ban | Brute-force ban after 5 attempts |
| Tailscale | Mesh VPN for remote access without port forwarding |
| zramswap | Compressed in-memory swap |


### 1. Server Pre-configuration
When executing the superuser tasks remotely, ansible can hit a 12 second ssh connection timeouts due to Ubuntu's interactive tty env checks. To solve this, one can do passwordless sudo (`NOPASSWD: ALL`). But to maintain industry-grade security, we can instead grant the passwordless privilege explicitly to the system's python interpreter engine that Ansible uses to execute its tasks.

Run the following commands on your target server **before** running the playbook to set up this secure automation profile:

```bash
# Create a restricted, audited rule for the standard system Python engine
echo "$USER ALL=(ALL) NOPASSWD: /usr/bin/python3" | sudo tee /etc/sudoers.d/ansible-automation

# Enforce strict read-only permissions on the file
sudo chmod 440 /etc/sudoers.d/ansible-automation
```

---

### 2. Host Machine Environment Setup
Install Ansible on your host machine:
```bash
# Ubuntu / Debian
sudo apt update
sudo apt install software-properties-common -y
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install ansible -y

# Fedora / RHEL
sudo dnf install ansible -y

# Arch Linux
sudo pacman -S --noconfirm ansible

# macOS (Alternative)
brew install ansible
```

Create a hosts.ini file in the project root directory to map the server's location

```ini
[homelab]
192.168.0.150 ansible_port=22
```

---

### 3. Configure your variables
Open `vars/config.yml` and set your values before running the playbook:

- 'username' - your server's primary user
- 'pub_key'  - path to your ssh pub key on the machine (e.g. `~/.ssh/id_ed25519.pub`)
- `ssh_port` - port for ssh (default `2222` is fine for most setups)
- mount_ntfs - set to `true` only if you have a NTFS drive to mount, otherwise leave it `false` 

---

### 4. Run the Ansible playbook
Execute the playbook with the following command:
```bash
ansible-playbook -i hosts.ini playbook.yml --user <your_username> --ask-pass
```

 Or run specific sections:
 ``` bash
 # Security hardening only
ansible-playbook -i hosts.ini playbook.yml --user <your_username> --tags security

# SSH setup only
ansible-playbook -i hosts.ini playbook.yml --user <your_username> --tags ssh

# Everything except storage
ansible-playbook -i hosts.ini playbook.yml --user <your_username> --skip-tags storage
​```