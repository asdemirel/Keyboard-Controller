from pynput.keyboard import Key,Listener
import datetime
import threading
import sys

class DriveKeyboard:
    def __init__(self):
        self.throttle = 0
        self.brake = 0
        self.right= 0
        self.left= 0
        self.handbrake= 0
        threading.Thread(target=self.write_out).start()
        threading.Thread(target=self.run).start()
        
    def on_press(self,key):
        key = str(key).replace("'","")
        with open('DrivelessCommandLogger.txt','a') as file:
            if key == "w":
                file.write(key)
                self.throttle+=1
            elif key == "s":
                file.write(key)
                self.throttle -=1
            elif key == "d":
                file.write(key)
                self.right +=1
            elif key == "a":
                file.write(key)
                self.left +=1

    def write_out(self):
        while True:
            print("THROTTLE = ",self.throttle,
                "LEFT =", self.left, 
                "RİGHT =", self.right
                 )
            #sys.stdout.write("\43[F")
            
                 
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
    DriveKeyboard()
