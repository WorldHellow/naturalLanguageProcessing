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
        for i in tokenized:
            words = nltk.word_tokenize(i)

            #parts of speech tagging
            tagged = nltk.pos_tag(words)

            chunk = r"""Find: {<RB.?>*<VB.?>*<NNP><NN>?}"""

            parser = nltk.RegexpParser(chunk)

            chunked = parser.parse(tagged)

            chunked.draw()
            print (chunked)
            

    except Exception as e:
         print(str(e))


process_content()
