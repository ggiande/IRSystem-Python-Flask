from unittest import TestCase
from utility import Utility
from IRSystem import IRSystem
from word import Word


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
    def test_build_system(self):
        self.fail()

    def test_word_search(self):
        """
        Check to see if a string is already in a Word Instance
        """
        irs = IRSystem()
        mock_list_words = create_word_list()

        w = create_word_instance()
        w.text_value_content = "Hello"
        w.num_occurrences_content = 4
        mock_list_words.append(w)

        # for x in list_words:
        #     Utility.print_word_contents(x)
        # Construct a list of expected
        w_expected_one = Word("Hello", 3)
        w_expected_two = Word("Hello", 4)
        w_expected_one.relevant_docs_content = ['S', 'S']
        w_expected_two.relevant_docs_content = ['S', 'S']
        list_expected = [w_expected_one, w_expected_two]

        self.assertEqual(list_expected, irs.word_search("Hello"))

    def test_query_search(self):
        self.fail()

    def test_word_frequency(self):
        self.fail()
