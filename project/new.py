import socket
import pyttsx3
import pyaudio
from vosk import Model, KaldiRecognizer
engine = pyttsx3.init()
switch = ['0','0','0','0','0','0','0','0']
model = Model(r"C:\Users\sachi\Downloads\vosk-model-small-en-in-0.4\vosk-model-small-en-in-0.4")
recognizer = KaldiRecognizer(model, 16000)
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True,frames_per_buffer=1000)
stream.start_stream()
temp1=""
def speak_text(text, rate=150):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def connect_to_device():
    sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    while True:
        try:
            sock.connect(("FC:A8:9A:00:14:9C", 1))
            return sock
        except:
            speak_text("Error connecting. Reconnecting with the device.")

hc05 = connect_to_device()

def main(switch_states,hc05):
    switch_data = ''.join(map(str, switch_states))
    hc05.send(switch_data.encode())

def commond(i,st,on,off):
    if switch[i]==on:
        print(st," is off")
        speak_text( st+" is off")
        switch[i]=off
        main(off,hc05)
    else :
        print(st," is on")
        speak_text( st+" is on")
        switch[i]=on
        main(on,hc05)

speak_text("say something")
COMMANDS = {
    "light": (7, "light", 8, "H"),
    "fan": (6, "fan", 7, "G"),
    "pan": (6, "fan", 7, "G"),
    "hen": (6, "fan", 7, "G"),
    "and": (6, "fan", 7, "G"),
    "so good": (5, "socket", 6, "F"),
    "socket": (5, "socket", 6, "F"),
    "night": (4, "night lamp", 5, "E"),
    "first":(0,"first switch",1,"A"),
}

while True:
    data = stream.read(1000)
    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        temp1=(text[14:-3])
    if temp1 in COMMANDS:
        command_data = COMMANDS[temp1]
        commond(*command_data)
    elif "all"==temp1 or "on"==temp1 or "i'm"==temp1:
        print("all lamp is off")
        speak_text("all lamp is off")
        main("I",hc05)
        switch = ['0','0','0','0','0','0','0','0']  
    temp1=""