import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.label import Label
from main import Main
from kivy.uix.floatlayout import FloatLayout

class TeamStrong(App):

    def build(self):

        return Main()


# not needed if using run_game.py in root directory
if __name__=='__main__':
    TeamStrong().run()
