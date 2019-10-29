import json
import random
import nltk
import multiprocessing as mp
import numpy as np
import time
import math

rating = [1.0, 2.0, 3.0, 4.0, 5.0]
data = []           # list from file
data_word_count = 0 # number of tokens from all the reviews
words = []          # list of tokens from all the reviews
words_count = []    # list of occurences of each tokens from all the reviews
start = time.time() # start time from processing the file

###############################################################################

reviews = []        # list of reviews

# load file
with open("reviewSelected100.json") as json_file:
    for p in json_file:
        data.append(json.loads(p))
# append reviews to array reviews        
for i in range(len(data)):
    reviews.append(data[i].get('text'))

# count number of words/tokens in all reviews
for review in reviews:
    tokens = nltk.word_tokenize(review)
    data_word_count += len(tokens)
    for i in range(len(tokens)):
        word = tokens[i].lower()
        if(word not in words):
            words.append(word)
            words_count.append(1)
                
        else:
            idx = words.index(word)
            words_count[idx] = words_count[idx] + 1
 
###############################################################################

def most_frequent_adj(star):

    rating_reviews = [] # list of reviews for a particular rating star
    for i in range(len(data)):
        if(data[i].get('stars') == star):
            rating_reviews.append(data[i].get('text'))

    print("Number of reviews with rating star", star, ": ", len(rating_reviews))
    print("")

    # list of adjectives in reviews with a particular rating star
    adj = []
    # list of adjectives count in reviews with a particular rating star
    adj_count = []

    # word count from reviews with a particular rating star
    rating_word_count = 0

    # identify and count number of adjectives and store in arrays
    for review in rating_reviews:
        tokens = nltk.word_tokenize(review)
        for i in range(len(nltk.pos_tag(tokens))):
            if((nltk.pos_tag(tokens))[i][1] == 'JJ'):
                word = (nltk.pos_tag(tokens))[i][0].lower()
                if(word not in adj):
                    adj.append(word)
                    adj_count.append(1)
                
                else:
                    idx = adj.index(word)
                    adj_count[idx] = adj_count[idx] + 1

        rating_word_count += len(tokens)
        review_idx = rating_reviews.index(review)
        
        # print duration
        if(review_idx %100 == 0):
            time_lapse = time.time() - start
            print(star, "rating review #", review_idx, ", time lapsed:", time_lapse)
            print("")

    # list of adjectives with respective count and indicativeness as tuples
    adj_count_list = []
    adj_ind_list = []
    for i in range(len(adj)):
        idx = words.index(adj[i])
        prob_adj_all = words_count[idx]/data_word_count
        prob_adj_rating = adj_count[i]/rating_word_count
        adj_indicative = prob_adj_rating * (math.log(prob_adj_rating / prob_adj_all))

        adj_count_tuple = (adj[i], adj_count[i])
        adj_count_list.append(adj_count_tuple)

        adj_ind_tuple = (adj[i], adj_indicative)
        adj_ind_list.append(adj_ind_tuple)
    
    # sort the list based on adjectives with highest count
    adj_count_sorted = sorted(adj_count_list, key=getKey, reverse=True)
    
    # list of top 10 adjectives in the reviews of rating star='star'
    adj_top10 = []
    for i in range(0,10):
        adj_top10.append(adj_count_sorted[i][0])

    # sort the list based on adjectives with highest indicativeness
    adj_ind_sorted = sorted(adj_ind_list, key=getKey, reverse=True)

    # list of top 10 adjectives in the reviews of rating star='star'
    adj_top10_ind = []
    for i in range(0,10):
        adj_top10_ind.append(adj_ind_sorted[i][0])

    # print duration
    time_lapse = time.time() - start
    print("Done rating", star, ",", len(rating_reviews), "reviews, time lapsed:", time_lapse)
    print("")

    return np.array([adj_top10, adj_top10_ind])

# for function sorted to return sorted array based on values in index 1
def getKey(item):
    return item[1]

###############################################################################

# main function with multiprocessing
def main():

    no_threads = mp.cpu_count()
    p = mp.Pool(processes = no_threads)
    paras = p.map(most_frequent_adj, rating)

    paras = np.array(paras)

    adj_top10, adj_top10_ind = paras[:,0], paras[:,1]

    print("")
    
    # print top 10 most used adjectives for each rating
    for i in range(len(rating)):
        print(i+1.0, "star(s) top 10 most used adjectives:", adj_top10[i])

    print("")

    # print top 10 most indicative adjectives for each rating
    for i in range(len(rating)):
        print(i+1.0, "star(s) top 10 most indicative adjectives:", adj_top10_ind[i])

    # print duration
    duration = time.time() - start
    print("Duration: ", duration)

    # end


if __name__ == '__main__':
    main()


