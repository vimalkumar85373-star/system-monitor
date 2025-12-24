#!/usr/bin/env python3

import shutil
import psutil
from datetime import datetime

# Get current time
time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Get CPU and memory usage
cpu_usage = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent

# Get disk usage
disk = shutil.disk_usage("/")
disk_usage = (disk.used / disk.total) * 100

# Create log entry
log_entry = (
    f"{time_now} | "
    f"CPU: {cpu_usage}% | "
    f"RAM: {memory}% | "
    f"Disk: {disk_usage:.2f}%\n"
)

# Write to log file
with open("logs/system_log.txt", "a") as log_file:
    log_file.write(log_entry)

print("System usage logged successfully.")
