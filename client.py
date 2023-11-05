import socket 
import time 
import os 
import sys
import base64
import numpy as np
import matplotlib.pyplot as plt
import pickle



class Client:
    server_address = ("192.168.0.36", 100)



    def __init__(self):

        self.Init_socket()

        while True:
            point = self.Recv_Data()


            print(point[0])

            break

        plt.show()

    


#########################################################################
#                    Declaring and Initiating socket                    #
#########################################################################

    def Init_socket(self):
        #Declaring the socket 
        self.client_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.client_socket.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)

        #Connect to the server
        self.client_socket.connect(self.server_address)
        print("Connection has been establish with server")
    

    def Recv_Data(self):

        data = self.client_socket.recv(4024)
        
        point = self.Decrypting(data)

        return point

#########################################################################
#                            Data De-cryption                           #
#########################################################################

    def Decrypting(self, Data):

        load = base64.b64decode(Data)

        point =  pickle.loads(load)

        return point
    
if __name__ == "__main__":
    Client()
