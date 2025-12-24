#!/usr/bin/env python3

import shutil
import psutil
from datetime import datetime
import os

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

# CSV log file
log_file_path = "logs/system_log.csv"

# Get current time
time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# System usage
cpu_usage = psutil.cpu_percent(interval=1)
memory_usage = psutil.virtual_memory().percent
disk = shutil.disk_usage("/")
disk_usage = (disk.used / disk.total) * 100

# Write header if file doesn't exist
if not os.path.exists(log_file_path):
    with open(log_file_path, "w") as f:
        f.write("timestamp,cpu_percent,ram_percent,disk_percent\n")

# Append log data
with open(log_file_path, "a") as f:
    f.write(f"{time_now},{cpu_usage},{memory_usage},{disk_usage:.2f}\n")

print("System usage logged to CSV.")
