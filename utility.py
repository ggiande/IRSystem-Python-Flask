from word import Word


class Utility:
    """
    Utility stores functions used for logging
    purposes or helper functions
    """

    def __init__(self) -> None:
        """
        Special method that replaces a constructor/__new()__
        """

    @classmethod
    def print_word_contents(cls, word: Word):
        """
        Special method that prints all the contents
        of a specific word
        :param word: Word instance
        :return: None
        """
        # print("Printing a new Word")
        print("String: ", word.text_value_content, "|| ", "Docs: ",
              word.relevant_docs_content, "|| ", "num occurrences: ",
              word.num_occurrences_content, "\n")
        # print("Docs: ", word.relevant_docs_content)
        # print("# occurrences", word.num_occurrences_content, "\n")

