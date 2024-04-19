from read_numbers import *
from fnn import FeedForwardNN


def main():
    train_data_inputs, train_data_labels = read_train_data(200)
    # we can't quite use the label as an output as the particular form of this model
    # makes it much difficult to output a label as an answer. Instead, format the data
    # as an array which is turned on at certain indices
    print(len(train_data_inputs), '\t', len(train_data_inputs[0]))
    train_data_outputs = []
    for label in train_data_labels:
        t = np.zeros(10)
        t[label] = 1
        train_data_outputs.append(t)
    mnist_fnn_model = FeedForwardNN(784, 300, 100, 10)

    """
    number = 100
    for j in range(28):
        string = ""
        for i in range(28):
            string = string + ' ' + str(train_data_input[number - 1][i + 28*j])
            # string = str("%s%c%i", string, ' ', train_data_input[number - 1][i + 28*j])
        print(string)
    print(train_data_label[number])
    """
    
    print(len(train_data_outputs), '\t', len(train_data_outputs[0]))

    # store the initial model
    mnist_fnn_model.save("before_training.fnn")
    
    # train the model
    idx = 17
    model_output = mnist_fnn_model.compute(train_data_inputs[idx])
    prev_output = model_output[-1]
    '''
    for output in model_output:
        print(output, '\n\n')
    '''
    print(type(train_data_inputs))
    mnist_fnn_model.train(train_data_inputs, train_data_outputs)

    # test the model
    model_output = mnist_fnn_model.compute(train_data_inputs[idx])
    curr_output = model_output[-1]
    print(prev_output)
    print(curr_output)
    print(train_data_labels[idx])
    print(train_data_outputs[idx])

    test_data_inputs, test_data_labels = read_test_data(10)
    test_data_outputs = []
    for label in test_data_labels:
        t = np.zeros(10)
        t[label] = 1
        test_data_outputs.append(t)
    mnist_fnn_model.test(test_data_inputs, test_data_outputs)


    print(mnist_fnn_model)
    
    

if __name__ == '__main__':
    main()
    