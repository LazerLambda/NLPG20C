import json
import random
import nltk

def pos_tag(file):
    data=[] #list

    with open(file) as json_file:
        for p in json_file:
            data.append(json.loads(p))


    random_sen=[]
    for i in range(0,5):
        x=random.randint(0,len(data))
        random_sen.append((data[x].get('text')))

    for sen in random_sen:
        print(sen)
        tokens=nltk.word_tokenize(sen)
        print("parts of speech:", nltk.pos_tag(tokens))


pos_tag("reviewSelected100.json")
