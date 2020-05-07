import unittest
from preceptron import Preceptron
import random 

class TestPreceptronModelClass(unittest.TestCase):
    def test_init(self):
        p = Preceptron(2)
        self.assertEqual(p.lr, 0.1)

    def test_feed_forward_with_valid_input(self):
        p = Preceptron(2, [0,0,0])
        result = p.feed_forward([0,0])
        self.assertEqual(result, 1)
    
    def test_feed_forward_with_invalid_input(self):
        p = Preceptron(2, [0,0,0])
        
        with self.assertRaises(Exception):
            p.feed_forward([0])
    
    def test_train_method(self):
        inputs = [0,0]
        weights = [-1,-1,1]
        target = 1

        p = Preceptron(2, weights)
        p.lr = 1
        result = p.feed_forward(inputs)
        self.assertEqual(result, 1)

        result = p.train([0,0], [1,1])
        print(result)

        self.assertEqual(1,2)

if __name__ == '__main__':
    unittest.main()
