import speech_recognition as sr
import pyttsx3
import datetime

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

speak("Hello! How can I help you?")

with sr.Microphone() as source:
    audio = r.listen(source)

try:
    command = r.recognize_google(audio).lower()

    if "hello" in command:
        speak("Hello! Nice to meet you.")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The time is " + time)

    elif "date" in command:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + date)

    else:
        speak("I heard " + command)

except:
    speak("Sorry, I could not understand you.")