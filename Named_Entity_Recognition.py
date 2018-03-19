import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train = state_union.raw("2005-GWBush.txt")
text = state_union.raw("2006-GWBush.txt")

#training custome tokenizer
custom_tokenizer = PunktSentenceTokenizer(train)

tokenized = custom_tokenizer.tokenize(text)

def process_content():
    try:
        for i in tokenized[2:]:
            words = nltk.word_tokenize(i)

            #parts of speech tagging
            tagged = nltk.pos_tag(words)

            namedEnt = nltk.ne_chunk(tagged, binary = True)
            namedEnt.draw()
            

    except Exception as e:
         print(str(e))


process_content()
