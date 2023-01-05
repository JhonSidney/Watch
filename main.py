import os, time, datetime

class Watch:

    def __init__(self, hours=0,minutes=0,seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def  adjust_hours(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def printWatch(self):
        while(self.hours != 24):
            self.tick()
            print( "Current Time: {0:02d}:{1:02d}:{2:02d}".format(self.hours,self.minutes,self.seconds))
            time.sleep(1)
            os.system('cls')
            
    def tick(self):
        if self.seconds == 59:
            self.seconds = 0
            if self.minutes == 59:
                self.minutes = 0
                if self.hours == 23:
                    self.hours = 0
                else:
                    self.hours+=1
            else:
                self.minutes+=1
        else:
            self.seconds+=1

now = datetime.datetime.now()
rel = Watch(now.hour,now.minute,now.second)
rel.printWatch()
