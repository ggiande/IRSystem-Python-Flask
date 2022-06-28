from controller.controller1 import Controller1
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
c = Controller1()


@app.route("/hi")
def hello_world():
    # callback()
    print("Accessing HI")
    name = "Gian"
    hobby = "coding"
    return {
        "followings": [
            {
                "name": name,
                "hobby": hobby
            }
        ]
    }


def callback() -> None:
    """
    Calls the element/widget after processing the input specifically for the text widget.
    This REQUIRES the instance to be passed as an argument, code breaking without.
    :param: self: instance of Main
    :return: No Return
    """
    # Get an input
    word = "cannon"

    if word.strip():
        # self.greeting.text = "Checking to see if " + self.user.text + " is in stock!"
        print("|| Main ||")
        print("Input:", word)
        data = c.retrieve_data(word.lower())
        print(f"Data Retrieved:{data}")

        if data[0] is None:
            print("Data is None and No Data Found")
            # self.greeting.text = "No Data Found With That Entry ;/"
        elif data[0] is not None:
            # Convert the long number to usable number
            percentage = round(data[0], 2)
            print(percentage)

    else:
        print("Empty is not a valid entry!")
        # self.greeting.text = "Empty is not a valid entry!"


if __name__ == "__main__":
    app.run()
