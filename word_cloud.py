import matplotlib.pyplot as plt
from wordcloud import WordCloud
from word_scrub import strip_punctuation, strip_stopwords, strip_other, strip_digits


def create_dict(words):
    counts = dict()
    for word in words:
        word = word.lower()
        counts[word] = counts.get(word, 0) + 1
    return counts


def del_min_vals(dict):
    delete = []
    for k, v in dict.items():
        if v < 50:
            delete.append(k)
    for i in delete:
        del dict[i]
    return dict


def plot_cloud(wordcloud):
    plt.figure()
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


with open('roots.txt', encoding="utf8") as f:
    f = f.readlines()
    roots_txt = []
    for line in f:
        line.split()
        roots_txt.append(line.strip())
    # get list of lower case words from list of sentences
    words = [lo.lower() for word in roots_txt for lo in word.split()]
    # strip away punctuation from each word in list
    words = [strip_punctuation(word) for word in words]
    # deep clean list, no digits and other
    words = strip_other(strip_digits(words))
    counts = create_dict(strip_stopwords(words))
    final_count = del_min_vals(counts)

    # Generate word cloud
    wordcloud = WordCloud(max_words=300, random_state=1, background_color='#000000', collocations=False)
    wc = wordcloud.generate_from_frequencies(final_count)
    plt.figure( figsize=(10, 5))
    plt.imshow(wc)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig('cloudimg.png')
    plt.show()
