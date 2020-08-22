import socket

class Internet_Info(object):
    def __init__(self):
        self.host = socket.gethostname()
        self.ip = socket.gethostbyname(self.host)

    def __repr__(self):
        return str(f"""\t
        Host-Name: \t{self.host}
        IP-Address: \t{self.ip}
        """)

if __name__ == "__main__":
    print(Internet_Info())
    print("")
    input("Enter:")