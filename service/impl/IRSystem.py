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


def change_directory_files(cwd):
    try:
        os.chdir(cwd)
        print("Inserting inside-", os.getcwd())
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
        snips = []  # list of strings used for word_snippets

        for file_path in self.list_files:

            # 1st document, run a different iteration than below
            with open(file_path, encoding="utf8", errors='ignore') as file:  # open file

                word_list = []  # Retrieves all the words from a line
                for line in file:  # iterate through all lines in the
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

        # TODO: ADD Word Snippets Implementation
        for file_path in self.list_files:

            # Open a file and read it
            with open(file_path, encoding="utf8", errors='ignore') as file:
                word_list = []  # Retrieves all the words from a line
                for line in file:  # iterate through all lines in the
                    line = re.sub("[^a-zA-Z0-9\s]+", " ",
                                  line).lower()  # file and store single words comma separated in an array
                    line = line.split()
                    word_list += line

            self.sliding_window(word_list)  # Implements word snippets
        #     After looking at the first file, we expect the words to already have instances. Iterate
        # through the word_snippets, at each middle point, we can add the list of words to that word.

        change_directory_files(cwd)  # revert directory

        super().words_total_count()
        print("Completed processing all files")
        print("Word Snippets: ", snips)

        # for item in self.list_words.retrieve_word_list:
        # DO NOT REMOVE BELOW, USED TO REFERENCE AN OBJECT
        # for w in self.list_words:
        #     print(w.text_value_content)

    # Note at this time, it voids 4 words in each file
    def sliding_window(self, list_string_of_doc: [str]) -> None:
        snips_list = list(zip(*[list_string_of_doc[i:] for i in range(Constant.SLIDING_WINDOW_SIZE)]))

        for dummy in snips_list:
            middle_int = int(len(dummy) / 2)
            middle_word = dummy[middle_int]
            word_search = self.word_search(middle_word)  # holds a list of the instance of Word

            # if the word exists, then do some logic
            if len(word_search):
                current_word = word_search[0].relevant_docs_content
                current_word.word_snippets_content(dummy)

    def word_search(self, word: str) -> list[Word]:
        """
        Helper method for build_system
        Searches if a string is in other instances of Word
        If so, it collects a list of words
        :return: list of word instance
        """
        # print("|| In Word Search ||")
        return [w for w in self.list_words if w.text_value_content == word]

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
        print(f"Inside IRSystem, QUERY SEARCH Function, Words: {words}")
        results_files = []

        # search for each word in the query and return the list of files for that word
        for dummy in words:  # Strings
            word_search = self.word_search(dummy)  # holds a list of the instance of Word
            # Utility.print_word_contents(word_search)
            # print("Word Instance in Query: ", word_search[0].num_occurrences_content)
            # if the word exists, then add the list of files to the results
            if len(word_search):
                #     one_doc = Utility.collect_one_relevant_document(self)
                # results_files.append(word_search[0].one_doc) # references
                # print("WordSearch[0]:", {Utility.print_word_contents(word_search[0])})
                # print(len(word_search))
                # grabs first element of the list (Word.relevant_docs_content)
                # print("WordSearch[0].relevant_docs_content:", {word_search[0].relevant_docs_content})
                results_files.append(word_search[0].relevant_docs_content)

        # overlap all the lists for the words then return only the overlap(INNER JOIN)
        # if there is no overlap, then the list will be empty
        overlap = []
        if len(results_files):
            # overlap = set(results_files[0]).intersection(*results_files[1:])
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
        print("|| Word Frequency ||")
        words = query_freq.split()
        entry = []
        for dummy in words:  # Strings
            entry = self.word_search(dummy)  # a list of Word
        if len(entry):
            # print(f"num occur: {entry[0].num_occurrences_content * 100 / self.total} and the total is: {self.total}")
            return entry[0].num_occurrences_content * 100 / self.total
        # else:
        #     print("No results found in word_search when checking for word_frequency")
