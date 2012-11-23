#!C:\Python27\python

import sys
import serial
import io
import urllib2, cookielib

##if len(sys.argv)<1:
##    print 'Usage:', sys.argv[0], 'database_id'
##    sys.exit(1)


cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.106 Safari/535.2')]

logFil = open("log.txt",'w')



def serialprint(data):
    
        ser = serial.Serial(port='COM5',baudrate=9600 )
        sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
        sio.write(unicode(data))
        sio.flush()
        ser.close()
    
        logFil.write("unknown error while writing from serial")

def serialread():
    
        ser = serial.Serial(port='COM5',baudrate=9600 )
        x = ser.read()
        ser.close()
        return x
        logFil.write("unknown error while reading from serial")
    

parseVal = "id="+'1'

print parseVal
f = opener.open('http://localhost/srishti/getDB.php?id='+'1',parseVal)

s = f.read()
s= '\n'+s
print s
logFil.write(s)
logFil.close()
serialprint("somedata")
serialread()









