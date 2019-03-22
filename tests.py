import unittest

from code import mahmoud98


class testclass(unittest.TestCase):
    def test_bad_val(self):
        with self.assertRaises(ValueError):
            mahmoud98.op(3, 8)

    def test_good_val(self):
        self.assertEqual(mahmoud98.op(3, 3), 'a = b')

    def test_op2(self):
        self.assertEqual(mahmoud98.op2(5), 10)


if __name__ == '__main__':
    unittest.main()
