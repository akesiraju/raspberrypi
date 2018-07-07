import RPi.GPIO as GPIO
import time

pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
pwm = GPIO.PWM(pin, 50)
pwm.start(0)

time.sleep(5)

def TurnLeft():
    SetAngle(70)
    time.sleep(2.0)
    SetAngle(90)

def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1.0)
    GPIO.output(pin, False)

if __name__ == '__main__':
    #for x in [90, 135,180,135,90,45,0, 45, 80]:
    for x in [100,80,100,120,100]:
        SetAngle(x)

    pwm.stop()
    GPIO.cleanup()
