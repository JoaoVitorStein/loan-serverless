import pytest
from src.exceptions.policy_exception import PolicyException
from src.domains.loan import Loan
import datetime
from src.policies.age_policy import AgePolicy


def test_shouldnt_throw_policy_exception():
    loan = Loan('name', 'cpf', datetime.date(2000, 7, 12), 1000, 6, 1000)
    AgePolicy().apply(loan)


def test_should_throw_policy_exception():
    with pytest.raises(PolicyException, match='Política negada: age'):
        loan = Loan('name', 'cpf', datetime.date.today(), 1000, 6, 1000)
        AgePolicy().apply(loan)
