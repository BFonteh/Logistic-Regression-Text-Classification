import io
from collections import defaultdict
import numpy as np
def build_dict(filename, threshold=1):
    fin = io.open(filename, 'r', encoding='utf-8')
    word_dict, label_dict = {}, {}
    counts = defaultdict(lambda: 0)
    for line in fin:
        tokens = line.split()
        label = tokens[0]

        if not label in label_dict:
            label_dict[label] = len(label_dict)

        for w in tokens[1:]:
            counts[w] += 1
            
    for k, v in counts.items():
        if v > threshold:
            word_dict[k] = len(word_dict)
    return word_dict, label_dict
def load_data(filename, word_dict, label_dict):
    fin = io.open(filename, 'r', encoding='utf-8')
    data = []
    dim = len(word_dict)
    for line in fin:
        tokens = line.split()
        label = tokens[0]

        yi = label_dict[label]
        xi = np.zeros(dim)
        for word in tokens[1:]:
            if word in word_dict:
                wid = word_dict[word]
                xi[wid] += 1.0
        data.append((yi, xi))
    return data