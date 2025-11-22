# piNAS - Raspberry Pi Zero 2 W NAS with Secure Remote Access  
_Samba + Tailscale · Low‑Power · Home Lab Friendly_

This project turns a Raspberry Pi Zero 2 W into a minimalist NAS (Network Attached Storage) with **SMB file sharing** on the local network and **secure remote access** via **Tailscale**, without exposing SMB to the public internet.

---

## ✨ Features

- 🧊 **Ultra‑low‑power NAS** on a Raspberry Pi Zero 2 W  
- 📁 **SMB (Samba) file sharing** for Linux (and later Windows/macOS/mobile)  
- 🔐 **Secure remote access** over Tailscale (no SMB ports exposed to the internet)  
- 🧑‍💻 **Headless setup**: SSH‑only, no monitor required after first boot  
- 🧱 Designed as a **learning + portfolio** project (documented architecture, trade‑offs, and future improvements)

---

## 🏗 Architecture Overview

**High level:**

- **Raspberry Pi Zero 2 W** running Raspberry Pi OS Lite  
- Storage initially on the **boot SD card** (128 GB) for simplicity  
- **Samba** exports a share (e.g. `/home/il/nas-share`) over the LAN  
- **Tailscale** connects the Pi, a Linux laptop, and (later) mobile devices into a private mesh network  
- Clients access the NAS via `smb://<tailscale-ip>/nas` or `//<tailscale-ip>/nas`

A diagram (recommended for the repo) can live in `assets/architecture-diagram.png` and be embedded here.

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

