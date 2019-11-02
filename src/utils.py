import collections
import json
import matplotlib.pyplot as plt
import operator


# parse the data from json to dict-list
def load_reviews(path) -> list:

    reviews = list()
    
    with open(path, 'r' , encoding="ISO-8859-1") as json_file:
        for p in json_file:
            reviews.append(json.loads(p))
            
    return reviews


# plot the data 
def plot_count(coll : collections.defaultdict(int), title : str, max : int, star : int) -> ():
    colors = ['darkblue', 'blue', 'cyan', 'gold', 'orange']
    sortedls = sorted(coll.items(), key=operator.itemgetter(1))
    top = list(sortedls)[-max:]
    top.reverse()

    


    labels = list(map(lambda x: str(x[0]), top))
    values = list(map(lambda x: x[1], top))
    print("\nResults: " + title)
    print("Labels: ", labels)
    print("Values;", values)

    bars = plt.bar(labels, values)
    
    #set colors for specific stars
    for e in bars:
        e.set_color(colors[star-1])

    SMALL_SIZE = 8
    MEDIUM_SIZE = 10
    BIGGER_SIZE = 12

    plt.rc('axes', labelsize=BIGGER_SIZE)
    plt.title(title)
    #plt.show()
    fig = plt.gcf()
    fig.savefig("".join(title.split(' ')))
    fig.clf()

def plot_graph(input_data, title, xlabel, ylabel, image_title):
    plt.figure()
    x = list(input_data.keys())
    y = list(input_data.values())
    plt.bar(x, y, width=1.0)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    SMALL_SIZE = 8
    MEDIUM_SIZE = 10
    BIGGER_SIZE = 12

    plt.rc('axes', labelsize=BIGGER_SIZE)
    plt.savefig(image_title)
