import evdev
from evdev import ecodes
import requests

mike_url = "http://192.168.2.54:5002/"

sensitivityX = 50
sensitivityY = 50
signalX = -1
signalY = -1

mode = "test"  # prod or test


def signal(signal_code):
    if mode == "prod":
        res = requests.get(f"{mike_url}{signal_code}")
        print(res.status_code)
    elif mode == "test":
        print(signal_code)


xbox = evdev.InputDevice("/dev/input/event1")
print(xbox)

for event in xbox.read_loop():
    # print(evdev.categorize(event))
    if event.type != 0 and event.value != 0:
        print(event)

    # Key A Code 304 Type 1 Value 1
    # Key X Code 307 Type 1 Value 1
    # Key B Code 305 Type 1 Value 1
    # Key Y Code 308 Type 1 Value 1

    # Key RT Code 311 Type 1 Value 1
    # Key RZ Code 09 Type 03 Value 1023
    # Key LT Code 310 Type 1 Value 1
    # Key LZ Code 10 Type 03 Value 1023

    # Left Stick Y axis Code 00 Type 03 Value
    # Left Stick X axis Code 01 Type 03

    # print(f"{event.ev_type}={event.code}={event.state}")

    # if event.ev_type == "Absolute":
    #     if event.code == "ABS_Y":
    #         if event.state > 10000:
    #             signal(258)  # forward
    #         elif event.state < -10000:
    #             signal(259)  # reverse
    #     if event.code == "ABS_X":
    #         if event.state > 10000:
    #             signal(261)  # turn right
    #         elif event.state < -10000:
    #             signal(260)  # turn left
    #     if event.code == "ABS_RZ" and event.state == 255:
    #         signal(301)  # rotate right hand clockwise
    #     if event.code == "ABS_Z" and event.state == 255:
    #         signal(303)  # rotate left hand clockwise
    # if event.ev_type == "Key":
    #     if event.code == "BTN_TR" and event.state == 1:
    #         signal(302)  # rotate right hand anti clockwise
    #     if event.code == "BTN_TL" and event.state == 1:
    #         signal(304)  # rotate left hand anti clockwise
    #     if event.code == "BTN_EAST" and event.state == 1:  # Button B
    #         signal(32)  # stop
