# Architecture

## High‑Level Overview

This project turns a Raspberry Pi Zero 2 W into a low‑power NAS that exposes an SMB share on the local network and can be reached securely over the internet via Tailscale.

### Components

- **Raspberry Pi Zero 2 W**
  - Raspberry Pi OS Lite
  - User: `your-username`
  - Storage v1: boot SD card (128 GB)
  - Services:
    - `smbd` (Samba) for file sharing
    - `tailscaled` (Tailscale daemon) for secure remote access

- **Local Network**
  - Wi‑Fi hotspot or home router
  - The Pi gets a private LAN IP (e.g. `192.168.137.26`)

- **Clients**
  - Linux laptop/desktop
    - Connects to SMB via LAN IP or Tailscale IP
  - (Future) Android/iOS devices
    - Connect via Tailscale + SMB‑capable file manager

- **Tailscale Network**
  - Creates a private mesh network between:
    - Raspberry Pi Zero 2 W
    - Linux client(s)
    - (Later) mobile devices
  - Each device gets a stable `100.x.y.z` IP

## Data Flows

1. **Local LAN access**
   - Client mounts `//192.168.x.x/nas` via SMB.
   - Traffic stays inside the home/hotspot network.

2. **Remote access over Tailscale**
   - Client runs Tailscale and gets a `100.x.y.z` IP.
   - Client mounts `//100.x.y.z/nas` via SMB.
   - SMB is never exposed directly to the public internet.

## Design Decisions

- **Samba (SMB)** chosen for broad client support.
- **Tailscale** chosen to avoid manual VPN server setup and port forwarding.
- **SD card storage (v1)** used for simplicity and cost, with clear note that USB SSD/HDD is recommended for heavier workloads in a later revision.
