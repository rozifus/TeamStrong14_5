import kivy
kivy.require('1.8.0')

from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.widget import Widget
from hanger import Hanger

class Game(FloatLayout):

    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)

        self.register_event_type('on_end_game')

        self.hanger = Hanger()
        self.add_widget(self.hanger)

    def end_game_button_pressed(self):
        self.dispatch('on_end_game')

    def on_end_game(self):
        pass

    def trans_hangar(self):
        pass

    def trans_scenario(self):
        pass

