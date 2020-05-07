from activation_functions import sign
import random  # used to generate random weights

# import vector object
import sys
sys.path.append('../vector/')
from vector import Vector



if __name__ == '__main__':
    print('hello preceptron')


class Preceptron():
    ''' Implementation of the preceptron learning algorithm

    Attributes
    ----------
    num_weights : int
        attribue of class
    weights : array
        weights of model
    lr : flaot
        learning rate

    Methods
    -------
    __init__(dim=num_weights)
        this method's description

    '''

    def __init__(self, num_weights, weights=None):
        ''' 

        '''

        self.num_weights = num_weights
        
        # learning rate
        self.weights = [] 
        self.lr = 0.1
        if (weights):
            self.weights = Vector.to_vector(weights)
        else:
            self.weights = Vector.randomize(Vector(num_weights + 1)) # +1 for bias


    '''
        param: inputs array
        return: expected output
    '''

    def feed_forward(self, inputs):

        if len(inputs) != self.num_weights:
            raise Exception('The number of inputs must match the number of weights')
        # add the bias as part of the input
        bias = 1
        inputs.append(bias)
        input_vec = Vector.to_vector(inputs)
        return sign(Vector.dot(input_vec, self.weights))

   
    def train(self, inputs, target):
        '''
            param input: data you want to use to train preceptron
            param target: float
                the known output for adjusting the weights ie the label 
        '''

        # get a guess based on the input (+1 or -1)
        guess_input = self.feed_forward(inputs)

        # get the error = known answer - guess
        error = target - guess_input
        # adjust the weights here (the bias is inclded as one of the weights)
        new_weights = self.weights.data[:]
        for indx, weight in enumerate(self.weights.data):
            # change the weights based on the previous weight, the LR,
            delta_weight = error * inputs[indx] * self.lr
            new_weights = weight + delta_weight

        self.weights = new_weights
        return new_weights

    '''
        runs train function over and over agian
    '''

    def fit(self, inputs_train_array, targets_train_array, inputs_test_array, targets_test_array):
        EPOCHS = 10     # amount of batches you should run
        BATCHSIZE = 100  # amount of times you should train model
        for epoch in range(EPOCHS):
            for _ in range(BATCHSIZE):
                # pick a random data point
                random_index = random.randrange(len(inputs_train_array))
                input = inputs_train_array[random_index]
                target = targets_train_array[random_index]
                # train on that datapoint
                self.train(input, target)
            # get the accuracy of the testing data
            acc = self.actual_accuracy(inputs_test_array, targets_test_array)
            print("Epoch: {} out of {} accuarcy: {}".format(epoch+1, EPOCHS, acc))

            if acc == 1.0:
                break

    def actual_accuracy(self, inputs_test_array, targets_test_array):
        average = 0
        # loop through the points
        for x, y in zip(inputs_test_array, targets_test_array):
            # get the inputs
            prediction = self.feed_forward(x)
            if prediction == y:
                average += 1

        return average / len(inputs_test_array)

    '''
        Splits the data into two categories, training and testing.
    '''

    def train_test_split(self, X, y, train_split=0.5):
        # this shuffles data keeping the mapping of the two lists in check
        '''
        src: https://stackoverflow.com/questions/13343347/randomizing-two-lists-and-maintaining-order-in-python
        a = ["Spears", "Adele", "NDubz", "Nicole", "Cristina"]
        b = [1, 2, 3, 4, 5]
        combined = list(zip(a, b))
        random.shuffle(combined)
        a[:], b[:] = zip(*combined)
        '''

        combined = list(zip(X, y))
        random.shuffle(combined)
        X[:], y[:] = zip(*combined)
        # print(y)

        splitting_index_X = int(len(X)*train_split)
        splitting_index_y = int(len(y)*train_split)

        X_train = X[:splitting_index_X]
        y_train = y[:splitting_index_y]
        X_test = X[splitting_index_X:]
        y_test = y[splitting_index_y:]
        return X_train, y_train, X_test, y_test

    '''
    (used in conjunction with the linear_functions Point method -> will be removed)
    not a good way of getting accuracy for real data

        param: array of points objects
        return: accuracy between 0 and 1
    '''

    def accuracy(self, points):
        average = 0
        # loop through the points
        for point in points:
            # get the inputs
            inputs = point.get_points()
            prediction = self.feed_forward(inputs)
            if prediction == point.label:
                average += 1
        return average / len(points)

    '''
        (used for data with 2 inputs and one output)
        param: point for which you want to know the y value
        usage: get the y value of the linear function
    '''

    def guess_y(self, x):
        # w0*x + w1*y + w2*b
        w0 = self.weights[0]
        w1 = self.weights[1]
        w2 = self.weights[2]

        m = -(w0/w1)
        b = -(w2/w1)  # * 1
        y = m * x + b
        return y

    '''
        (used for data with 3 inputs one output)
        param: point (x,y) for which you want to know the z value
        usage: get the z value of the plane
    '''

    def guess_z(self, x, y):
        # w0x + w1y + w2z + w3b = 0
        if len(self.weights) == 4:
            w0 = self.weights[0]
            w1 = self.weights[1]
            w2 = self.weights[2]
            w3 = self.weights[3]

            m1 = -(w0/w2)
            m2 = -(w1/w2)
            b = -(w3/w2)  # *1
            z = m1*x + m2*y + b
            return z
