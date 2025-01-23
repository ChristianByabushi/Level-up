import time
from datetime import datetime, timedelta
import sched 

def alarm_define(when_the_event_is_triggered, the_function, *args):
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(when_the_event_is_triggered,4,the_function,argument=args)
    # print(f"{the_function.__name__} () scheduled for  {time.localtime(when_the_event_is_triggered)}")
    s.run()


    

