# Return the distance to the block infront
# Libraries
from curses import wrapper
import RPi.GPIO as GPIO
import time
#import keyboard
import sys, tty
import threading

tty.setraw(sys.stdin.fileno())

prev_key=0
brakes = False
isturning = False
angle = 100
turningRadius=20
# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
# make right turn by deafault the first time
left = True

# ultra sonic controls, trigger and echo
trigger = 23
echo = 24

# servo motor data
servo = 18

# motor driver
input1 = 20
input2 = 16
enable1 = 21  # always disable after finishing and\or in catch

# set GPIO direction (IN / OUT)

# we send instructions to motor driver IC
GPIO.setup(input1, GPIO.OUT)
GPIO.setup(input2, GPIO.OUT)
# this will determine if signal should be sent to output pins
GPIO.setup(enable1, GPIO.OUT)

GPIO.setup(servo, GPIO.OUT)
pwm = GPIO.PWM(servo, 50)
pwm.start(0)

GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

def Log(msg):
    print(msg)
    #pass

def distance():
    GPIO.output(trigger, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigger, GPIO.LOW)
    startTime = time.time()
    stopTime = time.time()

    while GPIO.input(echo) == 0:
        startTime = time.time()

    while GPIO.input(echo) == 1:
        stopTime = time.time()

    elapsed = stopTime - startTime
    dist = (elapsed * 34300) / 2

    Log("distance = " + str(dist))

    return dist

def getDistance():
    while True:
            distance()
            time.sleep(1)

# Set servo motor angle
def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(servo, GPIO.HIGH)
    pwm.ChangeDutyCycle(duty)
    #time.sleep(1.0)
    GPIO.output(servo, GPIO.LOW)


# Turn the servomotor left


def TurnLeft():
    global isturning
    SetAngle(angle + turningRadius)
    isturning = True
    #time.sleep(3.0)
    #SetAngle(90)


# Turn the servo motor right


def TurnRight():
    global isturning
    SetAngle(angle - turningRadius)
    isturning = True
    #time.sleep(3.0)
    #SetAngle(90)


# Turn servo motor


def Turn():

    global left

    Log(left)

    if left == True:
        TurnRight()
        left = False
    else:
        TurnLeft()
        left = True


# drive forward
def  straight():
	global isturning

	if isturning == True:
		SetAngle(angle)
		isturning = False
	else:
		Log('no turning')

def back():
    

    straight()
    #Log('move start')

    GPIO.output(enable1, GPIO.HIGH)
    # if input1 and input2 are swapped a regular motor will go in reverse.
    GPIO.output(input1, GPIO.HIGH)
    # but lego will not as it has different pin for reverse. so we should disable this signal and enable that , creepy
    GPIO.output(input2, GPIO.LOW)

    # time.sleep(2)

    # GPIO.output(enable1, GPIO.LOW)


def front():
    #Log('move start')
    # if input1 and input2 are swapped we go in reverse.
	
    
    straight()
    GPIO.output(input1, GPIO.LOW)
    GPIO.output(input2, GPIO.HIGH)

    GPIO.output(enable1, GPIO.HIGH)

    # time.sleep(2)


    # GPIO.output(enable1, GPIO.LOW)
def clear():
    pwm.stop()
    GPIO.output(input1, GPIO.LOW)
    GPIO.output(enable1, GPIO.LOW)
    GPIO.cleanup()


def move(signal):
    global brakes

    if signal == 259:
        if brakes == True:
            GPIO.output(enable1, GPIO.HIGH)
            brakes = False
        front()

    if signal == 260:
        TurnLeft()

    if signal == 261:
        TurnRight()

    if signal == 258:
        back()

    if signal == 32:
        brakes = True
        GPIO.output(enable1, GPIO.LOW)

    if signal == 27:
        clear()
    
    return signal


def manual(stdscr):
    global prev_key
    stdscr.clear()

    t = threading.Thread(target = getDistance)
    t.daemon = True
    #t.start()

    end_time = time.time() + 300 * 5  #mins
    while time.time() < end_time:
        #time.sleep(0.01)
        v = stdscr.getch()
        
        if prev_key == v:
            pass
        else:
            prev_key = v
            Log(v)
            move(v)
            
        if v == 27:
            break

    
    stdscr.refresh()


def auto():
    front()

    end_time = time.time() + 30 * 1  # 60 is 1 minute
    while time.time() < end_time:

        Log('moving')        

        if distance() < 40:
            back()

        if distance() < 20:
            break

        if distance() > 200:
            front()

        time.sleep(0.5)

    clear()

turntime = 0.2
drivetime = 0.75

def square():
    end_time = time.time() + 30 * 1  # 60 is 1 minute
    while time.time() < end_time:
        front()
        time.sleep(drivetime)
        TurnRight()
        time.sleep(turntime)
        front()
        time.sleep(drivetime)
        TurnRight()
        time.sleep(turntime)
        front()
        time.sleep(drivetime)
        TurnRight()
        time.sleep(turntime)
        front()
        time.sleep(drivetime)
        TurnRight()
        time.sleep(turntime)
        break

    clear()

# if __name__ == "__main__":
    #wrapper(manual)
    #auto()
    #square()
