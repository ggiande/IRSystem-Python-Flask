from typing import List, Any

from service.impl.IRSystem import IRSystem
import os
from model.result import Result
from utils.constant import Constant
# read, organize the data, then another function should search an organized piece of data
# Controller should get called after UI finishes building to pre-process the data
from utils import Utility


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

    def process_files(self) -> None:
        """
        Pre Process a list of files using the IRSystem
        :return: None
        """
        arr = os.listdir(Constant.DATA_FOLDER)
        self.irsystem.build_system(arr)

    def retrieve_data(self, word: str) -> str:
        """
        Given word from input, returns available data to user
        :return: json string
        """
        query = list(self.irsystem.query_search(word))
        freq = self.irsystem.word_frequency(word)
        response = Result(query, freq, word)
        Utility.print_response_contents(response)
        return response.toJSON()

    def get_lucky_list(self):
        return self.irsystem.list_words
