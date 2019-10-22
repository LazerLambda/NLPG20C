import en_core_web_sm
import json
import re
import spacy


def load_reviews(path) -> list:

    reviews = list()

    with open(path, 'r', encoding="ISO-8859-1") as file:
        while file.readline():
            try:
                reviews.append(json.loads(file.readline()))
            except:
                continue

    return reviews


def get_neg_words(reviews : list) :

    import re

    neg_words = "(no|not|nothing)" # Unfortunately

    nlp = en_core_web_sm.load()

    for e in reviews:
        doc = nlp(e['text'])
        for elem in doc.sents:

            if re.findall(neg_words, elem.text):
                print(elem.text)
            


reviews = load_reviews('reviewSelected100.json')

get_neg_words(reviews)
