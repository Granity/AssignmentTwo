import unittest
from errors import ErrorHandler


class TestErrors(unittest.TestCase):

    def test_get_error_message_returns_correct_error(self):
        # Arrange
        error_number = 103
        expected_result = 'Illegal file path, please try again'

        # Act
        result = ErrorHandler.get_error_message(error_number)
        # Assert
        self.assertTrue(result == expected_result)

    def test_get_error_message_returns_formatted_message(self):
        # Arrange
        error_number = 104
        error_message = 'test case'
        expected_result = 'Exception in command line: test case'

        # Act
        result = ErrorHandler.get_error_message(error_number, error_message)
        # Assert
        self.assertTrue(result == expected_result)

    def test_get_error_message_returns_error_not_found(self):
        # Arrange
        error_number = 999
        expected_result = 'Unknown Error'
        # Act
        result = ErrorHandler.get_error_message(error_number)
        # Assert
        self.assertTrue(result == expected_result)

    def test_send_data_to_pickler(self):
        # Arrange
        to_pickle = 'test pickle'
        expected_result = '<class \'bytes\'>'
        # Act
        result = str(type(ErrorHandler.send_data_to_pickler()))
        # Assert
        self.assertTrue(result == expected_result)
