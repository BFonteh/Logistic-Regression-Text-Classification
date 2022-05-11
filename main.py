from data import data_loader
from train import sgd
from accuracy import compute_accuracy
import numpy as np

print("")
print("** Logistic Regression **")
print("")

word_dict, label_dict = data_loader.build_dict("data/train1.txt")
train_data = data_loader.load_data("data/train1.txt", word_dict, label_dict)
valid_data = data_loader.load_data("data/valid1.txt", word_dict, label_dict)

nlabels = len(label_dict)
dim = len(word_dict)
w = np.zeros([nlabels, dim])
w = sgd(w, train_data, 7)
print("")
print("Validation accuracy: %.3f" % compute_accuracy(w, valid_data))
print("")