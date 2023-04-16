from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

from lib.python import UI, WindowManger

Window.size = (360, 600)

# move textinput under the keyboard in above the keyboard
Window.keyboard_anim_args = {'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"



class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Purple"
        Window. softinput_mde = "below target"
        self.load_all_kv_files("lib/")
        return WindowManger()


if __name__ == '__main__':
    app = MyApp()
    app.run()
