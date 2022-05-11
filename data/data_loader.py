import io

def load_data(filename):
    fin = io.open(filename, 'r', encoding='utf-8')
    data = []
    for line in fin:
        tokens = line.split()
        data.append((tokens[0], tokens[1:]))
    return data