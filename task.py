import time
import datetime
from playsound import playsound

def set_alarm():
    alarm_time = input("Enter the alarm time in HH:MM format: ")
    return datetime.datetime.strptime(alarm_time, "%H:%M")

def main():
    print("Welcome to the Python Alarm Clock!")
    alarm = set_alarm()
    
    while True:
        now = datetime.datetime.now()
        if now.hour == alarm.hour and now.minute == alarm.minute:
            print("Wake up!")
            for _ in range(5):
                playsound("/usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga")
            break
        #time.sleep(30)

if __name__ == "__main__":
    main()
