import matplotlib.pyplot as plt
from wordcloud import WordCloud


def get_line_number(line_start, file_name):
    with open(file_name) as f:
        for n, line in enumerate(f):
            if line.startswith(line_start):
                return n


def strip_punctuation(word):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@', '(', ')']
    for i in punctuation_chars:
        word = word.replace(i, "")
    return word


def strip_stopwords(bk_word_lst):
    with open('stop-words.txt', 'r') as sw:
        stopwords = [w.strip() for w in sw]
        for a in stopwords:
            for w in bk_word_lst:
                if w == a:
                    bk_word_lst.remove(w)
        return bk_word_lst


def strip_digits(word_list):
    for ele in word_list:
        if ele.isdigit():
            word_list.remove(ele)
    return word_list


def strip_other(word_list):
    for e in word_list:
        if '{' in e or ']' in e:
            word_list.remove(e)
    return word_list


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


with open('roots.txt') as f:
    roots_txt = []
    for line in f:
        wrds = line.split()
        for word in wrds:
            roots_txt.append(word)
    # get list of lower case words from list of sentences
    words = [lo_word.lower() for lo_word in roots_txt]
    # strip away punctuation from each word in list
    words = [strip_punctuation(word) for word in words]
    # deep clean list, no digits and other
    words = strip_other(strip_digits(words))
    counts = create_dict(strip_stopwords(words))
    final_count = del_min_vals(counts)

    # Generate word cloud
    wordcloud = WordCloud(max_words=300, random_state=1, background_color='#daa520', collocations=False)
    wc = wordcloud.generate_from_frequencies(final_count)
    plot_cloud(wc)
