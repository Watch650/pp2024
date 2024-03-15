import curses

def get_input(stdscr, y, prompt):
    stdscr.clear()
    stdscr.addstr(y, 0, prompt)
    stdscr.refresh()
    curses.echo()
    input_data = stdscr.getstr().decode('utf-8')
    curses.noecho()
    return input_data

def get_float_input(stdscr, y, prompt):
    return float(get_input(stdscr, y, prompt))
