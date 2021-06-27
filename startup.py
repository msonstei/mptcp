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
# main() from which the application starts
#######S.T.O.P.P.##########
#Security
#Through
#Obscurity
#Packet
#Processing

import os
import math
import logging
import pickle
from datetime import datetime
import file_split
import file_join
import json


logging.basicConfig(filename='mptcp.log',level=os.environ.get("LOGLEVEL", "INFO"))
logging.basicConfig(format='%(asctime)s %(message)s')
#log = logging.getLogger(__name__)

def main():
    #Initialize variables
    #Array to store values of parsed data
    results = []
    #Establish default input filename
    filename = 't.txt' 
    #Array to store values of imported and in-process data
    file_array = []
    file_array_input = []
    #Establish default connections count
    conn = 3 
    #Establish default output filename
    newfile = 'testout.ob'
    #Establish class instances
    fs = file_split.file_split.splitRecords(file_array, conn)
    fj = file_join.file_join(file_array, conn)
    #Log starting of application
    logging.info('Starting MP-TCP Application ' + datetime.now().strftime("%d.%b %Y %H:%M:%S"))

    #Capture user provided inputs with error handling
    while True:
        try:            
            conn = int(input("Enter number of outbound connections\t"))
            break
        except Exception as e:
            print("That's not a valid, please enter an Integer")
            logging.error('Error: ' + str(e))

    """Input commented out during testing
       Uncomment prior to production """
    #filename = input("Enter source file to send\t\t")
    
    #Read file of data to be parsed with error handling
    try:
        with open(filename) as file:
            logging.info('Opening '+ filename + datetime.now().strftime("%d.%b %Y %H:%M:%S"))
            file_array = file.read()
            file.close()

    except Exception as e:
        print('An error was returned ',str(e))
        logging.error('Error: ' + str(e)+ datetime.now().strftime("%d.%b %Y %H:%M:%S"))
    
    #Call File_Split.py to break the inported data
    # into mulpile data streams 
    results = fs.splitRecords(file_array,conn)
    print("Preparing to write file")
    #TODO Ask user if encryption should be used and add encryption method

    #Write the parsed data to a file
    #This should be changed in the future to a network data stream
    #using MP-TCP
    try:
        with open(newfile, "wb") as file:
            logging.info('Writing output to file '+ newfile + datetime.now().strftime("%d.%b %Y %H:%M:%S"))
            pickle.dump(results,file)
            file.close()
    except Exception as e:
        print(str(e))
        logging.error('Error: ' + str(e)+ datetime.now().strftime("%d.%b %Y %H:%M:%S"))

    logging.info('Writing to file '+ newfile + ' complete ' + datetime.now().strftime("%d.%b %Y %H:%M:%S"))
    print("Starting readback")
    #Read input from file containing parsed data
    #This should be changed in the future to a network data stream
    #using MP-TCP
    
    try:
        with open(newfile,'rb') as file:
            while True:
                try:
                    file_array_input.append(pickle.load(file))
                except EOFError:
                    break
            file.close()

    except Exception as e:
        print(str(e))
        logging.error('Error: ' + str(e)+ datetime.now().strftime("%d.%b %Y %H:%M:%S"))
        
    print(fj.joinRecords(file_array_input,conn))
    

def __main__():
    print('__main__')
    main()
