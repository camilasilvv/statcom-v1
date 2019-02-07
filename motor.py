import socket
import struct
import rotctld

class Motor():
    def __init__(self, azimuth, elevation):
        self.azimuth = azimuth
        self.elevation = elevation
        # to do : verify if the mototrs serial number is needed in rotctld to connect

# to do : 1 - set up port tcp
#         2 - set up communication via rotctld
#         3 - set up thread