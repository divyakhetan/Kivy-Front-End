import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from camera import CameraCv
from kivy.clock import Clock
# from kivy.config import Config

kivy.require('1.11.1')
# Config.set('kivy', 'default_font', ['Roboto', 'data/fonts/Roboto-Regular.ttf', 'data/fonts/Roboto-Italic.ttf', 'data/fonts/Roboto-Bold.ttf', 'data/fonts/Roboto-BoldItalic.ttf'])
# Config.write()
# print('hello', Config.get('kivy', 'default_font'))

class ScreenIntroa(Screen):
    pass

class ScreenIntrob(Screen):
    pass


class Screen1(Screen):
    pass

class Screen1success(Screen):
    pass

class Screen1failure(Screen):
    pass

class Screen2(Screen):
    pass

class Screen2success(Screen):
    pass

class Screen2failure(Screen):
    pass

class Screen3a(Screen):
    pass

class Screen3b(Screen):
    pass

class Screen3c(Screen):
    pass

class Screen3d(Screen):
    pass

class Screen4(Screen):
    pass

class Screen5(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("MyApp.kv")


class MainApp(App):
    def build(self):
        return presentation

if __name__ == '__main__':
    MainApp().run()