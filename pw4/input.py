def get_input(stdscr, y, prompt):
    stdscr.addstr(y, 0, prompt)
    return stdscr.getstr().decode('utf-8')

def get_float_input(stdscr, y, prompt):
    return float(get_input(stdscr, y, prompt))
