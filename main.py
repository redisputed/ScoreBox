#!/usr/local/bin/python3
from kivy.uix.pagelayout import PageLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.app import App
import kivy
from kivy.uix.widget import Widget
kivy.require('2.0.0')  # replace with your current kivy version !


class gameInfo(GridLayout):
    pass


class ScoreBox(Widget):
    pass


class ScoreBoxApp(App):

    def build(self):
        return ScoreBox()


if __name__ == '__main__':
    ScoreBoxApp().run()
