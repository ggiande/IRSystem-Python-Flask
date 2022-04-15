from abc import ABC, abstractmethod


class IRSystemABC(ABC):

    # The class contains two variables:
    # list_files: containts the list of files that the system
    # is built upon
    # list_words: the list of words inside the files. Each entry is of type word

    @abstractmethod
    def __init__(self):
        self.list_files = []
        self.list_words = []
        self.total = 0

    # an abstract function that constructs the whole system
    @abstractmethod
    def build_system(self, list_files):
        pass

    # an abstract method that searchs for a single word
    # Input: word: a single word in the query we are looking for
    # Return: the list of files that contain that word
    @abstractmethod
    def word_search(self, word):
        pass

    # an abstract methods that searchs for a input query
    # It searches for every word in the query and return the list of files
    # that contains the most amount of words. Returns the files containing the words
    # even if there is no overlap between the files
    # input: query: a collection of words that we want to look for, the words are space separated
    # It does not contain any stop words. e.g., chocolate banana sugar
    # Return: the list of files containing the query
    @abstractmethod
    def query_search(self, query):
        pass

    # an abstract method that returns how frequent a word is
    # in all the files
    # Input: word: the word we are looking for
    # Return: a nunber representing the frequency of that word
    @abstractmethod
    def word_frequency(self, word):
        pass

    # counts the total number of words in all the files in order to calculate the
    # word frequency of each word
    def words_total_count(self):
        for word in self.list_words:
            self.total += word.count

    # String representation of the system

    def __str__(self):
        str_words = ''
        for word in self.list_words:
            str_words = str_words + str(word) + '\n'
        return str_words
