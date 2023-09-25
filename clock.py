from datetime import datetime 
import time
import os
import curses

# Initialize curses
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(True)
curses.noecho()

# Clear the screen
os.system('clear')

while True:
    try:
        d = datetime.now()
        clock = d.strftime("%H:%M:%S")
        day = d.strftime('%A')
        date = d.strftime('%d')
        year = d.strftime('%Y')
        month = d.strftime('%B')
        
        date_syntax = ['st', 'nd', 'rd', 'th']
        suffix = date_syntax[min(int(date) % 10 - 1, 3)]
        
        tabs_ = ''
        stdscr.clear()
        stdscr.addstr(0, 0, clock)
        stdscr.refresh()
        
        key = stdscr.getch()  # Read keyboard input
        if key == ord('q'):
            break
        elif key == ord('c'):
            with open('log.txt', 'a') as f:
                f.write(f"{clock}, {day} {date}{suffix} {month} {year}\n")
    except KeyboardInterrupt:
        break

# Cleanup curses
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
