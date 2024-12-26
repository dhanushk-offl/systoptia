import os

def optimize_cpu():
    os.system("renice -n -10 -p $(pgrep -x target_process)")
