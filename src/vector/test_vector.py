import unittest

from vector import Vector


class TestVectorClass(unittest.TestCase):

    def test_initalization(self):
        v1 = Vector()
        self.assertEqual(v1.dim, 2)
        self.assertEqual(Vector.initalize(dim=2), [0, 0])

    def test_scalar_multiplication(self):
        v1 = Vector()
        self.assertEqual(Vector.scalar_mul(v1, 1), [0, 0])

        v1.data = [1, 1]
        self.assertEqual(Vector.scalar_mul(v1, 1), [1, 1])
        self.assertEqual(Vector.scalar_mul(v1, -1), [-1, -1])
        self.assertEqual(Vector.scalar_mul(v1, 2), [2, 2])


if __name__ == '__main__':
    unittest.main()
