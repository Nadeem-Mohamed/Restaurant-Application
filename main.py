import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color,Rectangle
import itertools

# Define the list of possible meals with their corresponding calorie counts
MEALS = [
    {"name": "Cheese Pizza", "calories": 170},
    {"name": "Granola Bar", "calories": 100},
    {"name": "Waffles", "calories": 130},
    {"name": "Bag of Chips", "calories": 1200},
    {"name": "Steak", "calories": 300},
    {"name": "Meal 6", "calories": 1750},
    {"name": "Meal 7", "calories": 2000},
    {"name": "Meal 8", "calories": 2150},
    {"name": "Meal 9", "calories": 2200}
]


class RestaurantMenu(BoxLayout):
    def __init__(self, **kwargs):
        super(RestaurantMenu, self).__init__(**kwargs)

        # Set the background color for the header
        with self.canvas.before:
            Color(255, 0, 0, 1)
            self.header_rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_header_rect, size=self.update_header_rect)

        # Set the background color for the rest of the screen
        with self.canvas.before:
            Color(0, 0, 0, 1)
            self.body_rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_body_rect, size=self.update_body_rect)

        # Create a label to welcome the user to the app
        welcome_label = Label(text="Welcome to the Restaurant Menu App", 
                              size_hint=(1, 0.2), pos_hint={'top':0.550, 'y':0.5})
        self.add_widget(welcome_label)

        # Create a text input for the user to enter their desired calorie count
        self.calories_input = TextInput(hint_text="Enter desired calorie count",
                size_hint=(0.8, 0.05), multiline=False)
        self.calories_input.bind(on_text_validate=self.search_meals)
        self.add_widget(self.calories_input)

        # Create a button to trigger the search for meals
        search_button = Button(text="Search", 
                               size_hint=(0.2, 0.05))
        search_button.bind(on_press=self.search_meals)
        self.add_widget(search_button)

        # Create a label to display the list of meals
        self.meals_label = Label(text="", 
                                 size_hint=(1, 0.6))
        self.add_widget(self.meals_label)

    def update_header_rect(self, instance, value):
        self.header_rect.pos = instance.pos
        self.header_rect.size = instance.size

    def update_body_rect(self, instance, value):
        self.body_rect.pos = instance.pos
        self.body_rect.size = instance.size

    def search_meals(self, instance):
        # Get the desired calorie count entered by the user
        try:
            desired_calories = int(self.calories_input.text)
        except:
            desired_calories = -1

        # Find all possible combinations of meals that add up to the desired calorie count
        matching_meals = []
        for i in range(1, len(MEALS) + 1):
            for combo in itertools.combinations(MEALS, i):
                total_calories = sum([meal["calories"] for meal in combo])
                if total_calories == desired_calories:
                    matching_meals.append(list(combo))

        # Display the list of matching meals
        if matching_meals:
            meals_text = "Matching meals:\n\n"
            for meals in matching_meals:
                meals_text += ", ".join([meal["name"] for meal in meals]) + f" ({sum([meal['calories'] for meal in meals])} calories)\n"
            self.meals_label.text = meals_text
        else:
            self.meals_label.text = "No matching meals found"


class RestaurantMenuApp(App):
    def build(self):
        return RestaurantMenu()


if __name__ == '__main__':

    RestaurantMenuApp().run()
    
    
    
    
    
    
    
    
