text = input("Enter a sentence: ")

words = text.split()

print("\n--- Text Analysis ---")
print("Number of words:", len(words))
print("Number of characters:", len(text))
print("Number of characters without spaces:", len(text.replace(" ", "")))