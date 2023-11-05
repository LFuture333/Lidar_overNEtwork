import socket
import threading
import time
import sys
import Lidar
import numpy as np
import base64
import pickle


class Server:
#   The server address 
    server_addres = ('192.168.0.36', 100)
    

    def __init__(self):
        self.Init_socket()

        self.Initialize_Lidar()
        while True:
            encrypt_msg =  self.Lidar_Data()

            self.Send_Data(message=encrypt_msg)



#####################################################################
#                Declaring and Initiating socket                    #
#####################################################################

    def Init_socket(self):

        #Declaring socket 
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        #BINDING THE server address 
        self.server_socket.bind(self.server_addres)

        #Listen for connection
        self.server_socket.listen(100)

        #Accepting incoming connection and notify the address 
        self.CliAddr, self.addr = self.server_socket.accept()
        print("Client connect from: " + str(self.addr))


    def Send_Data(self, message):
        
        self.CliAddr.sendto(message, self.addr)

#####################################################################
#                          Data Encryption                          #
#####################################################################
    def Encrypt(self, data):

        


        #Dumping data as byte to be send over network

        byte = pickle.dumps(data)

        msg = base64.b64encode(byte)


        return msg


#####################################################################
#                Initiating Lidar Parameters                        #
#####################################################################
    def Initialize_Lidar(self):

        port = Lidar.Get_port()

        laser = Lidar.Parameters(port)

        self.ret, self.scan, self.laser = Lidar.Initialize_SDK(laser)


    def Lidar_Data(self):

        # Extract raw data from the lidar 
        x,y = Lidar.Extract_Data(self.ret, self.scan, self.laser)
        point = ([x],[y])
       


        msg_encrypted = self.Encrypt( data=point)
        
        return msg_encrypted


if __name__ == "__main__":
    Server()