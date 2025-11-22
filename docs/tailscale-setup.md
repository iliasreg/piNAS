# Tailscale Setup (Secure Remote Access)

## 1. Install Tailscale on the Pi

```bash
curl -fsSL https://tailscale.com/install.sh | sudo bash
sudo tailscale up
```

When prompted, open the provided URL in a browser, log in with your chosen account (e.g. GitHub), and approve the Pi device.

---

## 2. Get the Pi's Tailscale IP

```bash
tailscale ip
Example output:
100.x.y.z
```

**Record this IP; it will be used by remote clients.**

---

## 3. Install Tailscale on Linux client

On your Linux laptop/desktop:
```bash
curl -fsSL https://tailscale.com/install.sh | sudo bash
sudo tailscale up
```

Log in with the **same** account used on the Pi.

Verify connectivity:
```bash
ping 100.x.y.z # Pi's Tailscale IP
```

You should receive replies.

---

## 4. Mount the NAS over Tailscale

On the Linux client:
```bash
sudo apt install -y cifs-utils
sudo mkdir -p /mnt/pinas
sudo mount -t cifs //100.x.y.z/nas /mnt/pinas -o username=your-username
```

Enter your Samba password when prompted.

You now have secure remote access to the NAS over Tailscale