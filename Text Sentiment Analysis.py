from textblob import TextBlob

text = input("Enter your text: ")

analysis = TextBlob(text)
polarity = analysis.sentiment.polarity

print("Polarity:", polarity)

if polarity > 0:
    print("Positive 😊")
elif polarity < 0:
    print("Negative")
else:
    print("Neutral")