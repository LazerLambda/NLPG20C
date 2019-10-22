import collections
import en_core_web_sm
import json
import nltk
import math
import matplotlib.pyplot as plt
import operator
import random
import spacy

stop_words = ['a', 'the', 'of', 'and']
marks = ['(', ')', '?', '!', '.', '...', ',', '-']



def plot_count(input : collections.defaultdict(int), title : str, max : int) -> ():
    
    sortedls = sorted(input.items(), key=operator.itemgetter(1))
    top = list(sortedls)[-max:]
    top.reverse()

    print("\n" + title)
    print(top)

    labels = list(map(lambda x: x[0], top))
    values = list(map(lambda x: x[1], top))

    plt.bar(labels, values)
    plt.title(title)
    plt.tick_params(axis='x', which='major', labelsize=5)
    # plt.show()
    fig = plt.gcf()
    fig.savefig("".join(title.split(' ')))
    fig.clf()




def load_reviews(path) -> list:

    reviews = list()

    with open(path, 'r', encoding="ISO-8859-1") as file:
        while file.readline():
            try:
                reviews.append(json.loads(file.readline()))
            except:
                continue

    return reviews




def get_random_texts(reviews: list, number  : int) -> set:

    random_reviews = set()

    # for _ in range(100):
    #     r_tmp = random.randint(0, len(reviews) - 1)
    #     review = reviews[r_tmp]['text']
    #     if review in random_reviews:
    #         continue
    #     else:
    #         random_reviews.add(review)

    while len(random_reviews) < number:
        r_tmp = random.randint(0, len(reviews) - 1)
        random_reviews.add(reviews[r_tmp]['text'])


    return random_reviews




def sentence_seg(reviews: list) -> ():

    nlp = en_core_web_sm.load()

    rated_reviews = (
        [item for item in reviews if int(item['stars']) == 1],
        [item for item in reviews if int(item['stars']) == 2],
        [item for item in reviews if int(item['stars']) == 3],
        [item for item in reviews if int(item['stars']) == 4],
        [item for item in reviews if int(item['stars']) == 5],
    )


    def local_sent_seg(text: list) -> dict:
        ret_dict = collections.defaultdict(int)

        for elem in text:
            doc = nlp(elem['text'])
            length = len(list(doc.sents))
            ret_dict[length] = ret_dict[length] + 1

        return ret_dict

    rated_reviews = tuple(map(lambda x: local_sent_seg(x), rated_reviews))


    def create_figures(mapped_tuple : (dict, dict, dict, dict, dict)) -> ():
        for i in range(1,6):
            elem = rated_reviews[i - 1]
            plt.bar(range(len(elem)), list(elem.values()), align='center')
            plt.xticks(range(len(elem)), list(elem.keys()))
            plt.title( (str(i) + ' stars'))
            plt.xlabel('Length of a review')
            plt.ylabel('Number of reviews')
            plt.tick_params(axis='x', which='major', labelsize=5)
            fig = plt.gcf()

            fig.savefig( ( str(i) + '_stars.png') )

    create_figures(rated_reviews)




def tokandstem(reviews : list) -> ():


    # get all tokens
    tokenlist = list()
    for elem in reviews:
        tokens = nltk.tokenize.word_tokenize(elem['text'])
        for e in tokens:
            if not (str(e).lower() in stop_words or str(e).lower() in marks):
                tokenlist.append(e.lower())
    

    total_without_stemming = collections.defaultdict(int)

    for elem in tokenlist:
        total_without_stemming[elem] = total_without_stemming[elem] + 1



    from nltk.stem import PorterStemmer

    ps = PorterStemmer() 

    stemed_words = list()
    for e in tokenlist:
        if not (str(e).lower() in stop_words or str(e).lower() in marks):
            stemed_words.append(ps.stem(e).lower())

    total_with_stem = collections.defaultdict(int)

    for elem in stemed_words:
        total_with_stem[elem] = total_with_stem[elem] + 1

    plot_count(total_without_stemming, 'Most common words', 20)
    plot_count(total_with_stem, 'Most common words (stemmed)', 20)




def getPOSTags(reviews: list) -> ():

    for e in reviews:

        nlp = en_core_web_sm.load()
        doc = nlp(e)

        print("\n\nSentence:")
        print(e)

        for token in doc: 
            print(token, token.pos_)




