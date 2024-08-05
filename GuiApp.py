from tkinter import *
from playsound import playsound
from time import sleep
from datetime import datetime, timezone
import pytz
from PIL import Image, ImageTk

photo = None

def timersubmit():
    # global to access variables outside the function
    global user_minutes, user_seconds, timer_running, timer_label     
    try:
        user_minutes = int(minutes_entry.get())
        user_seconds = int(seconds_entry.get())
        timer_running = True  # set to true when timer starts
    
        update_timer()   
    except ValueError:
        timer_label.config(text="Invalid Input")

def update_timer():
    global user_minutes, user_seconds, timer_running
    
    if not timer_running:
        return
    if not (0<= user_minutes) or not (0 <= user_seconds <= 59):
        timer_label.config(text="Invalid input")
        return
    
    
    if user_seconds == 0 and user_minutes == 0:
        timer_label.config(text="Time's Up!",
                           fg="Red",
                           font=("Arial",30))
        timer_label.place(x=165,y=390)
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
    global minutes_entry, seconds_entry, timer_window, timer_label, photo

    timer_window = Toplevel()     # instance of timer window
    timer_window.geometry("540x540")
    timer_window.resizable(False, False)
    timer_window.title("Timer")

    timer_window.config(background="#333333")


    timerlabel = Label(timer_window,
                       image=photo,
                       text="Timer",
                       font=("Arial", 50),
                       bg="#333333",
                       relief=FLAT,
                       compound='center',
                       foreground="White"
                       )
    timerlabel.place(x=95,y=25)
    
    minutes_entry = Entry(timer_window)
    minutes_entry.config(font=("Arial", 10), width=5)
    minutes_entry.place(x=280,y=210)
    
    minutes_text = Label(timer_window,
                         text="Minutes:",
                         font=("Arial",15),
                         bg="#333333",
                         relief=FLAT,
                         foreground="White")
    minutes_text.place(x=180,y=203)
   
    
    seconds_entry = Entry(timer_window)
    seconds_entry.config(font=("Arial", 10), width=5)
    seconds_entry.place(x=280,y=270)
    
    seconds_text = Label(timer_window,
                         text="Seconds:",
                         font=("Arial",15),
                         bg="#333333",
                         relief=FLAT,
                         foreground="White")
    seconds_text.place(x=172,y=263)
    
    
    submittimer = Button(timer_window,
                         text="Submit",
                         font=("Arial", 10),
                         width=10,
                         command=timersubmit)
    submittimer.place(x=140,y=320)
    
    
    backbutton = Button(timer_window,
                        text="Back",
                        font=("Arial",10),
                        width=10,
                        command=lambda: open_main_menu(timer_window))
    backbutton.place(x=300, y=320)
    
    
    timer_label = Label(timer_window,
                        text="00:00",
                        font=("Arial", 45, "bold"),
                        bg="#333333",
                        fg="White")
    timer_label.place(x=184, y=390)
    
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
    global start_button, sw_label, sw_window, sw_seconds, sw_minutes, photo
    
    sw_minutes = 0
    sw_seconds = 0
    sw_window = Toplevel()
    sw_window.geometry("540x540")
    sw_window.resizable(False, False)
    

    sw_window.title("Stopwatch")
    sw_window.config(background="#333333")
    

    sw_header = Label(sw_window,
                      image=photo,
                      text="Stopwatch",
                      font=("Arial",45),
                      relief=FLAT,
                      bg="#333333",
                      compound='center',
                      fg="White")
    sw_header.place(x=95,y=25)
    
    start_button = Button(sw_window,
                          text="Start",
                          font=("Arial",10),
                          width=10,
                          command=update_stopwatch)
    start_button.place(x=110,y=360)
    
    back_button = Button(sw_window,
                         text="Back",
                         font=("Arial",10),
                         width=10,
                         command=lambda: open_main_menu(sw_window))
    back_button.place(x=320,y=360)
    
    sw_label = Label(sw_window,
                     text="00:00",
                     font=("Arial",45,"bold"),
                     bg="#333333",
                     fg="White")
    sw_label.place(x=184,y=210)
    
    sw_window.mainloop()

def open_main_menu(current_window):
    current_window.destroy()
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
    alarm_window.resizable(False, False)
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
    
    alarm_backbutton = Button(alarm_window,
                        text="Back",
                        font=("Arial",10,"bold"),
                        command=lambda: open_main_menu(alarm_window))
    alarm_backbutton.pack(pady= 20)
    
    alarm_label = Label(alarm_window,
                        text="00:00",
                        font=("Arial",25,"bold"))
    alarm_label.pack(pady=30)

    alarm_window.mainloop()

