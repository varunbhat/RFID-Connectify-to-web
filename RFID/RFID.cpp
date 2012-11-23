

#include "WConstants.h"
#include "RFID.h"

SoftwareSerial mySerial = SoftwareSerial(2,3);
RFID::RFID()
{
  for(int i=0;i<12;i++)
    tag[i]=-1;

  mySerial.begin(9600);

}



char* RFID::read()
{
  for(uint8_t i=0;i<12;)
  {
    tag[i] =   mySerial.read();
    if(tag[i]>=0)i++;
  }
  return tag;
}

SoftwareSerial::SoftwareSerial(uint8_t receivePin, uint8_t transmitPin)
{
  _receivePin = receivePin;
  _transmitPin = transmitPin;
  _baudRate = 0;
}


void SoftwareSerial::begin(long speed)
{
  _baudRate = speed;
  _bitPeriod = 1000000 / _baudRate;

  digitalWrite(_transmitPin, HIGH);
  delayMicroseconds( _bitPeriod); // if we were low this establishes the end
}

int SoftwareSerial::read()
{
  int val = 0;
  int bitDelay = _bitPeriod - clockCyclesToMicroseconds(50);
  

  while (digitalRead(_receivePin));

  // confirm that this is a real start bit, not line noise
  if (digitalRead(_receivePin) == LOW) {
    // frame start indicated by a falling edge and low start bit
    // jump to the middle of the low start bit
    delayMicroseconds(bitDelay / 2 - clockCyclesToMicroseconds(50));
	
    // offset of the bit in the byte: from 0 (LSB) to 7 (MSB)
    for (int offset = 0; offset < 8; offset++) {
	// jump to middle of next bit
	delayMicroseconds(bitDelay);
	
	// read bit
	val |= digitalRead(_receivePin) << offset;
    }
	
    delayMicroseconds(_bitPeriod);
    
    return val;
  }
  
  return -1;
}

void SoftwareSerial::print(uint8_t b)
{
  if (_baudRate == 0)
    return;
    
  int bitDelay = _bitPeriod - clockCyclesToMicroseconds(50); // a digitalWrite is about 50 cycles
  byte mask;

  digitalWrite(_transmitPin, LOW);
  delayMicroseconds(bitDelay);

  for (mask = 0x01; mask; mask <<= 1) {
    if (b & mask){ // choose bit
      digitalWrite(_transmitPin,HIGH); // send 1
    }
    else{
      digitalWrite(_transmitPin,LOW); // send 1
    }
    delayMicroseconds(bitDelay);
  }

  digitalWrite(_transmitPin, HIGH);
  delayMicroseconds(bitDelay);
}

void SoftwareSerial::print(const char *s)
{
  while (*s)
    print(*s++);
}

void SoftwareSerial::print(char c)
{
  print((uint8_t) c);
}

void SoftwareSerial::print(int n)
{
  print((long) n);
}

void SoftwareSerial::print(unsigned int n)
{
  print((unsigned long) n);
}

void SoftwareSerial::print(long n)
{
  if (n < 0) {
    print('-');
    n = -n;
  }
  printNumber(n, 10);
}

void SoftwareSerial::print(unsigned long n)
{
  printNumber(n, 10);
}

void SoftwareSerial::print(long n, int base)
{
  if (base == 0)
    print((char) n);
  else if (base == 10)
    print(n);
  else
    printNumber(n, base);
}

void SoftwareSerial::println(void)
{
  print('\r');
  print('\n');  
}

void SoftwareSerial::println(char c)
{
  print(c);
  println();  
}

void SoftwareSerial::println(const char c[])
{
  print(c);
  println();
}

void SoftwareSerial::println(uint8_t b)
{
  print(b);
  println();
}

void SoftwareSerial::println(int n)
{
  print(n);
  println();
}

void SoftwareSerial::println(long n)
{
  print(n);
  println();  
}

void SoftwareSerial::println(unsigned long n)
{
  print(n);
  println();  
}

void SoftwareSerial::println(long n, int base)
{
  print(n, base);
  println();
}


void SoftwareSerial::printNumber(unsigned long n, uint8_t base)
{
  unsigned char buf[8 * sizeof(long)]; // Assumes 8-bit chars. 
  unsigned long i = 0;

  if (n == 0) {
    print('0');
    return;
  } 

  while (n > 0) {
    buf[i++] = n % base;
    n /= base;
  }

  for (; i > 0; i--)
    print((char) (buf[i - 1] < 10 ? '0' + buf[i - 1] : 'A' + buf[i - 1] - 10));
}
