import fcntl, termios, struct
import time

def terminal_size():
    th, tw, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return tw, th

WIDTH, HEIGHT = terminal_size()
SCROLL_SPEED = 4 # lines per second

def line(char):
    print(char*WIDTH)

def side(char):
    print(char, end='')
    print(' ' * (WIDTH-2), end='')
    print(char)

def innerText(text, char):
    print(char, end='')
    print(text.center(WIDTH-2), end='')
    print(char)

def vSpace(n):
    for i in range(n):
        print()

def scroll(seconds):
    for i in range(seconds):
        print()
        time.sleep(1/SCROLL_SPEED)

def textBox(text, char):
    line(char)
    side(char)
    innerText(text, char)
    side(char)
    line(char)

def opening():
    scroll(3)
    textBox('Wilkommen in QuizzyGillespie!', '*')
    scroll(3)
