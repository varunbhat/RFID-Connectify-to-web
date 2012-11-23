#!/usr/bin/env python

####################################################################################
#Author:Varun Bhat
#Description: Get the data from the serial port and print 
#            it to an xml file and create an sqlite database 
#            that includes the id time and the text received from
#            Serial port itself
#Usage: python serialCommn.py -u <port address(default 0)> -b <baud rate(default 9600)> 
# email:varunbhat.kn@gmail.com
# This file is free to modify and use for any reason.Forgive me for not writing comments
# Note: for windows please change /dev/ttyusbX to COMX. it should work.
####################################################################################


import serial
from optparse import OptionParser
import thread
import time
#from Databasing import Databasing 


#//////////////////////////////////////////////////////
import sqlite3 as lite
class Databasing:
        
    def __init__(self,name,fields,type='a'):
        self.field = fields.keys()
        self.name = name.split('.')[0] 
        fieldType = fields.values()
        self.con = lite.connect(name)
        with self.con:
            cur = self.con.cursor()    
            if type=='w':
                cur.execute("DROP TABLE IF EXISTS "+self.name)
            command= "CREATE TABLE IF NOT EXISTS "+self.name+"(Id INTEGER PRIMARY KEY AUTOINCREMENT"
            for i in range(len(self.field)):
                command = command +','+ self.field[i] +" "+ fieldType[i]
            command = command + ')' 
            cur.execute(command)
#            print command

    def write(self,data):
        listx=[]
#        print data
        with self.con:
            cur = self.con.cursor()
#            print self.name
            cur.execute("SELECT * FROM "+self.name)
            rows = cur.fetchall()
#            print "i'm here",rows
#            for row in rows:
#                for i in range(len(self.field)):
#                    if data[self.field[i]] in row:
##                        print data[self.field[i]] , 'repeated'
#                        return 2
#                        break
            command = "INSERT INTO "+self.name+"("+self.field[0]
            listx.append(data[self.field[0]])
            for i in reversed(range(1,len(self.field))):
                command = command+','+self.field[i]
                listx.append(data[self.field[i]])
            command = command + ') VALUES (?'
            for i in range(1,len(self.field)):
                command = command + ',?'
            command = command + ')'
            cur.execute(command,listx)
            return 0

    def read(self):
        with self.con:
            cur = self.con.cursor()
            cur.execute("SELECT * FROM "+self.name)
            rows = cur.fetchall()
            for row in rows:
                print row  
                print "<br>"
            
    def update(self,field,update,otherField,constField):
        with self.con:
            cur = self.con.cursor()
            command = 'UPDATE '+self.name+' SET '+field+' = '+ update+' WHERE '+otherField +' = '+constField
            print command
            cur.execute(command)



#    def deleteDB(self):
#        con = lite.connect('Donor.db')
#        with con:    
#            cur = con.cursor()   
#            cur.execute("DROP TABLE IF EXISTS Donors")
#///////////////////////////////////////////////////////////////////////////////////////////////


#print time.time()
myvals = {'tag':"TEXT",'time':"TEXT"}
myDon = Databasing('rfid.db',myvals)
#
#PORT = 0
#BAUD = 9600
#
#rfid = serial.Serial('/dev/ttyUSB'+str(PORT), BAUD)
#
#x = rfid.readline()
#print x


#class myDef:
def exitThreadx():
    print "press e to exit"
    while 1:
        x=raw_input()
        if 'e' or 'E' in x:
            exit(0)
def getRfidString():
    
    while 1:
        text = rfid.read()
        if text == '':
            print text
            f = open('data.txt','a')
            f.write('<serial>')
            f.write('    <tag>'+str(text)+'</tag>\n')
            f.write('    <time>'+str(time)+'</time>\n')
            f.write('</serial>')
            f.close()
            
            myDon.write({'tag':text,'time':time.time()})
        


parser = OptionParser()
parser.add_option("-u", "--usbport", dest="usbport", default=0,
                    help="Add the usb device location ex:   ./serialCommn.py --usbport 1 [default: %default]")
parser.add_option("-b", "--baudrate", dest="baud", default=9600,
                    help="Baudrate of the device [default: %default]")

(options, args) = parser.parse_args()
PORT = int(options.usbport)
BAUD = int(options.baud)
#try:
#    rfid = serial.Serial('COM'+str(PORT), BAUD,timeout=1)
#    try:
#        thread.start_new_thread( getRfidString(), ("thread", 1, ) )
##        thread.start_new_thread( exitThreadx(), ("thread", 4, ) )
#    except:
#        print "Error: unable to start thread"
#except :
#    print "If using windows check if u connected the device or configured the device port properly"

try:
    rfid = serial.Serial('/dev/ttyUSB'+str(PORT), BAUD)
    try:
#        thread.start_new_thread( getRfidString(), ("thread", 1, ) )
#        thread.start_new_thread( exitThreadx(), ("thread", 4, ) )
        while 1:
            text = rfid.readline()
#            if text == '':
            print text
            f = open('data.txt','a')
            f.write('<serial>')
            f.write('    <tag>'+str(text)+'</tag>\n')
            f.write('    <time>'+str(time)+'</time>\n')
            f.write('</serial>')
            f.close()
            myDon.write({'tag':text,'time':time.ctime()})
    except:
        print "Error: unable to start thread"
except :
    print "If using linux check if u connected the device or configured the device port properly"
#        
#
#print "press e to exit:"
#inp = (raw_input())
#if inp == 'e' or 'E':
#    exit(0)
