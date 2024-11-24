import socket
import pyttsx3
import pyaudio
from vosk import Model, KaldiRecognizer
import json 
# Initialize speech synthesis engine
engine = pyttsx3.init()

# Initialize Vosk model and recognizer
model = Model(r"C:\Users\sachi\Downloads\vosk-model-small-en-in-0.4\vosk-model-small-en-in-0.4")
recognizer = KaldiRecognizer(model, 16000)

# Initialize microphone
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1000)
stream.start_stream()

# Bluetooth connection setup
def connect_to_device():
    sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    while True:
        try:
            sock.connect(("FC:A8:9A:00:14:9C", 1))
            return sock
        except:
            speak_text("Error connecting. Reconnecting with the device.")

hc05 = connect_to_device()

# Function to speak text
def speak_text(text, rate=150):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

# Function to send switch states to the device
def main(switch_states, hc05):
    switch_data = ''.join(map(str, switch_states))
    hc05.send(switch_data.encode())

# Function to process voice commands
def commond(i, st, on, off):
    if switch[i] == on:
        print(st, "is off")
        speak_text(st + " is off")
        switch[i] = off
        main(off, hc05)
    else:
        print(st, "is on")
        speak_text(st + " is on")
        switch[i] = on
        main(on, hc05)

speak_text("Say something")

COMMANDS = {
    "light": (7, "light", "8", "H"),
    "fan": (6, "fan", "7", "G"),
    "pan": (6, "fan", "7", "G"),
    "hen": (6, "fan", "7", "G"),
    "and": (6, "fan", "7", "G"),
    "so good": (5, "socket", "6", "F"),
    "socket": (5, "socket", "6", "F"),
    "night": (4, "night lamp", "5", "E"),
}
while True:
    # Read a small chunk of audio data
    data = stream.read(1024)

    # Process the audio chunk for speech recognition
    if recognizer.AcceptWaveform(data):
        result = recognizer.Result()
        result_json = json.loads(result)

        # Extract recognized text from the JSON
        if "text" in result_json:
            temp1 = result_json["text"].strip()
            print("Recognized:", temp1)

            # Process recognized command
            if temp1 in COMMANDS:
                command_data = COMMANDS[temp1]
                commond(*command_data)
            elif temp1 in ["all", "on", "I'm"]:
                print("All lamps are off")
                speak_text("All lamps are off")
                main("I", hc05)
                switch = ['0', '0', '0', '0', '0', '0', '0', '0']

            # Reset temporary variable
            temp1 = ""

