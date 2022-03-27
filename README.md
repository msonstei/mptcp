# mptcp

Applications and work associated with PhD research. The purpose of this research is to leverage MP-TCP to obfuscate data allowing safe transport without encryption requirements. 


The overall project consists of several key peices.

  - Initialize
  - Split data
  - Send data across several, disparit paths using MP-TCP
    - Ethernet
    - WiFi
    - Internet
    - FM transmitter
  - Receive data from multiple streams
  - Rebuild data into original order
  - Rebuild the different fines into the original (Pre-split) format

src/startup.py initiates the processing.
TODO: add GUI interface for ease of use.

src/file_split.py takes a file as input and seperates the data into a number of individual files (number specified by user input). 
src/file_join.py return seperated data to original format

Transmission of data over RF24 testing example. RPi recieves the data via intranet connection and sends to Arduino over sereal connection. Arduino then transfer data to distant end using RF24 transmission.

Basic layout of the RPi3 to Arduino Nano to transmit TCP received on the RPi3 over serial to the Nano

<img src="https://user-images.githubusercontent.com/17393233/159374336-6384f379-f9f4-4fc2-a64b-f222044065a0.png" alt="drawing" width="600"/>

