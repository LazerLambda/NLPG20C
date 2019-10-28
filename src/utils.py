import collections
import json
import matplotlib.pyplot as plt
import operator


# parse the data from json to dict-list
def load_reviews(path) -> list:

    reviews = list()

    with open(path, 'r', encoding="ISO-8859-1") as file:
        while file.readline():
            try:
                reviews.append(json.loads(file.readline()))
            except:
                continue

    return reviews


# plot the data 
def plot_count(coll : collections.defaultdict(int), title : str, max : int) -> ():
    sortedls = sorted(coll.items(), key=operator.itemgetter(1))
    top = list(sortedls)[-max:]
    top.reverse()

    print("\n" + title)
    print(top)

    labels = list(map(lambda x: str(x[0]), top))
    values = list(map(lambda x: x[1], top))

    print(labels)
    print(values)

    plt.bar(labels, values)
    plt.title(title)
    plt.tick_params(axis='x', which='major', labelsize=5)
    plt.show()
    fig = plt.gcf()
    fig.savefig("".join(title.split(' ')))
    fig.clf()