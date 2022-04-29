# An implementation for the IRSystemABC class
# This class will take the list of files, open them,
# process the words in the files, and build the IRSystem
import os
# TODO: Create test cases, create the main class

from IRSystemABC import IRSystemABC
from word import Word


class IRSystem(IRSystemABC):
    """
    IRSystem Model that inherits behavior from IRSystem ABC
    list_files: contains the list of files that the system is built upon
    list_words: the list of words inside the files. Each entry is of type word
    """

    def __init__(self):
        """
        Special method that replaces a constructor/__new()__, we super because we override methods from
        IRSystemABC
        """
        super().__init__()

    def build_system(self, list_files):
        """
        Fully processes the files for us
        """
        # TODO: try catch that os works for curr dir
        print("in build system")
        cwd = os.getcwd()
        os.chdir('kivy_venv/docs')

        self.list_files = list_files
        for file_path in self.list_files:
            with open(file_path) as file:  # open file
                for line in file:  # iterate through all lines (words) in the file
                    line = line.strip('\n')  # remove the trailing newlines

                    # Check if the word exists in the list of words
                    entry = self.word_search(line)
                    # If the word was encountered before, then we need to increment the count
                    # then check if the file we are working in was encountered before
                    # with for that word
                    if len(entry):
                        entry[0].count += 1
                        entry_file = [f for f in entry[0].list_files if f[0] == file_path]
                        # If the file was encountered before, increment the counter for that file
                        if len(entry_file):
                            entry_file[0][1] += 1
                        # If it was not encountered before, then add this file to that word
                        else:
                            entry[0].list_files.append([file_path, 1])
                    # if we did not encounter this word before, then add it to the list of words
                    else:
                        # relevant_docs: [str] = None,
                        # text_value: str = None,
                        # word_snippets: [str] = None,
                        # num_occurrences: int = 0) -> None:
                        word = Word(line, 1)
                        word._relevant_docs.append([file_path, 1])
                        self.list_words.append(word)
        print("Restoring the path")
        os.chdir(cwd)
        super().words_total_count()

    def word_search(self, word):
        """
        Helper method for build_system method
        """
        return [w for w in self.list_words if w.word == word]

    def query_search(self, query):
        """
        Method returns data associated with Word
        """
        words = query.split()
        results_files = []

        # search for each word in the query and return the list of files for that word
        for w in words:
            word_search = self.word_search(w)
            # if the word exists, then add the list of files to the results
            if len(word_search):
                results_files.append(word_search[0].get_list_of_files())

        # overlap all the lists for the words then return only the overlap
        # if there is no overlap, then the list will be empty
        overlap = []
        if len(results_files):
            overlap = set(results_files[0]).intersection(*results_files[1:])
        return overlap

    def word_frequency(self, word) -> int:
        """
        Returns the frequency of a word
        If the word does not exist, then it returns a -1
        :param word: word used to find its own number of occurrences
        :return: frequency/number of occurrences
        """
        entry = self.word_search(word)
        if len(entry):
            return (entry[0].count * 100 / self.total)
