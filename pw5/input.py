import os

def get_input(stdscr, y, prompt, file_path):
    stdscr.clear()
    stdscr.addstr(y, 0, prompt)
    stdscr.refresh()
    input_data = stdscr.getstr().decode('utf-8')
    with open(file_path, 'a') as file:
        file.write(prompt + input_data + '\n')
    return input_data

def get_float_input(stdscr, y, prompt, file_path):
    return float(get_input(stdscr, y, prompt, file_path))