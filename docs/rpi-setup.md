# Raspberry Pi Setup

## 1. Flash Raspberry Pi OS Lite

1. Use Raspberry Pi Imager.
2. Choose **Raspberry Pi OS Lite**.
3. In advanced options:
   - Set hostname (e.g. `pinas`).
   - Enable SSH.
   - Set username: `your-username`.
   - Set password.
   - Configure **2.4 GHz Wi‑Fi** (SSID + password + country).

Flash the SD card, insert it into the Pi, and power it on.

## 2. SSH into the Pi

From your main machine:

```bash
ssh your-username@<pi-ip-or-hostname>
```

Accept the host key and log in with your password.

## 3. Update the system

```bash
sudo apt update
sudo apt full-upgrade -y
sudo reboot
```

Reconnect via SSH after reboot.

## 4. Basic housekeeping

Optional but recommended:

1. Set correct timezone
    ```bash
    sudo raspi-config # then: Localisation Options → Timezone
    ```

2. Check disk usage
    ```bash
    df -h
    ```

3. Check IP address
    ```bash
    ip a
    ```