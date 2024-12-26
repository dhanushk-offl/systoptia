import subprocess

def schedule_tasks():
    subprocess.run(["crontab", "-l"])
