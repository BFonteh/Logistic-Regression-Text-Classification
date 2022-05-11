from predict import predict

def compute_accuracy(valid_data, mu, counts):
    accuracy = 0.0
    for label, sentence in valid_data:
      pred= predict(sentence, mu, **counts)
      
      if pred == label:
        accuracy+=1.0

     
    return (accuracy/float(len(valid_data))) * 100.00