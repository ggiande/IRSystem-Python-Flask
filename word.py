from __future__ import annotations


class Word:
    all_words = list["Word"]
    """
    Word Model
    """

    def __init__(self,
                 relevant_docs: [str] = None,
                 text_value: str = None,
                 word_snippets: [str] = None,
                 num_occurrences: int = 0) -> None:
        """
        Special method that replaces a constructor/__new()__
        :param relevant_docs: [str] List of document names where the word has appeared
        :param num_occurrences: int The number of times this specific word has been spotted
        :param text_value: str Literal string for searching
        :param word_snippets: [str] List of words near each instance of word
        """
        Word.all_words.append(self)
        self.relevant_docs = relevant_docs
        self.text_value = text_value
        self.word_snippets = word_snippets
        self.num_occurrences = num_occurrences

    def read_word(self) -> str:
        """
        :param self: instance of Word
        :return: str returns the text of the word
        """
        return self.text_value

    def read_num_occurrences(self) -> int:
        """
        :param self: instance of Word
        :return: int returns the number of occurrences of the
        word in all documents
        """
        return self.num_occurrences

    def read_word_snippets(self) -> [str]:
        """
        :param self: instance of Word
        :return: str[] returns a list of words near
        the word if found in other documents
        """
        return self.word_snippets

    def delete_word_value(self) -> None:
        """
        Clears the assignment of text_value to an empty string
        :param self: instance of Word
        :return: None
        """
        self.text_value = ""

    def delete_num_occurrences(self) -> None:
        """
        Clears the assignment of num_occurrences to None
        :param self: instance of Word
        :return: None
        """
        self.num_occurrences = None
