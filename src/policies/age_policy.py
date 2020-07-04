from src.policies.policy import Policy
from src.domains.loan import Loan
from datetime import date
from src.exceptions.policy_exception import PolicyException


class AgePolicy(Policy):

    def __init__(self):
        pass

    def apply(self, loan: Loan):
        age = self.__calculate_age(loan.birthdate)
        if age < 18:
            raise PolicyException('age')

    def __calculate_age(self, birthdate):
        today = date.today()
        return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
