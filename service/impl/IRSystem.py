# An implementation for the IRSystemABC class
# This class will take the list of files, open them,
# process the words in the files, and build the IRSystem
import os
import re
import sys

from utils import Utility
from service.IRSystemABC import IRSystemABC
from model.word import Word
from utils import Constant


def change_directory_files(cwd: str):
    """
    Static Method cannot be tested, out of scope. Helper method
    achieves changing directory using OS.
    :param cwd: a string representation of the directory in which to change to
    :return: None
    """
    try:
        os.chdir(cwd)
    except OSError:
        print("Something wrong with specified\
              directory. Exception- ", sys.exc_info())


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
        self.utility = Utility()

    def build_system(self, list_files: [str]) -> None:
        """
        Fully processes the files for IRSystem
        """
        cwd = os.getcwd()
        # Change into directory
        change_directory_files('data')
        self.list_files = list_files

        for file_path in self.list_files:
            # 1st document, run a different iteration than below
            with open(file_path, encoding="utf8", errors='ignore') as file_build_word:  # open file
                word_list = []  # Retrieves all the words from a line
                for line in file_build_word:  # iterate through all lines in the
                    line = re.sub("[^a-zA-Z0-9\s]+", " ",
                                  line).lower()  # file and store single words comma separated in an array
                    line = line.split()
                    word_list += line

                # Sends a word into word_search
                for single_word in word_list:  # iterate through single words
                    # Check if the word exists in the list of words
                    entry = self.word_search(single_word)
                    # If the word was encountered before, then we need to increment the count
                    # then check if the file we are working in was encountered before
                    # with for that word
                    if len(entry):  # entry = Word
                        entry[0].num_occurrences_content += 1
                        # One doc, if doc is from the current file, add it to the list of entries
                        # ALWAYS RETURNS EMPTY
                        entry_file_list = [f for f in entry[0].relevant_docs_content if f[0] == file_path]
                        # If the file was encountered before, increment the counter for that file
                        if len(entry_file_list):
                            print("We have encountered this file before")
                            entry_file_list[0][1] += 1
                        # If it was not encountered before, then add  this file to that word
                        else:
                            # print("We have not encountered this file before")
                            entry[0].relevant_docs_content = [file_path]
                    # if we did not encounter this word before, then add it to the list of words
                    else:
                        word = Word(single_word, 1)
                        word.relevant_docs.append([file_path])
                        self.list_words.append(word)
                file_build_word.seek(0)
                word_list_for_snippets = []  # Retrieves all the words from a line
                for line in file_build_word:  # iterate through all lines in the
                    line = re.sub("[^a-zA-Z0-9\s]+", " ",
                                  line).lower()  # file and store single words comma separated in an array
                    line = line.split()
                    word_list_for_snippets += line
                # print(word_list_for_snippets)
                self.sliding_window(word_list_for_snippets)  # Implements word snippets

            # After looking at the first file, we expect the words to already have instances. Iterate
            # through the word_snippets, at each middle point, we can add the list of words to that word.
            # file_build_word.close()
        change_directory_files(cwd)  # revert directory

        super().words_total_count()
        print("Completed processing all files")

    # Note at this time, it voids 4 words in each file
    def sliding_window(self, list_string_of_doc: [str]) -> None:
        """
        Helper method for build_system
        Implements the sliding window algorithm for the
        collection of word snippets
        :param list_string_of_doc: the list of files to traverse
        :return:
        """
        snips_list = list(zip(*[list_string_of_doc[i:] for i in range(Constant.SLIDING_WINDOW_SIZE)]))
        # print("sliding_window -> snips_list: ", snips_list)

        for dummy in snips_list:
            # print("sliding_window -> dummy: ", dummy)
            middle_int = int(len(dummy) / 2)
            middle_word = dummy[middle_int]

            word_search = self.word_search(middle_word)  # holds a list of the instance of Word
            # if the word exists, then do some logic
            if len(word_search):
                current_word = word_search[0]
                # print("sliding_window -> current word: ", current_word.text_value_content)
                current_word.word_snippets.append(dummy)
                # print("sliding_window -> current word: ", current_word.text_value_content)

    def word_search(self, word: str) -> list[Word]:
        """
        Helper method for build_system
        Searches if a string is in other instances of Word
        If so, it collects a list of words
        :return: list of word instance
        """
        w_list = []
        for w in self.list_words:
            if w.text_value_content == word:
                w_list.append(w)
        return w_list

    # TODO: Fix so specific queries can return ALL possible results and not a union
    def query_search(self, query: str) -> [str]:
        """
        Method returns relevant docs associated with Word
        :param query can be a word or words to look for in the processed files
        :return an overlap list of strings
        """
        print("|| Query Search ||")
        words = re.sub("[^a-zA-Z0-9\s]+", " ", query)
        words = words.split()
        results_files = []

        # search for each word in the query and return the list of files for that word
        for dummy in words:  # Strings
            word_search = self.word_search(dummy)  # holds a list of the instance of Word
            # if the word exists, then add the list of files to the results
            if len(word_search):
                results_files.append(word_search[0].relevant_docs_content)

        # overlap all the lists for the words then return only the overlap(INNER JOIN)
        # if there is no overlap, then the list will be empty
        overlap = []
        if len(results_files):
            overlap = set(results_files[0]).union(*results_files[1:])
        return overlap

    # TODO: Investigate bug where word frequency returns different results depending on how many times a word is
    #  looked up AND why "iron-heart" -> "iron" "heart" do not return values
    def word_frequency(self, query_freq: str) -> int:
        """
        Returns the frequency of a word
        If the word does not exist, then it returns a -1
        entry is a list
        :param query_freq: string used to find its own number of occurrences
        :return: frequency/number of occurrences as an integer
        """
        words = re.sub("[^a-zA-Z0-9\s]+", " ", query_freq)
        words = words.split()
        entry = []
        for dummy in words:  # Strings
            entry = self.word_search(dummy)  # a list of Word
        if len(entry):
            return entry[0].num_occurrences_content * 100 / self.total

    def word_snippets_collection(self, query_snips: str) -> [str]:
        """
        Helper method for build_system
        Searches if a string is in other instances of Word
        If so, it collects a list of word snippets found in documents
        :return: list of word_snippets as an array of strings
        """
        words = re.sub("[^a-zA-Z0-9\s]+", " ", query_snips)
        words = words.split()
        results_snips = []
        for dummy in words:  # Strings
            word_search = self.word_search(dummy)  # holds a list of the instance of Word
            if len(word_search):
                results_snips.append(word_search[0].word_snippets_content)
        return results_snips
