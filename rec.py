import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        # Using PocketSphinx for offline speech recognition
        text = recognizer.recognize_sphinx(audio)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error with the service; {0}".format(e))

def filter_text(text):
    # Simple filtering mechanism (e.g., removing profanity)
    filtered_text = text.replace("bad_word", "good_word")
    return filtered_text

if __name__ == "__main__":
    while True:
        user_input = input("Press 'r' to start recording, 'q' to quit: ")
        if user_input.lower() == 'r':
            recognized_text = recognize_speech()
            if recognized_text:
                filtered_text = filter_text(recognized_text)
                print("Filtered Text:", filtered_text)
        elif user_input.lower() == 'q':
            print("Quitting...")
            break
        else:
            print("Invalid input. Please try again.")
