from datetime import date
import random


class Dog:
    """
    A class to represent a dog.

    Attributes
    ----------

    name : str
        a dog's name
    birth_date : a datetime date object of the format date(YYYY, MM, DD)
        for example date(2023, 12, 31) for December 31st, 2023
        a dog's date of birth
    weight : float
        a dog's weight in kg
    color: str
        the main color of the dogs coat or multicolor
    wellness_status : dict
        a dictionary that represents various aspects of the dog's well-being
        wellness_status = {health_status: 'excellent',
                            food_status: 'ok',
                            water_status: 'ok',
                            energy_level: 'playful',
                            walk_status: 'want to go for a walk'}
    personality_type : str
        a dog's personality type, ex: active, outdoorsy, shy, social, curious, guard-dog
    num_toys: int
        number of toys that the dog has

    Methods
    ----------

    __str__:
        returns a string that describes the current instance of the Dog class in a user-friendly way
        prints the dogs name, age, color and personality type
    __repr__:
        returns a string that allows us to re-create the current object
    get_age:
        calculates a dog's age in years (integer)
    bark:
        prints out the dog's barking
    drink:
        prints out the dog's drinking (water)
    eat
    get_wellness_status:
        prints out the dogs wellness status in a friendly format
        summarizes if everything is ok or gives warnings and lists required actions
    get_in_car
    go_for_walk:
        prints the dog's name and personality type and how they go for a walk according to the dog's personality
    greet
    play
    run
    sleep:
        print: Dog <name> is sleeping. Zzzzzzzz ...
    wag_tail
        print the dog's name and personality type and how it wags their tail according to personality
    """

    default_dog_names = ['Luna', 'Rainbow', 'Buddy', 'Fetchington', 'Barkley', 'Zippy', 'Dreamer',
                         'Snugglebug', 'Peppy', 'Chillington', 'Philosopher', 'Patches']
    default_name = random.choice(default_dog_names)

    def __init__(self, name=default_name, birth_date=date.today(), weight=1, color='multicolor',
                 wellness_status='all_good', personality_type='friendly', num_toys=1):

        self.name = name
        self.birth_date = birth_date
        self.weight = weight
        self.color = color
        self.wellness_status = wellness_status
        self.personality_type = personality_type
        self.num_toys = num_toys

    @property
    def birth_date(self):
        """getter method for birth_date"""
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        """setter method for birth_date, validates input"""
        if type(value) is not date:  # also tried: not isinstance(value, date)
            raise TypeError('Dogs birthdate must be of type datetime.date ex. date(2020, 1, 31)')
        self._birth_date = value

    def __str__(self):
        # return f"Dog {self.name} {self._birth_date} {self.get_age()}"
        return f"Dog {self.name} is {self.get_age()} years old, {self.color} and {self.personality_type}."
        # return f"Dog {self.name} is {self.color} and {self.personality_type}."

    def __repr__(self):
        return (
            f"{type(self).__name__}("
            f"name='{self.name}', "
            f"birth_date=date({self.birth_date.strftime('%Y,%-m,%-d')}), "
            f"weight={self.weight}, "
            f"color='{self.color}', "
            f"wellness_status='{self.wellness_status}', "
            f"personality_type='{self.personality_type}', "
            f"num_toys={self.num_toys})"
        )

    def bark(self):
        print('Woof Woof!')

    def drink(self):
        print('Slurp Slurp')

    def wag_tail(self):
        print(f'The {self.personality_type} dog {self.name} is wagging their tail.')

    def get_age(self):
        """
        Calculates the dog's age using the birth_date attribute and today's date.

        Parameters
        ----------
        no parameters are required
        only the dog object and today's date is used to calculate the dog's age

        Returns
        ----------
        age: int
        dog's age
        """

        birth_date = self._birth_date
        today = date.today()
        age = today.year - birth_date.year
        # adjust if the birthday has not occurred this year yet
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        return age

    def get_wellness_status(self):
        print(f'Dog {self.name} is {self.wellness_status}.')
