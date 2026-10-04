import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

with sr.Microphone() as source:
    print("Say something...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("You said:", text)

    engine.say("You said " + text)
    engine.runAndWait()

except:
    print("Could not understand your speech.")