import os
import socket
import speedtest
import subprocess
import tabulate
from tabulate import tabulate

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    # Call in a loop to create terminal progress bar
    # @params:
    #     iteration   - Required  : current iteration (Int)
    #     total       - Required  : total iterations (Int)
    #     prefix      - Optional  : prefix string (Str)
    #     suffix      - Optional  : suffix string (Str)
    #     decimals    - Optional  : positive number of decimals in percent complete (Int)
    #     length      - Optional  : character length of bar (Int)
    #     fill        - Optional  : bar fill character (Str)
    #     printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print("\n")

def ip_finder():
    ip_addresse = "Error"
    host = socket.gethostname()
    ip_addresse = socket.gethostbyname(host)
    return ip_addresse

class Network(object):

    def __init__(self):
        self.parser = speedtest.Speedtest()

    def data(self):
        down = str(f"{round(self.parser.download() / 1_000_000, 2)} Mbps")
        printProgressBar(1, 2, prefix = 'Speedtest:', suffix = 'Download Complete', length = 50)
        up = str(f"{round(self.parser.upload() / 1_000_000, 2)} Mbps")
        printProgressBar(2, 2, prefix = 'Speedtest:', suffix = 'Upload Complete ', length = 50)
        return [["IP-Addresse", "Download", "Upload"], [ip_finder(), down, up]]
    
    def __repr__(self):
        speed = self.data()
        # os.system('cls')
        return tabulate(speed, headers="firstrow", tablefmt="simple")

class Internet_Info(object):
    def __init__(self):
        self.host = socket.gethostname()
        self.ip = socket.gethostbyname(self.host)

    def __repr__(self):
        return str(f"""\t
        Host-Name: \t{self.host}
        IP-Address: \t{self.ip}
        """)

def check_connection():
    output = subprocess.check_output(["nslookup", "google.com"])

    outputdec = output.decode("utf-8")

    if("DNS" in outputdec):
        return False
    else:
        return True

if __name__ == "__main__":
    connection = check_connection()
    if connection == False:
        os.system('cls')
        print("No Internet Connection Available")
        print("")
        input("Press ENTER to close")
    else:
        os.system('cls')
        print(Internet_Info())
        printProgressBar(0, 2, prefix = 'Speedtest:', suffix = 'Complete', length = 50)
        print(Network())
        print("")
        input("Press ENTER to close")