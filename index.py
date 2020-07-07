import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
kivy.require('1.11.1')

# class MyBoxLayout(BoxLayout):
#     pass


# class MyApp(App):

#     def build(self):
#         return MyBoxLayout()


# if __name__ == '__main__':
#     app = MyApp()
#     app.run()

class Screen1(Screen):
    pass

class Screen2(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("MyApp.kv")

class MainApp(App):
    def build(self):
        return presentation

if __name__ == '__main__':
    MainApp().run()