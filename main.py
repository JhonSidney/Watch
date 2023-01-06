import  watchAndCalendar

date = watchAndCalendar.WatchCalendar(23,59,40,31,12,2022,)
while(True):
    print(date.toString())
    date.tick_watchCalendar()
