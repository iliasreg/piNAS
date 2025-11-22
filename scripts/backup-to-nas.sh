#!/usr/bin/env bash
# Example backup script: sync a local directory to the NAS

SOURCE_DIR="$HOME/Documents"
DEST_MOUNT="/mnt/pinas"
DEST_SUBDIR="backup-$(hostname)"

if [ ! -d "${DEST_MOUNT}" ]; then
  echo "Destination ${DEST_MOUNT} not mounted. Mount NAS first."
  exit 1
fi

mkdir -p "${DEST_MOUNT}/${DEST_SUBDIR}"

rsync -avh --delete "${SOURCE_DIR}/" "${DEST_MOUNT}/${DEST_SUBDIR}/"
