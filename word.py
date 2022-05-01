from __future__ import annotations


class Word:
    """
    Word Model
    # The list of files containing the word and count of appearances, the word, a lit of words near the word, count of
    # occurrences of word in all files
    """

    def __init__(self,
                 text_value: str,
                 num_occurrences: int,
                 ) -> None:
        """
        Special method that replaces a constructor/__new()__
        # :param relevant_docs: [str] List of document names where the word has appeared
        :param num_occurrences: int The number of times this specific word has been spotted
        :param text_value: str Literal string for searching
        """
        self.relevant_docs = []
        self._text_value = text_value
        self._num_occurrences = num_occurrences

    @property
    def relevant_docs_content(self) -> [str]:
        """
        This is a list of documents that are relevant to our word
        :param self instance of Word
        :return: str returns the _relevant_docs of the word
        """
        # print(f"Getting the list of relevant documents for {self._text_value}")
        return [f[0] for f in self.relevant_docs]

    @relevant_docs_content.setter
    def relevant_docs_content(self, docs: [str]) -> None:
        """
        Sets a new list of _relevant_docs for a word in Word
        :param self instance of Word
        :param: docs the new list of relevant documents to replace _relevant_docs
        :return: None
        """
        # print(f"Setting a new list of relevant documents for {self._text_value}")
        self.relevant_docs.append(docs)

    @property
    def text_value_content(self) -> str:
        """
        This is the text value property of the word
        :param self instance of Word
        :return: str returns the _text_value of the word
        """
        # print(f"Getting the word: {self._text_value}")
        return self._text_value

    @text_value_content.setter
    def text_value_content(self, value: str) -> None:
        """
        Sets the text value property of the word
        :param self instance of Word
        :param: str value to replace the _text_value of the Word
        :return: None
        """
        # print(f"Setting {self._text_value} text value to {value!r}")
        self._text_value = value

    @text_value_content.deleter
    def text_value_content(self) -> None:
        """
        Removes the text_value of the Word
        :param self instance of Word
        :return: None
        """
        # print(f"Deleting {self._text_value} from Word")
        del self._text_value

    @property
    def num_occurrences_content(self) -> int:
        """
        Returns the num_occurrences of a Word
        :param self instance of Word
        :return: int returns the number of occurrences of the
        Word in all documents
        """
        # print(f"Getting the number of occurrences for {self._text_value}")
        return self._num_occurrences

    @num_occurrences_content.setter
    def num_occurrences_content(self, number: int) -> None:
        """
        Sets the num_occurrences for a word in Word
        :param self instance of Word
        :param number the number of occurrences of the
        Word in all documents
        """
        # print(f"Setting the number of occurrences for {self._text_value}")
        self._num_occurrences = number

    # num_occurrences_content, try to use it
    @num_occurrences_content.deleter
    def delete_num_occurrences(self) -> None:
        """
        Removes the _num_occurrences of the Word
        :param self instance of Word
        :return: None
        """
        # print(f"Deleting the number of occurrences for {self._text_value}")
        del self._num_occurrences

    # @property
    # def word_snippets_content(self) -> [str]:
    #     """
    #     Gets the list of word snippets for a word
    #     :param self: instance of Word
    #     :return: str[] returns a list of words near
    #     the word if found in other documents
    #     """
    #     print(f"Getting the list of word snippets for {self._text_value}")
    #     return self._word_snippets

    # @word_snippets_content.setter
    # def word_snippets_content(self, snippets: [str]) -> None:
    #     """
    #     Sets a new list of _word_snippets for a word in Word
    #     :param self instance of Word
    #     :param snippets the new list of word snippets to replace _word_snippets
    #     """
    #     print(f"Setting a new list of word snippets for {self._text_value}")
    #     self._word_snippets = snippets
    #
    # @word_snippets_content.deleter
    # def word_snippets_content(self) -> None:
    #     """
    #     Removes the list of word snippets from Word
    #     :param self instance of Word
    #     :return: None
    #     """
    #     del self._word_snippets
