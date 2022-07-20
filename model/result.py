import json


class Result:

    def __init__(self,
                 list_relevant_docs: [str],
                 frequency: int,
                 text_string: str,
                 word_snippets: [str]
                 ) -> None:
        super().__init__()
        self._list_relevant_docs = list_relevant_docs
        self._frequency = frequency
        self._text_string = text_string
        self._word_snippets = word_snippets

    @property
    def word_snippets_content(self) -> [str]:
        # print("IN RES -> GETTER: ", self.word_snippets_content)
        return self._word_snippets

    @word_snippets_content.setter
    def word_snippets_content(self, snips_list: [str]) -> None:
        # if self.word_snippets_content is not None:
        #     del self._word_snippets
        # print("IN RES -> ", self.word_snippets_content)
        self._word_snippets.append(snips_list)

    @word_snippets_content.deleter
    def word_snippets_content(self) -> None:
        del self._word_snippets

    @property
    def text_string_content(self) -> str:
        return self._text_string

    @text_string_content.setter
    def text_string_content(self, value: str) -> None:
        self._text_string = value

    @text_string_content.deleter
    def text_string_content(self) -> None:
        del self._text_string

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

    @list_relevant_docs_content.deleter
    def list_relevant_docs_content(self) -> None:
        self._list_relevant_docs

    @property
    def frequency_content(self) -> int:
        return self._frequency

    @frequency_content.setter
    def frequency_content(self) -> int:
        return round(self._frequency, 2)

    @frequency_content.deleter
    def frequency_content(self) -> None:
        del self._frequency

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
