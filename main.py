from data import data_loader
from train import count_words
from accuracy import compute_accuracy
print("")
print("** Naive Bayes **")
print("")

mu = 0.00001
train_data = data_loader.load_data("data/train1.txt")
valid_data = data_loader.load_data("data/valid1.txt")
counts = count_words(train_data)

print("Validation accuracy: %.3f" % compute_accuracy(valid_data, mu, counts))
print("")