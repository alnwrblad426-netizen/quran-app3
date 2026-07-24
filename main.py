from kivy.app import App
from kivy.uix.label import Label

class QuranApp(App):
    def build(self):
        return Label(text='مرحباً بك في تطبيق القرآن الكريم', font_size=24)

if __name__ == '__main__':
    QuranApp().run()
