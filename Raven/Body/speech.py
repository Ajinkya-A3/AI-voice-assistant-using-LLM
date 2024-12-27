import datetime

import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# 0 for male voice & 1 for female voice
# engine.setProperty('voice', voices[0].id)

engine.setProperty('voice', voices[1].id)

# to convert text into audio
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# to convert audio into text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 2
        audio = r.listen(source,timeout=None,phrase_time_limit=10)

        #keep timeout=None or exception from module will occure

        try:
            print("recognizing...")
            query = r.recognize_google(audio, language="en-US") 
            #marathi - mr-IN, english - en-US, hindi - hi-in 
            print(f"user said: {query}")

        except Exception as e:
            speak("...")
            return "none"
        
        return query

# to greet
def greet():
    hour = int(datetime.datetime.now().hour)
    time = datetime.datetime.now().strftime("%H:%M")
    print(time)

    if 0 < hour < 12:
        speak("good morning")
    elif 12 <= hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("this is Raven, how can i help you")



takeCommand()

