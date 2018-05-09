from validators.validate_age import ValidateAge as Va
from validators.validate_bmi import ValidateBmi as Vb
from validators.validate_date import ValidateDate as Vd
from validators.validate_emp_id import ValidateEmpId as Ve
from validators.validate_gender import ValidateGender as Vg
from validators.validate_salary import ValidateSalary as Vs
from validators.validate_sales import ValidateSales as Vsa
import sys


class DataProcessor(object):    # Claye #############  Duplicate code ###########
    @staticmethod
    def send_to_validate(dict_root, switch, dup_keys):
        dict_list = {'gender': 'Vg', 'bmi': 'Vb', 'birthday': 'Vd', 'age': 'Va', 'salary': 'Vs', 'sales': 'Vsa'}
        valid_rows = 0
        invalid_rows = 0
        for k, v in dict_root.items():
            valid = 0
            length_of_values = len(v)
            result = Ve.is_valid(k)
            if result[1]:
                valid += 1
            for kv in v.keys():
         # ---------------------NEW CODE ------------------------------
                if kv in dict_list.keys():
                    matching_key = dict_list[kv]
                    class_target = getattr(sys.modules[__name__], matching_key)
                    i = class_target()
                    result = i.is_valid(dict_root[k][kv])
                    if result[1]:
                        dict_root[k][kv] = result[0]
                        valid += 1
           # -------------------------------------------------------
            if valid == length_of_values:
                dict_root[k]['valid'] = '1'
                valid_rows += 1
            else:
                invalid_rows += 1
        if switch.upper() == 'D':
            print("{0} Rows Of Valid Data".format(valid_rows))
            print("{0} Rows Of Invalid Data".format(invalid_rows))
            print("{0} Duplicate ID Key(s) appended to log".format(dup_keys))
        return dict_root

    @staticmethod
    def validate_key(key_to_validate):
        """
        >>> DataProcessor.validate_key('a001')
        'A001'
        >>> DataProcessor.validate_key('a123')
        'A123'
        >>> DataProcessor.validate_key('abc5')
        'Abc5'
        >>> DataProcessor.validate_key('')
        ''
        >>> DataProcessor.validate_key('        ')
        ''
        """
        result = Ve.is_valid(key_to_validate)
        return result[0]


if __name__ == "__main__":
    import doctest

    doctest.testmod(Verbose=True)
