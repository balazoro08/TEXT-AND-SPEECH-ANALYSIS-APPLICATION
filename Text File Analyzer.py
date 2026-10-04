file = open("sample.txt", "r")

text = file.read()

words = text.split()

print("Characters:", len(text))
print("Words:", len(words))
print("Lines:", len(text.splitlines()))

file.close()