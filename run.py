from src.SentenceSegmentation import SentenceSegmentation
from src.AdjNounSum import PairAdjectiveNounSummarizer
from src.utils  import load_reviews
from src.pos_tagging import pos_tag
from src.token_stem import Tokenization
from src.most_frequent_adj_single import most_frequent_adj_single
from src.Application import App

# import data
REVIEWS = load_reviews('reviewSelected100.json')

# Data analysis
# -------------

# Sentence Segmentation
print("###################################################################")
print("Sentence Segmentation Results")
print("###################################################################")
Sentences = SentenceSegmentation(REVIEWS)
Sentences.sentence_seg()
Sentences.plot_sentence_length()
Sentences.avg()

# Tokenization and Stemming
print("###################################################################")
print("Tokenization and Stemming Results")
print("###################################################################")
Token = Tokenization(REVIEWS)
Token.review()
Token.common_tokens()

# POS tagging
print("###################################################################")
print("POS tagging Results")
print("###################################################################")
pos_tag(REVIEWS)

# Most frequent adjectives
print("###################################################################")
print("Most frequent adjectives Results")
print("###################################################################")
# running on single process
top10_adj = most_frequent_adj_single(REVIEWS)
top10_adj.top10()
# to run with multiprocessing, kindly proceed to run directly from the file src/most_frequent_adj.py

# Noun Adjective Pair Summarizer
print("###################################################################")
print("Noun Adjective Pair Summarizer Results")
print("###################################################################")
Pairs = PairAdjectiveNounSummarizer(REVIEWS)
Pairs.random_5_business()

# Application
print("###################################################################")
print("Application")
print("###################################################################")
App = App(REVIEWS)
App.run()
