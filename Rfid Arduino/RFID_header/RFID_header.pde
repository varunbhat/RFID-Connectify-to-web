#ifndef RFID_H
#define RFID_H

#include <SoftwareSerial.h>
#define rxPin 2
#define txPin 3
class RFID
{
private:
  char tag[12];
  SoftwareSerial mySerial(uint8_t,uint8_t);
public:
  RFID();
  char* read();
};
#endif



RFID::RFID()
{
  for(int i=0;i<12;i++)
    tag[i]=-1;
  SoftwareSerial mySerial =  SoftwareSerial(rxPin, txPin);
}

char* RFID::read()
{
  for(byte i=0;i<12;)
  {
    tag[i] =   mySerial.read();
    if(tag[i]>=0)i++;
  }
  return tag;
}


