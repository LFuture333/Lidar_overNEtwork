import socket 
import time 
import sys 
from collections import namedtuple
import matplotlib.pyplot as plt


class Client():

    Lidar_Data = namedtuple('Lidar', ['x','y','Loop_Count'])

    def __init__(self):

        self.initiate_socket()

        self.Recv_Data()

    def initiate_socket(self):

        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)


        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        
        ServerIp = input("Enter thr server ip: ")
        
        self.client.bind((ServerIp,  100))

    def Display_Data(self, x,y):
        plt.clf()
        plt.scatter(x,y)
        plt.pause(0.1)

    def Recv_Data(self):

        try:
            while True:

                data, addr = self.client.recvfrom(1024)
                
                
                plt.clf()
                plt.scatter(data.x,data.y)
                plt.pause(.1)
            plt.show()
            
        except KeyboardInterrupt:
            self.client.close()
            sys.exit()
if __name__ == "__main__":
    Client();