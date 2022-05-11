import math

def predict(sentence, mu, label_counts, word_counts, n_examples, n_words_per_label):
    best_label = None
    best_score = float('-inf')

    for label in word_counts.keys():
      score = 0.0
      voc_size= len(word_counts[label])

      for word in sentence:
        word_count_w= word_counts[label][word] + mu
        denominator= n_words_per_label[label] + voc_size*mu

        # print(denominator)

        score+= math.log(word_count_w/denominator)

        if score > best_score:
          best_score=score
          best_label= label
    return best_label