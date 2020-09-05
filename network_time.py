import speedtest
from tabulate import tabulate
import time

# Not Working.Only 1 run despite higher Input

class Network(object):
    def __init__(self):
        self.parser = speedtest.Speedtest()

    def data(self):
        Tstart = time.time()
        down = str(f"{round(self.parser.download() / 1_000_000, 2)} Mbps")
        up = str(f"{round(self.parser.upload() / 1_000_000, 2)} Mbps")
        Tend = time.time()
        Tfinal = Tend - Tstart
        return [["Time", "Download", "Upload"], [Tfinal, down, up]]
    
    def __repr__(self):
        speed = self.data()
        return tabulate(speed, headers="firstrow", tablefmt="simple")

def timetest():
    anzahl = input("Anzahl an durchläufen: ")
    i = int(anzahl)
    print(i)
    while i > 0:
        print(Network())
        i=-1

if __name__ == "__main__":
    timetest()