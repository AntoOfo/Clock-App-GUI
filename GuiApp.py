from tkinter import *
from playsound import playsound
from time import sleep

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
    
    # Create and display the timer label
    timer_label = Label(timer_window,
                        text="00:00",
                        font=("Arial", 25, "bold"))
    timer_label.pack(pady=30)

    timer_window.mainloop()



def main():
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
                              text="Stopwatch",
                              font=("Arial",15,"bold"))
    stopwatch_button.pack()

    alarm_button = Button(menu_window,
                          text="Alarm",
                          font=("Arial",15,"bold"))
    alarm_button.pack(pady=70)

    world_button = Button(menu_window,
                          text="World Clock",
                          font=("Arial",15,"bold"))
    world_button.pack(pady=0.3)
    menu_window.mainloop()   # puts window on screen and listens for events
    
main()