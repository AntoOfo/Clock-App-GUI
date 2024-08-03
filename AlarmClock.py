from playsound import playsound
from time import sleep
import threading
from datetime import datetime, timezone
import pytz

def stopwatch():
    global sw_user_input
    def check_stop():       # Function to check if user wants to stop the timer
                global sw_user_input
                while True:
                    stop_input = input()    # Wait for user input
                    if stop_input.strip().lower() == 's':
                        sw_user_input = 0
                        break
                    
    while True:
        try:                #   Try block to handle exceptions
            sw_minutes = 0
            sw_seconds = 0

            print("\nPress 1 for Stopwatch.\tPress 2 to exit.\tType 'S' to stop timer.")
            sw_user_input = int(input())

            stop_thread = threading.Thread(target=check_stop)   
            stop_thread.start()

            while sw_user_input == 1:           # Loop to start the timer
    
                if sw_seconds < 10 and sw_minutes < 10:    
                    print(f"0{sw_minutes}:0{sw_seconds}", end="\r") 
                    sleep(1)
                    sw_seconds = sw_seconds + 1
                    if sw_seconds > 59:
                        sw_minutes = sw_minutes + 1
                        sw_seconds = 0
                elif sw_seconds >= 10 and sw_minutes >= 10:
                     print(f"{sw_minutes}:{sw_seconds}", end="\r") 
                     sleep(1)
                     sw_seconds = sw_seconds + 1  
                     if sw_seconds > 59:
                        sw_minutes = sw_minutes + 1
                        sw_seconds = 0
                elif sw_seconds < 10 and sw_minutes >=10:
                       print(f"{sw_minutes}:0{sw_seconds}", end="\r") 
                       sleep(1)
                       sw_seconds = sw_seconds + 1
                       if sw_seconds > 59:
                        sw_minutes = sw_minutes + 1
                        sw_seconds = 0
                elif sw_seconds >= 10 and sw_minutes < 10: 
                      print(f"0{sw_minutes}:{sw_seconds}", end="\r")
                      sleep(1)
                      sw_seconds = sw_seconds + 1   
                      if sw_seconds > 59:
                        sw_minutes = sw_minutes + 1
                        sw_seconds = 0
                else:
                    print(f"0{sw_minutes}:{sw_seconds}", end="\r")
                    sleep(1)
                    sw_seconds = sw_seconds + 1   
                    if sw_seconds > 59:
                      sw_minutes = sw_minutes + 1
                      sw_seconds = 0    
            if sw_user_input == "s":
                print("Timer stopped.") 
                print()
                print(f"Minutes: {sw_minutes} Seconds: {sw_seconds}")
                return
            elif sw_user_input == 2:
                return
                
     
        except ValueError:
                print("Please choose between the given options..")
def timer():
    stop_timer = False
    
    def check_stop():       # Checks if user wants to stop the timer
        nonlocal stop_timer
        while True:
            stop_input = input().strip().lower() 
            if stop_input == "s":
                stop_timer = True
                break
            

    while True:
        try: 
            user_minutes = int(input("Enter minutes for timer: "))
            user_seconds = int(input("Enter seconds for timer: "))
            print("Enter 'S' to exit Timer")
    
            if user_minutes < 0 or user_seconds < 0:
                print("\nPlease enter a valid time.. \n")
                user_minutes = int(input("Enter minutes for timer: "))
                user_seconds = int(input("Enter seconds for timer: "))
                print("Enter 'S' to exit Timer")

            if user_seconds < 10:
                print(f"Minutes: {user_minutes}  Seconds: 0{user_seconds}")
            else:
                print(f"Minutes: {user_minutes}  Seconds: {user_seconds}")

            stop_thread = threading.Thread(target=check_stop)
            stop_thread.daemon = True   # Make sure the thread stops when the main program stops
            stop_thread.start()
            

            while user_seconds > 0 and user_minutes > -1:
                if stop_timer:
                    print("\nTimer stopped\n")
                    break
                user_seconds = user_seconds - 1
                sleep(1)
                print(f"{user_minutes}:0{user_seconds}" if user_seconds < 10 else f"{user_minutes}:{user_seconds}", end="\r")
                if user_seconds == 0 and user_minutes > 0:
                    user_seconds = user_seconds + 59
                    user_minutes = user_minutes - 1
                    print(f"Minutes: {user_minutes}  Seconds: {user_seconds}")
            
            if not stop_timer:
                print("Finished!") 
                playsound("C:/Users/anton/VSProjects/AlarmClock/AlarmClock/Alarm Clock Sound Effect (Animated).mp3")
            return
        
        except ValueError:
            print("Please enter a number for both minutes and seconds..")
