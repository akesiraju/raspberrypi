import socket
import time
import sys
from drive import move

TCP_IP = '192.168.2.18'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)

    conn, addr = s.accept()
    print('Connection address:', addr)
    end_time = time.time() + 300 * 1  # 1 minute
        
    while time.time() < end_time:   
        data = conn.recv(BUFFER_SIZE)
        if data:
            move(data)
            print("received data:", data)
        conn.send(data)  # echo
    conn.close()
except OSError as osErr:
    print(osErr)
except:
    print(sys.exc_info()[0])
else:
    conn.close()