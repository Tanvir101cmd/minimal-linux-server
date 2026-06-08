# Manual Linux Server Hardening Setup

> For automated deployment, see [README.md](../README.md).

---

## Table of Contents

- [1. System Update](#1-system-update)
- [2. Install Baseline Packages](#2-install-baseline-packages)
- [3. SSH](3-ssh)
- [4. SSH Keys (Client Side)](#4-ssh-keys-client-side)
- [5. Firewall](5-firewall)
  - [UFW - Ubuntu/Debian]((#ufw-debianubuntu))
  - [Firewalld - Rocky/AlmaLinux](#firewalld-rockyalmalinux)
- [6. Fail2ban](#6-fail2ban)
- [7. Automatic Security Updates](#7-automatic-security-updates)
- [8. Tailscale](#8-tailscale)
- [9. Lynis Recommended Kernel Hardening Parameters](#9-lynis-recommended-kernel-hardening-parameters)
- [10. Optional: zram Swap](#10-optional-zram-swap)
- [11. Optional: Mount NTFS Drive on Boot](#11-optional-mount-ntfs-drive-on-boot)

---

## 1. System Update

```bash
# Debian/Ubuntu
sudo apt update && sudo apt upgrade -y

# Rocky/AlmaLinux
sudo dnf update -y
```

> Some updates require a reboot.

---

## 2. Install Baseline Packages

```bash
# Debian/Ubuntu
sudo apt install -y curl git vim openssh-server ufw fail2ban \
  unattended-upgrades apt-listchanges auditd

# Rocky/AlmaLinux
sudo dnf install -y curl git vim openssh-server firewalld fail2ban \
  dnf-automatic audit
```

---

## 3. SSH

### Start the service

```bash
# Debian/Ubuntu
sudo systemctl enable --now ssh

# Rocky/AlmaLinux
sudo systemctl enable --now sshd
```

### Harden `/etc/ssh/sshd_config`

Back up the default config first:

```bash
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup
```

Apply these settings:

```ini
Port 2222
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
KbdInteractiveAuthentication no
AllowTcpForwarding no
ClientAliveCountMax 2
LogLevel VERBOSE
MaxAuthTries 3
MaxSessions 2
TCPKeepAlive no
X11Forwarding no
AllowAgentForwarding no
```

Restart to apply:

```bash
# Debian/Ubuntu
sudo systemctl restart ssh

# Rocky/AlmaLinux
sudo systemctl restart sshd
```

---

## 4. SSH Keys (Client Side)

Generate a key, then copy it to the server:

```bash
ssh-keygen -f ~/.ssh/filename -C "comment"
ssh-copy-id -i ~/.ssh/filename.pub -p 2222 username@<IP>
```

> If you get "UNPROTECTED PRIVATE KEY FILE": `chmod 600 ~/.ssh/filename`

Connect:

```bash
ssh -p 2222 username@<IP>
```

Simplify repeat connections with `~/.ssh/config`:

```ini
Host servername
    HostName <IP>
    IdentityFile ~/.ssh/filename
    User username
    Port 2222
```

---

## 5. Firewall

### UFW (Debian/Ubuntu)

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw limit 2222/tcp
sudo ufw allow in on tailscale0
sudo ufw enable
sudo ufw status verbose
```

### firewalld (Rocky/AlmaLinux)

```bash
sudo systemctl enable --now firewalld
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --permanent --add-port=2222/tcp
sudo firewall-cmd --permanent --zone=trusted --add-interface=tailscale0
sudo firewall-cmd --permanent --remove-service=ssh
sudo firewall-cmd --reload
```

---

## 6. Fail2ban

Enable and configure for SSH:

```bash
sudo systemctl enable --now fail2ban
```

Create `/etc/fail2ban/jail.d/sshd.conf`:

```ini
[sshd]
enabled  = true
port     = 2222
filter   = sshd
logpath  = /var/log/auth.log
maxretry = 5
bantime  = 24h
findtime = 10m
```

```bash
sudo systemctl restart fail2ban
```

---

## 7. Automatic Security Updates

```bash
# Debian/Ubuntu - enable via debconf
sudo dpkg-reconfigure -plow unattended-upgrades

# Rocky/AlmaLinux - security updates only
sudo sed -i 's/^upgrade_type.*/upgrade_type = security/' /etc/dnf/automatic.conf
sudo systemctl enable --now dnf-automatic.timer
```

---

## 8. Tailscale

```bash
# Both families - official install script handles distro detection
curl -fsSL https://tailscale.com/install.sh | sh

sudo systemctl enable --now tailscaled
sudo tailscale up        # opens auth link in browser
tailscale ip             # get your private Tailscale IP
```

> **Key expiry:** Tailscale node keys expire after 180 days by default, which will lock you out of an unattended server. Go to the [Admin Console](https://login.tailscale.com/admin/machines) -> your machine -> **Disable Key Expiry**.
>
> If your key does expire, reconnect via LAN and run `sudo tailscale up --force-reauth`.

---

## 9. Lynis Recommended Kernel Hardening Parameters

> **Proceed with caution** - some parameters may conflict with specific hardware.

```bash
sudo nano /etc/sysctl.d/99-custom.conf
```

```ini
# Network: IPv4
net.ipv4.tcp_syncookies = 1
net.ipv4.conf.all.rp_filter = 1
net.ipv4.conf.default.rp_filter = 1
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.default.accept_redirects = 0
net.ipv4.conf.all.send_redirects = 0
net.ipv4.conf.default.send_redirects = 0
net.ipv4.conf.all.accept_source_route = 0
net.ipv4.conf.default.accept_source_route = 0
net.ipv4.conf.all.log_martians = 1
net.ipv4.conf.default.log_martians = 1
net.ipv4.icmp_echo_ignore_broadcasts = 1

# Network: IPv6
net.ipv6.conf.all.accept_redirects = 0
net.ipv6.conf.default.accept_redirects = 0

# Kernel
kernel.randomize_va_space = 2
kernel.sysrq = 0
kernel.core_uses_pid = 1
kernel.dmesg_restrict = 1
kernel.kptr_restrict = 2
kernel.yama.ptrace_scope = 1

# Filesystem
fs.protected_hardlinks = 1
fs.protected_symlinks = 1
fs.suid_dumpable = 0
```

Apply immediately:

```bash
sudo sysctl --system
```

---

## 10. Optional: zram Swap

Compressed in-RAM swap - faster than disk, no HDD/SSD wear.

```bash
# Debian/Ubuntu
sudo apt install -y zram-tools
sudo systemctl enable --now zramswap

# Rocky/AlmaLinux
sudo dnf install -y zram-generator
# Create /etc/systemd/zram-generator.conf:
echo -e "[zram0]\nzram-size = ram / 2\ncompression-algorithm = zstd" \
  | sudo tee /etc/systemd/zram-generator.conf
sudo systemctl daemon-reload
sudo systemctl enable --now systemd-zram-setup@zram0.service
```

Remove the legacy swap file if no longer needed:

```bash
sudo swapoff /swap.img
sudo sed -i '/swap\.img/d' /etc/fstab
sudo rm -f /swap.img
```

---

## 11. Optional: Mount NTFS Drive on Boot

```bash
sudo mkdir -p /mnt/Files
lsblk -f                  # find your drive's UUID
```

Add to `/etc/fstab` (replace UUID with yours):

```
UUID=01D858C886F164A0 /mnt/Files ntfs3 defaults,uid=1000,gid=1000,umask=022,nofail,noauto,force,x-systemd.automount 0 0
```

```bash
sudo systemctl daemon-reload
```

> If the mount fails, the drive may need to be marked clean first: `sudo ntfsfix -d /dev/sdXX`
