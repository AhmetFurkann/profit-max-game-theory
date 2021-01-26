from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from screens import GetRowColScreen
from kivymd.uix.screen import Screen
from kivymd.app import MDApp


class GetInfoScreen(Screen):
    def __init__(self):
        super(GetInfoScreen, self).__init__()

        self.cols_info_input = MDTextField(hint_text="Number Of Cols")
        self.cols_info_input.size_hint_x = .5
        self.cols_info_input.pos_hint = {"center_x": .5, "center_y": .6}
        self.rows_info_input = MDTextField(hint_text="Number Of Rows")
        self.rows_info_input.size_hint_x = .5
        self.rows_info_input.pos_hint = {"center_x": .5, "center_y": .5}

        self.create_table_button = MDFillRoundFlatButton(text="Create Table For Player")
        self.create_table_button.size_hint_x = .5
        self.create_table_button.pos_hint = {"center_x": .5, "center_y": .4}

        self.add_widget(self.cols_info_input)
        self.add_widget(self.rows_info_input)
        self.add_widget(self.create_table_button)


class GetInfoScreenManager(Screen):
    def __init__(self):
        super(GetInfoScreenManager, self).__init__()
        main_layout = MDBoxLayout()

        self.first_player_screen_manager = ScreenManager()
        self.first_player_info_screen = GetInfoScreen()
        self.first_player_info_screen.name = "first_player_info"
        self.first_player_info_screen.create_table_button.bind(on_press=self.button_change_player_1_screen)
        self.first_player_screen_manager.add_widget(self.first_player_info_screen)
        self.first_player_screen_manager.current = "first_player_info"

        self.second_player_screen_manager = ScreenManager()
        self.second_player_info_screen = GetInfoScreen()
        self.second_player_info_screen.name = "second_player_info"
        self.second_player_screen_manager.add_widget(self.second_player_info_screen)
        self.second_player_screen_manager.current = "second_player_info"

        main_layout.add_widget(self.first_player_screen_manager)
        main_layout.add_widget(self.second_player_screen_manager)

        self.add_widget(main_layout)

    def add_player_1_input_screen(self):
        rows_number = int(self.first_player_info_screen.rows_info_input.text)
        cols_number = int(self.first_player_info_screen.cols_info_input.text)
        get_rows_cols_screen = GetRowColScreen(rows_number, cols_number)
        get_rows_cols_screen.name = "first_player_input"
        self.first_player_screen_manager.add_widget(get_rows_cols_screen)

    def change_player_1_input_screen(self):
        self.add_player_1_input_screen()
        self.first_player_screen_manager.current = "first_player_input"

    def button_change_player_1_screen(self, instance):
        self.change_player_1_input_screen()


class MainScreenManager(ScreenManager):
    def __init__(self):
        super(MainScreenManager, self).__init__()
        self.home_screen = GetInfoScreenManager()
        self.home_screen.name = "home_screen"

        self.table_screen = Screen()
        self.table_screen.name = "table_screen"

        self.add_widget(self.home_screen)
        self.add_widget(self.table_screen)

        self.current = "home_screen"


def change_screen(self, *args):
    self.current = "home_screen"


class GameTheoryApp(MDApp):
    def build(self):
        table_input_screen_manager = MainScreenManager()
        return table_input_screen_manager


if __name__ == "__main__":
    GameTheoryApp().run()
