from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.text import LabelBase

class RestaurantApp(App):
    def build(self):
        # Create a BoxLayout to hold the UI elements
        layout = BoxLayout(orientation='vertical')


        # Add a welcome message at the top of the screen
        welcome_label = Label(text='Welcome to the Restaurant!',
                              font_size='40sp',
                              color=(1, 0.6, 0, 1),
                              size_hint_y=None,
                              height=100)
        layout.add_widget(welcome_label)

        # Add a label and a TextInput for the calorie input
        calorie_label = Label(text='How many calories do you want to gain?',
                              
                              font_size='20sp',
                              size_hint_y=None,
                              height=50)
        layout.add_widget(calorie_label)

        calorie_input = TextInput(multiline=False)
        layout.add_widget(calorie_input)

        return layout

if __name__ == '__main__':
    RestaurantApp().run()