from car import Car
import threading
import time
from curses import wrapper

import sys, tty

def manual():
    tty.setraw(sys.stdin.fileno())
    stdscr.clear()

    my_car = Car()
    

    t = threading.Thread(target = my_car.getDistance())
    t.daemon = True
    prev_key = ''
    #t.start()

    end_time = time.time() + 300 * 5  #mins
    while time.time() < end_time:
        #time.sleep(0.01)
        v = stdscr.getch()
        
        if prev_key == v:
            pass
        else:
            prev_key = v
            my_car.move(v)
            
        if v == 27:
            break

    
    stdscr.refresh()


if __name__ == "__main__":
    wrapper(manual)