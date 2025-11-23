# piNAS - Raspberry Pi Zero 2 W NAS with Secure Remote Access  
_Samba + Tailscale · Low‑Power · Home Lab Friendly_

This project turns a Raspberry Pi Zero 2 W into a minimalist NAS (Network Attached Storage) with **SMB file sharing** on the local network and **secure remote access** via **Tailscale**, without exposing SMB to the public internet.

---

## ✨ Features

- **Ultra‑low‑power NAS** on a Raspberry Pi Zero 2 W  
- **SMB (Samba) file sharing** for Linux (and later Windows/macOS/mobile)  
- **Secure remote access** over Tailscale (no SMB ports exposed to the internet)  
-  **Headless setup**: SSH‑only, no monitor required after first boot  

---

## 🏗 Architecture Overview

**High level:**

- **Raspberry Pi Zero 2 W** running Raspberry Pi OS Lite  
- Storage initially on the **boot SD card** (128 GB) for simplicity  
- **Samba** exports a share (e.g. `/home/your-username/nas-share`) over the LAN  
- **Tailscale** connects the Pi, a Linux laptop, and (later) mobile devices into a private mesh network  
- Clients access the NAS via `smb://<tailscale-ip>/nas` or `//<tailscale-ip>/nas`

---

## 🚀 Quick Start

### 1. Prepare the Raspberry Pi

1. Flash **Raspberry Pi OS Lite** to the SD card using Raspberry Pi Imager.  
2. In the Imager advanced options, configure:
   - Username: `your-username`
   - Password: your strong password  
   - Wi‑Fi SSID + password (2.4 GHz)  
   - Enable SSH  
3. Boot the Pi and SSH into it from your main machine:
   `ssh your-username@<pi-ip-or-hostname>`

### 2. Update system
   `
   sudo apt update
   sudo apt full-upgrade -y
   `

---

## 📁 Local NAS via Samba

### 1. Create a NAS directory on the SD
### 2. Install and configure Samba
   - Edit `/etc/samba/smb.conf` and add at the end:
### 3. Test from Linux on the same LAN

---

## 📱 Future: Mobile Access

Planned (documented but optional for v1):

- Install **Tailscale** on Android/iOS.  
- Install a file manager with **SMB support**.  
- Configure a new SMB share pointing to the Pi’s **Tailscale IP** (`100.x.y.z`), share `nas`, user `your-username`.

This allows secure file access from phones, again without exposing SMB to the public internet.

---

## 🔒 Security & Design Notes

- **SMB is LAN‑only**; no port forwarding of 445/139 on the router.  
- **Remote access** is handled exclusively via Tailscale, using authenticated devices.  
- **Storage v1** uses the **boot SD card** for simplicity and low cost:
  - Good for learning and light personal use.  
  - Not ideal for heavy write workloads due to SD card wear.  
- **Future improvement**: move data to a dedicated USB SSD/HDD for better endurance and throughput.

---

## ✅ Status & Next Steps

**Current state (v1):**

- Pi Zero 2 W configured with Raspberry Pi OS Lite  
- Local NAS via Samba on the boot SD  
- Secure remote access via Tailscale  
- Linux client mounting over both LAN IP and Tailscale IP

**Planned next steps:**

- Add Android/iOS access instructions  
- Move storage to USB SSD/HDD  
- Add a simple backup script and/or status page  
- Include architecture and screenshot assets in `assets/`





