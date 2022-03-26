
#!/usr/bin/python
#################
# Author: Mark D. Sonstein
# Date June 26, 2021
#################
# Application to read file and split
# developed as part of MP-TCP research
# Developed using Python3
#################
# Specifically, this module performs data sending to server


import socket
import sys
import pickle

class client_send:
    def __init__(self,record,server,sock):
        self.record = []
        self.server = 'mptcp1.sonstein.ml'
        self.sock = 12345

    def sendRecords(self,record,server,sock):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(server,sock)

        s.connect((server,sock))

        #while True:
        s.send(pickle.dumps(record))
        print "N:",s.recv(24).decode()
        s.close()

