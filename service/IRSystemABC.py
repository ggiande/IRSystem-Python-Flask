from abc import ABC, abstractmethod

from model import Word


class IRSystemABC(ABC):

    # The class contains two variables:
    # list_files: contains the list of files that the system
    # is built upon
    # list_words: the list of words inside the files. Each entry is of type word
    # total could be the number of words in the entire document

    @abstractmethod
    def __init__(self):
        self.list_files = []
        self.list_words = []
        self.total = 0

    # an abstract function that constructs the whole system
    @abstractmethod
    def build_system(self, list_files: [str]) -> None:
        pass

    # an abstract function that construct a sliding window and
    # returns a list of strings, allowing for the conversion to word_snippets
    @abstractmethod
    def sliding_window(self, list_string_of_doc: [str]) -> None:
        pass

    # an abstract method that searches for a single word
    # Input: word: a single word in the query we are looking for
    # Return: the list of files that contain that word
    @abstractmethod
    def word_search(self, word: str) -> list[Word]:
        pass

    # an abstract methods that searches for an input query
    # It searches for every word in the query and return the list of files
    # that contains the most amount of words. Returns the files containing the words
    # even if there is no overlap between the files
    # input: query: a collection of words that we want to look for, the words are space separated
    # It does not contain any stop words. e.g., chocolate banana sugar
    # Return: the list of files containing the query
    @abstractmethod
    def query_search(self, query: str) -> [str]:
        pass

    # an abstract method that returns how frequent a word is
    # in all the files
    # Input: word: the word we are looking for
    # Return: a number representing the frequency of that word
    @abstractmethod
    def word_frequency(self, query_freq: str) -> int:
        pass

    # counts the total number of words in all the files in order to calculate the
    # word frequency of each word
    def words_total_count(self):
        for word in self.list_words:
            self.total += word.num_occurrences_content
        # print(f"In abc:{self.total}")

    def list_of_words(self):
        """
        Returns a list of words stored in IRS.
        :return:
        """
        if self.list_words:
            return self.list_words

    # # String representation of the system
    def __str__(self):
        str_words = ''
        for word in self.list_words:
            str_words = str_words + str(word) + '\n'
        return str_words
