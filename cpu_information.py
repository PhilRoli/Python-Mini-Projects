import psutil

def cpu_info():
    print("="*20, "CPU Information", "="*20)
    # Amount of Cores
    print("Physical cores: ", psutil.cpu_count(logical=False))
    print("Total cores: ", psutil.cpu_count(logical=True))
    # Frequencies
    cpufreq = psutil.cpu_freq()
    print(f"Max frequency: {cpufreq.max:.2f}Mhz")
    print(f"Min frequency: {cpufreq.min:.2f}Mhz")
    print(f"Current frequency: {cpufreq.current:.2f}Mhz")
    # Usage
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")

if __name__ == "__main__":
    cpu_info()
    input()