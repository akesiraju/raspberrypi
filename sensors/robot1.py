#This will blink when there is movement.
#This will also turn away when there is movement until there is no movement
#THis should say hello  (sound) when there is movement
#This should display hello (lcd) when there is movement

import RPi.GPIO as GPIO                           #Import GPIO library
import time                                       #Import time library
import lcd.lcddriver as lcddriver
import sys

lcd =  lcddriver.lcd()

#Clockwise increases sensitivity

GPIO.setmode(GPIO.BCM)

#this is where motion sensor is connected
pir = 21

#this is where led is connected to tell us about motion
light = 20

#motion sensor is input
GPIO.setup(pir, GPIO.IN)

#led is output
GPIO.setup(light, GPIO.OUT)

print("Waiting for sensor to settle")
time.sleep(2)
print("Detecting motion")



#We light up on 20 if there is movement
while True:
    if GPIO.input(pir):
        print('movement')
        #GPIO.output(light, GPIO.HIGH)
	lcd.lcd_display_string('Hello there',1)
        #for i in range(1,2):
        GPIO.output(light, GPIO.HIGH)
         #   time.sleep(0.1)
          #  GPIO.output(light, GPIO.LOW)
          #  time.sleep(0.1)

        #time.sleep()
    else:
	lcd.lcd_display_string('Good bye',1)
        print("no movement")
        GPIO.output(light, GPIO.LOW)
    time.sleep(1)

lcd.lcd_clear()
GPIO.cleanup()
