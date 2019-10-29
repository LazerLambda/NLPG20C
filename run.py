from src.SentenceSegmentation import SentenceSegmentation
from src.AdjNounSum import PairAdjectiveNounSummarizer
from src.utils  import load_reviews
from src.pos_tagging import pos_tag
from src.token_stem import Tokenization

# import data
REVIEWS = load_reviews('reviewSelected100.json')

# Data analysis
# -------------

# Sentence Segmentation
#Sentences = SentenceSegmentation(REVIEWS)
#Sentences.sentence_seg()
#Sentences.plot_sentence_length()
#Sentences.avg()

# Tokenization and Stemming
# Token = Tokenization(REVIEWS)
# Token.review()
# Token.common_tokens()

# POS tagging
#pos_tag(REVIEWS)

# Noun Adjective Pair Summarizer
# ------------------------------
Pairs = PairAdjectiveNounSummarizer(REVIEWS)
Pairs.random_5_business()
