import io, sys, math, re
from collections import defaultdict

def count_words(data):
    n_examples = 0
    n_words_per_label = defaultdict(lambda: 0)
    label_counts = defaultdict(lambda: 0)
    word_counts = defaultdict(lambda: defaultdict(lambda: 0.0))
    
    for example in data:
      label, sentence = example
      n_examples += 1
      label_counts[label]  +=1

      for word in sentence:
        word_counts[label][word] += 1
        n_words_per_label[label] += 1


    return {'label_counts': label_counts, 
            'word_counts': word_counts, 
            'n_examples': n_examples, 
            'n_words_per_label': n_words_per_label}