def most_frequent_adjs_ranking(revs : list) -> ():
    
    def adj(reviews : list) -> ():
        rated_reviews = (
            [item for item in reviews if int(item['stars']) == 5],
            [item for item in reviews if int(item['stars']) == 4],
            [item for item in reviews if int(item['stars']) == 3],
            [item for item in reviews if int(item['stars']) == 2],
            [item for item in reviews if int(item['stars']) == 1],
        )

        nlp = en_core_web_sm.load()

        adjs_in_tot = list()


        # get all adjectives
        for i in range(0,5):
            review_class = rated_reviews[i]
            adjectives = collections.defaultdict(int)
            for e in review_class:
                doc = nlp(e['text'])
                for token in doc:
                    if token.pos_ == "ADJ":
                        adjectives[str(token)] = adjectives[str(token)] + 1
            
            plot_count(adjectives, (str(5 - i) + ' Stars'), 10)

            # list 10 most common adjs
            adjs_in_tot.append(adjectives)
        print("Adjective listing finished")

    #adj(revs)


    def pre_(reviews : list) -> ():
        

        rated_reviews = (
            [item for item in reviews if int(item['stars']) == 5],
            [item for item in reviews if int(item['stars']) == 4],
            [item for item in reviews if int(item['stars']) == 3],
            [item for item in reviews if int(item['stars']) == 2],
            [item for item in reviews if int(item['stars']) == 1],
        )

        nlp = en_core_web_sm.load()

        adjs = collections.defaultdict(dict)
        length_of_texts = {'whole': 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

        for i in range(0,5):
            review_class = rated_reviews[i]
            for e in review_class:


                doc = nlp(e['text'])
                length_of_texts['whole'] += len(doc)
                length_of_texts[(i+1)] += len(doc)
                for token in doc:
                    if token.pos_ == "ADJ":
                        token_tmp = token.text.lower()


                        if not adjs[token_tmp]:
                            adjs[token_tmp] = collections.defaultdict(int)


                        # count for the whole text
                        adjs[token_tmp]['whole'] += 1


                        # count for the specific text
                        if i == 0:
                            adjs[token_tmp][1] += 1

                        if i == 1:
                            adjs[token_tmp][2] += 1

                        if i == 2:
                            adjs[token_tmp][3] += 1

                        if i == 3:
                            adjs[token_tmp][4] += 1
                        
                        if i == 4:
                            adjs[token_tmp][5] += 1

            print(
                """Count done for %d stars\nwords in total: %d
                """ 
                % (i+1, length_of_texts[(i+1)])
                )

    

        top_adj = [list(), list(), list(), list(), list()]
        
        for i in range(0,5):
            for e in adjs:
                if adjs[e][(i+1)] == 0:
                    continue

                pw          = adjs[e]['whole'] / length_of_texts['whole']
                pw_given_r  = adjs[e][(i+1)] / length_of_texts[(i+1)]

                if pw == 0 or pw_given_r == 0:
                    continue
                pre = pw_given_r * math.log(pw / pw_given_r)

                top_adj[i].append((e, pre))

        for i in range(0,5):
            
            # sort and splice the top 10 adjectives

            sortedls = sorted(top_adj[i], key=lambda x: x[1])
            
            top_adj[i] = list(sortedls)[-10:]
            top_adj[i].reverse()


            # display the adjectives

            labels = list(map(lambda x: x[0], top_adj[i]))
            values = list(map(lambda x: x[1], top_adj[i]))

            title = str(5 - i) + ' Stars PRE'

            plt.bar(labels, values)
            plt.title(title)
            plt.tick_params(axis='x', which='major', labelsize=5)
            #plt.show()
            fig = plt.gcf()
            fig.savefig("".join(title.split(' ')))
            fig.clf()

        print(top_adj)
            
    pre_(revs)



    # def pre(word : str, rating : int):

    #     occurances_within = 0
    #     occurances = 0
    #     total_within = 0
    #     total = 0

    #     adjs = collections.defaultdict(dict)

    #     for i in range(0,5):
    #         for elem in rated_reviews[i]:

    #             tokens = nltk.tokenize.word_tokenize(elem['text'])
    #             for e in tokens:
    #                 if not (str(e).lower() in stop_words or str(e) in marks):
    #                     if e.lower() == word.lower():
    #                         occurances += 1

    #                         if 5 - rating == i:
    #                             occurances_within += 1

    #                     if 5 - rating == i: 
    #                         total_within += 1

    #                     total += 1


    #     if occurances_within == 0 or occurances == 0 or total_within == 0 or total == 0:
    #         return 0

    #     word_prob = occurances / total # P(w)

    #     word_prob_within = occurances_within / total_within # P(w|R*)

    #     return word_prob_within * math.log(word_prob_within / word_prob) 

    # rated_probs = list()
    # for i in range(0,5):
    #     pre_val = list(map(lambda x : (x, pre(x, 5-i)), adjs_in_tot[i]))
    #     rated_probs.append(pre_val)

        

    #     sortedls = sorted(pre_val, key=lambda x: x[1])
    #     top = list(sortedls)[-10:]
    #     top.reverse()


    #     labels = list(map(lambda x: x[0], top))
    #     values = list(map(lambda x: x[1], top))

    #     title = str(5 - i) + ' Stars PRE'

    #     plt.bar(labels, values)
    #     plt.title(title)
    #     plt.tick_params(axis='x', which='major', labelsize=5)
    #     #plt.show()
    #     fig = plt.gcf()
    #     fig.savefig("".join(title.split(' ')))
    #     fig.clf()







reviews = load_reviews('reviewSelected100.json')

# writing style
random_text = get_random_texts(reviews, 10)
#print(len(random_text))

# sentence segmentation
sentence_seg(reviews)

# tokenization and stemming
#tokandstem(reviews)

# POS Tagging
#random_text = get_random_texts(reviews, 10)
#getPOSTags(list(random_text))

# Most Frequent Adjectivesfor each Rating
#most_frequent_adjs_ranking(reviews)