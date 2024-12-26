import argparse
from monitor import cpu_monitor, gpu_monitor, dashboard
from optimize import cpu_optimize, gpu_optimize

def run_cli():
    parser = argparse.ArgumentParser(description="SysOptAi CLI Tool")
    parser.add_argument("--monitor", action="store_true")
    parser.add_argument("--optimize-cpu", action="store_true")
    parser.add_argument("--optimize-gpu", action="store_true")
    
    args = parser.parse_args()
    
    if args.monitor:
        cpu = cpu_monitor()
        gpu = gpu_monitor()
        dashboard(cpu, gpu)
    if args.optimize_cpu:
        cpu_optimize()
    if args.optimize_gpu:
        gpu_optimize()
