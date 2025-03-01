def main():
    now = int(input("What is the User time now: "))
    alarm_hours = int(input("please enter the alarm wait hours: "))
    
    print(f"Current Time: {now:02}")
    alarm_time = now + alarm_hours
    
    if (alarm_time > 23):
        alarm_time = alarm_time % 24
    
    print(f"Alarm Time: {alarm_time:02}")
    
    

if __name__ == '__main__':
    main()