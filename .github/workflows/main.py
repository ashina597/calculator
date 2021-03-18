from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainApp(App):
    def build(self):
        mainlayout = BoxLayout(orientation="vertical")
        vboxlayout = BoxLayout(orientation="vertical")
        self.v1 = TextInput(halign="right",
                            readonly=True,
                            text="0",
                            multiline=False,
                            background_color='white',
                            font_size="64",
                            )
        vboxlayout.add_widget(self.v1)
        h1boxlayout = BoxLayout(orientation="horizontal")
        b1 = Button(text="7",
                    background_color='indigo',
                    )
        b1.bind(on_press=self.on_button_press)
        b2 = Button(text="8",
                    background_color='indigo'
                    )
        b2.bind(on_press=self.on_button_press)
        b3 = Button(text="9",
                    background_color='indigo'
                    )
        b3.bind(on_press=self.on_button_press)
        b4 = Button(text="/",
                    background_color='grey'
                    )
        b4.bind(on_press=self.on_button_press)
        h1boxlayout.add_widget(b1)
        h1boxlayout.add_widget(b2)
        h1boxlayout.add_widget(b3)
        h1boxlayout.add_widget(b4)
        h2boxlayout = BoxLayout(orientation="horizontal")
        b1 = Button(text="4",
                    background_color='indigo'
                    )
        b1.bind(on_press=self.on_button_press)
        b2 = Button(text="5",
                    background_color='indigo'
                    )
        b2.bind(on_press=self.on_button_press)
        b3 = Button(text="6",
                    background_color='indigo'
                    )
        b3.bind(on_press=self.on_button_press)
        b4 = Button(text="*",
                    background_color='grey'
                    )
        b4.bind(on_press=self.on_button_press)
        h2boxlayout.add_widget(b1)
        h2boxlayout.add_widget(b2)
        h2boxlayout.add_widget(b3)
        h2boxlayout.add_widget(b4)
        h3boxlayout = BoxLayout(orientation="horizontal")
        b1 = Button(text="1",
                    background_color='indigo'
                    )
        b1.bind(on_press=self.on_button_press)
        b2 = Button(text="2",
                    background_color='indigo'
                    )
        b2.bind(on_press=self.on_button_press)
        b3 = Button(text="3",
                    background_color='indigo'
                    )
        b3.bind(on_press=self.on_button_press)
        b4 = Button(text="-",
                    background_color='grey'
                    )
        b4.bind(on_press=self.on_button_press)
        h3boxlayout.add_widget(b1)
        h3boxlayout.add_widget(b2)
        h3boxlayout.add_widget(b3)
        h3boxlayout.add_widget(b4)
        h4boxlayout = BoxLayout(orientation="horizontal")
        b1 = Button(text="0",
                    background_color='indigo'
                    )
        b1.bind(on_press=self.on_button_press)
        b2 = Button(text=".",
                    background_color='indigo'
                    )
        b2.bind(on_press=self.on_button_press)
        b3 = Button(text="c",
                    background_color='indigo'
                    )
        b3.bind(on_press=self.on_button_press)
        b4 = Button(text="+",
                    background_color='grey'
                    )
        b4.bind(on_press=self.on_button_press)
        h4boxlayout.add_widget(b1)
        h4boxlayout.add_widget(b2)
        h4boxlayout.add_widget(b3)
        h4boxlayout.add_widget(b4)
        v1boxlayout = BoxLayout(orientation="horizontal")
        b5 = Button(text="=",
                    background_color='grey'
                    )
        b5.bind(on_press=self.on_solution)
        v1boxlayout.add_widget(b5)
        mainlayout.add_widget(vboxlayout)
        mainlayout.add_widget(h1boxlayout)
        mainlayout.add_widget(h2boxlayout)
        mainlayout.add_widget(h3boxlayout)
        mainlayout.add_widget(h4boxlayout)
        mainlayout.add_widget(v1boxlayout)

        return mainlayout

    def on_solution(self, text):
        text = self.v1.text
        if text:
            solution = str(eval(text))
            self.v1.text = solution

    def on_button_press(self, Button):
        current = self.v1.text

        if current == '0':
            self.v1.text = ''
            self.v1.text = f'{Button.text}'
        else:
            self.v1.text = f'{current}{Button.text}'

        if Button.text == "c":
            self.v1.text = "0"

if __name__ == "__main__":
    app = MainApp()
    app.run()
