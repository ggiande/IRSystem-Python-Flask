from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput


class MainWindow(GridLayout):
    """
    The main controller of the Kivy framework for the initial window.
    """

    def __init__(self, **kwargs):
        """
        Runs on initialization. Includes all the stying used to generate the initial window.
        Generates the widgets for the end user interaction.
        :param kwargs: pass a keyworded variable length of arguments upon initialization
        """
        super().__init__(**kwargs)

        self.window = GridLayout
        self.window.cols = 1
        self.window.size_hint = (0.60, 0.70)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.greeting = Label(
            text="What fruit do you have in stock?",
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
            background_color='#00FFCE'
        )
        self.button.bind(on_press=self.callback)
        self.add_widget(self.button)

    def callback(self, instance) -> None:
        """
        Calls the element/widget after processing the input specifically for the text widget.
        Note, this requires the instance to be passed as an argument, code breaking without.
        :param instance: instance of the window
        :return:
        """

        self.greeting.text = "An " + self.user.text + " is in stock!"

        info = self.user.text + "!"

        if self.user.text == "banana":
            instance_app.second_window.update_info(info)
            instance_app.screen_manager.current = "SecondWindow"


class SecondWindow(Screen):
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
            halign="center",
            valign="middle",
            font_size=30
        )
        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)

    def update_info(self, message: str) -> None:
        """
        Update's the information that processes the input
        :param message:
        :return: None
        """
        self.message.text = message

    def update_text_width(self, *_) -> None:
        """
        Updates the text's width; responsive text size
        :param _: declared variable that is ignored.
        :return: None
        """
        self.message.text_size = (self.message.width * 0.85, None)


class MyMainApp(App):
    """
    Main class of the module that is self calling upon the script running
    """
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
