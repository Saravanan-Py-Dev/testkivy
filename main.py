from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp

from lib.python import UI


class MyApp(MDApp):
    def build(self):
        self.load_all_kv_files("lib/")
        return UI()


if __name__ == '__main__':
    app = MyApp()
    app.run()
