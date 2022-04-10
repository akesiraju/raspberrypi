from inputs import devices
from inputs import get_gamepad
import requests

mike_url = "http://192.168.2.54:5002/"

sensitivityX = 50
sensitivityY = 50
signalX = -1
signalY = -1

mode = "prod"  # prod or test


def signal(signal_code):
    if mode == "prod":
        res = requests.get(f"{mike_url}{signal_code}")
        print(res.status_code)
    elif mode == "test":
        print(signal_code)


def main():
    while 1:
        events = get_gamepad()
        for event in events:
            print(f"{event.ev_type}={event.code}={event.state}")

            if event.ev_type == "Absolute":
                if event.code == "ABS_Y":
                    if event.state > 10000:
                        signal(258)  # forward
                    elif event.state < -10000:
                        signal(259)  # reverse
                if event.code == "ABS_X":
                    if event.state > 10000:
                        signal(261)  # turn right
                    elif event.state < -10000:
                        signal(260)  # turn left
                if event.code == "ABS_RZ" and event.state == 255:
                    signal(301)  # rotate right hand clockwise
                if event.code == "ABS_Z" and event.state == 255:
                    signal(303)  # rotate left hand clockwise
            if event.ev_type == "Key":
                if event.code == "BTN_TR" and event.state == 1:
                    signal(302)  # rotate right hand anti clockwise
                if event.code == "BTN_TL" and event.state == 1:
                    signal(304)  # rotate left hand anti clockwise
                if event.code == "BTN_EAST" and event.state == 1:  # Button B
                    signal(32)  # stop


if __name__ == "__main__":
    main()
