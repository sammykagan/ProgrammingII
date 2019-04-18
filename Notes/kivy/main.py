import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

Window.size = (600, 400)

class TempApp(App):
    def build(self):
        return TempLayout()

class TempLayout(BoxLayout):
    #will contain all of my functions
    pass


if __name__ == "__main__":
    app = TempApp()
    app.run()