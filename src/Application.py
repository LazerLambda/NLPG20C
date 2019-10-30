import json
import random
import nltk
import collections

class App:
    def __init__(self, reviews: list) -> ():
        self.reviews = reviews
        self.good = ['good', 'decent', 'ok', 'fine', 'average', 'great', 'delicious', 'friendly', 'wonderful', 'happy', 'excellent', 'nice', 'tasty', 'fresh', 'professional', 'helpful', 'fantastic', 'awesome']
        self.bad = ['horrible', 'terrible', 'bad', 'rude', 'poor', 'awful', 'unfprofessional', 'wrong', 'slow']
        self.negate = ['no', 'not', 'never', 'nobody']

    def run(self):
        print("Input business ID: ")
        name = input()

        good_feature = []
        bad_feature = []

        business_reviews = list()
        for review in self.reviews:
            if (review['business_id'] == name):
                business_reviews.append(review['text'])

        for review in business_reviews:
            tokens = nltk.word_tokenize(review)
            for i in range(len(tokens)):
                if i+1 in range(len(tokens)):
                    if tokens[i] in self.good:
                        if (nltk.pos_tag(tokens))[i+1][1] == 'NN':
                            if tokens[i-1] in self.negate:
                                bad_feature.append(tokens[i-1] + " " + tokens[i] + " " + tokens[i+1])
                            else:
                                good_feature.append(tokens[i] + " " + tokens[i+1])

                        elif tokens[i-1] in self.negate:
                            bad_feature.append(tokens[i-3] + " " + tokens[i-2] + " " + tokens[i-1] + " " + tokens[i])

                    elif tokens[i] in self.bad:
                        if (nltk.pos_tag(tokens))[i+1][1] == 'NN':
                            if tokens[i-1] in self.negate:
                                good_feature.append(tokens[i-1] + " " + tokens[i] + " " + tokens[i+1])
                            else:
                                bad_feature.append(tokens[i] + " " + tokens[i+1])
                        elif tokens[i-1] in self.negate:
                            good_feature.append(tokens[i-3] + " " + tokens[i-2] + " " + tokens[i-1] + " " + tokens[i])
                        
                
        good_feature_count = collections.Counter(good_feature)
        bad_feature_count = collections.Counter(bad_feature)
        print("Results %s" % name)
        print("Good features:", good_feature_count)
        print("")
        print("Bad features:", bad_feature_count)
        print("\n\n")



        
