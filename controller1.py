from IRSystem import IRSystem
import os


class Controller1:
    """
    Controller stores business logic between Word
    and the Kivy Interface
    """

    def __init__(self) -> None:
        self.irsystem = IRSystem()
        """
        Special method that replaces a constructor/__new()__
        :param relevant_docs: [str] List of document names where the word has appeared
        :param num_occurrences: int The number of times this specific word has been spotted
        :param text_value: str Literal string for searching
        :param word_snippets: [str] List of words near each instance of word    
        """

    # read, organize the data, then another function should search an organized piece of data
    # Controller should get called after UI finishes building to pre process the data

    def list_of_files(self):
        """
        Retrieves a list of files to be processed by the IRSystem
        :return: None
        """
        arr = os.listdir('kivy_venv/docs')
        print(f"Here are all the files: {arr}")
        self.irsystem.build_system(arr)
