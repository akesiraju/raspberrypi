import RPi.GPIO as GPIO
import lcd.lcddriver as lcddriver


#lcd = lcddriver.lcd()

#lcd.lcd_clear()

GPIO.setmode(GPIO.BCM)


#GPIO.setup([13,16,19,20,21,26], GPIO.OUT)
#GPIO.output([13,16,19,20,21,26], GPIO.LOW)
GPIO.cleanup()
