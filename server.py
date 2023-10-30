import socket
import time 
import sys 
import Lidar
from collections import namedtuple
import base64

class Server:

    Lidar_Data = namedtuple('Lidar', ['x','y', 'Loop_Count'])

    # Declaring the socket for the server
    def initiate_socket(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        self.server.settimeout(0.2)


        Client_Ip = input("Enter the Client IP: ")

        self.Cli_address= (Client_Ip, 100) 

    # Declare the lidar parameters 
    def initiate_Lidar(self):
    
        port = Lidar.Get_port()
    
        laser = Lidar.Parameters(port)
    
        self.ret, self.scan, self.laser = Lidar.Initialize_SDK(laser)


    def Encrypting_Data(self, x,y , count):
        point = (x, y)

        # encode the data to bytes 
        byte_data = str(point).encode('utf-8')

        #encode using base64
        decode_data = base64.b64decode(byte_data)

        return decode_data

    def Send_Data(self):
        count = 0
        try:
            while True:
                
                #extracting lidar data from the sdk
                x,y = Lidar.Extract_Data(self.ret, self.scan, self.laser)

                #Loop Count 
                count = count + 1 

                data = self.Encrypting_Data(x,y)

                # Store the data in the struct

                self.server.sendto(data, (self.Cli_address) )


        except KeyboardInterrupt:
            self.server.close()
            sys.exit()

    def __init__(self):
        self.initiate_socket()

        self.initiate_Lidar()

        self.Send_Data()


if __name__ == "__main__":

    Server();


    