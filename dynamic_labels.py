"""
CP1404 Prac 08
Dynamic Labels Program
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main program to create labels dynamically from a list."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Shriram"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')

        # Create a Label for each name
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)

        return self.root

DynamicLabelsApp().run()
