from socket import *
import time 
import sys 
import base64
from collections import namedtuple
import Lidar

#client runs on jetson nano & send lidar data to server to diasplay  
class Client:

    server_ip = input("Please Enter server ip: ")


    server_address = (server_ip, 100)


    client = socket(AF_INET, SOCK_DGRAM)


    def __init__(self):
        self.initiate_Lidar()


    def initiate_Lidar(self):
    
        port = Lidar.Get_port()
    
        laser = Lidar.Parameters(port)
    
        self.ret, self.scan, self.laser = Lidar.Initialize_SDK(laser)


    def Encrypting_Data(self, x, y):
        point = (x, y)

        #Encode the data to bytes
        byte_data = str(point).encode('utf-8')

        #encode using base64 
        decode_data = base64.b64encode(byte_data)

        return decode_data
    

    def Send_Data(self):
        try:
            while True:
                x,y = Lidar.Extract_Data(self.ret, self.scan, self.laser)
                
                point = self.Encrypting_Data(x,y)


                self.client.sendto((point), (self.server_address) )
                time.sleep(0.05)
                
        except KeyboardInterrupt:
            self.client.close()

            sys.exit()

