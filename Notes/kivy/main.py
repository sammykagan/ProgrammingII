import kivy
from kivy.app import App
from kivy.core.window import Window

Window.size = (800, 300)

class TempApp(App):
    pass

if __name__ == "__main__":
    app = TempApp()
    app.run()