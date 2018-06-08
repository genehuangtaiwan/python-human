from enum import Enum


class Sex(Enum):
    MALE = 'male'
    FEMALE = 'female'


class Human:
    """A class of humane"""
    c_id = 0

    def __init__(self, name=None):
        Human.c_id += 1
        self.id = Human.c_id
        self.__sex = None
        self.age = 0
        self.name = name

    def __str__(self):
        return "Human(ID:" + self.id.__str__() + ", Sex:" + (self.__sex if self.__sex else "Unknown") + \
            ", Name:" + (self.name if self.name else "Unknown") + ")"

    def __eq__(self, other):
        return True if (self.id == other.id) else False

    def get_sex(self):
        return self.__sex

    def set_sex(self, input_sex):
        self.__sex = input_sex.value

    sex = property(get_sex, set_sex)


class Male(Human):
    """A class of male"""

    def __init__(self, name=None):
        super().__init__(name)
        super().set_sex(Sex.MALE)

    def get_sex(self):
        return super().set_sex()

    def set_sex(self, input_sex):
        pass

    sex = property(get_sex, set_sex)


class Female(Human):
    """A class of Female"""

    def __init__(self, name=None):
        super().__init__(name)
        super().set_sex(Sex.FEMALE)

    def get_sex(self):
        return super().set_sex()

    def set_sex(self, input_sex):
        pass

    sex = property(get_sex, set_sex)