def alarm():
    stop_alarm = False  

    def listen_for_stop():      # Listens for user input to stop the alarm
        nonlocal stop_alarm
        while True:
            stop_input = input()
            if stop_input.strip().lower() == 's':
                stop_alarm = True
                print("Exiting alarm..\n")
                break

    while True:
        try:
            user_input = input("Enter hour (or 'S' to stop): ").strip().lower()
            if user_input == 's':
                print("Exiting alarm..\n")
                return
            hour = int(user_input)

            user_input = input("Enter minute (or 'S' to stop): ").strip().lower()
            if user_input == 's':
                print("Exiting alarm..\n")
                return
            minutes = int(user_input)

            user_input = input("am / pm (or 'S' to stop): ").strip().lower()
            if user_input == 's':
                print("Exiting alarm..\n")
                return
            am_or_pm = user_input

            if am_or_pm not in ["am", "pm"]:
                print("\nPlease choose either 'am' or 'pm'..")
                continue

            # Convert hour to 24-hour format
            if am_or_pm == "pm":
                if hour != 12:  
                    hour += 12
            elif am_or_pm == "am":
                if hour == 12:  
                    hour = 0

            if hour > 23 or hour < 0:
                print("\nPlease enter a proper hour (0-23)..")
                continue
            elif minutes > 59 or minutes < 0:
                print("\nPlease enter proper minutes (0-59)..")
                continue

            hour_str = f"{hour:02}"  # Turns hour to two digits
            minutes_str = f"{minutes:02}"  # Turns minutes to two digits

            print(f"\nAlarm set for {hour_str}:{minutes_str}")

            # Starts the listener
            stop_thread = threading.Thread(target=listen_for_stop)
            stop_thread.daemon = True
            stop_thread.start()

            
            while not stop_alarm:
                current_time = datetime.now()
                if (hour == current_time.hour and minutes == current_time.minute):
                    print("\nRise and Shine!")
                    playsound("C:/Users/anton/VSProjects/AlarmClock/AlarmClock/Alarm Clock Sound Effect (Animated).mp3")
                    return
                sleep(30)

            if stop_alarm:
                return

        except ValueError:
            print("Invalid input. Please enter numbers for hour and minutes.")
        finally:
            stop_alarm = False  
def wordclock():
    country_list = []
    
    for timeZone in pytz.common_timezones:
        country_list.append(timeZone)
        
    while True:    
        userinput = input("\nEnter a Country's captital to see their time ('S' to exit): ").strip().lower()
    
        match = None    # Stores the match

        for tz in country_list:    # Iterates over the list of time zones to find a match
            if userinput in tz.lower():
                match = tz
                break
        
        if userinput == "S".lower():
            return
        
        if match:
            get_utc = datetime.now(timezone.utc)
            get_timezone = get_utc.astimezone(pytz.timezone(match))
            format_str = '%H:%M'
            time_country = get_timezone.strftime(format_str)
            print(f"The timezone for {userinput} is ")
            print(time_country)
        else:
            print(f"Timezone {userinput} not found.")

def main_menu():
    while True:
        print("Welcome to your Clock App!")
        print("Press 1 to Open the Timer")
        print("Press 2 to Open the Stopwatch")
        print("Press 3 to Open the Alarm")
        print("Press 4 to Open the World Clock")
        print("Press 5 to Exit")

        try:
            user_input = int(input("Choose an option: "))

            if user_input == 1:
                timer()
            elif user_input == 2:
                stopwatch()
            elif user_input == 3:
                alarm()
            elif user_input == 4:
                wordclock()
            elif user_input == 5:
                print("Exiting the app. Goodbye!")
                break
            else:
                print("Invalid option. Please choose 1, 2, 3 or 4.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":      # Runs the main_menu function
    main_menu()
    

        






  




















    
