#!/usr/bin/env python3
import os
from datetime import datetime

from flask import Flask, render_template, jsonify

import pandas as pd

METRICS_FILE = "X:\metrics.csv"

app = Flask(__name__)


def load_metrics(limit=200):
    if not os.path.exists(METRICS_FILE):
        return pd.DataFrame()

    df = pd.read_csv(METRICS_FILE)
    # Parse timestamp for sorting
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")
    if limit is not None and len(df) > limit:
        df = df.iloc[-limit:]
    return df


@app.route("/")
def dashboard():
    df = load_metrics()
    if df.empty:
        return render_template("dashboard.html", has_data=False)

    last = df.iloc[-1]

    stats = {
        "samples": len(df),
        "hostname": last.get("hostname", "unknown"),
        "last_timestamp": last["timestamp"],
        "load_min": round(df["load_1m"].min(), 2),
        "load_max": round(df["load_1m"].max(), 2),
        "load_avg": round(df["load_1m"].mean(), 2),
        "temp_min": round(df["temp_c"].min(), 1),
        "temp_max": round(df["temp_c"].max(), 1),
        "temp_avg": round(df["temp_c"].mean(), 1),
        "mem_used_last": int(last["mem_used_mb"]),
        "mem_total_last": int(last["mem_total_mb"]),
        "disk_used_last": str(last["disk_used"]),
        "disk_total_last": str(last["disk_total"]),
        "disk_used_pct_last": str(last["disk_used_pct"]),
        "samba_connections_last": int(last["samba_connections"]),
    }

    # Prepare simple time‑series for charts (as lists)
    df_chart = df.tail(100)  # last 100 points max
    chart_data = {
        "timestamps": df_chart["timestamp"].dt.strftime("%H:%M").tolist(),
        "load_1m": df_chart["load_1m"].round(2).tolist(),
        "temp_c": df_chart["temp_c"].round(1).tolist(),
    }

    return render_template(
        "dashboard.html",
        has_data=True,
        stats=stats,
        chart_data=chart_data,
    )


@app.route("/api/metrics/latest")
def api_latest():
    df = load_metrics(limit=None)
    if df.empty:
        return jsonify({"error": "no data"}), 404
    last = df.iloc[-1].to_dict()
    # Convert timestamp to ISO string
    last["timestamp"] = (
        pd.to_datetime(last["timestamp"]).to_pydatetime().isoformat()
    )
    return jsonify(last)


if __name__ == "__main__":
    # For development. For production, run via gunicorn/systemd, etc.
    app.run(host="0.0.0.0", port=5000, debug=False)
