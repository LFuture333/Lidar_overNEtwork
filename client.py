import socket
import time
import os 
import sys 
import base64
from collections import namedtuple
import Lidar

#client runs on jetson nano & send lidar data to server to diasplay  
class Client:

    server_ip = input("Please Enter server ip: ")


    server_address = (server_ip, 100)

    def __init__(self):
        self.initiate_Lidar()

        self.Initiate_Socket()

        self.Send_Data()

##########################################################################
##                                 Lidar  Stuff                         ##
##########################################################################
    def initiate_Lidar(self):
    
        port = Lidar.Get_port()
    
        laser = Lidar.Parameters(port)
    
        self.ret, self.scan, self.laser = Lidar.Initialize_SDK(laser)


##########################################################################
##                             Data  Encryption                         ##
##########################################################################
    def Encrypting_Data(self, x, y):
        point = (x, y)

        #Encode the data to bytes
        byte_data = str(point).encode('utf-8')

        #encode using base64 
        decode_data = base64.b64encode(byte_data)

        return decode_data
    


##########################################################################
##                             Socket Stuff                             ##
##########################################################################
    def Initiate_Socket(self):
        self.client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.client.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
        
        self.client.connect(self.server_address)

    
    
    def Send_Data(self):
        try:
            while True:
                x,y = Lidar.Extract_Data(self.ret, self.scan, self.laser)
                
                point = self.Encrypting_Data(x,y)


                self.client.send(  (point) )

                time.sleep(0.05)
                
        except KeyboardInterrupt:
            self.client.close()

            sys.exit()

