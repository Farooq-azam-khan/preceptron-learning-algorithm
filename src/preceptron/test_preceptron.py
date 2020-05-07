import unittest
from preceptron import Preceptron
import random 

class TestPreceptronModelClass(unittest.TestCase):
    def test_init(self):
        p = Preceptron(2)
        self.assertEqual(p.lr, 0.1)

    def test_feed_forward(self):
        random.seed(1)
        p = Preceptron(2)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
