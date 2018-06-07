from enum import Enum


class Sex(Enum):
    MALE = 'male'
    FEMALE = 'female'


class Human:
    """A calss of humane"""
    c_id = 0

    def __init__(self):
        Human.c_id += 1
        self.id = Human.c_id
        self.sex = None
        self.age = 0
        self.name = None

    def __str__(self):
        return "Human(ID:" + self.id.__str__() + ", Sex:" + (self.sex if self.sex else "Unknown") + \
            ", Name:" + (self.name if self.name else "Unknown") + ")"
