import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager

class MainApp(App):
    def build(self):
        return MainScreen()

class MainScreen(ScreenManager):
    def __init__(self, **kwargs):
        super.__init__(self, **kwargs)
