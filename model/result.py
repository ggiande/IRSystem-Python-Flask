import json


class Result:
    """
    """
    def __init__(self,
                 list_relevant_docs: [str],
                 frequency: int,
                 text_string: str
                 ) -> None:
        super().__init__()
        self._list_relevant_docs = list_relevant_docs
        self._frequency = frequency
        self._text_string = text_string

    @property
    def text_string_content(self) -> str:
        return self._text_string

    @text_string_content.setter
    def text_string_content(self, value: str) -> None:
        self._text_string = value

    @property
    def list_relevant_docs_content(self) -> [str]:
        """
        """
        return self._list_relevant_docs

    @list_relevant_docs_content.setter
    def list_relevant_docs_content(self, value: [str]) -> None:
        """
        Sets the text value property of the word
        :param value:
        """
        self._list_relevant_docs = value

    @property
    def frequency_content(self) -> int:
        return self._frequency

    @frequency_content.setter
    def frequency_content(self) -> int:
        return round(self._frequency, 2)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
