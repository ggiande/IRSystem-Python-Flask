from unittest import TestCase

from IRSystemABC import IRSystemABC
from utility import Utility
from IRSystem import IRSystem
from word import Word
from unittest.mock import Mock


def create_word_instance() -> Word:
    text_value = "Hello"
    num_occurrences = 3
    w = Word(text_value, num_occurrences)
    w.relevant_docs = ["Script1", "Script2"]
    return w


def create_word_list() -> list[Word]:
    w1 = create_word_instance()
    w2 = create_word_instance()
    w2.text_value_content = "World"
    w2.num_occurrences_content = 2
    w2.relevant_docs = ["Script1", "Script2"]
    list_of_word = [w1, w2]
    return list_of_word


class TestIRSystem(TestCase):
    mock = Mock()

    def test_build_system(self):
        self.fail()

    def test_word_search(self):
        """
        Check to see if a string is already in a Word Instance
        """
        irs = IRSystem()
        irs.list_words = []
        w_expected_one = Word("Hello", 3)
        w_expected_one.relevant_docs.append(["S", 1])
        irs.list_words.append(w_expected_one)
        list_expected = [w_expected_one]
        self.assertEqual(list_expected, irs.word_search("Hello"))

    def test_query_search(self):
        # Do Two Can
        self.fail()

    def test_word_frequency(self):
        """
        Matches the frequency of the occurrences of a word
        """
        irs = IRSystem()
        irs.list_words = []
        w_expected_one = Word("Hello", 3)
        w_expected_one.relevant_docs.append(["S", 1])
        irs.list_words.append(w_expected_one)
        irs.total = 3
        self.assertEqual(100, irs.word_frequency("Hello"))
