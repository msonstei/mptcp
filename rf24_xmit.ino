/*
*Code used to accept Serial data
* and transmit over RF24 radio
*
*Arduino Serial to RF
*Radio segment of MP-TCP Project
*
*by Mark Sonstein
*
* Library: TMRh20/RF24, https://github.com/tmrh20/RF24/
*/
//Include Libraries
//#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
//#define ARDUINO_AVR_UNO
#include <DirectIO.h>
//create an RF24 object
RF24 radio(9, 10);  // CE, CSN
InputPort<PORT_D, 2, 8> my_port;
//create data input pins
//int Pin1 = 1;
int myBytes;
int bits;
char buf[8];
//struct bits{int b0; int b1; int b3; int b4; int b5; int b6; int b7;};
//address through which two modules communicate.
const byte address[6] = "00001";

void setup(){
  Serial.begin(9600);
  my_port.setup();
  radio.begin();
  //pinMode(Pin1, INPUT);
  //set the address
  radio.openWritingPipe(address);
  //Set module as transmitter
  radio.stopListening(); 
}

void loop(){
  //Serial.println("Start read");
  u8 myByte = my_port.read(); 
  //myBytes = digitalRead(2);
  //myByte |= digitalRead(3);
  //myByte |= digitalRead(4);
  //myByte |= digitalRead(5);
  //myByte |= digitalRead(6);
  //myByte |= digitalRead(7);
  //myByte |= digitalRead(8);
  //Send message to receiver
  if(myBytes){
    Serial.print("MyBytes: ");
    Serial.println(myBytes);}
  if (myByte){

    Serial.print("Reading: \n");
    //Serial.println(b"{myByte}");
    for (int i = 0; i < 8; i++)
    {
        bool b = myByte & 0x80;
        Serial.print(b);        
        myByte = myByte << 1;
    }
    send(bits);
    Serial.println();
    //const char text[] = "Hello World";
    //radio.write(&text, sizeof(text));
    
    //delay(1000);
  }
}

void send(u8 myByter){ 
  Serial.print("Sending: ");
  Serial.println(myByter);
  radio.write(&myByter, sizeof(myByter));
}
