import socket
# import subprocess
# # results = subprocess.check_output(["netsh", "wlan", "show", "network"])

# r = subprocess.run(["netsh", "wlan", "show", "network"], capture_output=True, text=True).stdout
# ls = r.split("\n")

# ssids = [v.strip() for k,v in (p.split(':') for p in ls if 'SSID' in p)]

# print(ssids)

def ip_finder():
    ip_addresse = "Error"
    host = socket.gethostname()
    ip_addresse = socket.gethostbyname(host)
    return ip_addresse

if __name__ == "__main__":
    print(ip_finder())