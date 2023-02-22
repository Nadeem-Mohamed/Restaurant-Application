from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        label=Label(text="Welcome to the Resteraunt", font_size=30)
        label.y=250
        label.color=(100,100,0,10)

        return label

if __name__ == '__main__':
    app = MainApp()
    app.run()