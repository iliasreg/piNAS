#!/usr/bin/env python3
import csv
from datetime import datetime

METRICS_FILE = "data/metrics.csv"  # path on your laptop

def parse_ts(s):
    return datetime.fromisoformat(s)

def main():
    rows = []
    with open(METRICS_FILE, newline="") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)

    if not rows:
        print("No data.")
        return

    # Basic stats
    loads = [float(r["load_1m"]) for r in rows]
    temps = [float(r["temp_c"]) for r in rows]
    mem_used = [int(r["mem_used_mb"]) for r in rows]
    mem_total = [int(r["mem_total_mb"]) for r in rows]
    last = rows[-1]

    print("Samples:", len(rows))
    print(f"Load 1m: min={min(loads):.2f}, max={max(loads):.2f}, avg={sum(loads)/len(loads):.2f}")
    print(f"Temp °C: min={min(temps):.1f}, max={max(temps):.1f}, avg={sum(temps)/len(temps):.1f}")
    print(f"Mem used MB: min={min(mem_used)}, max={max(mem_used)}, avg={sum(mem_used)/len(mem_used):.1f}")
    print(f"Mem total MB (reported): {mem_total[-1]}")
    print()
    print("Last sample:")
    for k in last:
        print(f"  {k}: {last[k]}")

if __name__ == "__main__":
    main()
