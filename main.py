from datetime import date
import PetsOOP as p


Spot = p.Dog('Spot', date(2022, 12, 31), 20,'spotty', wellness_status='all_good',
             personality_type='outdoorsy', num_toys=10)
Clifford = p.Dog('Clifford', date(1963, 1, 1), 100, 'red', 'all_good',
                 'social', 100)
DefaultDog = p.Dog()


if __name__ == '__main__':
    print('Welcome to PetsOOP - the Python Object Oriented programming practice!\n')

print(DefaultDog)
print(repr(DefaultDog))
print(DefaultDog.birth_date)
DefaultDog.bark()
# print(Clifford)
# print(repr(Clifford))
# print(Clifford.get_age())
# Clifford.bark()
# Clifford.wag_tail()
# Clifford.get_wellness_status()
# Clifford.drink()
