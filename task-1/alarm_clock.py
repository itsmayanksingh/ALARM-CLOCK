#****************************************************** task-1 ******************************************#

from datetime import datetime
from playsound import playsound
import datetime

alarm_time = (input("Please enter the time in HH:MM:SS AM/PM: "))
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_second=alarm_time[6:8]
alarm_period=alarm_time[9:11]
print("setting up..")

while True:
    now = datetime.datetime.now()
    current_hour=now.strftime("%I")
    current_minute=now.strftime("%M")
    current_second=now.strftime("%S")
    current_period=now.strftime("%p")
    
    if(alarm_period==current_period):
        if(alarm_hour==current_hour):
            if(alarm_minute==current_minute):
                if(alarm_second==current_second):
                
                    print("uth jao malik")
                    playsound("twirling-intime-lenovo-k8-note-alarm-tone-41440.mp3")
                    break