import time
import pyttsx3
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
 
t=int(time.strftime('%H'))
if(t<=12):
    speak("   Good morning  devil")
elif(t>12 and t<=17):
    speak("   Good afternoon  devil")
elif(t>17 and t<=19):
    speak("   good eveening  devil")
else :
    speak("   Good night devil")
t=time.strftime('%H:%M:%S')
print(t)
speak("Good bye take care boss")