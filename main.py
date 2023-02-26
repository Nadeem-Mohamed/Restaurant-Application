import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# Define the list of possible meals with their corresponding calorie counts
MEALS = [
    {"name": "Meal 1", "calories": 500},
    {"name": "Meal 2", "calories": 800},
    {"name": "Meal 3", "calories": 1000},
    {"name": "Meal 4", "calories": 1200},
    {"name": "Meal 5", "calories": 1500},
    {"name": "Meal 6", "calories": 2000},
    {"name": "Meal 6", "calories": 2150},
    {"name": "Meal 6", "calories": 2200}
]

class RestaurantMenu(BoxLayout):

    def __init__(self, **kwargs):
        super(RestaurantMenu, self).__init__(**kwargs)

        # Create a label to welcome the user to the app
        welcome_label = Label(text="Welcome to the Restaurant Menu App", 
                              size_hint=(1, 0.2))
        self.add_widget(welcome_label)

        # Create a text input for the user to enter their desired calorie count
        self.calories_input = TextInput(hint_text="Enter desired calorie count",
                                        size_hint=(0.8, 0.2))
        self.add_widget(self.calories_input)

        # Create a button to trigger the search for meals
        search_button = Button(text="Search", 
                               size_hint=(0.2, 0.2))
        search_button.bind(on_press=self.search_meals)
        self.add_widget(search_button)

        # Create a label to display the list of meals
        self.meals_label = Label(text="", 
                                 size_hint=(1, 0.6))
        self.add_widget(self.meals_label)

    def search_meals(self, instance):
        # Get the desired calorie count entered by the user
        desired_calories = int(self.calories_input.text)

        # Find the meals that match the desired calorie count
        matching_meals = []
        for meal in MEALS:
            if meal["calories"] == desired_calories:
                matching_meals.append(meal)

        # Display the list of matching meals
        if matching_meals:
            meals_text = "Matching meals:\n\n"
            for meal in matching_meals:
                meals_text += f"{meal['name']} ({meal['calories']} calories)\n"
            self.meals_label.text = meals_text
        else:
            self.meals_label.text = "No matching meals found"

class RestaurantMenuApp(App):

    def build(self):
        return RestaurantMenu()

if __name__ == '__main__':
    RestaurantMenuApp().run()