#!/usr/bin/env python3
import csv
import os
import socket
import subprocess
from datetime import datetime

METRICS_DIR = "/home/il/nas-metrics"
METRICS_FILE = os.path.join(METRICS_DIR, "metrics.csv")

def run(cmd):
    return subprocess.check_output(cmd, shell=True, text=True).strip()

def get_load_1m():
    out = run("cut -d' ' -f1 /proc/loadavg")
    return float(out)

def get_mem():
    out = run("free -m | awk 'NR==2{print $3\" \"$2}'")
    used, total = out.split()
    return int(used), int(total)

def get_disk():
    out = run("df -h / | awk 'NR==2{print $3\" \"$2\" \"$5}'")
    used, total, pct = out.split()
    return used, total, pct

def get_temp_c():
    # Works on most Raspberry Pi OS kernels
    out = run("vcgencmd measure_temp | cut -d'=' -f2 | cut -d\"'\" -f1")
    return float(out)

def get_samba_connections():
    try:
        out = run("smbstatus -p | tail -n +5 | wc -l")
        return int(out)
    except Exception:
        return -1  # smbstatus not available or error

def ensure_header():
    os.makedirs(METRICS_DIR, exist_ok=True)
    if not os.path.exists(METRICS_FILE):
        with open(METRICS_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "timestamp",
                "hostname",
                "load_1m",
                "mem_used_mb",
                "mem_total_mb",
                "disk_used",
                "disk_total",
                "disk_used_pct",
                "temp_c",
                "samba_connections",
            ])

def main():
    ensure_header()
    ts = datetime.utcnow().isoformat()
    hostname = socket.gethostname()
    load_1m = get_load_1m()
    mem_used, mem_total = get_mem()
    disk_used, disk_total, disk_pct = get_disk()
    temp_c = get_temp_c()
    samba_conn = get_samba_connections()

    with open(METRICS_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            ts,
            hostname,
            load_1m,
            mem_used,
            mem_total,
            disk_used,
            disk_total,
            disk_pct,
            temp_c,
            samba_conn,
        ])

if __name__ == "__main__":
    main()
