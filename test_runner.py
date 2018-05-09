import unittest
import test_file_reader_claye
import test_data_processor

loader = unittest.TestLoader()
all_my_tests = unittest.TestSuite()

all_my_tests.addTests(loader.loadTestsFromModule(test_file_reader_claye))
all_my_tests.addTests(loader.loadTestsFromModule(test_data_processor))

runner = unittest.TextTestRunner()
result = runner.run(all_my_tests)
