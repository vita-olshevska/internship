import unittest
from password_generator import decompose, create_password


class DecomposeTestCase(unittest.TestCase):
    def test_decompose(self):
        number = 16
        count = 4

        decomposition = decompose(number, count)

        self.assertEqual(list, type(decomposition))
        self.assertEqual(count, len(decomposition))
        self.assertEqual(number, sum(decomposition))

    def test_decompose_invalid_input(self):
        number = 4
        count = 16

        with self.assertRaises(ValueError):
            decompose(number, count)


class CreatePasswordTestCase(unittest.TestCase):
    def test_create_password(self):
        list_of_parts = ["1234", "abcde", "ABCDEFG"]
        list_of_lengths = [3, 1, 2]

        password = create_password(list_of_parts, list_of_lengths)

        self.assertEqual(str, type(password))
        self.assertEqual(sum(list_of_lengths), len(password))
        for part, length in zip(list_of_parts, list_of_lengths):
            self.assertEqual(length, len([ch for ch in password if ch in part]))

    def test_create_password_invalid_list_of_parts_type(self):
        list_of_parts = ("1234", "abcde", "ABCDEFG")
        list_of_lengths = [3, 1, 2]

        with self.assertRaises(TypeError):
            create_password(list_of_parts, list_of_lengths)

    def test_create_password_invalid_list_of_lengths_type(self):
        list_of_parts = ["1234", "abcde", "ABCDEFG"]
        list_of_lengths = (3, 1, 2)

        with self.assertRaises(TypeError):
            create_password(list_of_parts, list_of_lengths)

    def test_create_password_invalid_input_length(self):
        list_of_parts = ["1234", "abcde", "ABCDEFG"]
        list_of_lengths = [3, 1, 2, 2]

        with self.assertRaises(ValueError):
            create_password(list_of_parts, list_of_lengths)


if __name__ == '__main__':
    unittest.main()
