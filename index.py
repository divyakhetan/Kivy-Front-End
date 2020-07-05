import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

kivy.require('1.11.1')

class MyBoxLayout(BoxLayout):
    pass


class MyApp(App):

    def build(self):
        # mainLayout = BoxLayout(orientation="vertical")
        
        # hBoxLayout = BoxLayout(orientation="horizontal")
        # btn1 = Button(text="click me 1")
        # btn2 = Button(text="click me 2")
        # hBoxLayout.add_widget(btn1)
        # hBoxLayout.add_widget(btn2)

        # vBoxLayout = BoxLayout(orientation="vertical")
        # btn3 = Button(text="click me 3")
        # btn4 = Button(text="click me 4")
        # vBoxLayout.add_widget(btn3)
        # vBoxLayout.add_widget(btn4)

        # mainLayout.add_widget(hBoxLayout)
        # mainLayout.add_widget(vBoxLayout)

        return MyBoxLayout()


if __name__ == '__main__':
    app = MyApp()
    app.run()