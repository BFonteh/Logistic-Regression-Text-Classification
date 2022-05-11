import numpy as np
def softmax(x):
  max = x.max() #get the maximum component of x
  numerator = np.exp(x - max)
  denominator = np.sum(numerator)
  softMax = numerator/denominator
  return softMax 

def predict(w, x):
  pred= softmax(np.dot(w, x))
  return np.argmax(pred)