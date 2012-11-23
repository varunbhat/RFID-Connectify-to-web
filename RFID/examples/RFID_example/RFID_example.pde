
#include <RFID.h>
// connect the pin 3 to the rs232 pin of the RFID reader
RFID varun = RFID();

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  char *a;
  a = varun.read();
  for(int i=0;i<12;i++)Serial.print(a[i]);
  Serial.println();
}
