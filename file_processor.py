import os.path
import sys

from openpyxl import load_workbook

from data_processor import DataProcessor
from databases.database_sqlite import CompanyDatabase
from log_file_handler import LogFileHandler
from file_saver import FileSaver

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


class FileProcessor(object):  # Claye

    dict_root = {}

    def split_file(self, file, switch, separator=","):
        results = False
        for line in file:
            results = self.process_file(line, separator)
        if results[0]:
            valid_dict = DataProcessor.send_to_validate(self.dict_root, switch, results[1])
            FileSaver.write_file(FileSaver(), valid_dict)

    @staticmethod
    def process_file(line, separator):
        keep_going = True
        dup_keys = 0
        fields = line.split(separator)
        checked_id = DataProcessor.validate_key(fields[0])
        if checked_id in FileProcessor.dict_root:
            dup_keys += 1
            FileProcessor.log_duplicate_row(fields)
        else:
            keep_going = FileProcessor.assign_data_to_fields(checked_id, fields)
        return keep_going, dup_keys

    @staticmethod
    def assign_data_to_fields(checked_id, fields):
        try:
            print(fields)
            FileProcessor.dict_root.update({checked_id: {'gender': fields[1], 'age': fields[2], 'sales': fields[3],
                                                         'bmi': fields[4], 'salary': fields[5], 'birthday': fields[6],
                                                         'valid': '0'}})

            return True
        except IndexError:
            print(Err.get_error_message(211), 'harro2')
            return False

    @staticmethod
    def log_duplicate_row(fields):
        try:
            fields[6] = fields[6].rstrip()
            data_to_log = "Duplicate Key" + str(fields[0:])
            LogFileHandler.append_file('log.txt', data_to_log)
        except IndexError:
            print(Err.get_error_message(211))


