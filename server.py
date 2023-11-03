from socket import *
import time 
import sys

import matplotlib.pyplot as plt
import base64


class Server:

    def __init__(self):
        self.initate_socket();
    
        self.Recv_Data()

    def initate_socket(self):
        ip = input("Enter Ip address: ")


        self.address = (ip, 100)
        self.s = socket(AF_INET, SOCK_DGRAM)

        self.s.settimeout(0.2)
        self.s.bind(self.address)

    def Decrypting_Data(self, Data):
        decode_data = base64.b64decode(Data)

        point = decode_data.decode('utf-8')

        return point
    


    def Recv_Data(self):
        try:    
            while True:
                x= 0 
                y = 0
                data, addr = self.s.recvfrom(1024)

                point = self.Decrypting_Data(data)

                plt.clf()
                plt.scatter(point)
                plt.pause(0.1)

            plt.show()


        except KeyboardInterrupt:
            self.s.close()
            sys.exit()

if __name__ ==  "__main__":

    
    Server()