import time
import pyttsx3
import ctypes
import os

# Function to minimize the command prompt window
def minimize_console():
    user32 = ctypes.windll.user32
    hWnd = user32.GetForegroundWindow()
    user32.ShowWindow(hWnd, 6)  # 6 is the command to minimize the window

# Text-to-speech function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# Minimize the command prompt window
minimize_console()

# Get the current hour
t = int(time.strftime('%H'))

# Determine the greeting based on the current hour
if t <= 12:
    speak("Good morning devil")
elif t > 12 and t <= 17:
    speak("Good afternoon devil")
elif t > 17 and t <= 19:
    speak("Good evening devil")
else:
    speak("Good night devil")

# Get the current time
current_time = time.strftime('%H:%M:%S')
print(current_time)

# Speak goodbye message
speak("Goodbye, take care boss")
