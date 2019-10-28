import collections
import spacy
import en_core_web_sm



class PairAdjectiveNounSummarizer:

    def __init__(self, reviews: list) -> ():
        self.reviews = reviews
        self.nlp = en_core_web_sm.load()

    def pair(self) -> ():
        pairs = list()

        for e in self.reviews:
            text = e['text']
            doc = self.nlp(text)
            for token in doc:

        #        if not e['business_id'] == 'vMpJzMFst_9GP4boeqWIRg':
        #            continue

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
                        pair = ( token.text.lower(), noun[0].text.lower() )
                        pairs.append(pair)
                
                # maybe using the lemma ?
                
        observations = collections.Counter(pairs)#collections.defaultdict(int)

        print(observations.most_common(20))