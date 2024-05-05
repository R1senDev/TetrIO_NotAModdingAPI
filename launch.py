from threading import Thread
from getpass   import getuser
from os        import startfile, listdir


TIO_PATH = f'C:/Users/{getuser()}/AppData/Local/Programs/tetrio-desktop/TETR.IO.exe'

threads = []


try: startfile(TIO_PATH)
except FileNotFoundError:
    input('Seems like TETR.IO is not installed. Press [ENTER] to exit. ')
    exit()


for mod in listdir('mods/'):

    if mod.startswith('__'): continue

    def thr(mod):
        print(f'{mod}: starting')
        exec(f'from mods.{mod.rstrip(".py")} import run; run()')
        print(f'{mod}: done')

    threads.append(Thread(
        target = thr,
        args   = (mod,),
        daemon = True,
        name   = mod
    ))


for thread in threads:
    thread.start()
for thread in threads:
    thread.join()