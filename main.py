from typing import Optional

from controller.controller1 import Controller1
from flask import Flask
from flask_cors import CORS

from model.response import Response
from utils import Utility

app = Flask(__name__)
CORS(app)
c = Controller1()


# Endpoint for an example
@app.route("/example")
def query_example() -> str:
    word = "cannon"
    response = callback(word)
    print("Accessing example")
    return response


# Endpoint for query
@app.route("/<string:word>")
def hello_world(word: str) -> str:
    print("Accessing async call")
    response = callback(word)
    return response


def callback(word: str) -> str:
    """
    Calls the element/widget after processing the input specifically for the text widget.
    This REQUIRES the instance to be passed as an argument, code breaking without.
    :param: self: instance of Main
    :return: No Return
    """
    if word.strip():
        print("|| Main ||")
        print("Input:", word)
        c.process_files()
        response = c.retrieve_data(word)
        if response is not None:
            # print("Got a Response")
            return response
        else:
            print("No Response")
    else:
        print("Empty is not a valid entry!")
        # self.greeting.text = "Empty is not a valid entry!"


if __name__ == "__main__":
    app.run()
