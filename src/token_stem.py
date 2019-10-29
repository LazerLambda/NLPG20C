import json
import random
import nltk
import collections
import matplotlib.pyplot as plt
import pandas as pd
import operator
from nltk.corpus import stopwords
from src.utils import plot_graph

class Tokenization:
    def __init__(self, reviews : list) -> ():
        self.reviews = reviews
        self.stop_words = set(stopwords.words('english'))
        self.marks = ['(', ')', '?', '!', '.', '...', ',', '-', '$']
        self.ps = nltk.stem.PorterStemmer()

    def review(self):
        self.df = pd.DataFrame(pd.read_json('reviewSelected100.json', lines=True))

        # tokens in each review
        self.df['tokenizedwords'] = self.df.apply(lambda x: nltk.word_tokenize(x['text']), axis = 1)
        self.df['lengthoftokenized'] = self.df.apply(lambda x: len(set(x['tokenizedwords'])), axis = 1)
        self.tokencounts = self.df['lengthoftokenized'].value_counts().to_dict()
        self.tokencounts = collections.OrderedDict(sorted(self.tokencounts.items(), key=lambda t: t[0]))
        plot_graph(self.tokencounts, "Tokenized Reviews (without Stemming)", "No. of tokens in a review", "No. of reviews", "token_review.png")

        # stems in each review
        self.df['stemmedwords'] = self.df['tokenizedwords'].apply(lambda x: [self.ps.stem(y) for y in x])
        self.df['lengthofstemmedtokens'] = self.df.apply(lambda x: len(set(x['stemmedwords'])), axis = 1)
        self.stemcounts = self.df['lengthofstemmedtokens'].value_counts().to_dict()
        self.stemcounts = collections.OrderedDict(sorted(self.stemcounts.items(), key=lambda t: t[0]))
        plot_graph(self.stemcounts, "Tokenized Reviews (with Stemming)", "No. of tokens in a review", "No. of reviews", "token_stemmed_review.png")
    
    def common_tokens(self):
        self.tokenlist = []
        for review in self.reviews:
            self.tokens = nltk.word_tokenize(review['text'])
            for token in self.tokens:
                if not (str(token).lower() in self.stop_words or str(token).lower() in self.marks):
                    self.tokenlist.append(token.lower())

        self.token_total = collections.Counter(self.tokenlist)
        self.most_common_token = self.token_total.most_common(20)
        print("Most common tokens: ", self.most_common_token)

        self.stemlist = []
        for token in self.tokenlist:
            if not (str(token).lower() in self.stop_words or str(token).lower() in self.marks):
                self.stemlist.append(self.ps.stem(token).lower())
        
        self.stem_total = collections.Counter(self.stemlist)
        self.most_common_stem = self.stem_total.most_common(20)
        print("Most common stems: ", self.most_common_stem)