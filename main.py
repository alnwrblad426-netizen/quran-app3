from kivy.app import App
from kivy.uix.label import Label

class QuranApp(App):
    def build(self):
        return Label(text='تطبيق القرآن الكريم', font_name='Cairo-VariableFont_slnt,wght.ttf')

if __name__ == '__main__':
    QuranApp().run()
