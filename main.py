from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.screen import Screen
from kivymd.app import MDApp


class GetInfoScreen(Screen):
    def __init__(self, gamer_number):
        super(GetInfoScreen, self).__init__()

        self.cols_info_input = MDTextField(hint_text="Number Of Cols")
        self.cols_info_input.size_hint_x = .5
        self.cols_info_input.pos_hint = {"center_x": .5, "center_y": .6}

        self.rows_info_input = MDTextField(hint_text="Number Of Rows")
        self.rows_info_input.size_hint_x = .5
        self.rows_info_input.pos_hint = {"center_x": .5, "center_y": .5}

        self.create_table_button = MDFillRoundFlatButton(text="Create Table For Player " + gamer_number)
        self.create_table_button.size_hint_x = .5
        self.create_table_button.pos_hint = {"center_x": .5, "center_y": .4}

        self.add_widget(self.cols_info_input)
        self.add_widget(self.rows_info_input)
        self.add_widget(self.create_table_button)


class GetInfoScreenManager(Screen):
    def __init__(self):
        super(GetInfoScreenManager, self).__init__()
        main_layout = MDBoxLayout()

        first_player_screen_manager = ScreenManager()
        first_player_info_screen = GetInfoScreen("1")
        first_player_info_screen.name = "first_player_info"
        first_player_screen_manager.add_widget(first_player_info_screen)
        first_player_screen_manager.current = "first_player_info"

        second_player_screen_manager = ScreenManager()
        second_player_info_screen = GetInfoScreen("2")
        second_player_info_screen.name = "second_player_info"
        second_player_screen_manager.add_widget(second_player_info_screen)
        second_player_screen_manager.current = "second_player_info"

        main_layout.add_widget(first_player_screen_manager)
        main_layout.add_widget(second_player_screen_manager)

        self.add_widget(main_layout)


class MainScreenManager(ScreenManager):
    def __init__(self):
        super(MainScreenManager, self).__init__()
        self.home_screen = GetInfoScreenManager()
        self.home_screen.name = "home_screen"
        
        # Todo: Add A Screen For the Tables
        self.table_screen = Screen()
        self.table_screen.name = "another_screen"
        
        self.add_widget(self.home_screen)
        self.add_widget(self.table_screen)
        
        self.current = "home_screen"


class GameTheoryApp(MDApp):
    def build(self):
        table_input_screen_manager = MainScreenManager()
        return table_input_screen_manager


if __name__ == "__main__":
    GameTheoryApp().run()
