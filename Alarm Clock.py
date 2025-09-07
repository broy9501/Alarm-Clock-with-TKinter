# Import required libraries
from tkinter import *              # Tkinter base library
import customtkinter as ctk        # CustomTkinter for modern UI
import datetime as dt              # To handle current time/date
import time                        # (Not used directly, can be removed)
import winsound                    # To play alarm sound (Windows only)
from tkinter import messagebox     # To show popup alert when alarm rings

# Create the main window
root = ctk.CTk()
root.geometry("800x400")           # Set window size
root.title("Alarm Clock")          # Set window title

# Create main frame with transparent background (matches root color)
frame = ctk.CTkFrame(root, fg_color='transparent')
frame.pack(expand=True, fill=BOTH)

# Title label (blue background, white text)
ctk.CTkLabel(
    frame,
    text="Alarm Clock",
    text_color='white',
    fg_color='#01a6f8',           # Blue background
    width=200,
    height=50,
    font=('Bold', 20),
    corner_radius=8,
    anchor='center',
    wraplength=180
).pack(pady=30)

# Get current system date and time
date = dt.datetime.now()
currentTime = date.strftime("%H:%M:%S")
currentDate = date.strftime("%d-%m-%Y")

# Show current date
labelDate = ctk.CTkLabel(frame, text=currentDate, font=("Helvetica", 20))
labelDate.pack(pady=20)

# Show current time (this will update every second)
labelTime = ctk.CTkLabel(frame, text=currentTime, font=("Helvetica", 20))
labelTime.pack(pady=20)

# Subframe for time input fields (Hour & Minute)
timeFrame = ctk.CTkFrame(frame, corner_radius=8, fg_color='transparent')
timeFrame.pack(padx=20, pady=20)

# Hour input
ctk.CTkLabel(timeFrame, text="Hour", font=("Helvetica", 20), fg_color="transparent").pack(side=LEFT, padx=10, pady=10)
hour = ctk.CTkEntry(timeFrame, width=60, font=("Helvetica", 20))
hour.pack(side=LEFT, padx=10, pady=10)

# Minute input
ctk.CTkLabel(timeFrame, text="Minute", font=("Helvetica", 20), fg_color="transparent").pack(side=LEFT, padx=10, pady=10)
min = ctk.CTkEntry(timeFrame, width=60, font=("Helvetica", 20))
min.pack(side=LEFT, padx=10, pady=10)

# Variable to store alarm time
alarmTime = None

# Function to set the alarm
def setAlarm():
    global alarmTime
    alarmHour = hour.get().zfill(2)   # Get hour (ensure 2 digits)
    alarmMin = min.get().zfill(2)     # Get minute (ensure 2 digits)
    alarmTime = f"{alarmHour}:{alarmMin}:00"

    print("Alarm set for:", alarmTime)

    # Show confirmation on screen
    ctk.CTkLabel(root, text=f"Alarm set for: {alarmTime}", font=("Helvetica", 20)).pack(pady=20)

# Function that checks current time every second
def alarm():
    global alarmTime
    currentTime = dt.datetime.now().strftime("%H:%M:%S")
    labelTime.configure(text=currentTime)  # Update clock display

    # Check if alarm time matches current time
    if alarmTime and currentTime == alarmTime:
        # messagebox.showinfo("Alarm Clock", "Time to Wake up!")  # Popup alert
        ctk.CTkLabel(frame, text="Alarm Clock, Time to Wake up!", font=("Helvetica", 20)).pack(pady=20)
        winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)  # Initial beep
        for x in range(5):  # Play beep sound 5 times
            winsound.Beep(1000, 500)
        alarmTime = None   # Reset alarm so it doesn’t repeat

    # Call this function again after 1000ms (1 second)
    root.after(1000, alarm)

# Button to set alarm
ctk.CTkButton(timeFrame, text="Set Alarm", font=("Helvetica", 20), command=setAlarm).pack(padx=30, pady=10)

# Start the alarm function loop
alarm()

# Run the Tkinter event loop
root.mainloop()
