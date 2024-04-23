# Clean up words for wordcloud


def strip_punctuation(word):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@', '(', ')', "'"]
    return ''.join([c for c in word if c not in punctuation_chars])

def strip_stopwords(word_list):
    with open('stop_words.txt', 'r') as sw:
        stopwords = {w.strip() for w in sw}
        return [word for word in word_list if word not in stopwords]

def strip_digits(word_list):
    return [word for word in word_list if not word.isdigit()]

def strip_other(word_list):
    return [word for word in word_list if not ('{' in word or ']' in word)]