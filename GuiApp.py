from tkinter import *
from playsound import playsound
from time import sleep
from datetime import datetime

def timersubmit():
    # global to access variables outside the function
    global user_minutes, user_seconds, timer_running, timer_label     

    user_minutes = int(minutes_entry.get())
    user_seconds = int(seconds_entry.get())
    timer_running = True  # set to true when timer starts
    
    update_timer()     

def update_timer():
    global user_minutes, user_seconds, timer_running

    if not timer_running:
        return

    if user_seconds == 0 and user_minutes == 0:
        timer_label.config(text="Time's Up!")
        playsound("C:/Users/anton/VSProjects/AlarmClock/AlarmClock/Alarm Clock Sound Effect (Animated).mp3")
        timer_running = False
        return

    if user_seconds == 0:
        user_seconds = 59
        user_minutes = user_minutes - 1
    else:
        user_seconds = user_seconds - 1

    timer_text = f"{user_minutes:02}:{user_seconds:02}" # new format where pads w zeros if needed
    timer_label.config(text=timer_text)

    # schedules next update after 1 sec
    timer_window.after(1000, update_timer)     

def timerwindow():
    global minutes_entry, seconds_entry, timer_window, timer_label

    timer_window = Tk()     # instance of timer window
    timer_window.geometry("540x540")
    timer_window.title("Timer")

    timer_window.config(background="#9E9E9E")

    timerlabel = Label(timer_window,
                       text="TIMER",
                       font=("Arial", 40, "bold"),
                       bg="#9E9E9E",
                       relief=SUNKEN,
                       padx=5,
                       pady=5)
    timerlabel.pack(pady=20)

    minutes_entry = Entry(timer_window)
    minutes_entry.config(font=("Arial", 10), width=5)
    minutes_entry.pack()

    seconds_entry = Entry(timer_window)
    seconds_entry.config(font=("Arial", 10), width=5)
    seconds_entry.pack(pady=30)

    submittimer = Button(timer_window,
                         text="Submit",
                         font=("Arial", 10, "bold"),
                         command=timersubmit)
    submittimer.pack(pady=30)
    
    backbutton = Button(timer_window,
                        text="Back",
                        font=("Arial",10,"bold"),
                        command=open_main_menu)
    backbutton.pack(pady= 20)
    
   
    timer_label = Label(timer_window,
                        text="00:00",
                        font=("Arial", 25, "bold"))
    timer_label.pack(pady=30)

    timer_window.mainloop()

def update_stopwatch():
    global sw_minutes, sw_seconds
    
    sw_seconds = sw_seconds + 1
    if sw_seconds > 59:
        sw_seconds = 0
        sw_minutes = sw_minutes + 1
            
    sw_text = f"{sw_minutes:02}:{sw_seconds:02}"
    sw_label.config(text=sw_text)
    sw_window.after(1000, update_stopwatch)
    
    
def stopwatchwindow():
    global start_button, sw_label, sw_window, sw_seconds, sw_minutes
    
    sw_minutes = 0
    sw_seconds = 0
    sw_window = Tk()
    sw_window.geometry("540x540")
    sw_window.title("Stopwatch")
    sw_window.config(background="#9E9E9E")
    sw_header = Label(sw_window,
                      text="Stopwatch",
                      font=("Arial",40,"bold"),
                      bg="#9E9E9E")
    sw_header.pack()
    
    start_button = Button(sw_window,
                          text="Start",
                          font=("Arial",15,"bold"),
                          command=update_stopwatch)
    start_button.pack(pady=30)
    
    back_button = Button(sw_window,
                         text="Back",
                         font=("Arial",15,"bold"),
                         command=open_main_menu)
    back_button.pack(pady=20)
    
    sw_label = Label(sw_window,
                     text="0:00",
                     font=("Arial",40,"bold"),
                     bg="#9E9E9E")
    sw_label.pack(pady=20)
    
    sw_window.mainloop()

def open_main_menu():
    menu_window.deiconify()
  
def alarmsubmit():
    global alarm_user_hours, alarm_user_mins, alarm_running

    try:
        alarm_user_hours = int(alarm_hour_entry.get())
        alarm_user_mins = int(alarm_mins_entry.get())

        # coverts 12hr format to 24hr
        if (x.get()==0) and alarm_user_hours != 12:
            alarm_user_hours += 12
        elif (x.get()==1) and alarm_user_hours == 12:
            alarm_user_hours = 0

        #case
        if not (0 <= alarm_user_hours < 24) or not (0 <= alarm_user_mins < 60):
            alarm_label.config(text="Invalid time")
            return

        alarm_running = True
        alarm_label.config(text=f"Alarm set for {alarm_user_hours:02}:{alarm_user_mins:02}")
        update_alarm()
        
    except ValueError:
        alarm_label.config(text="Invalid input")
    
