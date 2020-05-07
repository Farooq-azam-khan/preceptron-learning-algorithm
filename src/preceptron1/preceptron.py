import numpy as np 

def sign(val):
    if val >= 0:
        return 1
    return -1 

class Preceptron():
    def __init__(self, n_inputs, weights=None, lr=0.1, activation_fn=sign):
        self.n_inputs = n_inputs
        self.weights = np.random.rand(n_inputs+1)
        self.lr = lr
    
    @property
    def weights(self):
        return self.weights

    @property
    def lr(self):
        return self.lr 

    @lr.setter
    def lr(self, new_lr):
        self.lr = new_lr

    
    @weights.setter
    def weights(self, wgt):
        if not (type(wgt) == np.ndarray):
            raise ValueError('Input must be an numpy ndarray')

        self.weights = wgt
        self.n_inputs = n_inputs
    
    def feed_forward(self, inputs):
        if type(inputs) != np.ndarray:
            raise ValueError('Input must be an ndarray')
        
        return activation_fn(np.dot(Preceptron.get_actual_input(inputs), self.weights))
    
    @staticmethod
    def get_actual_input(inputs)
    ''' adds the bias to the input ''' 
    return np.append(inputs, 1)

    def train(self, inputs, targets): 
        ''' finds the error and adjusts the weights '''

        if type(inputs) != np.ndarray:
            raise ValueError('Input must be an ndarray')

        error = self.feed_forward(inputs) - targets 

        new_weights = np.zeros(self.n_inputs + 1)
        for indx in range(self.n_inputs+1):
            delta_weight = error * inputs[indx] * self.lr
            new_weights[indx] = self.weights[indx] + delta_weight
        
        self.weights = new_weights
        return self.weights

    def __repr__(self):
        return self.weights.__repr__()
    
    def __str__(self):
        return self.weights.__str__()
