import random
import array as arr
import pyttsx3
import os
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def check(b):
    m = 0
    for k in range(10):
        if (b == a[k]):
            m = m+1
            break
    if (m == 0):
        return 0
    else:
        return 1


question = ["Who is the current Prime Minister of India?", "Which city is known as the Pink City of India?",
            "What is the national animal of India?",
            "Who wrote the Indian national anthem, Jana Gana Mana ?",
            "Which Indian state is famous for the backwaters of Alleppey?",
            " Which city is home to the iconic Taj Mahal?",
            "Who is known as the Father of the Indian Constitution?",
            " Which Indian city is famous for its annual Kumbh Mela festival?",
            "Which Indian cricketer holds the record for the highest individual score in Test cricket?",
            "What is the currency of India?",
            "Who was the first President of India?",
            " Which Indian state is known as the Land of the Rising Sun?",
            "Which Indian city is known as the Silicon Valley of India?",
            "Who is the Missile Man of India?",
            "Which Indian state is home to the Kaziranga National Park, known for its one-horned rhinoceros?"]
option = [['Lalu shingh', 'Narendra Modi', 'Bengal tiger', 'Dr.B.R. Ambedak'],
          ['Jaipur', 'Delhi', 'kolkata', 'Indore'],
          ['Bengal Tiger', 'Elephant', 'Lion', 'Panther'],
          ['Chetan Bhagat', 'Arundhati Roy',
              'Rabindranath Tagore', 'Salman Rushdie'],
          ['Gujarat', 'Madhy Pradesh', 'Uttar Pradesh', 'Kerala'],
          ['Agra', 'Mumbai', 'New Delhi', 'Kolkatta'],
          ['Rajendra Prasad', 'Jawaharlal Neharu',
              'Dr B.R. Ambedakar', 'G.V. Mavlankar'],
          ['Prayagraj', 'Jaipur', 'Varansi', 'Kolkatta'],
          ['Sachin T.', 'Dhoni', 'Rohit', 'Brian Lara'],
          ['INR', 'USD', 'JPY', 'GBP'],
          ['Velikkakathu Sankaran', 'Pawar',
              'Dr. Rajendra Prasad', 'Zakir Husen Khan'],
          ['Gujarat', 'Arunanchal Pradesh', 'Bihar', 'Sikkim'],
          ['Bengaluru', 'Chennai', 'New Delhi', 'Mayamar'],
          ['Ravindrnath Tagore', 'Dr.A.P.J Abdul Kalam',
              'Narenedrmodi', 'Lalu singh'],
          ['Assam', 'Sikkimm', 'Kashmir', 'Karnatak']]
answer = [2, 1, 1, 3, 4, 1, 3, 1, 4, 1, 3, 2, 1, 2, 1]
i = 0
o = 0
ruppes = 0
a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for j in range(25):
    temp = random.choice(range(len(question)))
    n = check(temp)
    if (n == 1):
        j = j
    else:
        a[i] = temp
        i = i+1
        o = o+1
        print("question number", "(", end="")
        print(o, end="")
        print(")")
        speak("question number")
        speak(o)
        print(question[temp])
        print("(1)=", option[temp][0])
        print("(2)=", option[temp][1])
        print("(3)=", option[temp][2])
        print("(4)=", option[temp][3])
        speak(question[temp])
        speak("(1)")
        speak(option[temp][0])
        speak("(2)")
        speak(option[temp][1])
        speak("(3)")
        speak(option[temp][2])
        speak("(4)")
        speak(option[temp][3])

        number = int(input("Please chose correct answer"))
        if (answer[temp] == number):
            print("coreect answer")
            speak("coreect answer")
            ruppes = ruppes+1000
            print("you won ", ruppes, "Ruppes")
            speak("you won")
            speak(ruppes)
            speak("Ruppes")
            os.system('cls')
        else:
            print("You game is end")
            speak("your game is end")
            break
        if (o == 10):
            print("Great you reached the highest level of the game")
            speak("Great you reached the highest level of the game")
            exit(0)
