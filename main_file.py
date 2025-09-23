from ifood_class import Ielio
from alicia_class import Alicia
import sys
import keyboard
import time
from threading import Thread

def quit_check(ali):
    while True:
        time.sleep(5)
        if ali.quit():
            ali.reproduzir_audio("Encerrando")
            sys.exit()
            break

keyboard.wait("f10")

ali = Alicia()
t = Thread(target=quit_check,args=(ali,))
t.start()

ifood = Ielio("ifoood061@gmail.com")
# ifood.initialize_ifood()
