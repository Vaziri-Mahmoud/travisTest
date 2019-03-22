import unittest

from code import mahmoud98


class testclass(unittest.TestCase):
    def test_bad_val(self):
        with self.assertRaises(ValueError):
            mahmoud98.op(3, 8)
    '''
    def test_good_val(self):
        self.assertEqual(code.mahmoud98.op(3, 3), 'a = b')
    '''


if __name__ == '__main__':
    unittest.main()
