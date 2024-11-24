import socket
import speech_recognition as sr
import pyttsx3
import pyaudio
from vosk import Model, KaldiRecognizer
engine = pyttsx3.init()
switch = ['0','0','0','0','0','0','0','0']
model = Model(r"C:\Users\sachi\Downloads\vosk-model-small-en-us-0.15\vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True,frames_per_buffer=1000)
stream.start_stream()
temp1=""
def speak_text(text1,text):
    engine.say(text1)
    engine.say(text)
    engine.runAndWait()
def connect_to_hc05(device_address):
    port = 1 
    sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    sock.connect((device_address, port))
    print("","Connected to HC-05 at address")
    return sock
hc05 = connect_to_hc05("FC:A8:9A:00:14:9C")

def main(switch_states,hc05):
    switch_data = ''.join(map(str, switch_states))
    hc05.send(switch_data.encode())
def commond(i,st,on,off):
    if switch[i]==on:
        print(st," is off")
        speak_text( st," is off")
        switch[i]=off
        main(off,hc05)
    else :
        print(st," is on")
        speak_text( st," is on")
        switch[i]=on
        main(on,hc05)
        
speak_text("","say something")
while True:
       data = stream.read(1000)
       if recognizer.AcceptWaveform(data):
          text = recognizer.Result()
          temp1=(text[14:-3])
       data=""
       if temp1!=None:
           print(temp1)
       if temp1=="light":
           commond(7,temp1,"8","H")
       elif temp1=="fan" or temp1=="pan" or temp1=="hen" or temp1=="and":
            commond(6,temp1,"7","G")
       elif temp1=="so good":   
            commond(5,"socket","6","F")
       elif temp1=="night":
            commond(4,temp1,"5","E")
       temp1=None
# main("G",hc05)