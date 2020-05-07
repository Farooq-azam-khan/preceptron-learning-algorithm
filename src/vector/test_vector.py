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

    def test_array_to_vector(self):
        arr = [1, 2, 3]
        v = Vector.to_vector(arr)
        self.assertEqual(v.dim, 3)
        self.assertEqual(v.data, [1, 2, 3])

    def test_vector_to_array(self):
        v = Vector.to_vector([1, 2, 3])
        self.assertEqual(v.data, [1, 2, 3])
        self.assertEqual(v.dim, 3)

    def test_valid_element_wise_multiplication(self):
        v1 = Vector.to_vector([1, 2, 3])
        self.assertEqual(v1.dim, 3)

        v2 = Vector.to_vector([4, 5, 6])
        result = v1*v2

        self.assertEqual(result.data, [4*1, 5*2, 3*6])

    def test_invalid_element_wise_multiplication(self):
        v1 = Vector()
        v1 = Vector.to_vector([1, 2, 3])
        v2 = Vector()

        with self.assertRaises(Exception):
            v1*v2

    def test_valid_dot_product_function(self):
        v1 = Vector()
        v2 = Vector()
        result = Vector.dot(v1, v2)
        self.assertEqual(result, 0)

        v1 = Vector.to_vector([1, 2, 3])
        v2 = Vector.to_vector([4, 5, 6])
        result = Vector.dot(v1, v2)
        self.assertEqual(result, 4*1+5*2+3*6)

    def test_invalid_dot_product_function(self):
        v1 = Vector.to_vector([1, 2, 3])
        v2 = Vector()

        with self.assertRaises(Exception):
            Vector.dot(v1, v2)


if __name__ == '__main__':
    unittest.main()
