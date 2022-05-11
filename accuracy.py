from predict import predict

def compute_accuracy(w, valid_data):
    accuracy = 0.0
    for y_i, x_i in valid_data:

        ## FILL CODE
      pred= predict(w, x_i)
      
      if pred == y_i:
        accuracy+=1.0
  
    return (accuracy/float(len(valid_data))) * 100.00  