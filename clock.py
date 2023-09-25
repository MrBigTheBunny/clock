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
        date_syntax = ['st ','nd ','rd ','th ']
        while len(date) >= 1:
            if int(date[1]) >= 4:
                i = 3
                break
            else:
                if int(date[1]) == 1:
                    i = 0
                    break
                elif int(date[1]) ==2:
                    i = 1
                    break
                elif int(date[1]) == 3:
                    i = 2
                    break
        tabs_ = ''
        stdscr.clear()
        stdscr.addstr(0, 0, clock)
        stdscr.refresh()
        
        key = stdscr.getch()  # Read keyboard input
        if key == ord('q'):
            break
        elif key == ord('c'):
            with open('log.txt', 'a') as f:
                f.write(f"{clock}, {day} {date}{date_syntax[i]} {month} {year}\n")
    except KeyboardInterrupt:
        break
    time.sleep(1)
# Cleanup curses
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
