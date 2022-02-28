text = input("Please Enter Your Text here:")
vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
for letter in text:
    if letter in vowels:
        text = text.replace(letter, "")

print("New Text is :", text)

