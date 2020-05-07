import unittest
from preceptron import Preceptron
import random 

class TestPreceptronModelClass(unittest.TestCase):
    def test_init(self):
        p = Preceptron(2)
        self.assertEqual(p.lr, 0.1)

    def test_init_with_custom_weights(self):
        # give invalid weights
        with self.assertRaises(Exception):
            p = Preceptron(2, [1,1])

    def test_feed_forward_with_valid_input(self):
        p = Preceptron(2, [0,0,0])
        result = p.feed_forward([0,0])
        self.assertEqual(result, 1)
    
    def test_feed_forward_with_invalid_input(self):
        p = Preceptron(2, [0,0,0])
        
        with self.assertRaises(Exception):
            p.feed_forward([0])
    
    def test_train_method(self):
        # 2 inputs: x1, x2
        # x1*w1 x2*w2 + 1*w3
        inputs = [0,0]
        weights = [0,0,0] # last one is the bias
        target = 1

        p = Preceptron(2, weights)
        self.assertEqual(p.num_weights, 2)
        self.assertEqual(len(p.weights.data), 3)
        p.lr = 1
        result = p.feed_forward(inputs)
        self.assertEqual(result, 1)

        result = p.train(inputs, target)
        self.assertEqual(result.data, [0,0,0])
    
    def test_train_method_2(self):
        inputs = [0, 0]
        weights = [1,1,1]
        target = 0
        p = Preceptron(2, weights)
        p.lr = 1
        result = p.feed_forward(inputs)
        self.assertEqual(result, 1)
        result = p.train(inputs, target)
        self.assertEqual(result.data, [1,1,0])


if __name__ == '__main__':
    unittest.main()
