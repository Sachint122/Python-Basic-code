import time
import pyttsx3

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Initialize pyttsx3 engine
engine = pyttsx3.init()

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
# Speak goodbye message
speak("Goodbye, take care boss")
