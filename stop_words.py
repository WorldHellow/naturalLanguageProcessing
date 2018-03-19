from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

text = "Typically text classification, including sentiment analysis  can be performed in one of 2 ways: 1. Supervised learning if there is enough training data and 2. A unsupervised training followed by a supervised classifier if there is not enough training data to train a deep neural network model."
stop_words = set(stopwords.words("english"))

words = word_tokenize(text)

filtered = []

#filtering out stop words
for w in words:
    if w not in stop_words:
        filtered.append(w)

print (filtered)        

#one liner for filtering
filter_one_liner = [w for w in words if not w in stop_words]

print (filter_one_liner)
