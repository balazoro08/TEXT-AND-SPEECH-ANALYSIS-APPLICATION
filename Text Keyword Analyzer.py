text = input("Enter text: ").lower()

keywords = ["python", "java", "ai", "cloud", "data"]

for word in keywords:
    count = text.count(word)
    print(word, ":", count)