import collections
import spacy
import en_core_web_sm
import random

from src.utils import plot_count



class PairAdjectiveNounSummarizer:

    def __init__(self, reviews: list) -> ():
        self.reviews = reviews
        self.nlp = en_core_web_sm.load()

    def random_5_business(self):
        business = set()
        while len(business)<5:
            r_tmp = random.randint(0, len(self.reviews)-1)
            business.add(self.reviews[r_tmp]['business_id'])

        

        for i in business:
            random_review = list()
            for review in self.reviews:
                if (review['business_id'] == i):
                    random_review.append(review)
            self.pair(random_review, i)


    def pair(self, reviews : list, name : str) -> ():
        
        pairs = list()

        for e in reviews:
            
            text = e['text']
            doc = self.nlp(text)
            for token in doc:

                # <Adj, Noun>
                pair = None

                # the case that the adjective is a direct amod
                if token.dep_ == 'amod':
                    pair = ( token.text.lower(), token.head.text.lower() )
                    pairs.append(pair)

                # the case that the adjective is a adj complement
                if token.dep_ == 'acomp':
                    noun = [e for e in token.head.children if e.dep_ == "nsubj"]
                    if noun:
                        for e in noun:

                            # skip non nouns
                            if not e.pos_ == 'NOUN':
                                continue

                            # lemmatize the tokens
                            if e.lemma_ == '-PRON-':
                                pair = ( token.lemma_.lower(), e.text.lower() )
                            else:
                                pair = ( token.lemma_.lower(), e.lemma_.lower() )
                            pairs.append(pair)
                
                
        observations = collections.Counter(pairs)#collections.defaultdict(int)
        print("Results %s" % name)
        print(observations.most_common(20))
        print("\n\n")