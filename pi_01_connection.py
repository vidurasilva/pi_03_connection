import requests
url='https://bazura.000webhostapp.com'
payload={'id':'1','val':'test'}

#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import MySQLdb
from decimal import Decimal
GPIO.setmode(GPIO.BCM)

TRIG = 17
ECHO = 22

temp=0

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

checker=True
while (checker==True):


        GPIO.output(TRIG,False)

        time.sleep(5)

        GPIO.output(TRIG,True)
        time.sleep(0.00001)
        GPIO.output(TRIG,False)

        while GPIO.input (ECHO)==0:
                pulse_start = time.time()

        while GPIO.input (ECHO)==1:
                pulse_end = time.time()



        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration*17150
                                                          

        distance = round(distance,2)
        distance = distance*100/60
        distance = 100-distance
        passw=""

        a=int(float(distance))
        if distance < 100 and distance > 0:
                if distance< temp-5 or distance > temp+5:
                        try:
                                #con=MySQLdb.connect(host="127.0.0.1",port=3306,user="root",db="pitest")
                                #con=MySQLdb.connect(host="192.168.137.1",port=3306,user="test",passwd="test",db="pitest")
                                #curs=con.cursor()
                                #curs.execute ("UPDATE dusbins  SET fillPercentage=%s  WHERE dusid= 1 ",(distance))
                                #curs.execute("""SELECT * FROM tempdata""")
                                #con.commit()
				payload={'id':'1','val':(distance)}

			


				r=requests.get(url)
				r=requests.get(url,params=payload)
				r.text
				r.status_code




	
                                print "data Commited"
                        except Exception, e:
                                print "Error"
                                print str(e)
                                #con.rollback()
                        temp=distance


        print "Volume : ",distance, "%"

        #if distance>90:
                #checker=False
GPIO.cleanup()

