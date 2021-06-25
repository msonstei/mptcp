#!/usr/bin/python
#################
# Author: Mark D. Sonstein
# Date May 3, 2021
#################
# Application to read file and split
# developed as part of MP-TCP research
# Developed using Python3
#################
# Specifically, this module contains
# main() from which the application starts

import os
import math
import logging
import pickle
from datetime import datetime
import file_split
import file_join
#from file_split import file_split

logging.basicConfig(filename='mptcp.log',level=os.environ.get("LOGLEVEL", "INFO"))
logging.basicConfig(format='%(asctime)s %(message)s')
#log = logging.getLogger(__name__)

def main():
    print('main')
    results = []
    logging.info('Starting MP-TCP Application ' + datetime.now().strftime("%d.%b %Y %H:%M:%S"))#,datetime.now())
    while True:
        try:
            conn = 2
            #conn = int(input("Enter number of outbound connections\t"))
            break
        except Exception as e:
            print("That's not a valid, please enter an Integer")
            log.error('Error: ' + str(e))
    
    #filename = input("Enter source file to send\t\t")
    filename = 't.txt'
    file_array = []
    try:
        with open(filename) as file:
            logging.info('Opening '+ filename)
            file_array = file.read()
            file.close()

    except Exception as e:
        print(str(e))
        logging.error('Error: ' + str(e))
    
    print(str(len(file_array)))
    
    results = file_split.file_split.splitRecords(file_array,conn)
    print("Preparing to write file")
    #newfile = input("Enter destination file\t\t")
    newfile = 'testout.ob'
    try:
        with open(newfile, "w") as file:
            for listitem in results:
                file.write(listitem)
            file.close()
    except Exception as e:
        print(str(e))
        logging.error('Error: ' + str(e))

    print('Write complete')
    print("Starting readback")
    file_array = []
    try:
        with open(newfile,'r') as file:
            filecontent = file.readlines()
            logging.info('Opening '+ newfile)
            for line in filecontent:
                data = line[:-1]
                file_array.append(data)
            file.close()

    except Exception as e:
        print(str(e))
        logging.error('Error: ' + str(e))
        
    file_join.file_join.joinRecords(file_array,conn)
    print(str(len(file_array)))

def __main__():
    print('__main__')
    main()
