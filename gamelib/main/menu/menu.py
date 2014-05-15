import kivy
kivy.require('1.8.0')

from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.widget import Widget
from kivy.uix.button import Button

class Menu(BoxLayout):

    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)

        self.register_event_type('on_new_game_button_pressed')

    def new_game_button_pressed(self):
        self.dispatch('on_new_game_button_pressed')

    def on_new_game_button_pressed(self):
        pass

