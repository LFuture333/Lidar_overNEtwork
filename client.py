import socket 
import time 
import sys 
import base64
from collections import namedtuple
import Lidar


class Client():

    def __init__(self):

        self.initiate_socket()

        self.initiate_Lidar()

        self.Send_Data()



    def initiate_socket(self):

        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM )


     # Declare the lidar parameters 
    def initiate_Lidar(self):
    
        port = Lidar.Get_port()
    
        laser = Lidar.Parameters(port)
    
        self.ret, self.scan, self.laser = Lidar.Initialize_SDK(laser)

    def Encrypting_Data(self, x,y ):
        point = (x, y)

        # encode the data to bytes 
        byte_data = str(point).encode('utf-8')

        #encode using base64
        decode_data = base64.b64encode(byte_data)

        return decode_data
    

    def Send_Data(self):

        try:
            while True:
                x,y = Lidar.Extract_Data(self.ret, self.scan, self.laser)
            
                #encrypt the data 
                data = self.Encrypting_Data(x,y)
            
                self.client.sendto(data, ('192.168.0.36', 100))
                
                
                
            
        except KeyboardInterrupt:
            self.client.close()
            sys.exit()
if __name__ == "__main__":
    Client();