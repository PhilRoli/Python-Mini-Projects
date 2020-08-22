import os
import speedtest
from tabulate import tabulate

class Network(object):
    def __init__(self):
        self.parser = speedtest.Speedtest()

    def data(self):
        down = str(f"{round(self.parser.download() / 1_000_000, 2)} Mbps")
        print("Dowload Done")
        up = str(f"{round(self.parser.upload() / 1_000_000, 2)} Mbps")
        return [["Interface", "Download", "Upload"], ["TP-LINK_1234", down, up]]
    
    def __repr__(self):
        speed = self.data()
        os.system('cls')
        return tabulate(speed, headers="firstrow", tablefmt="fancy_grid")

if __name__ == "__main__":
    print(Network())
    print("")
    input("Enter:")