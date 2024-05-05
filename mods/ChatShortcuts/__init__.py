from keyboard import add_hotkey, write, send
from time     import sleep


CHAT_HOTKEY = 't'
HELLO_HOTKEY = 'ctrl+h'
HELLO_TEXT = 'gl&hf'
GOODBYE_HOTKEY = 'ctrl+g'
GOODBYE_TEXT = 'ggs'


def say_hello():
    send(CHAT_HOTKEY)
    write(HELLO_TEXT)
    send('enter')


def say_goodbye():
    send(CHAT_HOTKEY)
    write(GOODBYE_TEXT)
    send('enter')

def run():
    add_hotkey(HELLO_HOTKEY,   say_hello)
    add_hotkey(GOODBYE_HOTKEY, say_goodbye)

    try:
        while True: sleep(1)
    except KeyboardInterrupt: ...


if __name__ == '__main__': run()