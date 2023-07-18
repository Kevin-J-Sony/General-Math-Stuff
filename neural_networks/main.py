from read_numbers import *
from fnn import FeedForwardNN


def main():
    train_data_input, train_data_label = read_train_data(20)
    # we can't quite use the label as an output as the particular form of this model
    # makes it much difficult to output a label as an answer. Instead, format the data
    # as an array which is turned on at certain indices
    train_data_output = []
    for label in train_data_label:
        t = np.zeros(10)
        t[label] = 1
        train_data_output.append(t)
    mnist_fnn_model = FeedForwardNN(784, 100, 10)

    # store the initial model
    mnist_fnn_model.save("before_training.fnn")
    
    # train the model
    model_output = mnist_fnn_model.compute(train_data_input[0])
    for output in model_output:
        print(output, '\n\n')
    # print(model_output[len(model_output) - 1])
    

if __name__ == '__main__':
    main()
    