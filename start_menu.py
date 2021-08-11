import curses

def start_menu():
    stdscr = curses.initscr()
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLUE)
    titlePadX = curses.COLS//4
    titlePadY = curses.LINES//5
    midY = curses.LINES//2
    midX = curses.COLS//2
    options = ['Start', 'Tutorial', 'Load Custom', 'Quit']
    highlight = 0

    jjamm =[[1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1],
            [0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
            [0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
            [0,0,1,0,0,0,0,0,1,0,0,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1],
            [1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1],
            [1,1,1,0,0,0,1,1,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1]]

    pad = curses.newpad(curses.LINES-1, curses.COLS-1)
    title = curses.newpad(titlePadY, titlePadX)
    title.nodelay(False)
    pad.nodelay(True)
    pad.box()
    pad.keypad(True)

    for i in range(len(jjamm)):
        for j in range(len(jjamm[i])):
            if(jjamm[i][j]):
                pad.addch(i+2, j+2, 'T', curses.color_pair(1))

    choice = ' ' 
    while choice != 'Quit':
        for i in range(len(options)):
            if i == highlight:
                pad.attron(curses.A_REVERSE)
            pad.addstr(i+midY, midX, options[i])
            pad.attroff(curses.A_REVERSE)

        cursor = pad.getch()
        if cursor == curses.KEY_UP and highlight > 0:
            highlight -= 1
        elif cursor == curses.KEY_DOWN and highlight < len(options):
            highlight += 1
        elif cursor == curses.KEY_ENTER:
            curses.endwin()
            return options[highlight]
        pad.refresh(0,0,0,0,curses.LINES-1,curses.COLS-1)

