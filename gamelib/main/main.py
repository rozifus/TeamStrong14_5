import kivy
kivy.require('1.8.0')

from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.widget import Widget
from menu import Menu
from game import Game

class Main(FloatLayout):

    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)

        #self.button = Button(size_hint=(1,1))

        self.menu = Menu()
        self.menu.bind(on_new_game_button_pressed=self.trans_game)

        self.game = Game()
        self.game.bind(on_end_game=self.trans_menu)

        self.trans_menu()

    def trans_menu(self, obj=None):
        self.clear_widgets()
        self.add_widget(self.menu)

    def trans_game(self, obj=None):
        self.clear_widgets()
        self.add_widget(self.game)


