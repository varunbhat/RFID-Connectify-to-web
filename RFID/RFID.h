
#ifndef SoftwareSerial_h
#define SoftwareSerial_h

#include <inttypes.h>

class SoftwareSerial
{
  private:
    uint8_t _receivePin;
    uint8_t _transmitPin;
    long _baudRate;
    int _bitPeriod;
    void printNumber(unsigned long, uint8_t);
  public:
    SoftwareSerial(uint8_t, uint8_t);
    void begin(long);
    int read();
    void print(char);
    void print(const char[]);
    void print(uint8_t);
    void print(int);
    void print(unsigned int);
    void print(long);
    void print(unsigned long);
    void print(long, int);
    void println(void);
    void println(char);
    void println(const char[]);
    void println(uint8_t);
    void println(int);
    void println(long);
    void println(unsigned long);
    void println(long, int);
};

#endif





#ifndef RFID_H
#define RFID_H

#include <inttypes.h>

#define rxPin 2
#define txPin 3


class RFID
{
private:
  char tag[12];
 // SoftwareSerial mySerial ;
public:
  RFID();
  char* read();
};
#endif




