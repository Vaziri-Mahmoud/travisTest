import unittest

import code


class mahmoud98(unittest.TestCase):
    def test_bad_val(self):
        with self.assertRaises(ValueError):
            code.mahmoud98.op(3, 8)


if __name__ == '__main__':
    unittest.main()
