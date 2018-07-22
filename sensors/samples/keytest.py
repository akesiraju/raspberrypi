import keyboard

print('hello')

while True:
    if keyboard.is_pressed('up'):
        print('up')
    if keyboard.is_pressed('down'):
        print('down')
        break
