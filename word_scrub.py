# Clean up words for wordcloud


def strip_punctuation(word):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@', '(', ')', "'"]
    for i in punctuation_chars:
        word = word.replace(i, "")
    return word


def strip_stopwords(bk_word_lst):
    with open('stop_words.txt', 'r') as sw:
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