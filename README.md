# System Resource Monitor (Linux + Python)

A simple Linux-based system monitoring tool written in Python.
It logs CPU, RAM, and Disk usage with timestamps.

## Features
- CPU usage monitoring
- RAM usage monitoring
- Disk usage monitoring
- Automatic logging to file
- Linux-compatible design

## Technologies Used
- Python 3
- Linux
- psutil library
- Git & GitHub

## Usage
```bash
python src/monitor.py

## Automation

This project supports automatic system monitoring using Linux cron jobs.
The script can be scheduled to run at regular intervals and log system
resource usage without manual execution.

## Results and Analysis

The system monitoring data was collected over time and analyzed using both
visualization and basic statistical methods.

- CPU usage shows significant fluctuations, reflecting varying system activity.
- RAM usage remains relatively stable, indicating consistent memory allocation.
- Disk usage shows minimal change, as storage usage varies slowly over time.

The results demonstrate how different system resources behave under normal usage.
