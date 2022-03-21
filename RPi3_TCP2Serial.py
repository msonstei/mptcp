import socket
from gpiozero import LED
from time import sleep
import RPi.GPIO as GPIO
import sys
import struct
import os
from struct import *

host = '192.168.1.7'
port = 1338

def light_leds(bits):
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(21, GPIO.OUT)
   GPIO.setup(2, GPIO.OUT)
   GPIO.setup(3, GPIO.OUT)
   GPIO.setup(4, GPIO.OUT)
   GPIO.setup(5, GPIO.OUT)
   GPIO.setup(6, GPIO.OUT)
   GPIO.setup(7, GPIO.OUT)
   GPIO.setup(8, GPIO.OUT)
#   print(f"Received {bits}")
   x = []
   count = 0
   print("off")
   sleep(1)
   for var in bits:
      x.insert(count, var)
#      print(f"{count} = {var}")
      count = count + 1
   while (count < 9):
      x.insert(count,0)
      count = count + 1
   count = 0
   while (count < 9):
       print(x[count])
       count = count + 1

   print("mixed")
   if (x[2] == '0'):
      GPIO.output(21, False)
      #print("Pin 1 off")
   else:
      GPIO.output(21, True)
      #print("Pin 1 on")

   if (x[3] == '0'):
      GPIO.output(2, False)
      #print("Pin 2 off")
   else:
      GPIO.output(2, True)
      #print("Pin 2 on")
   if (x[4] == '0'):
      GPIO.output(3, False)
      #print("Pin 3 off")
   else:
      GPIO.output(3, True)
      #print("Pin 3 on")
   if x[5] == '0':
      GPIO.output(4, False)
      #print("Pin 4 off")
   else:
      GPIO.output(4, True)
      #print("Pin 4 on")
   if x[6] == '0':
      GPIO.output(5, False)
      #print("Pin 5 off")
   else:
      GPIO.output(5, True)
      #print("Pin 5 on")
   if x[7] == '0':
      GPIO.output(6, False)
      #print("Pin 6 off")
   else:
      GPIO.output(6, True)
      #print("Pin 6 on")
   if x[8] == '0':
      GPIO.output(7, False)
      #print("Pin 7 off")
   else:
      GPIO.output(7, True)
      #print("Pin 7 on")
   if x[8] == 0:
      GPIO.output(8, False)
      #print("Pin 8 off")
   else:
      GPIO.output(8, True)
      #print("Pin 8 on")
   sleep(1)
   return()

def main():
 # Start by openning a socket to receive information in RAW format
 try:
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
 except socket.error as exc:
    print('Socket could not be created. Error Code : ' + str(exc[0]) +     '           Message ' + exc[1])
    sys.exit()

 # Recieved a packet of information
 while True:
    packet = s.recvfrom(65565)

  #packet string from tuple
    packet = packet[0]

  #take first 20 characters for the ip header
    ip_header = packet[0:20]
    data = packet[21:len(packet)]
  #now unpack them :)
    iph = unpack('!BB3HBBH4s4s' , ip_header)

    version_ihl = iph[0]
    version = version_ihl >> 4
    ihl = version_ihl & 0xF

    iph_length = ihl * 4

    ttl = iph[5]
    protocol = iph[6]
    s_addr = '192.168.1.11'
    d_addr = '127.0.0.1'

    print('Version : ' + str(version) + ' IP Header Length : ' +   str(ihl) + ' TTL : ' + str(ttl) + ' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr))
    try:
      file = 'test.txt'
      fileOpen = open('test.txt', 'a')
      print ("\n[*] Capture file %s will be written to %s.  " %                     (file,os.getcwd()))

    except:
      print("\n[*] ERROR! There was issue opening your file")
      sys.exit()



    fileOpen.write("\n\t[-] Layer 3[-]\n\n[*] Source IP: %s\n[*] Destination IP: %s\n" % (s_addr, d_addr))

    tcp_header = packet[iph_length:iph_length+20]

  #now unpack them :)
    tcph = unpack('!HHLLBBHHH' , tcp_header)

    source_port = 1338
    dest_port = 1338
    sequence = tcph[2]
    acknowledgement = tcph[3]
    doff_reserved = tcph[4]
    tcph_length = doff_reserved >> 4

    print('Source Port : ' + str(source_port) + ' Dest Port : ' +      str(dest_port) + ' Sequence Number : ' + str(sequence) + ' Acknowledgement : ' + str(acknowledgement) + ' TCP header length : ' + str(tcph_length))

    fileOpen. write("\n\t[-]Layer 4[-]\n\n[*]Source Port: %s\n[*]Destination Port: %s\n" % (source_port,dest_port))
    fileOpen.write("Data found: %s" %(data))
    fileOpen.close()

#  with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP) as s:
#     s.bind((host, port))
#     s.listen()
#     conn, addr = s.accept()


    if(packet):
#          print(f"Connection from {addr}")
#          while True:
#            data = conn.recv(1024)
#            listTest = list(data)
#            print(listTest)
#            try:
#              file = 'testfile.txt'
#              file = open(file, "a")
#            except:
#              print("Error creating file")
           for var in packet:
               bits = bin(int(var))
               print(bits)
               print("sending")
               light_leds(bin(int(var)))
           if not packet:
                 conn.close()
                 GPIO.cleanup()
#  sys.exit(1)


if __name__ == "__main__":
    main()
