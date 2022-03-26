#!/usr/bin/python
#################
# Author: Mark D. Sonstein
# Date June 26, 2021
#################
# Application to read file and split
# developed as part of MP-TCP research
# Developed using Python3
#################
# Specifically, this module contains
# TCP transport

import socket
import sys

#host = '192.168.1.22' #socket.gethostname()
#port = 23                   # The same port as used by the server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.1.22', 12345)
#print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.connect(server_address)

try:

    # Send data
    message = 'This is the message.  It will be repeated.'
#    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
#        print >>sys.stderr, 'received "%s"' % data

finally:
#    print >>sys.stderr, 'closing socket'
    sock.close()
