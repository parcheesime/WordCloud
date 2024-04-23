import matplotlib.pyplot as plt
from wordcloud import WordCloud
from word_scrub import strip_punctuation, strip_stopwords, strip_other, strip_digits
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
import time
from collections import Counter


with open('roots.txt', encoding="utf8") as f:
    f = f.readlines()
    roots_txt = []
    for line in f:
        line.split()
        roots_txt.append(line.strip())
    # get list of lower case words from list of sentences
    words = [lo.lower() for word in roots_txt for lo in word.split()]
    
    # Clean words
    words = [strip_punctuation(word) for word in words]
    words = strip_digits(words)
    words = strip_other(words)
    words = strip_stopwords(words)

    # Create word count dictionary
    word_counts = Counter(words)
    final_count = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True)[:50])

    # Generate word cloud
    wordcloud = WordCloud(max_words=300, random_state=1, background_color='#000000', collocations=False)
    wc = wordcloud.generate_from_frequencies(final_count)
    plt.figure( figsize=(10, 5))
    plt.imshow(wc)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig('cloudimg.png')
    plt.show()