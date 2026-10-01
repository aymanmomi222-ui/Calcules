from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.metrics import dp

Window.size = (360, 640)


class CalculatorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=dp(10), spacing=dp(8), **kwargs)

        self.expression = ""

        self.display = Label(
            text="0",
            font_size=dp(36),
            halign="right",
            valign="middle",
            size_hint_y=0.22,
            text_size=(None, None),
        )
        self.display.bind(size=self.update_text_size)
        self.add_widget(self.display)

        buttons = [
            ["C", "⌫", "(", ")"],
            ["7", "8", "9", "÷"],
            ["4", "5", "6", "×"],
            ["1", "2", "3", "−"],
            ["0", ".", "=", "+"],
        ]

        grid = GridLayout(cols=4, spacing=dp(7), size_hint_y=0.78)

        for row in buttons:
            for text in row:
                button = Button(
                    text=text,
                    font_size=dp(24),
                )
                button.bind(on_release=self.button_pressed)
                grid.add_widget(button)

        self.add_widget(grid)

    def update_text_size(self, instance, value):
        instance.text_size = (instance.width - dp(10), instance.height)

    def button_pressed(self, button):
        value = button.text

        if value == "C":
            self.expression = ""
            self.display.text = "0"
            return

        if value == "⌫":
            self.expression = self.expression[:-1]
            self.display.text = self.expression or "0"
            return

        if value == "=":
            self.calculate()
            return

        conversions = {
            "÷": "/",
            "×": "*",
            "−": "-",
        }

        self.expression += conversions.get(value, value)
        self.display.text = self.expression

    def calculate(self):
        try:
            if not self.expression:
                return

            # Allow only calculator characters.
            allowed = "0123456789+-*/(). "
            if any(char not in allowed for char in self.expression):
                raise ValueError

            result = eval(self.expression, {"__builtins__": None}, {})

            if isinstance(result, float) and result.is_integer():
                result = int(result)

            self.expression = str(result)
            self.display.text = self.expression

        except Exception:
            self.expression = ""
            self.display.text = "خطأ"


class CalculatorApp(App):
    title = "آلة حاسبة"

    def build(self):
        return CalculatorLayout()


if __name__ == "__main__":
    CalculatorApp().run()
