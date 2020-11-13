import pandas as pd

class TableManager():

    @classmethod
    def set_show_max_rows(cls, size):
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', size)

    @classmethod
    def set_show_max_columns(cls, size):
        pd.set_option('display.max_columns', size)
    
    @classmethod
    def set_show_all_columns(cls):
        pd.set_option('display.max_columns', None)

    @classmethod
    def set_show_all_rows(cls):
        pd.set_option('display.max_rows', None)

    @classmethod
    def set_show_all_rows_and_columns(cls):
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)