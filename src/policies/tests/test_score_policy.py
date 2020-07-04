import pytest
from src.domains.loan import Loan
import datetime
from src.policies.score_policy import ScorePolicy
from src.adapters.tests.fake_external_api_adapter import FakeExternalApiAdapter
from src.exceptions.policy_exception import PolicyException


def test_shouldnt_throw_policy_exception():
    fake_adapter = FakeExternalApiAdapter(600, 0)
    loan = Loan('name', 'cpf', datetime.date(2000, 7, 12), 1000, 6, 1000)
    ScorePolicy(fake_adapter).apply(loan)


def test_should_throw_policy_exception():
    with pytest.raises(PolicyException, match='Política negada: score'):
        fake_adapter = FakeExternalApiAdapter(599, 0)
        loan = Loan('name', 'cpf', datetime.date(2000, 7, 12), 1000, 6, 1000)
        ScorePolicy(fake_adapter).apply(loan)
