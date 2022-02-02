import RPi.GPIO as GPIO
import time

left_hand = [7,11,13,15]
right_hand = [12,16,18,22]
head = [32,36,38,40]

def rotate(control_pins):

  GPIO.setmode(GPIO.BOARD)

  for pin in control_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
    
    halfstep_seq = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]
  ]

  for i in range(512):
    for halfstep in range(8):
      for pin in range(4):
        GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
      time.sleep(0.001)

  GPIO.cleanup()


# rotate(left_hand)
# rotate(right_hand)
rotate(head)
