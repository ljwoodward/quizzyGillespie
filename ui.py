import fcntl, termios, struct
import time

def terminal_size():
    th, tw, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return tw, th

WIDTH, HEIGHT = terminal_size()
SCROLL_SPEED = 6 # lines per second

def line(char):
    return char*WIDTH

def side(char):
    t = char
    t += ' ' * (WIDTH-2)
    t += char
    return t

def innerText(text, char):
    t = char
    t += text.center(WIDTH-2)
    t += char
    return t

def vSpace(n):
    t = ''
    for i in range(n):
        t += '\n'
    return t

def scroll(text):
    spl = text.split('\n')
    for i in spl:
        print(i)
        time.sleep(1/SCROLL_SPEED)

def textBox(text, char):
    return '\n'.join([line(char), side(char), innerText(text, char), side(char), line(char)])

def opening():
    txt = vSpace(3) + textBox('Wilkommen in QuizzyGillespie!', '*') + vSpace(3)
    scroll(txt)
