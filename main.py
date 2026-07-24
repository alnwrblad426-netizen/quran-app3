from kivy.app import App
from kivy.uix.label import Label
import arabic_reshaper
from bidi.algorithm import get_display

class QuranApp(App):
    def build(self):
        text = "تطبيق القرآن الكريم"
        reshaped_text = arabic_reshaper.reshape(text)
        bidi_text = get_display(reshaped_text)
        return Label(text=bidi_text, font_name='Cairo-VariableFont_slnt,wght.ttf')

if __name__ == '__main__':
    QuranApp().run()
