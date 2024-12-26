import GPUtil

def monitor_gpu():
    gpus = GPUtil.getGPUs()
    return [(gpu.id, gpu.load * 100, gpu.temperature) for gpu in gpus]
