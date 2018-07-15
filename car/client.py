import socket
import time
import keyboard

TCP_IP = '192.168.2.18'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

sock=''
prev_time = 0
prev_key=''

def gotinput(evt):

    global prev_time, prev_key
    diff = evt.time-prev_time
    
    print(diff)
    
    if prev_key != evt.name:
        #print(evt.scan_code)
        #print(evt.time)
        #print(evt.name)
        print('-----')    
        try:
            sock.send(bytearray(evt.name, "utf-8"))
        except ConnectionRefusedError as con:
            #print(con)
            print('-')
        except OSError as os:
            print('os')
    
    # save prev time
    prev_time = evt.time
    prev_key = evt.name
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, TCP_PORT))
except ConnectionRefusedError as con:
        print(con)

keyboard.hook(gotinput)
keyboard.wait('esc')

sock.close()
