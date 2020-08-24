import subprocess

output = subprocess.check_output(["nslookup", "google.com"])

outputdec = output.decode("utf-8")

if("DNS" in outputdec):
    print("No Internet Connection Availible")
else:
    print("Internet conection availible")