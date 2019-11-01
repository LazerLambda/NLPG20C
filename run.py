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
Sentences = SentenceSegmentation(REVIEWS)
Sentences.sentence_seg()
Sentences.plot_sentence_length()
Sentences.avg()

# Tokenization and Stemming
Token = Tokenization(REVIEWS)
Token.review()
Token.common_tokens()

# POS tagging
pos_tag(REVIEWS)

# Most frequent adjectives
# running on single process
top10_adj = most_frequent_adj_single(REVIEWS)
top10_adj.top10()
# to run with multiprocessing, kindly proceed to run directly from the file src/most_frequent_adj.py

# Noun Adjective Pair Summarizer
# ------------------------------
Pairs = PairAdjectiveNounSummarizer(REVIEWS)
Pairs.random_5_business()

# Application
App = App(REVIEWS)
App.run()
