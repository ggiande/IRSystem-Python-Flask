import unittest
from model.word import Word


class TestWord(unittest.TestCase):

    def test_initial_value(self):
        self.setUpClass()
        word = Word("Hello", 1)
        assert word.text_value_content == "Hello"
        assert word.num_occurrences_content == 1

    def test_text_value_content(self):
        word = Word("Hello", 1)
        self.assertEqual("Hello", word.text_value_content)
        word.text_value_content = "World"
        self.assertEqual("World", word.text_value_content)
        del word.text_value_content
        with self.assertRaises(AttributeError):
            word.text_value_content

    def test_num_occurrences_content(self):
        word = Word("Hello", 1)
        self.assertEqual(1, word.num_occurrences_content)
        word.num_occurrences_content = 2
        self.assertEqual(2, word.num_occurrences_content)

    def test_relevant_docs_content(self):
        word = Word("Hello", 1)
        word.relevant_docs = ["ABC", "DEF"]
        self.assertEqual(["A", "D"], word.relevant_docs_content)


if __name__ == '__main__':
    unittest.main()
