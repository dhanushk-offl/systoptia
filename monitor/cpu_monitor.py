import psutil

def monitor_cpu():
    return psutil.cpu_percent(interval=1)
