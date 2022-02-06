import motor

forward_pin = 29
reverse_pin = 33
enable_pin = 23


def walk():
    motor.run(enable_pin, forward_pin, reverse_pin)


def reverse():
    motor.run(enable_pin, reverse_pin, forward_pin)


def stop():
    motor.stop(enable_pin)
