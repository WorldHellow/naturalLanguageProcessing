from nltk.corpus import wordnet

words = wordnet.synsets("tired")

print (words[1].definition())
print (words[1].examples())

syns = []
anto = []

#get synonyms and antonyms
for word in wordnet.synsets("tired"):
    for l in word.lemmas():
        syns.append(l.name())
        if l.antonyms():
            anto.append(l.antonyms()[0].name())

print (set(syns))
print (set(anto))

#semantic similarity

#checking the similarity
w1 = wordnet.synset("good.n.01")
w2 = wordnet.synset("better.n.01")

print(w1.wup_similarity(w2))



