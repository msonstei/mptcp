#!/usr/bin/python
#################
# Author: Mark D. Sonstein
# Date May 5, 2021
#################
# Application to read a split file and combine it
# developed as part of MP-TCP research
# Developed using Python3
#################
# Specifically, this module performs data post-transport processing


import os
import math
import logging

logging.basicConfig(filename='mptcp.log',level=os.environ.get("LOGLEVEL", "INFO"))
logging.basicConfig(format='%(asctime)s %(message)s')
#log = logging.getLogger(__name__)

# The splitRecords method accepts an array [] of string data
# and splints it by the number of buckets.
# This method takes two arguments:
# resplit - an array of data characters to be split for data transfer.
# cnt - represents the number of outbound connections to use.
# Buckets are calculated as a whole number equal the number of connections being used  

class file_join:
    def __init__(self,prejoin,cnt):
        self.prejoin = prejoin
        self.cnt = cnt 

    def joinRecords(prejoin,cnt):
        #ititialize required variables
        results = []
        d = {}
        x=0
        final = ""

        # Produce containers for the data equal to the number of connections
        # since there are nth possible connections this is built dynamically 
        print('Building {0} buckets'.format(cnt))
        while x < cnt:
            # Make a blank array bucket
            d['data{0}'.format(x)] = []
            x+=1
        x = 0
        print(prejoin)
        # Add files to containers
        while x < cnt:
            d['data{0}'.format(x)] = prejoin[x]
            x+=1
        print(d['data0'])
        #newcount = len(d['data0'])
        # Split data provided by 'prejoin' equally
        # into the buckets from previous statement
 #       print('Starting file split')
 #       while x < cnt:
 #           d['data{0}'.format(x)] = prejoin[x::cnt]
 #           x+=1
 #           final = str(len(d['data{0}'.format(0)]))
 #       print("Produced {0} buckets with {1} entries".format(cnt,final))
 #       logging.info("Produced {0} buckets with {1} entries".format(cnt,final))
 #       x=0

        #Append records into an array and 
        # return results to calling function
#        while x < cnt:
#            #print(x,'\n',d['data{0}'.format(x)],'\n\n')
#            results.append(d['data{0}'.format(x)])
#            x=x+1
#        return results
