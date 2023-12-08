import unittest
from question2 import num_in_sequence


class TestNumInSequence(unittest.TestCase):

    def test_num_in_sequence_zero(self):
        result = num_in_sequence(0)
        self.assertEqual(result, 1)

    def test_num_in_sequence_positive_num(self):
        result = num_in_sequence(3)
        # 1 + 7 + 7 + 7 = 22
        self.assertEqual(result, 22)

    def test_num_in_sequence_large_num(self):
        result = num_in_sequence(10)
        # 1 + 7*10 = 71
        self.assertEqual(result, 71)


if __name__ == '__main__':
    unittest.main()
