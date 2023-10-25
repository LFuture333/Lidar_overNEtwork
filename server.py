import socket
import time 
import sys 
from collections import namedtuple

class Server:
    Lidar_Data = namedtuple('Lidar', ['x','y', 'Loop_Count'])

    def __init__(self):
        print()
        struct = self.Lidar(x=[4.0,4,4,3], y=[4.0,4,4,3], Loop_Count=0)

        print(struct)