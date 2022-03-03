import unittest
from word import Word

# TODO: Add docstrings
class TestWord(unittest.TestCase):

    def test_initial_value(self):
        word1 = Word(["Hello"], "Hello World", ["Snippet One", "Snippet Two"], 1)
        assert word1.relevant_docs == ["Hello"]
        assert word1.text_value == "Hello World"
        assert word1.word_snippets == ["Snippet One", "Snippet Two"]
        assert word1.num_occurrences == 1

    def test_clear_word(self):
        word1 = Word(["Hello"], "Hello World", ["Snippet One", "Snippet Two"], 1)
        self.assertEqual(word1.clear_word(), "")
#         None = ""


if __name__ == '__main__':
    unittest.main()