def update_alarm():
    global alarm_user_hours, alarm_user_mins, alarm_running

    if not alarm_running:
        return

    current_time = datetime.now()
    current_hours = current_time.hour
    current_minutes = current_time.minute
    current_seconds = current_time.second   # debugging sake

    #debugging purpose
    print(f"Current Time: {current_hours:02}:{current_minutes:02}:{current_seconds:02}")
    print(f"Alarm Time: {alarm_user_hours:02}:{alarm_user_mins:02}")

    if alarm_user_hours == current_hours and alarm_user_mins == current_minutes:
        alarm_label.config(text="Rise and Shine!")
        try:
            playsound("C:/Users/anton/VSProjects/AlarmClock/AlarmClock/Alarm Clock Sound Effect (Animated).mp3")
        except Exception as e:
            print(f"Error playing sound: {e}")
        alarm_running = False
        return

    # checks every second
    alarm_label.after(1000, update_alarm)
    

def alarm_window():
    global alarm_hour_entry, alarm_mins_entry, x, alarm_label
    alarm_window = Tk()
    alarm_window.geometry("540x540")
    alarm_window.title("Alarm")
    
    alarm_window.config(background="#9E9E9E")
    
    alarm_header = Label(alarm_window,
                         text="ALARM",
                         font=("Arial",40,"bold"),
                         bg="#9E9E9E")
    alarm_header.pack()
    
    alarm_hour_entry = Entry(alarm_window)
    alarm_hour_entry.config(font=("Arial", 10), width=5)
    alarm_hour_entry.pack(pady=20)
    
    alarm_mins_entry = Entry(alarm_window)
    alarm_mins_entry.config(font=("Arial", 10), width = 5)
    alarm_mins_entry.pack(pady=25)
    
    ampm_list = ["AM","PM"]
    x = IntVar()        # variable of am and pm
    for index in range(len(ampm_list)):
        ampm_radio = Radiobutton(alarm_window,
                                 text=ampm_list[index],
                                 variable=x,    # groups buttons 
                                 value=index,    #gives each button diff values
                                 font=("Arial", 10))
        ampm_radio.pack()
    
    submitalarm = Button(alarm_window,
                         text="Submit",
                         font=("Arial", 10, "bold"),
                         command=alarmsubmit)
    submitalarm.pack(pady=30)
    
    alarm_label = Label(alarm_window,
                        text="00:00",
                        font=("Arial",25,"bold"))
    alarm_label.pack(pady=30)

    alarm_window.mainloop()

def worldclock_window():
   world_window = Tk()
   world_window.geometry("540x540")
   world_window.title("World Clock")
   
   

   world_window.mainloop()

    
def main():
    global menu_window
    menu_window = Tk()      # instance of window
    menu_window.geometry("540x540")
    menu_window.title("Clock App")

    icon = PhotoImage(file="Clock.png") # Turns png to photoimage
    menu_window.iconphoto(True, icon)
    menu_window.config(background="#9E9E9E")

    label = Label(menu_window,      # title
                  text="CLOCK", 
                  font=("Arial",40,"bold"), 
                  bg="#9E9E9E",
                  relief=SUNKEN,
                  padx=5,
                  pady=5)
    label.pack()    # places label to top center

    timer_button = Button(menu_window,
                          command=timerwindow,  # opens timer window
                          text="Timer",
                          font=("Arial",15,"bold"))
    timer_button.pack(pady=80)

    stopwatch_button = Button(menu_window,
                              command=stopwatchwindow,
                              text="Stopwatch",
                              font=("Arial",15,"bold"))
    stopwatch_button.pack()

    alarm_button = Button(menu_window,
                          text="Alarm",
                          font=("Arial",15,"bold"),
                          command=alarm_window)
    alarm_button.pack(pady=70)

    world_button = Button(menu_window,
                          text="World Clock",
                          font=("Arial",15,"bold"),
                          command=worldclock_window)
    world_button.pack(pady=0.3)
    menu_window.mainloop()   # puts window on screen and listens for events
    
main()