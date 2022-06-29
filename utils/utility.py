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
        :param args: Word instance or list of Word instances
        :return: None
        """
        print("|| In Utility Method ||")
        for word in args:
            # print(word[0].text_value_content)
            print("String: ", word.text_value_content)
            print("Docs: ", word.relevant_docs_content)
            print("num occurrences: ", word.num_occurrences_content, "\n")

    @classmethod
    def print_response_contents(cls, *args):
        """
        Special method that prints all the contents
        of a specific word
        :param args: Response instance or list of Responses instances
        :return: None
        """
        print("|| In Utility Method ||")
        for res in args:
            print("list_relevant_docs: ", res.list_relevant_docs_content)
            print("frequency: ", res.frequency_content)
            print("text_string: ", res.text_string_content, "\n")
