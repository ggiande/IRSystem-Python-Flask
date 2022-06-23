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
    def print_word_contents(cls, *args):
        """
        Special method that prints all the contents
        of a specific word
        :param list:
        :param word: Word instance
        :return: None
        """
        print("|| In Utility Method ||")
        for word in args:
            print("String: ", word[0].text_value_content)
            print("Docs: ", word[0].relevant_docs_content)
            print("num occurrences: ", word[0].num_occurrences_content, "\n")
