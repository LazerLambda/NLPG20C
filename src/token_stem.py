import json
import random
import nltk
import collections
import matplotlib.pyplot as plt
import pandas as pd
import operator
from nltk.corpus import stopwords
from src.utils import plot_graph

stop_words = set(stopwords.words('english'))
marks = ['(', ')', '?', '!', '.', '...', ',', '-', '$']
ps = nltk.stem.PorterStemmer()

def ReviewTokens():
    df = pd.DataFrame(pd.read_json('reviewSelected100.json', lines=True))

    # tokens in each review
    df['tokenizedwords'] = df.apply(lambda x: nltk.word_tokenize(x['text']), axis = 1)
    df['lengthoftokenized'] = df.apply(lambda x: len(set(x['tokenizedwords'])), axis = 1)
    tokencounts = df['lengthoftokenized'].value_counts().to_dict()
    tokencounts = collections.OrderedDict(sorted(tokencounts.items(), key=lambda t: t[0]))
    plot_graph(tokencounts, "Tokenized Reviews (without Stemming)", "No. of tokens in a review", "No. of reviews", "token_review.png")

    # stems in each review
    df['stemmedwords'] = df['tokenizedwords'].apply(lambda x: [ps.stem(y) for y in x])
    df['lengthofstemmedtokens'] = df.apply(lambda x: len(set(x['stemmedwords'])), axis = 1)
    stemcounts = df['lengthofstemmedtokens'].value_counts().to_dict()
    stemcounts = collections.OrderedDict(sorted(stemcounts.items(), key=lambda t: t[0]))
    plot_graph(stemcounts, "Tokenized Reviews (with Stemming)", "No. of tokens in a review", "No. of reviews", "token_stemmed_review.png")

# list of 20 most common tokens and stems
def CommonTokens(reviews):
    tokenlist = []
    for review in reviews:
        tokens = nltk.word_tokenize(review['text'])
        for token in tokens:
            if not (str(token).lower() in stop_words or str(token).lower() in marks):
                tokenlist.append(token.lower())

    token_total = collections.Counter(tokenlist)
    most_common_token = token_total.most_common(20)
    print("Most common tokens: ", most_common_token)

    stemlist = []
    for token in tokenlist:
        if not (str(token).lower() in stop_words or str(token).lower() in marks):
            stemlist.append(ps.stem(token).lower())
    
    stem_total = collections.Counter(stemlist)
    most_common_stem = stem_total.most_common(20)
    print("Most common stems: ", most_common_stem)
