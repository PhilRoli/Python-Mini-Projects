import subprocess

showProfiles = subprocess.check_output("netsh wlan show profile", shell=True).split()

print(showProfiles)