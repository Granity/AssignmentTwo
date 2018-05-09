import os.path
import sys

from openpyxl import load_workbook

from data_processor import DataProcessor
from databases.database_sqlite import CompanyDatabase
from log_file_handler import LogFileHandler



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


class FileSaver(object):  # Claye

    def __init__(self):
        self.db = CompanyDatabase

    def write_file(self, dict_valid):  # Claye
        u = self.get_input("Are you sure you want to save data? Y/N >>> ")
        if u.upper() == "Y":
            # Rochelle
            db = self.get_input("Do you want to save to a database ot file? D/F >>> ")
            if db.upper() == "D":  # Rochelle
                self.write_to_database(dict_valid)  # Rochelle
            elif db.upper() == "F":
                file_target = input("Please input filename to save to >>> ")
                if self.check_path_exists(file_target):
                    u2 = input("File exists, do you want to append Y/N >>> ")
                    if u2.upper() == 'Y':
                        ids_already_in_file = self.remove_duplicates(file_target)
                        self.commit_save(dict_valid, file_target, ids_already_in_file)
                    if u2.upper() == 'N':
                        print('Data not saved')
                else:
                    self.commit_save(dict_valid, file_target)
            else:
                print(Err.get_error_message(102))
        elif u.upper() == "N":
            print("Data Not saved")
        else:
            print(Err.get_error_message(102))

    def save_pickle_file(self, data_to_write):  # Claye, Graham
        u = input("Are you sure you want to save data? Y/N >>> ")
        if u.upper() == "Y":
            file_target = input("Please input the filename to save to >>> ")
            self.commit_pickle_save(file_target, data_to_write)
        elif u.upper() == "N":
            print("Data Not saved")

    @staticmethod
    def commit_pickle_save(file_target, data_to_write):  # Claye, Graham
        file = open(file_target, "wb")
        data_to_write = str(data_to_write)
        file.write(data_to_write + "\n")
        file.close()

    def commit_save(self, dict_valid, file_target, ids_already_in_file=[]):  # Claye and Graham
        dup_keys = 0
        rows_saved = 0
        rows = 0

        try:
            z = open(file_target, "a")
            for key in dict_valid:
                if key not in ids_already_in_file:
                    z.write("\n")
                    z.write(key + ",")
                    for value in dict_valid[key]:
                        h = str(dict_valid[key][value]) + ","
                        z.write(value + ' ' + h)

                    rows_saved += 1
                    rows += 1
                else:
                    dup_keys += 1
                    rows += 1
            z.write("\n")
            z.close()
            if dup_keys == 0:
                print("File saved, {} rows added".format(rows_saved))
            elif dup_keys == rows:
                print("All ID's already existed in the output file. Nothing added.")
            elif dup_keys > 0:
                print("{} of {} rows were duplicate keys and not inserted again".format(dup_keys, rows))
                print("{} rows were added, and the file saved".format(rows_saved))
        except OSError:
            print(Err.get_error_message(103))
            self.write_file(dict_valid)

    @staticmethod
    def check_path_exists(path):  # Claye
        result = False
        try:
            if os.path.exists("{}".format(path)):
                result = True
                return result
            else:
                return result
        except OSError:
            print(Err.get_error_message(103))

    # Rochelle
    def write_to_database(self, dict_valid):  # Rochelle

        db = CompanyDatabase()
        db.create_connection()

        data = []
        keys = []
        keys += dict_valid.keys()
        data += dict_valid.values()
        count = 0
        try:
            for item in data:
                if item['valid'] == '1':
                    db_v = item['valid']
                    db_id = keys[count]
                    count += 1
                    if item['gender']:
                        db_g = item['gender'] + ","
                    if item['age']:
                        db_a = item['age'] + ","
                    if item['sales']:
                        db_sale = item['sales'] + ","
                    if item['bmi']:
                        db_bm = item['bmi'] + ","
                    if item['salary']:
                        db_sala = item['salary'] + ","
                    if item['birthday']:
                        db_bi = item['birthday'] + ","

                    db.insert_staff([(db_id, db_g, db_a, db_sale, db_bm,
                                      db_sala, db_bi, db_v)])

            print(count, "persons added! Congratulations!")
            # Rochelle
            view_db = input("Do you want to see data saved to database? Y/N >>> ")
            if view_db.upper() == "Y":
                db.get_staff()
        except KeyError:
            print('A Key Pair name was invalid')
        db.close()

    @staticmethod
    def remove_duplicates(file_name):  # Graham
        ids_already_in_file = []

        try:
            file = open(file_name, "r")
        except FileNotFoundError:
            print(Err.get_error_message(201))
        else:
            for line in file:
                fields = line.split(',')
                if fields[0] != "\n":
                    ids_already_in_file.append(fields[0])

            file.close()

        return ids_already_in_file

    @staticmethod
    def get_input(text):
        return input(text)

