import PetsOOP as p
import unittest
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta


class TestGetAge(unittest.TestCase):

    def test_get_age_born_today(self):
        # Dog was born today. Expected age = 0
        born_today = p.Dog(name='born_today', birth_date=date.today(), weight=1, color='multicolor',
                           wellness_status='all_good', personality_type='social', num_toys=1)
        self.assertEqual(0, born_today.get_age(), 'Test Failed: test_get_age_born_today')
        print('Test Succeeded: test_get_age_born_today')

    def test_get_age_born_yesterday(self):
        # Dog was born yesterday. Expected age = 0
        birth_date = date.today() - timedelta(days=1)
        born_yesterday = p.Dog(name='born_yesterday', birth_date=birth_date, weight=1, color='multicolor',
                               wellness_status='all_good', personality_type='social', num_toys=1)
        self.assertEqual(0, born_yesterday.get_age(), 'Test Failed: test_get_age_born_yesterday')
        print('Test Succeeded: test_get_age_born_yesterday')

    def test_get_age_born_1month_ago(self):
        # Dog was born 1 month ago. Expected age = 0
        birth_date = date.today() - relativedelta(months=1)
        born_1month_ago = p.Dog(name='born_1month_ago', birth_date=birth_date, weight=1, color='multicolor',
                                wellness_status='all_good', personality_type='social', num_toys=1)
        self.assertEqual(0, born_1month_ago.get_age(), 'Test Failed: test_get_age_born_1month_ago')
        print('Test Succeeded: test_get_age_born_1month_ago')

    def test_get_age_almost_2years_old(self):
        # Dog is almost 2 years old, less than 1 day. Expected age = 1
        birth_date = date.today() - relativedelta(years=2) + timedelta(days=1)
        almost_2years_old = p.Dog(name='almost_2years_old', birth_date=birth_date, weight=1, color='multicolor',
                                  wellness_status='all_good', personality_type='social', num_toys=1)
        self.assertEqual(1, almost_2years_old.get_age(), 'Test Failed: test_get_age_almost_2years_old')
        print('Test Succeeded: test_get_age_almost_2years_old')

    def test_get_age_1year_birthday_today(self):
        # Dog's 1 year birthday is today. Expected age = 1
        birth_date = date.today() - relativedelta(years=1)
        exactly_1year_old = p.Dog(name='exactly_1year_old', birth_date=birth_date, weight=1, color='multicolor',
                                  wellness_status='all_good', personality_type='social', num_toys=1)
        self.assertEqual(1, exactly_1year_old.get_age(), 'Test Failed: test_get_age_1year_birthday_today')
        print('Test Succeeded: test_get_age_1year_birthday_today')

    def test_get_age_5year_birthday_today(self):
        # Dog's 5 year birthday is today. Expected age = 5
        birth_date = date.today() - relativedelta(years=5)
        exactly_5years_old = p.Dog(name='exactly_5years_old', birth_date=birth_date, weight=1, color='multicolor',
                                  wellness_status='all_good', personality_type='social', num_toys=1)
        self.assertEqual(5, exactly_5years_old.get_age(), 'Test Failed: test_get_age_5year_birthday_today')
        print('Test Succeeded: test_get_age_5year_birthday_today')

    def test_get_age_born_feb28_2020(self):
        # 2020 was a leap year, the dog was born on Feb 28th, 2020
        # tester should set the expected age manually depending on the date when testing
        # For example, on Dec 15th, 2024 the dog should be 4 years old
        birth_date = date(2020, 2, 28)
        expected_age = 4
        born_feb28_2020 = p.Dog(name='born_feb28_2020', birth_date=birth_date, weight=1, color='multicolor',
                                wellness_status='all_good', personality_type='social', num_toys=1)
        self.assertEqual(expected_age, born_feb28_2020.get_age(), 'Test Failed: test_get_age_born_feb28_2020')
        print('Test Succeeded: test_get_age_born_feb28_2020')

    def test_get_age_born_feb29_2020(self):
        # 2020 was a leap year, the dog was born on Feb 29th, 2020
        # tester should set the expected age manually depending on the date when testing
        # For example, on Dec 15th, 2024 the dog should be 4 years old
        birth_date = date(2020, 2, 29)
        expected_age = 4
        born_feb29_2020 = p.Dog(name='born_feb29_2020', birth_date=birth_date, weight=1, color='multicolor',
                                wellness_status='all_good', personality_type='social', num_toys=1)
        self.assertEqual(expected_age, born_feb29_2020.get_age(), 'Test Failed: test_get_age_born_feb29_2020')
        print('Test Succeeded: test_get_age_born_feb29_2020')


if __name__ == '__main()__':
    unittest.main()
