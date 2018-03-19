from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

words = ["java", "javaning", "javar", "javali"]

for i in words:
    print(ps.stem(i))

text = "It is very import to be javali if you want to code in java. All javars are javaning all the time."

word = word_tokenize(text)

for w in word:
    print(ps.stem(w))
