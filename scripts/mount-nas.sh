#!/usr/bin/env bash
# Example: manual mount of NAS share on Linux

PI_TAILSCALE_IP="100.x.y.z"   # replace with your Pi's Tailscale IP
MOUNT_POINT="/mnt/piNAS" 
USERNAME="your-username"      # replace with your username

sudo mkdir -p "${MOUNT_POINT}"

sudo mount -t cifs //"${PI_TAILSCALE_IP}"/nas "${MOUNT_POINT}" \
  -o username="${USERNAME}"

echo "Mounted //${PI_TAILSCALE_IP}/nas at ${MOUNT_POINT}"
