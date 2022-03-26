#!/usr/bin/python
#################
# Author: Mark D. Sonstein
# Date June 26, 2021
#################
# Application to read a split file and combine it
# developed as part of MP-TCP research
# Developed using Python3
#################
# Specifically, this module performs data pre-processing


import os
import math
import logging
import numpy as np
from datetime import datetime

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

    def Extract(lst):
        return [item[0] for item in lst]     


    def joinRecords(prejoin,cnt):
        #ititialize required variables
        results, results1, result = '', '', ''
        d = {}
        x,y=0,0
        final = ""
        inner_cnt, outer_cnt = 0,0
        # Produce containers for the data equal to the number of connections
        # since there are nth possible connections this is built dynamically 
        logging.info('Building {0} buckets'.format(cnt) + datetime.now().strftime("%d.%b %Y %H:%M:%S"))

        # Add files to containers
        for item in prejoin:
            result = item
            
        #print("Result: ", result[1])
         
        outer_cnt = len(result)
        inner_cnt = len(result[0])

        
        while x < inner_cnt:
            y=0
            try:
                while y < (outer_cnt):
                    if x> inner_cnt:
                        print('Y: ',y)
                        logging.error("Count Exceeded"+ datetime.now().strftime("%d.%b %Y %H:%M:%S"))
                    final+=result[y][x]
                    #final+=results1[x]
                    y+=1
            except Exception as e:
                print(x,y)
                logging.error(str(e) + datetime.now().strftime("%d.%b %Y %H:%M:%S"))
                print('\n', str(e))
                break
            if x > 920:
                print('X: ',x)
            x+=1
     
        return final      
        

