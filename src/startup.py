#!/usr/bin/python
#################
# Author: Mark D. Sonstein
# Date March 26, 2022
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
#################


import os
import math
import logging
import pickle
from datetime import datetime
import file_split
import file_join
import json
import time
from cryptography.fernet import Fernet
# Import for GUI build
import tkinter as tk
from msilib.schema import RadioButton


# Configure logging activities
logging.basicConfig(filename='mptcp.log',level=os.environ.get("LOGLEVEL", "INFO"))
logging.basicConfig(format='%(asctime)s %(message)s')


def main():
    """Initialize variables
    Array to store values of parsed data"""
    results = []
        #Establish default input filename
    filename = '2city12p.txt' 
        #Array to store values of imported and in-process data
    file_array = []
    file_array_input = []
        #Establish default connections count
    conn = 3 
        #Establish default output filename
    newfile = 'testout.ob'
        #Establish class instances
    fs = file_split.file_split #.splitRecords(file_array, conn)
    fj = file_join.file_join #(file_array, conn)

    #Log starting of application
    logging.info(f'\nStarting MP-TCP Application ' + datetime.now().strftime("%d.%b %Y %H:%M:%S.%f"))
    # Uncomment below to enable GUI processing
    #frame()

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
    
    # Start timing the message splitting function and activities
    timer_start = time.time()
   
    # Call the open_file function
    file_array = open_file(filename)
    

    #Call File_Split.py to break the inported data into mulpile data streams 
    results = fs.splitRecords(file_array,conn)

    # Capture ending time and calculate total time
    timer_end = time.time()
    total_time = 1000 * (timer_end - timer_start)
    print(f"Splitting file took {total_time} milliseconds")
    logging.info(f"Splitting file took {total_time} milliseconds")
    print("Preparing to write file")

    #TODO Ask user if encryption should be used and add encryption method
    while True:
        try:            
            answer = input("Do you want to encrypt outbound traffic (Y/n)\t").upper()
            if answer == "YES":
                do_encrypt(filename)
                break
            elif answer == "Y":
                do_encrypt(filename)
                break
            elif answer == "":
                do_encrypt(filename)
                break
            elif answer == "NO":    
                break
            elif answer == "N":    
                break
            else:
                raise Exception("Unknown Input for Encryption")
            
        except Exception as e:
            print("Unknown Input")
            logging.error('Error: ' + str(e))

    """Write the parsed data to a file
    This should be changed in the future to a network data stream
    using MP-TCP"""
    try:
        with open(newfile, "wb") as file:
            logging.info('Writing output to file '+ newfile + datetime.now().strftime("%d.%b %Y %H:%M:%S.%f"))
            pickle.dump(results,file)
            file.close()
    except Exception as e:
        print(str(e))
        logging.error('Error: ' + str(e)+ datetime.now().strftime("%d.%b %Y %H:%M:%S.%f"))

    logging.info('Writing to file '+ newfile + ' complete ' + datetime.now().strftime("%d.%b %Y %H:%M:%S.%f"))
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
    # Uncomment to print the recorded data    
    # print(fj.joinRecords(file_array_input,conn))

def frame():
    root = tk.Tk()
    greeting = tk.Label(text="S.T.O.P.P.", foreground = "red",background="black" )
    greeting.pack()

    frame_a = tk.Frame(master=root, relief=tk.RIDGE, borderwidth=5)
    label_a = tk.Label(master=frame_a, text="Enter Source File Name")
    text_box = tk.Text()
    text_box.pack()
    text_box.get("1.0", tk.END)
    label_a.pack()
    

    
    label = tk.Label(
        text="Do you require Encryption",
        foreground="white",  # Set the text color to white
        background="black"  # Set the background color to black
    )
    selection = "You selected the option " 
        #label.config(text = selection)
    
    var = tk.StringVar()
    R1 = tk.Radiobutton(root, text = "Yes", variable = var, value = "Y")#,command = sel)
    R1.pack()

    R2 = tk.Radiobutton(root, text = "No", variable = var, value = "N")#,command = sel)
    R2.pack()

    #R3 = tk.Radiobutton(root, text = "Option 3", variable = var, value = 3)#,command = sel)
    #R3.pack() # anchor = W)
    #label.config(text = "Do you require encry")
    #label = Label(root)
    #label.pack()
    #top.mainloop()
    root.mainloop()

def open_file(filename):
    file_array = []
 #Read file of data to be parsed with error handling
    try:
        with open(filename) as file:
            logging.info(f'Opening {filename} ' + datetime.now().strftime("%d.%b %Y %H:%M:%S.%f"))
            file_array = file.read()
            file.close()

    except Exception as e:
        print('An error was returned ',str(e))
        logging.error('Error: ' + str(e)+ datetime.now().strftime("%d.%b %Y %H:%M:%S.%f"))
    return file_array

def do_encrypt(filename):
    # key generation
    key = Fernet.generate_key()
  
    # string the key in a file
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)

    # Measure the to encrypt the same data
    # Start timing the activities
    timer_start = time.time()

    # opening the key
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
    
    # using the generated key
    fernet = Fernet(key)
    
    # opening the original file to encrypt
    with open(filename, 'rb') as file:
        original = file.read()
        
    # encrypting the file
    encrypted = fernet.encrypt(original)

    # Capture ending time
    timer_end = time.time()
    total_time = 1000 * (timer_end - timer_start)
    print(f"Encrypting file took {total_time} milliseconds")
    logging.info(f"Encrypting file took {total_time} milliseconds")


    # opening the file in write mode and 
    # writing the encrypted data
    with open('encyptedfile.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    return

def __main__():
    print('__main__')
    main()
