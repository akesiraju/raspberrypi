import RPi.GPIO as GPIO  # Import GPIO library
import time  # Import time library

# Clockwise increases sensitivity

GPIO.setmode(GPIO.BCM)

# this is where motion sensor is connected
pir = 21

# this is where led is connected to tell us about motion
light = 20

# motion sensor is input
GPIO.setup(pir, GPIO.IN)

# led is output
# GPIO.setup(light, GPIO.OUT)

print("Waiting for sensor to settle")
time.sleep(2)
print("Detecting motion")

# We light up on 20 if there is movement
try:
    while True:
        if GPIO.input(pir):
            print("movement")
            # #GPIO.output(light, GPIO.HIGH)

            # for i in range(1,10):
            #     GPIO.output(light, GPIO.HIGH)
            #     time.sleep(0.1)
            #     GPIO.output(light, GPIO.LOW)
            #     time.sleep(0.1)

            # #time.sleep(2)
        else:
            print("no movement")
        time.sleep(1)
except KeyboardInterrupt:
    print("keyboard interrupt")
    GPIO.cleanup()
    exit()
