from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.metrics import dp


class GetRowColScreen(Screen):
    def __init__(self, rows_number, cols_number):
        super(GetRowColScreen, self).__init__()
        self.rows_number = rows_number
        self.cols_number = cols_number
        self.rows_text_input = []
        self.cols_text_input = []
        self.create_rows_text_inputs()
        self.create_cols_text_inputs()
        self.background = MDBoxLayout()
        self.background.orientation = "vertical"
        self.background.padding = [20, 20, 20, 20]

        print("Rows: ", self.rows_text_input)
        print("Cols: ", self.cols_text_input)
        self.add_input_to_bg()

        self.confirm_button = MDFillRoundFlatButton()
        self.confirm_button.text = "Create"
        self.confirm_button.size_hint_x = .5
        self.confirm_button.size_hint_y = self.element_size_hint / 2
        self.confirm_button.pos_hint = {"center_x": .5}

        self.background.add_widget(self.confirm_button)
        self.add_widget(self.background)

    def create_rows_text_inputs(self):
        for sep in range(self.rows_number):
            text_field = MDTextField()
            text_field.id = "row_" + str(sep + 1)
            text_field.hint_text = "Row " + str(sep + 1) + " Value"
            self.rows_text_input.append(text_field)

    def create_cols_text_inputs(self):
        for sep in range(self.cols_number):
            text_field = MDTextField()
            text_field.id = "col_" + str(sep + 1)
            text_field.hint_text = "Col " + str(sep + 1) + " Value"
            self.cols_text_input.append(text_field)

    def add_input_to_bg(self):
        self.element_size_hint = 1 / (self.rows_number + self.cols_number + 1)

        for row in self.rows_text_input:
            row.size_hint_x = .5
            row.pos_hint = {"center_x": .5}
            row.size_hint_y = self.element_size_hint
            row.mode = "rectangle"
            self.background.add_widget(row)

        for col in self.cols_text_input:
            col.size_hint_x = .5
            col.pos_hint = {"center_x": .5}
            col.size_hint_y = self.element_size_hint
            col.mode = "rectangle"
            self.background.add_widget(col)
            
            
class RowColInputScreen(Screen):
    def __init__(self):
        super(RowColInputScreen, self).__init__()
        self.__main_layout = MDBoxLayout()
        self.__main_layout.orientation = "vertical"

        self.__text_fields_bg_layout = MDGridLayout()
        self.__text_fields_bg_layout.size_hint_y = .8
        self.confirm_button = MDFillRoundFlatButton()
        self.confirm_button.text = "CREATE TABLE"
        self.confirm_button.size_hint_x = .8
        self.confirm_button.size_hint_y = .1
        self.confirm_button.pos_hint = {"center_x": .5, "center_y": .5}

        self.__text_fields_bg_layout.spacing = 20
        self.__text_fields_bg_layout.bind(size=self.update_padding)
        self.__text_fields_bg_layout.bind(pos=self.update_padding)

        self.__rows_number = None
        self.__cols_number = None
        self.__text_fields = []

    @property
    def rows_number(self):
        return self.__rows_number

    @property
    def cols_number(self):
        return self.__cols_number

    @property
    def get_text_fields(self):
        return self.__text_fields

    @rows_number.setter
    def rows_number(self, rows_num):
        self.__rows_number = rows_num + 1

    @cols_number.setter
    def cols_number(self, cols_num):
        self.__cols_number = cols_num + 1
        self.__text_fields_bg_layout.cols = cols_num + 1

    def update_padding(self, *args):
        self.__main_layout.padding = [self.__main_layout.size[0] * .1,
                                      self.__main_layout.size[1] * .2,
                                      self.__main_layout.size[0] * .1,
                                      self.__main_layout.size[1] * .2]

    def create_text_inputs(self):
        number_of_text_inputs = self.__cols_number * self.__rows_number
        row_values = 1
        for sep in range(number_of_text_inputs):
            text_field = MDTextField()
            # text_field.size_hint_y = 1 / (self.__rows_number*2)
            text_field.id = "cell_" + str(sep)

            if sep == 0:
                text_field.hint_text = ""

            elif sep < self.__cols_number:
                text_field.hint_text = "Column " + str(sep) + " Value"
                text_field.mode = "fill"
                text_field.fill_color = [.3, .3, .3, .3]

            elif sep != 0 and sep % self.__cols_number == 0:
                text_field.hint_text = "Row " + str(row_values) + " Value"
                text_field.mode = "fill"
                text_field.fill_color = [.1, .1, .9, .4]
                row_values += 1

            else:
                text_field.hint_text = "Cell Value"


            self.__text_fields_bg_layout.add_widget(text_field)
            self.__text_fields.append(text_field)

        self.__main_layout.add_widget(self.__text_fields_bg_layout)
        self.__main_layout.add_widget(self.confirm_button)
        self.add_widget(self.__main_layout)
            
            
class TableScreen(Screen):
    def __init__(self):
        super(TableScreen, self).__init__()
        self.background = MDBoxLayout()
        self.background.orientation = "vertical"
        
        self.table_name_label = MDLabel(text="Company X")
        self.table_name_label.halign = "center"
        self.table_name_label.font_style = "H4"
        self.table_name_label.size_hint_y = 0.3

        self.__table_rows = [("A", "Value1", "Value1", "Value1"),
                             ("B", "Value2", "Value2", "Value2"),
                             ]
        self.__table_cols = [("", dp(20)),
                             ("1", dp(20)),
                             ("2", dp(20)),
                             ("3", dp(20))]
        
        self.create_table()
        self.add_widgets_to_layout()
        self.add_widget(self.background)
        
        def create_table(self):
            self.table = MDDataTable(size_hint=(0.7, 0.6),
                                 pos_hint={"center_x": .5},
                                 column_data=self.__table_cols,
                                 row_data=self.__table_rows)
            
        def add_widgets_to_layout(self):
            self.background.add_widget(self.table_name_label)
            self.background.add_widget(self.table)
            
            
