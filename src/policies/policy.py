from abc import ABC, abstractmethod
from src.domains.loan import Loan


class Policy(ABC):

    @abstractmethod
    def apply(self, loan: Loan):
        pass
