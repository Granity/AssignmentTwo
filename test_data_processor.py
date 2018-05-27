import unittest
import io
import sys
from data_processor import DataProcessor


class TestDataProcessor(unittest.TestCase):

    def test_send_to_validate_male_returns_correctly(self):
        # Arrange
        dict_root = {'12345': {'gender': 'male'}}
        expected_result = {'12345': {'gender': 'M', 'valid': '1'}}

        # Act
        result = DataProcessor.send_to_validate(dict_root, '', 0)
        print(result)
        # Assert
        self.assertTrue(result == expected_result)

    def test_send_to_validate_female_returns_correctly(self):
        # Arrange
        dict_root = {'12345': {'gender': 'female'}}
        expected_result = {'12345': {'gender': 'F', 'valid': '1'}}

        # Act
        result = DataProcessor.send_to_validate(dict_root, '', 0)
        print(result)
        # Assert
        self.assertTrue(result == expected_result)

    def test_send_to_validate_invalid_gender_returns_correctly(self):
        # Arrange
        dict_root = {'12345': {'gender': 'wrongdata'}}
        expected_result = {'12345': {'gender': 'wrongdata'}}

        # Act
        result = DataProcessor.send_to_validate(dict_root, '', 0)
        print(result)
        # Assert
        self.assertTrue(result == expected_result)

    def test_send_to_validate_bmi_returns_correctly(self):
        # Arrange
        dict_root = {'12345': {'bmi': 'normal'}}
        expected_result = {'12345': {'bmi': 'Normal', 'valid': '1'}}

        # Act
        result = DataProcessor.send_to_validate(dict_root, '', 0)
        print(result)
        # Assert
        self.assertTrue(result == expected_result)

    def test_send_to_validate_invalid_bmi_returns_correctly(self):
        # Arrange
        dict_root = {'12345': {'bmi': 'wrongdata'}}
        expected_result = {'12345': {'bmi': 'wrongdata'}}

        # Act
        result = DataProcessor.send_to_validate(dict_root, '', 0)
        print(result)
        # Assert
        self.assertTrue(result == expected_result)

    def test_send_to_validate_birthday_returns_correctly(self):
        # Arrange
        dict_root = {'12345': {'birthday': '20/01/1876'}}
        expected_result = {'12345': {'birthday': '20/01/1876', 'valid': '1'}}

        # Act
        result = DataProcessor.send_to_validate(dict_root, '', 0)
        print(result)
        # Assert
        self.assertTrue(result == expected_result)

    def test_send_to_validate_invalid_birthday_returns_correctly(self):
        # Arrange
        dict_root = {'12345': {'birthday': '200/011/180176'}}
        expected_result = {'12345': {'birthday': '200/011/180176'}}

        # Act
        result = DataProcessor.send_to_validate(dict_root, '', 0)
        print(result)
        # Assert
        self.assertTrue(result == expected_result)

    def test_send_to_validate_age_returns_correctly(self):
        # Arrange
        dict_root = {'12345': {'age': '25'}}
        expected_result = {'12345': {'age': '25', 'valid': '1'}}

        # Act
        result = DataProcessor.send_to_validate(dict_root, '', 0)
        print(result)
        # Assert
        self.assertTrue(result == expected_result)

    def test_send_to_validate_invalid_age_returns_correctly(self):
        # Arrange
        dict_root = {'12345': {'age': '125'}}
        expected_result = {'12345': {'age': '125'}}

        # Act
        result = DataProcessor.send_to_validate(dict_root, '', 0)
        print(result)
        # Assert
        self.assertTrue(result == expected_result)


    def test_send_to_validate_invalid_salary_returns_correctly(self):
        # Arrange
        dict_root = {'12345': {'salary': '9000'}}
        expected_result = {'12345': {'salary': '9000'}}

        # Act
        result = DataProcessor.send_to_validate(dict_root, '', 0)
        print(result)
        # Assert
        self.assertTrue(result == expected_result)

    def test_send_to_validate_sales_returns_correctly(self):
        # Arrange
        dict_root = {'12345': {'sales': '123'}}
        expected_result = {'12345': {'sales': '123', 'valid': '1'}}

        # Act
        result = DataProcessor.send_to_validate(dict_root, '', 0)
        print(result)
        # Assert
        self.assertTrue(result == expected_result)


    def test_send_to_validate_invalid_sales_returns_correctly(self):
        # Arrange
        dict_root = {'12345': {'sales': '12345'}}
        expected_result = {'12345': {'sales': '12345'}}

        # Act
        result = DataProcessor.send_to_validate(dict_root, '', 0)
        print(result)
        # Assert
        self.assertTrue(result == expected_result)

    def test_validate_key_returns_correctly(self):
        # Arrange
        key_to_validate = 'a123'
        expected_result = 'A123'

        # Act
        result = DataProcessor.validate_key(key_to_validate)
        print(result)
        # Assert
        self.assertTrue(result == expected_result)

    def test_validate_key_invalid_returns_correctly(self):
        # Arrange
        key_to_validate = 'QWE12345'
        expected_result = 'Qwe12345'

        # Act
        result = DataProcessor.validate_key(key_to_validate)
        print(result)
        # Assert
        self.assertTrue(result == expected_result)

    def test_send_to_validate_rows_of_valid_data(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        # the method you're testing here

        dict_root = {'12345': {'sales': '123'}}
        DataProcessor.send_to_validate(dict_root, 'd', 0)

        sys.stdout = sys.__stdout__
        expected_output = '1 Rows Of Valid Data'
        print(captured_output.getvalue())
        # Check if the printed output includes expected strings I'm looking for
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        # Assert
        self.assertTrue(result)

    def test_send_to_validate_rows_of_invalid_data(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        # the method you're testing here

        dict_root = {'12345': {'sales': '12345'}}
        DataProcessor.send_to_validate(dict_root, 'd', 0)

        sys.stdout = sys.__stdout__
        expected_output = '1 Rows Of Invalid Data'
        print(captured_output.getvalue())
        # Check if the printed output includes expected strings I'm looking for
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        # Assert
        self.assertTrue(result)

    def test_send_to_validate_rows_of_duplicate_data(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        # the method you're testing here

        dict_root = {'12345': {'sales': '12345'}}
        DataProcessor.send_to_validate(dict_root, 'd', 0)

        sys.stdout = sys.__stdout__
        expected_output = '0 Duplicate ID Key(s) appended to log'
        print(captured_output.getvalue())
        # Check if the printed output includes expected strings I'm looking for
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        # Assert
        self.assertTrue(result)
