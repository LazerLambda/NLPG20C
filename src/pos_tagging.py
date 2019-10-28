import json
import random
import nltk

def pos_tag(reviews : list) -> ():

    random_sen=[]
    for i in range(0,5):
        x=random.randint(0,len(reviews)-1)
        random_sen.append((reviews[x].get('text')))

    for sen in random_sen:
        print(sen)
        tokens=nltk.word_tokenize(sen)
        print("parts of speech:", nltk.pos_tag(tokens))


