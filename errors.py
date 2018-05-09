from databases.pickler import Pickler


class ErrorHandler(object):  # Claye

    @staticmethod
    def get_error_message(error_code, name=""):

        error_dict = ErrorHandler.get_error_dict(name)

        try:
            return error_dict[error_code]
        except KeyError:
            return "Unknown Error"

    @staticmethod
    def send_data_to_pickler():
        to_pickle = ErrorHandler.get_error_dict('')
        pickled = Pickler.pickle_list(to_pickle)
        return pickled

    @staticmethod
    def get_error_dict(name):
        error_dictionary = {  # CLI Errors -----
            101: "Command not supported",
            102: "Invalid Input, please try again",
            103: "Illegal file path, please try again",
            104: "Exception in command line: {}".format(name),
            105: "Invalid switch - Use /? to see valid options",
            # File Errors -----
            201: "File not found",
            202: "Unable to load file",
            203: "Unable to save file",
            204: "Unsupported file format",
            205: "Unable to edit log file",
            206: "Empty data field",
            207: "Invalid data field",
            208: "File empty",
            209: "Database empty",
            210: "No valid data found",  # Rochelle
            211: "Data file already processed",  # Graham
            # Validation Errors -----
            301: "Unable to validate data",
            # System File Errors ----- # Graham
            401: "Warning - {} file could not be created".format(name),
            402: "Warning - Unknown error creating {} file".format(name),
            403: "Warning - {} not found".format(name),
            404: "Fatal Error - {} not found".format(name),
            405: "Error - {} file is read only".format(name),
            # Database Errors ----- # Graham
            501: "Error - {} key is not valid, please try again".format(name),
            # Chart Errors ----- # Graham
            601: "Data in this chart type not supported",
            602: "Not enough data given to the chart",
            # General Errors ----- # Graham
            901: "Exception during import: {}".format(name)
        }

        return error_dictionary
