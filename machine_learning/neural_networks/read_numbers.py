import numpy as np

# read training data
# returns a list of the testing data as well as the label of each testing data
def read_train_data(number_of_data):
    file = open("data/train-images.idx3-ubyte",'rb')
    a = file.read(4)
    b = file.read(4)
    length = file.read(4)
    width = file.read(4)

    ''' Purely for sanity check
    print
    magic = int.from_bytes(a, "big")
    total = int.from_bytes(b, "big")
    print(a)
    print(b)
    print(magic)
    print(total)
    ''' 

    raw_numbers = []
    for iter in range(number_of_data):
        raw_number = np.zeros(784)
        for i in range(784):
            a = int.from_bytes(file.read(1), "big")
            raw_number[i] = a
        raw_numbers.append(raw_number / 256)

    file.close()

    file = open("data/train-labels.idx1-ubyte",'rb')
    a = file.read(4)
    b = file.read(4)

    labels = []
    for label in range(number_of_data):
        labels.append(int.from_bytes(file.read(1), "big"))

    file.close()

    return np.array(raw_numbers), labels


# read test data
# returns two outputs, a list of the testing data as well as the label of each testing data
def read_test_data(number_of_data):
    file = open("data/t10k-images.idx3-ubyte",'rb')
    a = file.read(4)
    b = file.read(4)

    ''' Purely for sanity check
    magic = int.from_bytes(a)
    total = int.from_bytes(b)    
    print(a)
    print(b)
    print(magic)
    print(total)
    '''

    raw_numbers = []
    for iter in range(number_of_data):
        raw_number = np.zeros(784)
        for i in range(784):
            a = int.from_bytes(file.read(1))
            raw_number[i] = a
        raw_numbers.append(raw_number / 255)

    file.close()

    file = open("data/t10k-labels.idx1-ubyte",'rb')
    a = file.read(4)
    b = file.read(4)

    labels = []
    for label in range(number_of_data):
        labels.append(int.from_bytes(file.read(1)))

    file.close()

    return np.array(raw_numbers), labels

if __name__ == '__main__':
    raw_numbers, labels = read_train_data(10)
    print(labels)