import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

text = "Mr Saad, how are you? I hate my life and I want to die."

###tokenizes sentence
##print (sent_tokenize(text))
##
###tokenizes words
##print (word_tokenize(text))

for i in word_tokenize(text):
    print (i)
