from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
import arabic_reshaper
from bidi.algorithm import get_display

def fix_arabic(text):
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)

# الشاشة الرئيسية للتطبيق (تحتوي على الأقسام الكبرى)
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=25, spacing=20)
        
        # عنوان التطبيق
        title = Label(
            text=fix_arabic("تطبيق ترتيل القرآن"),
            font_name='cairo.ttf',
            font_size=28,
            size_hint_y=None,
            height=60
        )
        layout.add_widget(title)
        
        # أزرار الأقسام الرئيسية
        btn_quran = Button(
            text=fix_arabic("المصحف الشريف (السور)"),
            font_name='cairo.ttf',
            font_size=20,
            size_hint_y=None,
            height=60
        )
        btn_quran.bind(on_release=lambda x: setattr(App.get_running_app().screen_manager, 'current', 'quran_list'))
        layout.add_widget(btn_quran)
        
        btn_tafsir = Button(
            text=fix_arabic("التفسير (في ظلال القرآن)"),
            font_name='cairo.ttf',
            font_size=20,
            size_hint_y=None,
            height=60
        )
        btn_tafsir.bind(on_release=lambda x: setattr(App.get_running_app().screen_manager, 'current', 'tafsir_screen'))
        layout.add_widget(btn_tafsir)
        
        btn_tajweed = Button(
            text=fix_arabic("أحكام التجويد والتصحيح"),
            font_name='cairo.ttf',
            font_size=20,
            size_hint_y=None,
            height=60
        )
        btn_tajweed.bind(on_release=lambda x: setattr(App.get_running_app().screen_manager, 'current', 'tajweed_screen'))
        layout.add_widget(btn_tajweed)
        
        self.add_widget(layout)

# شاشة قائمة السور
class QuranListScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        title = Label(
            text=fix_arabic("فهرس السور"),
            font_name='cairo.ttf',
            font_size=24,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(title)
        
        scroll = ScrollView()
        list_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
        list_layout.bind(minimum_height=list_layout.setter('height'))
        
        # نموذج لبعض السور (يمكن التوسع لاحقاً عبر قاعدة بيانات)
        surahs = ["سورة الفاتحة", "سورة البقرة", "سورة آل عمران", "سورة الإخلاص"]
        for s in surahs:
            b = Button(
                text=fix_arabic(s),
                font_name='cairo.ttf',
                font_size=18,
                size_hint_y=None,
                height=55
            )
            list_layout.add_widget(b)
            
        scroll.add_widget(list_layout)
        layout.add_widget(scroll)
        
        back_btn = Button(
            text=fix_arabic("الرجوع للقائمة الرئيسية"),
            font_name='cairo.ttf',
            font_size=16,
            size_hint_y=None,
            height=50
        )
        back_btn.bind(on_release=lambda x: setattr(App.get_running_app().screen_manager, 'current', 'home'))
        layout.add_widget(back_btn)
        
        self.add_widget(layout)

# شاشة التفسير
class TafsirScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        title = Label(
            text=fix_arabic("تفسير في ظلال القرآن"),
            font_name='cairo.ttf',
            font_size=24,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(title)
        
        scroll = ScrollView()
        content = Label(
            text=fix_arabic("هنا سيتم عرض تفسير الآيات لسيد قطب رحمه الله...\n(يتم ربطه لاحقاً بقاعدة البيانات المركزية لتفادي ضغط الملفات)."),
            font_name='cairo.ttf',
            font_size=16,
            size_hint_y=None,
            halign='center',
            valign='top'
        )
        content.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        scroll.add_widget(content)
        layout.add_widget(scroll)
        
        back_btn = Button(
            text=fix_arabic("الرجوع"),
            font_name='cairo.ttf',
            font_size=16,
            size_hint_y=None,
            height=50
        )
        back_btn.bind(on_release=lambda x: setattr(App.get_running_app().screen_manager, 'current', 'home'))
        layout.add_widget(back_btn)
        
        self.add_widget(layout)

# شاشة أحكام التجويد
class TajweedScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        title = Label(
            text=fix_arabic("أحكام التجويد والتصحيح"),
            font_name='cairo.ttf',
            font_size=24,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(title)
        
        scroll = ScrollView()
        content = Label(
            text=fix_arabic("قواعد التجويد:\n1. أحكام النون السكنية والتنوين\n2. أحكام الميم السكنية\n3. المدود وأنواعها..."),
            font_name='cairo.ttf',
            font_size=16,
            size_hint_y=None,
            halign='center',
            valign='top'
        )
        content.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        scroll.add_widget(content)
        layout.add_widget(scroll)
        
        back_btn = Button(
            text=fix_arabic("الرجوع"),
            font_name='cairo.ttf',
            font_size=16,
            size_hint_y=None,
            height=50
        )
        back_btn.bind(on_release=lambda x: setattr(App.get_running_app().screen_manager, 'current', 'home'))
        layout.add_widget(back_btn)
        
        self.add_widget(layout)

# التطبيق الأساسي ومدير الشاشات
class QuranApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        
        self.screen_manager.add_widget(HomeScreen(name='home'))
        self.screen_manager.add_widget(QuranListScreen(name='quran_list'))
        self.screen_manager.add_widget(TafsirScreen(name='tafsir_screen'))
        self.screen_manager.add_widget(TajweedScreen(name='tajweed_screen'))
        
        return self.screen_manager

if __name__ == '__main__':
    QuranApp().run()
