from tkinter import *

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