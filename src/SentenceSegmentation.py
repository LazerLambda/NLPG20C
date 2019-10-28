import collections
import en_core_web_sm
import spacy

from src.utils  import plot_count


class SentenceSegmentation:

    
    def local_sent_seg(self, text : list) -> dict:
        ret_dict = collections.defaultdict(int)

        for elem in text:
            doc = self.nlp(elem['text'])
            length = len(list(doc.sents))
            ret_dict[length] = ret_dict[length] + 1

        return ret_dict


    def __init__(self, reviews : list) -> ():
        self.reviews = reviews
        self.nlp = en_core_web_sm.load()


    def sentence_seg(self) -> ():
        rated_reviews = (
            [item for item in self.reviews if int(item['stars']) == 1],
            [item for item in self.reviews if int(item['stars']) == 2],
            [item for item in self.reviews if int(item['stars']) == 3],
            [item for item in self.reviews if int(item['stars']) == 4],
            [item for item in self.reviews if int(item['stars']) == 5],
        )

        self.rated_reviews = tuple(map(lambda x: self.local_sent_seg(x), rated_reviews))
    
    def plot_sentence_length(self):
        for i in range(1,6):
            plot_count(self.rated_reviews[i-1], (str(i) + ' stars'), 10)
            




