# Manual Ubuntu server hardening setup

> **Note:** The document contains manual step-by-step references for configuring the server. For automated, production-grade deployment using Ansible, please refer to the main [README.md](../README.md) 

---

## First make sure the system is up to date
```bash
sudo apt update && sudo apt upgrade -y
```

Note: Some updates may require a reboot after completion.

## Starting with SSH

All you need is a base system and **OpenSSH** to start.  
Remember, SSH follows a **server–client model**.

### Installation

```bash
sudo apt install openssh-server
```

### Starting the SSH Service:
```bash
sudo systemctl enable --now ssh
```

### Hardening SSH Configuration

It's a good idea to backup the default config file before making any changes, make the backup in this case by:
```bash
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup
```

Edit your SSH daemon config at `/etc/ssh/sshd_config`:

```ini
Port 2222                               # Change this to your prefered port number 
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
KbdInteractiveAuthentication no
```

Reload the config file via:
```bash
sudo systemctl restart ssh
```

---

## Setting Up SSH Keys (Client-Side)

SSH keys are the backbone of secure connections.  
It’s good practice to use **unique keys for different servers,** like using different keys for different doors.

### Generate a new SSH key
```bash
ssh-keygen -f ~/.ssh/filename -C "comment"
```
Sometimes users run into “UNPROTECTED PRIVATE KEY FILE” errors. You can simply fix it by:
```bash
chmod 600 ~/.ssh/filename
```

### Find Server IP (run this on the server)
```bash
ip addr show
```

### Copy your public key to the server
```bash
ssh-copy-id -i ~/.ssh/filename -p 2222 username@<IP_ADDRESS_or_HOSTNAME>
```

### Connect to the server
```bash
ssh -p 2222 username@<IP_ADDRESS_or_HOSTNAME>
```

### Simplify with SSH Config

You can make connections effortless by creating a config file at `~/.ssh/config`:

```ini
Host servername
    HostName <IP_ADDRESS_or_HOSTNAME>
    IdentityFile ~/.ssh/filename
    User Username
    Port 2222
```

---

## Tailscale (To access from anywhere)

**Tailscale** is a mesh VPN that makes your SSH server accessible **from anywhere with internet**.  
It assigns private static IPs to devices, allowing secure and direct communication without port forwarding.

First, install tailscale by: 
```bash
curl -fsSL https://tailscale.com/install.sh | sh
```

Enable Tailscale on boot:
```bash
sudo systemctl enable --now tailscaled
```

To get private static ip with tailscale:
```bash
sudo tailscale up
```
It will show or open a link in your browser. Go there and sign in with your account to get the private IP. Connect your other devices with the same account to establish connection between devices securely.

To get tailscale ip:
```bash
tailscale ip
```

Another thing about tailscale is that Tailscale security keys (Node Keys) for user-authenticated devices expire by default, typically after 180 days. So it will disconnect automatically from your unattended server.

To prevent lockouts:

- Log into the [Tailscale Admin Console](https://login.tailscale.com/admin/machines) on your local machine.

- Navigate to the Machines tab.

- Find your newly connected server.

- Click on your server and select Disable Key Expiry.

If your key does expire, you must use a non-Tailscale connection (like a local LAN IP) to run 
```sudo tailscale up --force-reauth ``` and re-authenticate.

---


## UFW (Uncomplicated Firewall)

Start with a safe default configuration:

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

Then allow essential ports:

```bash
sudo ufw allow 80/tcp      # HTTP traffic
sudo ufw allow 443/tcp     # HTTPS traffic
sudo ufw limit 2222/tcp    # Rate-limits connections to port 2222, good to prevent bruteforce attacks
sudo ufw allow in on tailscale0 # Allows Tailscale traffic on the server
```

Enable UFW:
```bash
sudo ufw enable
```

To verify UFW status and active rules:
```bash
sudo ufw status verbose
```

---

## fail2ban (Brute Force Protection)

To install:
```bash
sudo apt install fail2ban
```

Start the service by:
```bash
sudo systemctl enable --now fail2ban
```

Create or edit the jail config at `/etc/fail2ban/jail.d/sshd.conf`:

```ini
[sshd]
enabled  = true
port     = 2222                         # Must match the Port value set in sshd_config above
filter   = sshd
logpath  = /var/log/auth.log
maxretry = 5
bantime  = 1h
findtime = 10m
```

After editing, restart the fail2ban service to reload the config file:
```bash
sudo systemctl restart fail2ban
```
---

# Optional tweaks

## Mounting NTFS Drives on Boot

I have some NTFS drives that I keep my backups on. 

First make a empty directory that will be used to mount the NTFS drive
```bash
sudo mkdir -p /mnt/Files
```

Add this line to your `/etc/fstab` to automatically mount your NTFS drive at boot (make sure the UUID is correct)
```bash
UUID=01D858C886F164A0 /mnt/Files ntfs3 defaults,uid=1000,gid=1000,umask=022,nofail,noauto,force,x-systemd.automount 0 0
```

To see the partition UUID:
``` bash
lsblk -f
```

Reload the new fstab by:
``` bash
sudo systemctl daemon-reload
```

You might need run the below command to make sure the drive is 'clean':
```bash
sudo ntfsfix -d /dev/sdxx
```

---

## Configure Zram
Zram creates compressed swap space in RAM instead of using slow disk storage. It's much faster than traditional swap and doesn't use your SSD/HDD.

To install zram:
```bash
sudo apt install zram-tools
```

To start the service simply (if not done already):
```bash
sudo systemctl enable --now zramswap
```

## Remove swapfile if it exists
Disable and remove the default swap file if zram is enough for your usecases:
```bash
# Disable and remove the default swapfile
sudo swapoff /swap.img

# Remove it from fstab
sudo sed -i '/swap.img/d' /etc/fstab

# Delete the file
sudo rm -f /swap.img
```