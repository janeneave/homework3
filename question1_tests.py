import unittest
from question1 import get_final_queue_order


class TestQueueOrder(unittest.TestCase):

    def setUp(self):
        input_data = """JUMP Amal
        JOIN Belle
        JUMP Charlie
        JOIN Dylan
        """
        with open('question1_test_input.txt', 'w') as temp_file:
            temp_file.write(input_data)

    def test_mixed_commands(self):
        expected_output = ['Charlie', 'Amal', 'Belle', 'Dylan']
        actual_output = get_final_queue_order('question1_test_input.txt')
        self.assertEqual(actual_output, expected_output)

    def test_empty_input(self):
        input_data = ""
        with open('question1_test_input.txt', 'w') as temp_file:
            temp_file.write(input_data)
        expected_output = []
        actual_output = get_final_queue_order('question1_test_input.txt')
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
