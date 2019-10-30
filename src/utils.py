import collections
import json
import matplotlib.pyplot as plt
import operator


# parse the data from json to dict-list
def load_reviews(path) -> list:

    reviews = list()
    
    #somehow this part only loads half of the reviews
    # with open(path, 'r', encoding="ISO-8859-1") as file:
    #     while file.readline():
    #         try:
    #             reviews.append(json.loads(file.readline()))
    #         except:
    #             continue
    
    #loads all 15300 reviews
    with open(path) as json_file:
        for p in json_file:
            reviews.append(json.loads(p))
            
    return reviews


# plot the data 
def plot_count(coll : collections.defaultdict(int), title : str, max : int, star : int) -> ():
    colors = ['darkblue', 'blue', 'cyan', 'gold', 'orange']
    sortedls = sorted(coll.items(), key=operator.itemgetter(1))
    top = list(sortedls)[-max:]
    top.reverse()

    print("\n" + title)
    print(top)

    labels = list(map(lambda x: str(x[0]), top))
    values = list(map(lambda x: x[1], top))

    print(labels)
    print(values)

    bars = plt.bar(labels, values)
    
    #set colors for specific stars
    for e in bars:
        e.set_color(colors[star-1])

    plt.title(title)
    plt.tick_params(axis='x', which='major', labelsize=5)
    #plt.show()
    fig = plt.gcf()
    fig.savefig("".join(title.split(' ')))
    fig.clf()

def plot_graph(input_data, title, xlabel, ylabel, image_title):
    x = list(input_data.keys())
    y = list(input_data.values())
    plt.bar(x, y, width=1.0)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(image_title)
