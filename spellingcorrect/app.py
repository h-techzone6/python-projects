from textblob import TextBlob

words = input("Enter any words")

print("Wrong words:",words)

correctWord = TextBlob(words)

print("Correct Words:",correctWord.correct())

