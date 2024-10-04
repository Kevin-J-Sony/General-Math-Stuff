import numpy as np

# This class is a rudementary Neural Netowrk.
class BasicNeuralNetwork:
    
    # In initialization, the network is established.
    # For n layers, n-1 weight matrices are used and n-1 bias "vector" are made
    # Rather than the traditional method of y = A*x + b, instead, use yT = xT*A + b.
    # This means multiplication progresses from left to right rather than right to left
    # This ends up effecting how rows and columns should behave. The reason why we have chosen
    # to do it in this manner is for the input x to come in a simple vector, which is just a 
    # matrix of dimension (1 x input_size).
    # The dimensions of each weight matrices are (previous_layer_size x next_layer_size)
    # The dimension of each bias "vectors" are (1 x next_layer_size)
    def __init__(self,*args):
        np.random.seed(100)
        self.weight_layers = []
        self.bias_layers = []
        if len(args) > 0:
            for idx in range(len(args) - 1):
                self.weight_layers.append(np.ones((args[idx], args[idx + 1])) - 0.5)
                self.bias_layers.append(np.ones((1, args[idx + 1])) - 0.5)
        self.n_layers = args

    # NOT TO BE USED AT ALL LMAO. I DID IT JUST TO CONFIRM MY CLASS WORKS
    def reveal(self):
        for weight in self.weight_layers:
            print(weight,'\n\n')
        for bias in self.bias_layers:
            print(bias,'\n\n')
        print(self.n_layers)

    # This loads up
    def load(self, filename):
        if self.n_layers != 0:
            print("warning, the current network is going to be discarded")
        # set all the variables to zero
        self.weight_layers = []
        self.bias_layers = []
        self.n_layers = []

        # read all the lines and close the file
        file = open(filename, "r")
        lines = file.readlines()
        file.close()

        # get the arguments from the first line
        str_args = lines[0].split('\t')[:-1]
        for arg in str_args:
            self.n_layers.append(int(arg))

        # now that we have the arguments, we use it
        # to fill in the weight matrices and basis vectors

        # keep a line number index
        line_idx = 2
        for idx in range(len(self.n_layers) - 1):
            row = self.n_layers[idx]
            col = self.n_layers[idx + 1]
            current_wmat = np.zeros((row, col))

            # go through "row" lines
            for i in range(row):
                arrow = lines[line_idx + i].split('\t')[:-1]
                for j in range(len(arrow)):
                    current_wmat[i][j] = float(arrow[j])
            self.weight_layers.append(current_wmat)
            line_idx += row
        line_idx += 1
        # load the basis vectors
        for i in range(1, len(self.n_layers)):
            current_bvec = np.zeros((1,self.n_layers[i]))
            arrow = lines[line_idx].split('\t')[:-1]
            for j in range(len(arrow)):
                current_bvec[0][j] = float(arrow[j])
            self.bias_layers.append(current_bvec)
            line_idx += 1

    def save(self, filename):
        file = open(filename, "w")
        
        for arg in self.n_layers:
            file.write(str(arg)+'\t')
        file.write('\n')
        file.write('###\n')
        for weight in self.weight_layers:
            for row in weight:
                for element in row:
                    file.write(str(element)+'\t')
                file.write('\n')
        file.write('###\n')
        for bias in self.bias_layers:
            for element in bias[0]:
                file.write(str(element)+'\t')
            file.write('\n')
        
        file.close()

    # to each element in this matrix
    def transform(matrix):
        # return 1/(1+np.exp(-matrix))
        return matrix * (matrix > 0)

    def dtransform(matrix):
        # temp = BasicNeuralNetwork.transform(matrix)
        # return np.exp(-matrix) * (temp*temp)
        return 1 * (matrix > 0)

    def compute(self, input):
        if len(input) != len(self.weight_layers[0]):
            print(len(input))
            print(len(self.weight_layers[0]))
            raise Exception("The number of inputs does not fit the model")
        Z = [input]
        for idx in range(len(self.weight_layers)):
            A = np.matmul(Z[idx], self.weight_layers[idx]) + self.bias_layers[idx]
            Z.append(BasicNeuralNetwork.transform(A))
        return Z

    '''
    This is the met of the Neural Network. The training algorithm is a gradient descent. The basic idea is
    using the chain rule on smooth manifolds to find the gradient of the error function at a given "input". However,
    crucially, our input in this case is a simple matrix which 
    '''
    def train(self, train_data_inputs, train_data_outputs):
        if len(train_data_inputs) != len(train_data_outputs):
            print('# of train inputs: ', len(train_data_inputs))
            print('# of train outputs: ', len(train_data_outputs))
            raise Exception("The number of inputs does not match the number of outputs")

        n_loops = 1

        for loop in range(n_loops):
            n_of_layers = len(self.n_layers)

            input = train_data_inputs
            correct_output = train_data_outputs
            intermediate_outputs = [input]
            for j in range(n_of_layers - 1):
                A = np.matmul(intermediate_outputs[j], self.weight_layers[j]) + self.bias_layers[j]
                intermediate_outputs.append(BasicNeuralNetwork.transform(A))
            # backpropagate with intermediate outputs
            ideal_output = [0 for i in range(n_of_layers)]
            ideal_output[-1] = correct_output

            momentum_w = 0
            momentum_b = 0
            gamma = 0.01

            # print(len(intermediate_outputs))
            for j in range(-1, -n_of_layers, -1):
                #print(ideal_output[j])
                # breakpoint()
                dE = (intermediate_outputs[j] - ideal_output[j]) / len(train_data_inputs)
                if type(intermediate_outputs[j]) == type([1, 2]):
                    #print(intermediate_outputs[j])
                    print(type(input))
                dy = BasicNeuralNetwork.dtransform(intermediate_outputs[j])
                
                grad_w = np.matmul(np.transpose(dE * dy), intermediate_outputs[j - 1]).T
                #print(np.shape(dE))
                #print(np.shape(dy))
                #print(np.shape(intermediate_outputs[j - 1]))
                    
                #print(np.shape(grad_w))
                #print(np.shape(sum(grad_w)))

                grad_b = dE * dy * 1
                #print(np.shape(grad_b))
                #print(np.shape(sum(grad_b)))
                

                #momentum_w = 0.08*momentum_w + grad_w
                #momentum_b = 0.08*momentum_b + sum(grad_b)
                #breakpoint()
                momentum_w = grad_w
                momentum_b = sum(grad_b)
                
                self.weight_layers[j] = self.weight_layers[j] - gamma * (momentum_w)
                
                self.bias_layers[j] = self.bias_layers[j] - gamma * (momentum_b)

                if j != -n_of_layers:
                    #print(np.shape(dE * dy))
                    #print(np.shape(intermediate_outputs[j - 1]))
                    #print(np.shape(self.weight_layers[j]))
                    grad_x = np.matmul(dE * dy, np.transpose(self.weight_layers[j])) # intermediate_outputs[j - 1]
                    #print(np.shape(grad_x))
                    ideal_output[j - 1] = intermediate_outputs[j - 1] - gamma*(-j) * (grad_x)

                #if j == -1:
                #print(sum(dE))
                Error = 0.5 * (dE ** 2)
                print(sum(Error))
                print('----------------------------------------')

            

    def test(self, test_data_inputs, test_data_outputs):
        
        if len(test_data_inputs) != len(test_data_outputs):
            raise Exception("The number of inputs does not match the number of outputs")
        for idx in range(len(test_data_inputs)):
            ti = test_data_inputs[idx]
            to = test_data_outputs[idx]

            H = self.compute(ti)
            
            me = np.max(H[-1])
            co = np.zeros(len(H[-1]))
            for i in range(len(H[-1])):
                #print(H[-1][i])
                ...
            ##print(co)
            


if __name__ == '__main__':
    fnn = BasicNeuralNetwork(10, 10, 5)
    fnn.save("temp.ann")

    fnn2 = BasicNeuralNetwork()
    fnn2.load("temp.ann")
    
    # check they are the same
    fnn_w = fnn.weight_layers
    fnn2_w = fnn2.weight_layers
    for i in range(len(fnn_w)):
        print(fnn_w[i] - fnn2_w[i])

    fnn_b = fnn.bias_layers
    fnn2_b = fnn2.bias_layers
    for i in range(len(fnn_b)):
        print(fnn_b[i] - fnn2_b[i])


    