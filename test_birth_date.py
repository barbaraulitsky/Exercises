import PetsOOP as p
import unittest
from datetime import date


class TestBirthDate(unittest.TestCase):
    def test_birth_date_invalid_type_int(self):
        with self.assertRaises(TypeError):
            test_birth_date_invalid_type_int = p.Dog(birth_date=5)
        print('Test Succeeded: test_birth_date_invalid_type_int')

    def test_birth_date_invalid_type_float(self):
        with self.assertRaises(TypeError):
            test_birth_date_invalid_type_float = p.Dog(birth_date=3.2)
        print('Test Succeeded: test_birth_date_invalid_type_float')

    def test_birth_date_invalid_type_string(self):
        with self.assertRaises(TypeError):
            test_birth_date_invalid_type_string = p.Dog(birth_date='date(2020, 1, 31)')
        print('Test Succeeded: test_birth_date_invalid_type_string')


if __name__ == '__main()__':
    unittest.main()
