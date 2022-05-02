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
        """

    # read, organize the data, then another function should search an organized piece of data
    # Controller should get called after UI finishes building to pre process the data

    def process_files(self):
        """
        Pre Process a list of files using the IRSystem
        :return: None
        """
        arr = os.listdir('kivy_venv/movie_scripts')
        # print(f"Here are all the files: {arr}")
        self.irsystem.build_system(arr)

    def retrieve_data(self, word: str) -> [str]:
        """
        Given word from input, returns available data to user
        If data can be retrieved, do something
        :return:
        """
        # print(f"Controller: {word} Calling for word_freq and query_search")
        # print(type(self.irsystem.word_frequency(word)))
        return self.irsystem.word_frequency(word), self.irsystem.query_search(word)
