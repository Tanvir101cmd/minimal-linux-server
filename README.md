# Server-Setup

This guide documents my personal setup process for setting up a baseline for a homelab or remote server, starting from mounting drives to configuring SSH and network protection tools like **fail2ban** and **UFW**.

---

If you prefer to understand the under-the-hood mechanics or just want to execute the steps line-by-line by manually, please refer to the [Manual Setup](./docs/MANUAL_SETUP.md)

## IaC
Instead of doing all the steps manually, **I  highly recommend** using the Ansible playbook to automate everything.

### 1. Before running the playbook
When executing the superuser tasks remotely, ansible can hit a 12 second ssh connection timeouts due to Ubuntu's interactive tty env checks. To solve this, one can do passwordless sudo (`NOPASSWD: ALL`). But to maintain industry-grade security, we can instead grant the passwordless privilege explicitly to the system's python interpreter engine that Ansible uses to execute its tasks.

Run the following commands on your target server **before** running the playbook to set up this secure automation profile:

```bash
# Create a restricted, audited rule for the Ansible python execution engine
echo 'tanvir ALL=(ALL) NOPASSWD: /usr/bin/python3.14' | sudo tee /etc/sudoers.d/ansible-automation
```

Set the correct secure file permissions (Read-only)
```bash
sudo chmod 440 /etc/sudoers.d/ansible-automation
```

### 2. Local Setup from host -> server
```bash
# Install Ansible via Homebrew (for macOS)
brew install ansible
```

Create a hosts.ini file in the project root directory to map the server's location

```ini
[homelab]
192.168.0.150 ansible_port=22
```

### 3. Run the Ansible playbook

```bash
ansible-playbook -i hosts.ini playbook.yml --user tanvir --ask-pass
```
