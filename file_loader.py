import os.path
import sys

from openpyxl import load_workbook

from data_processor import DataProcessor
from databases.database_sqlite import CompanyDatabase
from log_file_handler import LogFileHandler
from file_saver import FileSaver
from file_processor import FileProcessor

try:
    from errors import ErrorHandler as Err
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - Err.py not found.")
    sys.exit()

try:
    from database_excel import DatabaseExcel as Dbexel
except NameError and ModuleNotFoundError and ImportError:
    print(Err.get_error_message(404, "database_excel"))
    sys.exit()


class FileLoader(object):  # Claye

    def call_file(self, switch, separator):
        file_name = input("Please enter the filename to read data from >>> ")
        split_filename = file_name.split(".")
        file_extension = split_filename[-1]
        if file_extension == "xls" or file_extension == "xlsx":
            try:
                wb = load_workbook(file_name)
                i = Dbexel()
                data_to_save = i.create_connection(wb, switch)
                FileSaver.write_file(FileSaver(), data_to_save)
            except FileNotFoundError:
                print(Err.get_error_message(201))
            except OSError:
                print(Err.get_error_message(103))
        elif file_extension == "txt" or file_extension == "csv":
            try:
                self.open_file(file_name, switch, separator)
                # file = open(file_name, "r")
                # file.close()
                # FileProcessor.split_file(FileProcessor(), file_name, switch, separator)
            except FileNotFoundError:
                print(Err.get_error_message(201))
            except OSError:
                print(Err.get_error_message(103))
        else:
            print(Err.get_error_message(204))

    def open_file(self, file_name, switch, separator=","):
        try:
            file = open(file_name, "r")
        except FileNotFoundError:
            print(Err.get_error_message(201))
        else:
            FileProcessor.split_file(FileProcessor(), file, switch, separator)

    def load_pickle_file(self):  # Claye, Graham
        file_target = self.get_input("Please input the filename to load from >>> ")
        # self.commit_pickle_save(file_target, data_to_write)
        try:
            file = open(file_target, "rb")
            with open(file_target) as file:
                lines = file.readlines()
                print(lines)
                return lines
        except FileNotFoundError:
            print(Err.get_error_message(201))
        except OSError:
            print(Err.get_error_message(103))

    @staticmethod
    def get_input(text):
        return input(text)
