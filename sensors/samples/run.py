#Libraries
import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
left=True
trigger=23
echo=24

servo = 18

input1 = 20
input2 = 16
enable1 = 21

#set GPIO direction (IN / OUT)

GPIO.setup(input1, GPIO.OUT)
GPIO.setup(input2, GPIO.OUT)
GPIO.setup(enable1, GPIO.OUT)

GPIO.setup(servo, GPIO.OUT)
pwm=GPIO.PWM(servo, 50)
pwm.start(0)

GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

def distance():
    GPIO.output(trigger, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigger, GPIO.LOW)
    startTime = time.time()
    stopTime = time.time()

    while GPIO.input(echo) ==0:
        startTime = time.time()

    while GPIO.input(echo)==1:
        stopTime = time.time()

    elapsed = stopTime-startTime
    dist = (elapsed*34300)/2
    
    print('%.1f', dist)
    
    return dist


def SetAngle(angle):
    duty=angle/18+2
    GPIO.output(servo, GPIO.HIGH)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1.0)
    GPIO.output(servo, GPIO.LOW)



def TurnLeft():
    SetAngle(60)
    time.sleep(3.0)
    SetAngle(90)

def TurnRight():
    SetAngle(120)
    time.sleep(3.0)
    SetAngle(90)

def Turn():
    
    global left

    print(left)
    
    if left == True:
        TurnRight()
        left = False
    else:
        TurnLeft()
        left = True

def front():
	print('move start')

	GPIO.output(enable1, GPIO.HIGH)
	GPIO.output(input1, GPIO.HIGH)
	GPIO.output(input2, GPIO.LOW)

	#time.sleep(2)

	#GPIO.output(enable1, GPIO.LOW)
	

if __name__ == '__main__':
    try:

        front()
	
        end_time = time.time() + 5 * 1 # 1 minute
        while time.time() < end_time:
     
            print('moving')

            if distance() < 100:
                Turn()

            if distance() < 20:
                break

            time.sleep(1)
	
        pwm.stop()
        GPIO.output(input1, GPIO.LOW)
        GPIO.output(enable1, GPIO.LOW)
        GPIO.cleanup()
     
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

