from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput


class MainWindow(GridLayout):
    # runs on initialization
    def __init__(self, **kwargs):
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

    def callback(self, instance):
        self.greeting.text = "An " + self.user.text + " is in stock!"

        info = self.user.text + "!"

        if self.user.text == "banana":
            instance_app.second_window.update_info(info)
            instance_app.screen_manager.current = "SecondWindow"


class SecondWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.message = Label(
            halign="center",
            valign="middle",
            font_size=30
        )
        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)

    def update_info(self, message):
        self.message.text = message

    def update_text_width(self, *_):
        self.message.text_size = (self.message.width * 0.85, None)


class MyMainApp(App):
    def build(self):
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    instance_app = MyMainApp()
    instance_app.run()
