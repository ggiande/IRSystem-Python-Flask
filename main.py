from controller.controller1 import Controller1
from flask import Flask
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)


@app.route("/ping", methods=['GET'])
def ping_health_check():
    print("|| FLASK -> Ping Endpoint ||")
    from flask import jsonify
    resp = jsonify(success=True)
    return resp


@app.route("/example", methods=['GET'])
def query_example() -> str:
    print("FLASK -> Example Endpoint")
    word = "cannon"
    response = first_call(word)
    return response


@app.route("/query/<string:word>", methods=['POST', 'GET'])
def adhoc_query(word: str) -> str:
    print("FLASK -> adhoc_query Endpoint")
    response = callback(word)
    return response


@app.route("/lucky")
def query_lucky_word() -> str:
    print("FLASK -> query_lucky_word Endpoint")
    c = Controller1()
    list_text_of_words = c.get_lucky_list()
    random_word = random.choice(list_text_of_words)  # holds a word
    word = random_word.text_value_content
    response = callback(word)
    return response


def first_call(word: str) -> str:
    """
    Calls the element/widget after processing the input specifically for the text widget.
    This REQUIRES the instance to be passed as an argument, code breaking without.
    :param: self: instance of Main
    :return: No Return
    """

    if word.strip():
        print("|| FIRST CALL ||")
        # print("Input:", word)
        c = Controller1()
        c.process_files()
        response = c.retrieve_data(word.lower())
        if response is not None:
            return response
        else:
            print("No Response")


def callback(word: str) -> str:
    """
    Calls the element/widget after processing the input specifically for the text widget.
    This REQUIRES the instance to be passed as an argument, code breaking without.
    :param: self: instance of Main
    :return: No Return
    """
    if word.strip():
        print("|| CALLBACK ||")
        c = Controller1()
        response = c.retrieve_data(word.lower())
        if response is not None:
            return response
        else:
            print("No Response")


if __name__ == "__main__":
    app.run()
