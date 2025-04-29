from enum import Enum


class ChoiceEnum(Enum):
    @classmethod
    def get_value(cls, member):
        return cls[member].value[0]

    @classmethod
    def get_choices(cls):
        return tuple(x.value for x in cls)

class UserType(ChoiceEnum):
    customer = ('C', 'Customer')
    rider = ('R', 'Rider')
    restaurant = ('rt', 'Restaurant')


class StatusType(ChoiceEnum):
    in_progress = ('0', 'In Progress')
    accepted = ('1', 'Accepted')
    rejected = ('2', 'Rejected')
    picked = ('3', 'Picked')
    delivered = ('4', 'Delivered')
