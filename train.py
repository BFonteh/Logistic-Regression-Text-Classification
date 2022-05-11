import numpy as np
import math
from predict import softmax
def sgd(w, data, niter):
    nlabels, dim = w.shape
    for iter in range(niter):
      train_err= 0.0
      for yi, xi in data:
        pred= softmax(np.dot(w, xi))
        # print(pred[yi])
        # break
        train_err+= math.log(pred[yi])
 
        # gradient is the partial derivative of train error with respect to w.
        zero_vec=np.zeros(nlabels)
        zero_vec[yi]= 1.0
        error= pred-zero_vec
        gradient= error.reshape(nlabels, 1)*xi.reshape((1, dim))
        w= w- 0.5*gradient
      print("iter: %02d loss: %.3f" % (iter, train_err/len(data)))
    return w