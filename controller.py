from typing import List

from word import Word


class Controller:
    all_words = List["Word"]
    """
    Controller stores business logic between Word
    and the Kivy Interface
    """

    def __init__(self):
        """
        Special method that replaces a constructor/__new()__
        :param relevant_docs: [str] List of document names where the word has appeared
        :param num_occurrences: int The number of times this specific word has been spotted
        :param text_value: str Literal string for searching
        :param word_snippets: [str] List of words near each instance of word    
        """

    word = Word()
    word.text_value = "Golden"
    search_document(word)

    # read, organize the data, then another function should search an organized piece of data
    # preprocess the data, put file data into a list

    # inefficient traversal a file
    def search_document(self, word) -> None:
        # Determine if the string is inside the file
        string1 = word.text_value
        filename = "ggiande:README.md"
        # opening a file and uses r for recurisve
        file1 = open(filename, "r")
        # read file content
        readfile = file1.read()
        # checking condition for string found or not
        if string1 in readfile:
            print('String', string1, 'Found In File')
        else:
            print('String', string1, 'Not Found')
            # closing a file
        file1.close()

# Parse the input into a list of words
# Search for the words in documents
# Store the results of word in Word

# send email to hatem to send me the code for processing a document
