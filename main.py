from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from controller.controller1 import Controller1

c = Controller1()


class MainWindow(GridLayout):
    """
    The main controller of the Kivy framework for the initial window
    that inherits from the GridLayout.
    """

    def __init__(self, **kwargs):
        """
        Runs on initialization. Includes all the styling used to generate the initial window.
        Generates the widgets for the end user interaction.
        :param kwargs: pass a keyworded variable length of arguments upon initialization
        """
        super().__init__(**kwargs)

        self.window = GridLayout
        self.window.cols = 1
        self.window.size_hint = (0.60, 0.70)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.greeting = Label(
            text="Check to see if a self is in stock!",
            font_size=30,
            color='#00FFCE')
        self.add_widget(self.greeting)

        self.user = TextInput(
            multiline=False,
            padding_y=(20, 20),
            size_hint=(1, 0.5)
        )
        self.add_widget(self.user)

        # button widget
        self.button = Button(
            text="GREET",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#36424b'
        )
        # after creation of window
        # Begin the pre-processing of the files
        c.process_files()
        self.button.bind(on_press=self.callback)
        self.add_widget(self.button)

    def callback(self, instance) -> None:
        """
        Calls the element/widget after processing the input specifically for the text widget.
        This REQUIRES the instance to be passed as an argument, code breaking without.
        :param: instance: instance of the window
        :param: self: instance of MainWindow
        :return: No Return
        """
        word = self.user.text

        if word.strip():
            self.greeting.text = "Checking to see if " + self.user.text + " is in stock!"
            print("|| Main ||")
            print("Input:", word)
            data = c.retrieve_data(word.lower())
            print(f"Data Retrieved:{data}")

            if data[0] is None:
                print("Data is None and No Data Found")
                self.greeting.text = "No Data Found With That Entry ;/"
            elif data[0] is not None:
                # Convert the long number to usable number
                percentage = round(data[0], 2)
                print(percentage)
                self.greeting.text = "Checking to see if " + self.user.text + " is in stock!"
                instance_app.second_window.update_info(word, percentage, data[1])
                instance_app.screen_manager.current = "SecondWindow"
        else:
            self.greeting.text = "Empty is not a valid entry!"


class SecondWindow(GridLayout):
    """
    The main controller of the Kivy framework for the second window.
    """

    def __init__(self, **kwargs) -> None:
        """
        Generates the second window after input is acknowledged and processed.
        :param kwargs: pass a keyworded variable length of arguments upon initialization
        """
        super().__init__(**kwargs)
        self.cols = 1
        self.message = Label(
            width=100,
            font_size=30
        )
        self.word_frequency_content = Label(
            width=100,
            font_size=30
        )
        self.query_search_files_content = Label(
            width=100,
            font_size=30
        )

        # self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)
        self.add_widget(self.word_frequency_content)
        self.add_widget(self.query_search_files_content)

    def update_info(self, message: str, word_frequency_content: int, query_search_files_content: str) -> None:
        """
        Update's the information that processes the input
        :message:
        :word_frequency_content:
        :query_search_files_content:
        :return: None
        """

        # Convert incoming texts into their final form before becoming widgets
        self.message.text = f"Searched for: {message}"
        self.word_frequency_content.text = f"This word comes up with a frequency of {str(word_frequency_content)}%"
        self.query_search_files_content.text = f"This word can be found in the following " \
                                          f"file(s):{str(query_search_files_content)}"

    def update_text_width(self, *_) -> None:
        """
        Updates the text's width; responsive text size
        :param _: declared variable that is ignored.
        :return: None
        """
        self.message.text_size = (self.message.width * 0.75, None)


class MyMainApp(App):
    """
    Main class of the module that is self calling upon the script running
    """

    def __init__(self, **kwargs):
        super().__init__()
        self.second_window = None
        self.main_window = None
        self.screen_manager = None

    def build(self):
        """
        Loads the screen managers for each window and builds the interface
        :return: ScreenManager; controller of windows
        """
        self.screen_manager = ScreenManager()

        self.main_window = MainWindow()
        screen = Screen(name="MainWindow")
        screen.add_widget(self.main_window)
        self.screen_manager.add_widget(screen)

        self.second_window = SecondWindow()
        screen = Screen(name="SecondWindow")
        screen.add_widget(self.second_window)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == '__main__':
    """
    Runs the script
    """
    instance_app = MyMainApp()
    instance_app.run()
