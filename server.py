import socket
import time 
import sys 
import Lidar
from collections import namedtuple
import base64

class Server:

    

    # Declaring the socket for the server
    def initiate_socket(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        self.server.settimeout(0.2)


        Client_Ip = input("Enter the Client IP: ")

        self.Cli_address= ("192.168.0.2", 100) 

   

    
    def Decrypting_Data(self, Data):

        decode_data = base64.b64decode(Data)

        point = decode_data.decode('utf-8')

        return point
    

    def Send_Data(self):
        count = 0
        try:
            while True:
                
                #extracting lidar data from the sdk
                
                #Decrypting The data



        except KeyboardInterrupt:
            self.server.close()
            sys.exit()

    def __init__(self):
        self.initiate_socket()

        self.initiate_Lidar()

        self.Send_Data()


if __name__ == "__main__":

    Server();


    