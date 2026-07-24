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

# 1. الشاشة الرئيسية للتطبيق (تضم الأقسام الكبرى)
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=25, spacing=15)
        
        # عنوان التطبيق
        title = Label(
            text=fix_arabic("تطبيق ترتيل القرآن"),
            font_name='cairo.ttf',
            font_size=26,
            size_hint_y=None,
            height=60
        )
        layout.add_widget(title)
        
        # زر المصحف الشريف (السور)
        btn_quran = Button(
            text=fix_arabic("📖 المصحف الشريف (فهرس السور)"),
            font_name='cairo.ttf',
            font_size=18,
            size_hint_y=None,
            height=60
        )
        btn_quran.bind(on_release=lambda x: setattr(App.get_running_app().screen_manager, 'current', 'quran_list'))
        layout.add_widget(btn_quran)
        
        # زر تفسير في ظلال القرآن
        btn_tafsir = Button(
            text=fix_arabic("📚 تفسير في ظلال القرآن (سيد قطب)"),
            font_name='cairo.ttf',
            font_size=18,
            size_hint_y=None,
            height=60
        )
        btn_tafsir.bind(on_release=lambda x: setattr(App.get_running_app().screen_manager, 'current', 'tafsir_screen'))
        layout.add_widget(btn_tafsir)
        
        # زر أحكام التجويد والتصحيح
        btn_tajweed = Button(
            text=fix_arabic("🎧 أحكام التجويد والتصحيح"),
            font_name='cairo.ttf',
            font_size=18,
            size_hint_y=None,
            height=60
        )
        btn_tajweed.bind(on_release=lambda x: setattr(App.get_running_app().screen_manager, 'current', 'tajweed_screen'))
        layout.add_widget(btn_tajweed)
        
        self.add_widget(layout)

# 2. شاشة فهرس السور (المصحف الشريف)
class QuranListScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        title = Label(
            text=fix_arabic("فهرس السور (114 سورة)"),
            font_name='cairo.ttf',
            font_size=22,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(title)
        
        scroll = ScrollView()
        list_layout = BoxLayout(orientation='vertical', spacing=8, size_hint_y=None)
        list_layout.bind(minimum_height=list_layout.setter('height'))
        
        # نموذج مفصل للسور (يمكنك إضافة بقية السور هنا تباعاً)
        surahs = [
            "سورة الفاتحة", "سورة البقرة", "سورة آل عمران", "سورة النساء", 
            "سورة المائدة", "سورة الأنعام", "سورة الأعراف", "سورة الإخلاص", "سورة الفلق", "سورة الناس"
        ]
        
        for s in surahs:
            b = Button(
                text=fix_arabic(s),
                font_name='cairo.ttf',
                font_size=16,
                size_hint_y=None,
                height=50
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

# 3. شاشة تفسير في ظلال القرآن (سيد قطب)
class TafsirScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        title = Label(
            text=fix_arabic("تفسير في ظلال القرآن"),
            font_name='cairo.ttf',
            font_size=22,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(title)
        
        scroll = ScrollView()
        tafsir_content = (
            "مقدمة تفسير في ظلال القرآن - للإمام سيد قطب رحمه الله:\n\n"
            "هذا القرآن.. ما أعمق دلالاته، وما أروع إيقاعاته في النفس البشرية!\n"
            "إنه يخاطب الوجدان والعقل معا، ليقيم الحياة على أساس من الإيمان واليقين.\n\n"
            "(سيتم استعراض تفاسير الآيات تباعاً وفقاً لاختيار السورة)."
        )
        
        content_label = Label(
            text=fix_arabic(tafsir_content),
            font_name='cairo.ttf',
            font_size=16,
            size_hint_y=None,
            halign='center',
            valign='top'
        )
        content_label.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        
        scroll.add_widget(content_label)
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

# 4. شاشة أحكام التجويد والتصحيح
class TajweedScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        title = Label(
            text=fix_arabic("أحكام التجويد والتصحيح"),
            font_name='cairo.ttf',
            font_size=22,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(title)
        
        scroll = ScrollView()
        tajweed_rules = (
            "دليل أحكام التجويد الأساسية:\n\n"
            "1. أحكام النون السكنية والتنوين:\n"
            "   - الإظهار، الإدغام، الإقلاب، الإخفاء.\n\n"
            "2. أحكام الميم السكنية:\n"
            "   - إخفاء شفوي، إدغام شفوي، إظهار شفوي.\n\n"
            "3. المدود:\n"
            "   - المد الطبيعي، المد المتصل، المد المنفصل، المد اللازم."
        )
        
        content_label = Label(
            text=fix_arabic(tajweed_rules),
            font_name='cairo.ttf',
            font_size=16,
            size_hint_y=None,
            halign='center',
            valign='top'
        )
        content_label.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        
        scroll.add_widget(content_label)
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

# إدارة التطبيق والشاشات
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
