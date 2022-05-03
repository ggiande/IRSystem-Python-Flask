import unittest
from word import Word

# TODO: Add docstrings and REDO all function call
class TestWord(unittest.TestCase):

    def test_initial_value(self):
        self.setUpClass()
        word1 = Word(["Hello"], "Hello World", ["Snippet One", "Snippet Two"], 1)
        assert word1.relevant_docs == ["Hello"]
        assert word1.text_value == "Hello World"
        assert word1.word_snippets == ["Snippet One", "Snippet Two"]
        assert word1.num_occurrences == 1

    def test_read_word_text_value(self):
        word1 = Word(["Hello"], "Hello World", ["Snippet One", "Snippet Two"], 1)
        self.assertEqual(word1.read_word_text_value(), word1.text_value)

    def test_delete_word_text_value(self):
        word1 = Word(["Hello"], "Hello World", ["Snippet One", "Snippet Two"], 1)
        self.assertEqual(word1.delete_word_text_value(), word1.read_word_text_value())

    def test_read_num_occurrences(self):
        word1 = Word(["Hello"], "Hello World", ["Snippet One", "Snippet Two"], 1)
        self.assertEqual(word1.read_num_occurrences(), word1.num_occurrences)

    def test_delete_num_occurrences(self):
        word1 = Word(["Hello"], "Hello World", ["Snippet One", "Snippet Two"], 1)
        self.assertEqual(word1.delete_num_occurrences(), word1.read_num_occurrences())

    def test_read_word_snippets(self):
        word1 = Word(["Hello"], "Hello World", ["Snippet One", "Snippet Two"], 1)
        self.assertEqual(word1.read_word_snippets(), word1.word_snippets)

    def test_delete_word_snippets(self):
        word1 = Word(["Hello"], "Hello World", ["Snippet One", "Snippet Two"], 1)
        self.assertEqual(word1.delete_word_snippets(), word1.read_word_snippets())


if __name__ == '__main__':
    unittest.main()
