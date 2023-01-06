import os, time
class Watch:

    def __init__(self, hour,minutes,seconds, *args, **kwargs):
        super(Watch,self).__init__(*args,**kwargs)
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds

    def  adjust_hour(self,hour,minutes,seconds):
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds
    
    def printWatch(self):
        return " {0:02d}:{1:02d}:{2:02d} ".format(self.hour,self.minutes,self.seconds)   
            
    def tick_watch(self):
        if self.seconds == 59:
            self.seconds = 0
            if self.minutes == 59:
                self.minutes = 0
                if self.hour == 23:
                    self.hour = 0
                else:
                    self.hour+=1
            else:
                self.minutes+=1
        else:
            self.seconds+=1


class Calendar:
    lim_months = (31,28,31,30,31,30,31,31,30,31,30,31)

    def __init__(self,day, month, year, *args, **kwargs):
        super(Calendar,self).__init__(*args, **kwargs)
        self.day = day
        self.month = month
        self.year = year
    
    def adjust_calendar(self,day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    def printCalendar(self):
        return " {0:02d}/{1:02d}/{2:4d} ".format(self.day,self.month,self.year)
    
    def next_day(self):
        maxDay = Calendar.lim_months[self.month - 1]

        if self.day == maxDay:
            if self.month == 12:
                self.month = 1
                self.year+=1
            else:
                self.month+=1
            self.day = 1
        else:
            self.day+=1

class WatchCalendar(Watch,Calendar):
    def __init__(self, hour, minutes, seconds, day, month, year):
        super(WatchCalendar,self).__init__(hour=hour, minutes=minutes, seconds=seconds, day=day, month=month, year=year)

    def tick_watchCalendar(self):
        hora_anterior = self.hour
        Watch.tick_watch(self)
        if (self.hour < hora_anterior):
            self.next_day()

    def toString(self):
        time.sleep(0.5)
        os.system('cls')
        return "{}|{}".format(Watch.printWatch(self),Calendar.printCalendar(self))
