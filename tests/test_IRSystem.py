from unittest import TestCase
from service.impl.IRSystem import IRSystem
from model.word import Word
from unittest.mock import Mock, MagicMock


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
        irs = IRSystem()
        irs.build_system = MagicMock(name='method')
        irs.build_system("AMD-Chip-on-Android-Studio:README.md")
        self.assertEqual(irs.build_system.call_count, 1)

    def test_sliding_window(self):
        irs = IRSystem()
        w_expected_one = Word("now", 1)
        irs.list_words.append(w_expected_one)
        irs.sliding_window(
            ['https', 'packagephobia', 'now', 'sh', 'badge', 'p', 'node', 'fetch', 'https', 'packagephobia', 'now',
             'sh', 'result', 'p', 'node', 'fetch', 'phin', 'phin', 'package', 'size', 'https', 'packagephobia', 'now',
             'sh', 'badge', 'p', 'phin', 'https', 'packagephobia', 'now', 'sh', 'result', 'p', 'phin'])
        self.assertEqual(('https', 'packagephobia', 'now', 'sh', 'badge'), w_expected_one.word_snippets[0])

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
        irs = IRSystem()
        irs.list_words = []
        w_expected_one = Word("Hello", 3)
        w_expected_one.relevant_docs.append(["S", 1])
        w_expected_one.relevant_docs.append(["S1", 1])
        w_expected_one.relevant_docs.append(["S1", 1])
        w_expected_one.relevant_docs.append(["S2", 1])
        irs.list_words.append(w_expected_one)
        self.assertEqual({"S", "S1", "S2"}, irs.query_search("Hello"))

    def test_query_search_phrase(self):
        irs = IRSystem()
        irs.list_words = []
        w_expected_one = Word("Two", 2)
        w_expected_one.relevant_docs.append(["S", 1])
        w_expected_one.relevant_docs.append(["S1", 1])
        w_expected_two = Word("Can", 2)
        w_expected_two.relevant_docs.append(["S", 1])
        w_expected_two.relevant_docs.append(["S_Can2", 1])
        irs.list_words.append(w_expected_one)
        irs.list_words.append(w_expected_two)
        self.assertEqual({"S"}, irs.query_search("Two Can"))

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

    def test_word_snippets_collection(self):
        irs = IRSystem()
        irs.list_words = []
        w_expected_one = Word("Hello", 3)
        w_expected_one.relevant_docs.append(["S", 1])
        w_expected_one.word_snippets.append("Hello I am Gian")
        irs.list_words.append(w_expected_one)
        irs.total = 3
        self.assertEqual(["Hello I am Gian"], irs.word_snippets_collection("Hello")[0])
