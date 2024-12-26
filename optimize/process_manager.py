import os

def manage_process(pid, priority):
    os.system(f"renice -n {priority} -p {pid}")
