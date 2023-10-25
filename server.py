import socket
import time 
import sys 
from collections import namedtuple

class Server:
# Declaring the socket for the server
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    server.settimeout(0.2)

# Declare the lidar parameters 


    Lidar_Data = namedtuple('Lidar', ['x','y', 'Loop_Count'])

    def __init__(self):
        print()




    


    