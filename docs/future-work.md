# Future Work

This project is intentionally versioned as a learning + portfolio build. Planned improvements:

## Storage

- Move from SD card to a **USB SSD/HDD** for:
  - Better write endurance
  - Higher throughput
  - Cleaner separation of OS and data

## Mobile & Cross‑Platform

- Android:
  - Tailscale app + SMB‑capable file manager
- iOS:
  - Tailscale app + Files app or a third‑party SMB client
- Optional: simple web UI for basic status and file upload.

## Reliability & Monitoring

- Simple backup script (e.g. `rsync`) from laptop to NAS on a schedule.
- Basic monitoring:
  - Disk usage
  - Uptime
  - Temperature

## Security Enhancements

- Periodic updates and unattended‑upgrades.
- Firewall rules (e.g. UFW) restricting incoming traffic to:
  - SSH
  - SMB on LAN
  - Tailscale (managed via Tailscale itself)
