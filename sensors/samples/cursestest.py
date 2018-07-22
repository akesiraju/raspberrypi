from curses import wrapper

def main(stdscr):
      # Clear screen
    stdscr.clear()
    # This raises ZeroDivisionError when i == 10.
    i=0
    while i<10:
       print(stdscr.getch())
       i=i+1

    
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
