import left_leg, right_leg, left_hand, right_hand, head
import time


def shake_right_hand():
    right_hand.lift_up()
    time.sleep(2)
    right_hand.lift_down()


def shake_left_hand():
    left_hand.lift_up()
    time.sleep(2)
    left_hand.lift_down()


def turn_left():
    left_leg.stop()
    right_leg.walk()


def turn_right():
    right_leg.stop()
    left_leg.walk()


def walk_forward():
    left_leg.walk()
    right_leg.walk()


def walk_backward():
    left_leg.reverse()
    right_leg.reverse()


def stop_walk():
    left_leg.stop()
    right_leg.stop()
