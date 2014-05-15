import kivy
kivy.require('1.8.0')

from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.widget import Widget

class Hanger(BoxLayout):

    def __init__(self, **kwargs):
        super(Hanger, self).__init__(**kwargs)


