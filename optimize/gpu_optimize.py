import subprocess

def optimize_gpu():
    subprocess.run(["nvidia-smi", "-pm", "1"])
