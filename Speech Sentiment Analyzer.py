import speech_recognition as sr
from textblob import TextBlob

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak your opinion...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)

    print("Text:", text)

    result = TextBlob(text)
    score = result.sentiment.polarity

    if score > 0:
        print("Sentiment: Positive")
    elif score < 0:
        print("Sentiment: Negative")
    else:
        print("Sentiment: Neutral")

except:
    print("Speech not recognized.")