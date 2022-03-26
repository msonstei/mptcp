#!/usr/bin/python
#################
# Author: Mark D. Sonstein
# Date March 26, 2022
#################
# Application to read file and split
# developed as part of MP-TCP research
# Developed using Python3
#################
# Specifically, this module performs data pre-processing


import os
import math
import logging
from datetime import datetime
import timeit
import pickle

logging.basicConfig(filename='mptcp.log',level=os.environ.get("LOGLEVEL", "INFO"))
logging.basicConfig(format='%(asctime)s %(message)s')
#log = logging.getLogger(__name__)

# The splitRecords method accepts an array [] of string data
# and splints it by the number of buckets.
# This method takes two arguments:
# resplit - an array of data characters to be split for data transfer.
# cnt - represents the number of outbound connections to use.
# Buckets are calculated as a whole number equal the number of connections being used  

class file_split:
    def __init__(self,presplit,cnt):
        self.presplit = presplit
        self.cnt = cnt 




    def splitRecords(presplit,cnt):
        logging.info('\nInitializing Data Split' + datetime.now().strftime("%d.%b %Y %H:%M:%S.%f"))
        #ititialize required variables
        results = []
        result0 = []
        result1 = []
        result2 = []
        d = {}
        x=0
        final = ""

        
        # Produce containers for the data equal to the number of connections
        # since there are nth possible connections this is built dynamically 
        logging.info('\nBuilding buckets '+ str(cnt)+' ' + datetime.now().strftime("%d.%b %Y %H:%M:%S.%f"))
        while x < cnt:
            # Make a blank array bucket
            d['data{0}'.format(x)] = []
            x+=1
        x = 0

        # Split data provided by 'presplit' equally
        # into the buckets from previous statement
        logging.info('Starting Data Split' + datetime.now().strftime("%d.%b %Y %H:%M:%S.%f"))
        while x < cnt:
            d['data{0}'.format(x)] = presplit[x::cnt]
            x+=1
            final = str(len(d['data{0}'.format(0)]))
            
        # print("Produced {0} buckets with {1} entries".format(cnt,final))
        logging.info("Produced {0} buckets with {1} entries".format(cnt,final) + datetime.now().strftime("%d.%b %Y %H:%M:%S.%f"))
        x=0

        #Append records into an array and 
        # return results to calling function
        while x < cnt:
            #print(x,'\n',d['data{0}'.format(x)],'\n\n')
            results.append(d['data{0}'.format(x)])
            x+=1
        try:
          result0.append(d['data{0}'.format(0)])
          newfile0 = 'file0.txt'
        except Exception as e:
            print(str(e))
            logging.error('Error: ' + str(e) + datetime.now().strftime("%d.%b %Y %H:%M:%S.%f"))  
            

        try:
            result1.append(d['data{0}'.format(1)])
            newfile1 = 'file1.txt'

        except Exception as e:
            print(str(e))
            logging.error('Error: ' + str(e)+ datetime.now().strftime("%d.%b %Y %H:%M:%S.%f"))
        

        try:
            result2.append(d['data{0}'.format(2)])
            newfile2 = 'file2.txt'

        except Exception as e:
            print(str(e))
            logging.error('Error: ' + str(e)+ datetime.now().strftime("%d.%b %Y %H:%M:%S.%f"))
       
        #Write the parsed data to a file
        #This should be changed in the future to a network data stream
        #using MP-TCP
        try:
            with open('newfile0', 'wb') as file:
                logging.info('Writing output to file '+ newfile0 + datetime.now().strftime("%d.%b %Y %H:%M:%S.%f"))
                pickle.dump(result0,file)
                file.close()
        except Exception as e:
            print(str(e))
            logging.error('Error: ' + str(e)+ datetime.now().strftime("%d.%b %Y %H:%M:%S.%f") + str(e))

        logging.info('Writing to file '+ newfile0 + ' complete ' + datetime.now().strftime("%d.%b %Y %H:%M:%S.%f"))

        try:
            with open('newfile1', 'wb') as file:
                logging.info('Writing output to file '+ newfile1 + datetime.now().strftime("%d.%b %Y %H:%M:%S.%f"))
                pickle.dump(result1,file)
                file.close()
        except Exception as e:
            print(str(e))
            logging.error('Error: ' + str(e)+ datetime.now().strftime("%d.%b %Y %H:%M:%S.%f") + str(e))

        logging.info('Writing to file '+ newfile1 + ' complete ' + datetime.now().strftime("%d.%b %Y %H:%M:%S.%f"))

        try:
            with open('newfile2', 'wb') as file:
                logging.info('Writing output to file '+ newfile2 + datetime.now().strftime("%d.%b %Y %H:%M:%S.%f"))
                pickle.dump(result2,file)
                file.close()
        except Exception as e:
            print(str(e))
            logging.error('Error: ' + str(e)+ datetime.now().strftime("%d.%b %Y %H:%M:%S.%f") + str(e))

        #logging.info(f'Writing to file {newfile2} complete ' + datetime.now().strftime("%d.%b %Y %H:%M:%S.%f"))
        #print(f"Results are: {result0}")
        return results