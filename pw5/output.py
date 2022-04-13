from curses import wrapper


def main(stdscr):
    stdscr.clear()
    stdscr.refresh()
wrapper(main)