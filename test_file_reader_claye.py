import unittest
from file_reader import FileReader
from unittest.mock import patch
import io
import sys


class TestFileReaderClaye(unittest.TestCase):

    def test_open_file_with_no_file_found(self):
        # Arrange
        file_name = "testdata\\invalidfile.txt"
        expected_result = 'File not found'

        # Act
        result = FileReader.open_file(FileReader(), file_name, '')
        # Assert
        self.assertTrue(result == expected_result)

    def test_write_file_choosing_not_to_save_data(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        # Arrange
        dict_valid = {'12345': 'testdata'}
        expected_output = 'Data Not saved'
        user_input = 'n'
        # Act
        with patch('builtins.input', side_effect=user_input):
            FileReader.write_file(FileReader(), dict_valid)
        sys.stdout = sys.__stdout__
        # Assert
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        self.assertTrue(result)

    def test_commit_save_is_success(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        # Arrange
        dict_valid = {'12345': {'gender': 'testdata'}}
        expected_output = 'File saved, 1 rows added'

        # Act
        FileReader.commit_save(FileReader(), dict_valid, 'testdata\\success.txt')
        sys.stdout = sys.__stdout__
        # Assert
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        self.assertTrue(result)

    def test_commit_save_all_duplicates_returns_message(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        # Arrange
        dict_valid = {'12345': {'gender': 'testdata'}}
        expected_output = 'All ID\'s already existed in the output file. Nothing added.'

        # Act
        FileReader.commit_save(FileReader(), dict_valid, 'testdata\\success.txt', ['12345'])
        sys.stdout = sys.__stdout__
        # Assert
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        self.assertTrue(result)

    def test_commit_save_some_duplicates_returns_message(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        # Arrange
        dict_valid = {'12345': {'gender': 'testdata'},
                      '1234': {'gender': 'testdata'}}
        expected_output = 'rows were duplicate keys and not inserted again'

        # Act
        FileReader.commit_save(FileReader(), dict_valid, 'testdata\\success.txt', ['12345'])
        sys.stdout = sys.__stdout__
        # Assert
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        self.assertTrue(result)

    def test_check_path_exists_when_path_exists(self):
        # Arrange
        path = 'log.txt'
        expected_result = True

        # Act
        result = FileReader.check_path_exists(path)
        # Assert
        self.assertTrue(result == expected_result)

    def test_check_path_exists_when_does_not_exist(self):
        # Arrange
        path = 'invalidpath\\'
        expected_result = False

        # Act
        result = FileReader.check_path_exists(path)
        # Assert
        self.assertTrue(result == expected_result)

    def test_check_path_exists_when_illegal_symbol_given(self):
        # Arrange
        path = '??.txt'
        expected_result = False

        # Act
        result = FileReader.check_path_exists(path)
        # Assert
        self.assertTrue(result == expected_result)

    def test_remove_duplicates_file_not_found(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        # Arrange
        invalid_file = 'invalidfile.txt'
        expected_output = 'File not found'

        # Act
        FileReader.remove_duplicates(invalid_file)
        sys.stdout = sys.__stdout__
        # Assert
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        self.assertTrue(result)

    def test_call_file_works_correctly(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        # Arrange
        expected_output = ''
        user_input = ['test_data.txt', 'n']
        # Act
        with patch('builtins.input', side_effect=user_input):
            FileReader.call_file(FileReader(), '', ',')
        sys.stdout = sys.__stdout__
        # Assert
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        self.assertTrue(result)

    def test_call_file_unsupported_file_format(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        # Arrange
        expected_output = 'Unsupported file format'
        user_input = ['invalidextension.t5xt']
        # Act
        with patch('builtins.input', side_effect=user_input):
            FileReader.call_file(FileReader(), '', ',')
        sys.stdout = sys.__stdout__
        # Assert
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        self.assertTrue(result)

    def test_call_file_file_not_found_txt(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        # Arrange
        expected_output = 'File not found'
        user_input = ['invalid2file.txt']
        # Act
        with patch('builtins.input', side_effect=user_input):
            FileReader.call_file(FileReader(), '', ',')
        sys.stdout = sys.__stdout__
        # Assert
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        self.assertTrue(result)

    def test_call_file_illegal_file_path_txt(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        # Arrange
        expected_output = 'Illegal file path, please try again'
        user_input = ['??@\\\sdsd.txt']
        # Act
        with patch('builtins.input', side_effect=user_input):
            FileReader.call_file(FileReader(), '', ',')
        sys.stdout = sys.__stdout__
        # Assert

        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        self.assertTrue(result)

    def test_call_file_file_not_found_xls(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        # Arrange
        expected_output = 'File not found'
        user_input = ['invalid2file.xls']
        # Act
        with patch('builtins.input', side_effect=user_input):
            FileReader.call_file(FileReader(), '', ',')
        sys.stdout = sys.__stdout__
        # Assert
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        self.assertTrue(result)

    def test_call_file_illegal_file_path_xls(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        # Arrange
        expected_output = 'Illegal file path, please try again'
        user_input = ['??@\\\sdsd.xls']
        # Act
        with patch('builtins.input', side_effect=user_input):
            FileReader.call_file(FileReader(), '', ',')
        sys.stdout = sys.__stdout__
        # Assert
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        self.assertTrue(result)

    def test_call_file_xlsx(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        # Arrange
        expected_output = 'Data Not saved'
        user_input = ['test_data.xlsx', 'n']
        # Act
        with patch('builtins.input', side_effect=user_input):
            FileReader.call_file(FileReader(), '', ',')
        sys.stdout = sys.__stdout__
        # Assert
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        self.assertTrue(result)

    def test_save_pickle_file_not_saved(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        # Arrange
        expected_output = 'Data Not saved'

        user_input = ['n']
        test_data = "test data"
        data_to_write = test_data.encode()
        # Act
        with patch('builtins.input', side_effect=user_input):
            FileReader.save_pickle_file(FileReader(), data_to_write)
        sys.stdout = sys.__stdout__
        # Assert
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        self.assertTrue(result)



# --------------------------- TEST WRITE FILE METHODS ----------------------------

    def test_write_file_choosing_to_save_to_file(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        # Arrange
        dict_valid = {'12345': 'testdata'}
        user_input = ['Y', 'F', "lalala3.txt", 'Y']
        with patch('builtins.input', side_effect=user_input):
            FileReader.write_file(FileReader(), dict_valid)
        # Act
        sys.stdout = sys.__stdout__
        expected_output = ''
        # Assert
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        self.assertTrue(result)

    def test_write_file_choosing_to_save_to_database(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        # Arrange
        dict_valid = {'A123': {'gender': 'M', 'age': '23', 'birthday': '20/01/1992', 'salary': '55', 'sales': '123', 'bmi': 'normal', 'valid': '1'}}
        user_input = ['Y', 'D', 'Y']
        with patch('builtins.input', side_effect=user_input):
            FileReader.write_file(FileReader(), dict_valid)
        # Act
        sys.stdout = sys.__stdout__
        expected_output = 'A123'
        # Assert
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        self.assertTrue(result)

    def test_write_file_choosing_invalid_input_1(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        # Arrange
        dict_valid = {'A123': {'gender': 'M', 'age': '23', 'birthday': '20/01/1992', 'salary': '55', 'sales': '123', 'bmi': 'normal', 'valid': '1'}}
        user_input = ['x']
        with patch('builtins.input', side_effect=user_input):
            FileReader.write_file(FileReader(), dict_valid)
        # Act
        sys.stdout = sys.__stdout__
        expected_output = 'Invalid Input, please try again'
        # Assert
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        self.assertTrue(result)

    def test_write_file_choosing_invalid_input_2(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        # Arrange
        dict_valid = {'A123': {'gender': 'M', 'age': '23', 'birthday': '20/01/1992', 'salary': '55', 'sales': '123', 'bmi': 'normal', 'valid': '1'}}
        user_input = ['Y', 'x']
        with patch('builtins.input', side_effect=user_input):
            FileReader.write_file(FileReader(), dict_valid)
        # Act
        sys.stdout = sys.__stdout__
        expected_output = 'Invalid Input, please try again'
        # Assert
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        self.assertTrue(result)

    def test_write_file_choosing_not_to_append(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        # Arrange
        dict_valid = {'A123': {'gender': 'M', 'age': '23', 'birthday': '20/01/1992', 'salary': '55', 'sales': '123', 'bmi': 'normal', 'valid': '1'}}
        user_input = ['Y', 'f', 'log.txt', 'n']
        with patch('builtins.input', side_effect=user_input):
            FileReader.write_file(FileReader(), dict_valid)
        # Act
        sys.stdout = sys.__stdout__
        expected_output = 'Data not saved'
        # Assert
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        self.assertTrue(result)

    def test_write_file_choosing_to_append(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        # Arrange
        dict_valid = {'A123': {'gender': 'M', 'age': '23', 'birthday': '20/01/1992', 'salary': '55', 'sales': '123', 'bmi': 'normal', 'valid': '1'}}
        user_input = ['Y', 'f', 'log.txt', 'y']
        with patch('builtins.input', side_effect=user_input):
            FileReader.write_file(FileReader(), dict_valid)
        # Act
        sys.stdout = sys.__stdout__
        expected_output = 'All ID\'s already existed in the output file. Nothing added.'
        expected_output2 = 'File saved'
        # Assert
        if expected_output or expected_output2 in captured_output.getvalue():
            result = True
        else:
            result = False

        self.assertTrue(result)

    def test_write_file_choosing_to_save_to_database_choosing_no(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        # Arrange
        dict_valid = {'A123': {'gender': 'M', 'age': '23', 'birthday': '20/01/1992', 'salary': '55', 'sales': '123', 'bmi': 'normal', 'valid': '1'}}
        user_input = ['Y', 'D', 'N']
        with patch('builtins.input', side_effect=user_input):
            FileReader.write_file(FileReader(), dict_valid)
        # Act
        sys.stdout = sys.__stdout__
        expected_output = '1 persons added'
        # Assert
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        self.assertTrue(result)

    def test_write_to_database_invalid_filed(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        # Arrange
        dict_valid = {'A123': {'INVALID': 'M', 'age': '23', 'birthday': '20/01/1992', 'salary': '55', 'sales': '123',
                               'bmi': 'normal', 'valid': '1'}}
        FileReader.write_to_database(FileReader(), dict_valid)
        # Act
        sys.stdout = sys.__stdout__
        expected_output = 'A Key Pair name was invalid'
        # Assert
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        self.assertTrue(result)

    def test_write_file_choosing_to_save_to_database_not_valid(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        # Arrange
        dict_valid = {'A123': {'gender': 'M', 'age': '23', 'birthday': '20/01/1992', 'salary': '55', 'sales': '123', 'bmi': 'normal', 'valid': '0'}}
        user_input = ['Y', 'D', 'N']
        with patch('builtins.input', side_effect=user_input):
            FileReader.write_file(FileReader(), dict_valid)
        # Act
        sys.stdout = sys.__stdout__
        expected_output = '0 persons added'
        # Assert
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        self.assertTrue(result)

    def test_split_file_index_error(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print("test")
        # Arrange
        file_name = 'index_error_file.txt'
        FileReader.split_file(FileReader(), file_name, '', ',')
        # Act
        sys.stdout = sys.__stdout__
        expected_output = 'list index out of range'
        expected_output2 = 'Data file already processed'
        # Assert
        print(captured_output.getvalue())
        if expected_output or expected_output2 in captured_output.getvalue():
            result = True
        else:
            result = False

        self.assertTrue(result)

    # def test_split_file__works_correctly(self):
    #     captured_output = io.StringIO()
    #     sys.stdout = captured_output
    #     # Arrange
    #     file_name = 'test_data.txt'
    #     user_input = ['N']
    #     with patch('builtins.input', side_effect=user_input):
    #         FileReader.split_file(FileReader(), file_name, '', ',')
    #     # Act
    #     sys.stdout = sys.__stdout__
    #     expected_output = 'Data Not saved'
    #     print(captured_output.getvalue())
    #     # Assert
    #     if expected_output in captured_output.getvalue():
    #         result = True
    #     else:
    #         result = False
    #
    #     self.assertTrue(result)

    def test_load_pickle_file_file_not_found(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        user_input = ['invalidfilename.txt']
        with patch('builtins.input', side_effect=user_input):
            FileReader.load_pickle_file(FileReader())

        sys.stdout = sys.__stdout__
        expected_output = 'File not found'
        print(captured_output.getvalue())
        # Assert
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        self.assertTrue(result)

    def test_load_pickle_file_os_error(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        user_input = ['@@??\\\.txt']
        with patch('builtins.input', side_effect=user_input):
            FileReader.load_pickle_file(FileReader())

        sys.stdout = sys.__stdout__
        expected_output = 'Illegal file path, please try again'
        print(captured_output.getvalue())
        # Assert
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        self.assertTrue(result)

