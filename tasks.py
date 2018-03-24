import os
from collections import Counter


def count_words(filename, most_common=10):
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    with open(os.path.join(data_dir, filename), 'r') as f:
        word_count = Counter(f.read().split())
    return dict(word_count.most_common(most_common))
