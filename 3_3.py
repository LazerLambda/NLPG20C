import json
import spacy
import en_core_web_sm


def load_reviews(path) -> list:
    import json
    reviews = list()

    with open(path, 'r', encoding="ISO-8859-1") as file:
        while file.readline():
            try:
                reviews.append(json.loads(file.readline()))
            except:
                continue

    return reviews


# class NounAdjPairSumm():

#     def __init__(self):
#         pass

#     def getPairs(self):
#         pass

def test(reviews : list):

    nlp = en_core_web_sm.load()
    
    noun_adj_pairs = []
    for e in reviews:
        doc = nlp(e['text'])
        root = [token for token in doc if token.head == token][0]
        subject = list(root.lefts)[0]
        print([e for e in subject.subtree])
        # for i,token in enumerate(doc):
        #     print(token.text, token.pos_)

        for i,token in enumerate(doc):
            if token.pos_ == 'NOUN':
                pass
                # print(token)
                # print([token_.text for token_ in doc[i].lefts])
                # print([token_.text for token_ in doc[i].rights])
                # print([token_.text for token_ in doc[i].lefts if token_.pos_ == 'ADJ'])
                # print([token_.text for token_ in doc[i].rights if token_.pos_ == 'ADJ'])

        for i,token in enumerate(doc):
            if token.pos_ not in ('NOUN','ADJ'):
                continue
            for j in range(i+1,len(doc)):
                if doc[j].pos_ == 'ADJ':
                    noun_adj_pairs.append((token, doc[j]))
                    break
        print(doc)



reviews = load_reviews('reviewSelected100.json')
test(reviews)