def world_time():
    selected_tz = y.get()
    get_utc = datetime.now(timezone.utc)
    get_timezone = get_utc.astimezone(pytz.timezone(selected_tz))
    format_str = '%H:%M'
    time_country = get_timezone.strftime(format_str)
   
    world_time_label.config(text=time_country)
    world_time_label.after(1000, world_time)

def worldclock_window():
   global y, world_time_label
   world_window = Tk()
   world_window.geometry("540x540")
   world_window.resizable(False, False)
   world_window.title("World Clock")
   
   world_window.config(background="#9E9E9E")
   
   world_header = Label(world_window,
                        text="WORLD CLOCK",
                        font=("Arial",30,"bold"),
                        bg="#9E9E9E")
   world_header.pack()
   
   worldsubmit = Button(world_window,
                        text="Submit",
                        font=("Arial",10,"bold"),
                        command=world_time)
   worldsubmit.pack()
   
   world_backbutton = Button(world_window,
                        text="Back",
                        font=("Arial",10,"bold"),
                        command=lambda: open_main_menu(world_window))
   world_backbutton.pack(pady= 20)
     
   y = StringVar(world_window)
   y.set("America/New_York")        # default text set
   capital_drop = OptionMenu(world_window,      # option menu created
                              y,
                              "America/New_York","America/Los_Angeles","Europe/London","Europe/Paris","Asia/Tokyo","Australia/Sydney")
   capital_drop.config(font=("Arial",12))
   capital_drop.pack(padx=10, pady=50, fill='x')
   
   world_time_label = Label(world_window,
                      text="00:00",
                      font=("Arial",15,"bold"),
                      bg="#9E9E9E")
   world_time_label.pack()
   

   world_window.mainloop()

    
def main():
    global menu_window, photo
    menu_window = Tk()      # instance of window
    menu_window.geometry("540x540")
    menu_window.resizable(False, False) # Cant resize window
    menu_window.title("Clock App")
    

    icon = PhotoImage(file="Clock.png") # Turns png to photoimage
    menu_window.iconphoto(True, icon)
    menu_window.config(background="#333333")
    
    image = Image.open("C:/Users/anton/VSProjects/AlarmClock/AlarmClock/bluebutton.png")
    small_bluebutton = image.resize((330,140), Image.LANCZOS)   # numbers are width/height
    photo = ImageTk.PhotoImage(small_bluebutton)

    label = Label(menu_window,      # title
                  image=photo,
                  text="Clock App", 
                  font=("Calibri",50), 
                  foreground="White",
                  compound='center',
                  bg = "#333333")
    label.place(x=105, y=25)   # places label to top center
    
    timer_button_image = image.resize((115, 60), Image.LANCZOS)
    photo_timer_button = ImageTk.PhotoImage(timer_button_image)
    timer_button = Button(menu_window,
                          image=photo_timer_button,
                          command=timerwindow,  # opens timer window
                          text="Timer",
                          font=("Arial",25),
                          foreground="White",
                          compound='center',
                          bg="#333333",
                          relief=FLAT)
    timer_button.place(x=60, y=175)
    
    sw_button_image = image.resize((175, 60), Image.LANCZOS)
    photo_sw_button = ImageTk.PhotoImage(sw_button_image)
    stopwatch_button = Button(menu_window,
                              image=photo_sw_button,                          
                              command=stopwatchwindow,
                              text="Stopwatch",
                              font=("Arial",25),
                              fg="White",
                              compound='center',
                              bg="#333333",
                              relief=FLAT)
    stopwatch_button.place(x=340,y=175)
    
    alarm_button_image = image.resize((115, 60), Image.LANCZOS)
    photo_alarm_button = ImageTk.PhotoImage(alarm_button_image)
    alarm_button = Button(menu_window,
                          image=photo_alarm_button,
                          text="Alarm",
                          font=("Arial",25),
                          fg="White",
                          command=alarm_window,
                          compound='center',
                          bg="#333333",
                          relief=FLAT)
    alarm_button.place(x=60,y=330)
    
    world_button_image = image.resize((200, 60), Image.LANCZOS)
    photo_world_button = ImageTk.PhotoImage(world_button_image)
    world_button = Button(menu_window,
                          image=photo_world_button,                      
                          text="World Clock",
                          font=("Arial",25),
                          fg="White",
                          compound='center',
                          bg="#333333",
                          relief=FLAT,
                          command=worldclock_window)
    world_button.place(x=330,y=330)
    menu_window.mainloop()   # puts window on screen and listens for events
    
main()