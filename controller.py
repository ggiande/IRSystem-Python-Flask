
class Controller(object):
    """
    Controller stores business logic between Word
    and the Kivy Interface
    """
    def __init__(self, word, view):
        self.word = word
        self.view = view

        """
        Special method that replaces a constructor/__new()__
        :param relevant_docs: [str] List of document names where the word has appeared
        :param num_occurrences: int The number of times this specific word has been spotted
        :param text_value: str Literal string for searching
        :param word_snippets: [str] List of words near each instance of word
        """

    def search_documents(self, word: isinstance("Word")) -> None:
        pass

    def send_documents(self) -> None:
        pass

