from kivy.app import App
from kivy.uix.behaviors import button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button


class MainApp(App):
    def build(self):
        label = Label(text='Hello from Kivy',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})
        #return label

        img = Image(source='/path/to/real_python.png',
                    size_hint=(1, .5),
                    pos_hint={'center_x':.5, 'center_y':.5})
        btn = Button(text="Button")
        return btn

if __name__ == '__main__':
    app = MainApp()
    app.run()