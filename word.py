class Word:
    """
    Word that Kivy requires displaying to the Screen Manager
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

        self.relevant_docs = relevant_docs
        self.text_value = text_value
        self.word_snippets = word_snippets
        self.num_occurrences = num_occurrences

    def clear_word(self) -> None:
        """
        Clears the assignment of text_value to an empty string
        :param self: instance of Word
        :return: None
        """
        self.text_value = ""
