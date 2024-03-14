import curses

def clear_screen(stdscr):
    stdscr.clear()
    stdscr.refresh()

def display_menu(stdscr, menu_items):
    clear_screen(stdscr)
    for i, item in enumerate(menu_items, start=2):
        stdscr.addstr(i, 0, item)
    stdscr.refresh()

def display_message(stdscr, y, message):
    stdscr.addstr(y, 0, message)
    stdscr.refresh()
