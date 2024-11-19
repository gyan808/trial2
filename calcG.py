from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class CalculatorApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.result_label = Label(size_hint_y=0.2, text="Result will show here")
        self.layout.add_widget(self.result_label)

        self.input1 = TextInput(hint_text="Enter first number", multiline=False)
        self.layout.add_widget(self.input1)
        self.input2 = TextInput(hint_text="Enter second number", multiline=False)
        self.layout.add_widget(self.input2)

        for op in ["Add", "Subtract", "Multiply", "Divide"]:
            btn = Button(text=op)
            btn.bind(on_press=self.calculate)
            self.layout.add_widget(btn)

        return self.layout

    def calculate(self, instance):
        try:
            num1 = float(self.input1.text)
            num2 = float(self.input2.text)
            if instance.text == "Add":
                result = num1 + num2
            elif instance.text == "Subtract":
                result = num1 - num2
            elif instance.text == "Multiply":
                result = num1 * num2
            elif instance.text == "Divide":
                result = "Error" if num2 == 0 else num1 / num2
            self.result_label.text = f"Result: {result}"
        except ValueError:
            self.result_label.text = "Invalid Input!"

if __name__ == "__main__":
    CalculatorApp().run()
