#Libraries
import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

input1 = 20
input2 = 16
enable1 = 21

input3=13
input4=19
enable2 = 26

#set GPIO direction (IN / OUT)
GPIO.setup(input1, GPIO.OUT)
GPIO.setup(input2, GPIO.OUT)
GPIO.setup(enable1, GPIO.OUT)

GPIO.setup(input3, GPIO.OUT)
GPIO.setup(input4, GPIO.OUT)
GPIO.setup(enable2, GPIO.OUT)

def front():
	print('move start')

	GPIO.output(enable1, GPIO.HIGH)
	GPIO.output(input1, GPIO.HIGH)
	GPIO.output(input2, GPIO.LOW)

	time.sleep(2)

	GPIO.output(enable1, GPIO.LOW)
	

def back():
    print('moving back')

    GPIO.output(enable1, GPIO.HIGH)
    GPIO.output(input1, GPIO.LOW)
    GPIO.output(input2, GPIO.HIGH)

    time.sleep(2)

    GPIO.output(enable1, GPIO.LOW)


if __name__ == '__main__':
    try:
        front()
        back()     
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

