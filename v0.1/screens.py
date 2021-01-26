from kivymd.uix.textfield import MDTextField
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.metrics import dp


from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel
from kivy.metrics import dp


class GetRowColScreen(Screen):
    def __init__(self, rows_number=1, cols_number=1):
        super(GetRowColScreen, self).__init__()
        self.rows_number = rows_number
        self.cols_number = cols_number
        self.rows_text_input = []
        self.cols_text_input = []
        self.background = MDBoxLayout()
        self.confirm_button = MDFillRoundFlatButton()
        self.confirm_button.text = "Create"

        self.background.orientation = "vertical"
        self.background.padding = [60, 60, 60, 60]
        print("Rows: ", self.rows_text_input)
        print("Cols: ", self.cols_text_input)
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

    def add_input_text_to_bg(self):
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

        self.confirm_button.size_hint_y = self.element_size_hint / 2
        self.confirm_button.size_hint_x = .5
        self.confirm_button.pos_hint = {"center_x": .5}
        # self.add_widget(self.confirm_button)
        self.background.add_widget(self.confirm_button)

    def add_all_widget_to_background(self):
        self.create_rows_text_inputs()
        self.create_cols_text_inputs()
        self.add_input_text_to_bg()


class RowColInputScreen(Screen):
    def __init__(self):
        super(RowColInputScreen, self).__init__()
        self.__main_layout = MDBoxLayout()
        self.__main_layout.orientation = "vertical"

        self.__text_fields_bg_layout = MDGridLayout()
        self.__text_fields_bg_layout.size_hint_y = .8

        self.confirm_button = MDFillRoundFlatButton()
        self.confirm_button.text = "CREATE TABLE"
        self.confirm_button.size_hint_x = .6
        self.confirm_button.size_hint_y = .1
        self.confirm_button.pos_hint = {"center_x": .5, "center_y": .5}

        self.__text_fields_bg_layout.spacing = 20
        self.__text_fields_bg_layout.bind(size=self.update_padding)
        self.__text_fields_bg_layout.bind(pos=self.update_padding)

        self.__rows_number = None
        self.__cols_number = None
        self.__row_headers = []
        self.__col_headers = []
        self.__cell_values = []
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

    @property
    def row_headers(self):
        return self.__row_headers

    @property
    def col_headers(self):
        return self.__col_headers

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
                self.__col_headers.append(text_field)

            elif sep != 0 and sep % self.__cols_number == 0:
                text_field.hint_text = "Row " + str(row_values) + " Value"
                text_field.mode = "fill"
                text_field.fill_color = [.1, .1, .9, .4]
                row_values += 1
                self.__row_headers.append(text_field)

            else:
                text_field.hint_text = "Cell Value"
                self.__cell_values.append(text_field)

            self.__text_fields_bg_layout.add_widget(text_field)
            self.__text_fields.append(text_field)

        self.__main_layout.add_widget(self.__text_fields_bg_layout)
        self.__main_layout.add_widget(self.confirm_button)
        self.add_widget(self.__main_layout)

    def get_row_md_table_format(self):
        rows = []
        for row_header in self.__row_headers:
            rows.append([row_header.text])

        col_control_value = 0
        col_number = self.__cols_number - 1
        number_of_cells = len(self.__cell_values)

        for sep in range(number_of_cells):
            print("Sep: ", sep)
            print("Col Control Stat: ", col_control_value)
            rows[col_control_value].append(self.__cell_values[sep].text)

            """ Updating for the column order """
            control_stat = sep != 0 and sep % col_number == 0
            if control_stat:
                col_control_value += 1

        for sep in range(len(rows)):
            rows[sep] = tuple(rows[sep])

        return rows

    def get_col_md_table_format(self):
        cols = []
        for column in self.__col_headers:
            cols.append(tuple([column.text, dp(20)]))

        return cols


class TableScreen(Screen):
    def __init__(self):
        super(TableScreen, self).__init__()
        self.background = MDBoxLayout()
        self.background.orientation = "vertical"
        self.__table = None
        self.__table_rows = None
        self.__table_cols = None

        self.table_name_label = MDLabel(text="Company X")
        self.table_name_label.halign = "center"
        self.table_name_label.font_style = "H4"
        self.table_name_label.size_hint_y = 0.3
        self.background.add_widget(self.table_name_label)

    def load_table_rows(self, rows):
        self.__table_rows = rows

    def load_table_cols(self, cols):
        self.__table_cols = cols

    def get_table_rows(self):
        return self.__table_rows

    def create_table(self):
        self.add_space_first_column()
        self.__table = MDDataTable(size_hint=(0.7, 0.6),
                                   pos_hint={"center_x": .5},
                                   column_data=self.__table_cols,
                                   row_data=self.__table_rows)
        # self.__table.bind(on_row_press=self.on_row_press)

    def print_row_cols(self):
        print("Table Rows: ", self.__table_rows)
        print("Table Cols: ", self.__table_cols)

    def add_space_first_column(self):
        self.__table_cols.insert(0, ("", dp(30)))

    def add_widget_to_layout(self):
        self.background.add_widget(self.__table)
        self.add_widget(self.background)

    def place_widget(self):
        self.create_table()
        self.add_widget_to_layout()