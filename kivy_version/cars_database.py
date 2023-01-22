from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import Screen
Window.size = (310,500)

screen_helper = """
Screen:
    BoxLayout:
        orientation : 'vertical'
        MDTopAppBar :
            title: "Автокомплекс 'ВЕРОС'"   
            font_size: '20sp'
            left_action_items: [["menu",lambda x:app.navigation_draw()]]
            
        MDLabel:
            text: 'Here will be the input and storing data'
            halign: 'center'
        
        MDBottomAppBar:

            MDTopAppBar:
                title: "Брой коли: 0"
                font_size: '1sp'
                icon: "tools"
                type: "bottom"
                left_action_items: [["toolbox", lambda x: x]]
                mode: "end"

    
"""


class cars_database(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Red'
        screen = Builder.load_string(screen_helper)
        return screen


    def navigation_draw(self):
        print("Navigation")





cars_database().run()