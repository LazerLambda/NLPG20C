from src.SentenceSegmentation import SentenceSegmentation
from src.AdjNounSum import PairAdjectiveNounSummarizer
from src.utils  import load_reviews
from src.pos_tagging import pos_tag
from src.token_stem import ReviewTokens, CommonTokens

# import data
REVIEWS = load_reviews('reviewSelected100.json')

# Data analysis
# -------------

# Sentence Segmentation
Sentences = SentenceSegmentation(REVIEWS)
Sentences.sentence_seg()
Sentences.plot_sentence_length()

# Tokenization and Stemming
ReviewTokens()
CommonTokens(REVIEWS)

# POS tagging
pos_tag(REVIEWS)

# Noun Adjective Pair Summarizer
# ------------------------------
Pairs = PairAdjectiveNounSummarizer(REVIEWS)
Pairs.pair()
