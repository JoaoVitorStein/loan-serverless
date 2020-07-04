from src.adapters.tests.fake_external_api_adapter import FakeExternalApiAdapter
from src.domains.loan import Loan
from src.policies.commitment_policy import CommitmentPolicy
from src.exceptions.policy_exception import PolicyException
import datetime
import pytest
from decimal import Decimal


def test_should_pass_policy_with_other_terms():
    fake_adapter = FakeExternalApiAdapter(900, Decimal(0.66))
    loan = Loan('name', 'cpf', datetime.date(2000, 7, 12), Decimal(2500), 6, Decimal(1000))
    loan.person_score = 900
    CommitmentPolicy(fake_adapter).apply(loan)
    assert loan.terms == 9


def test_should_pass_policy_with_desired_terms():
    fake_adapter = FakeExternalApiAdapter(900, Decimal(0.5))
    loan = Loan('name', 'cpf', datetime.date(2000, 7, 12), Decimal(2500), 6, Decimal(1000))
    loan.person_score = 900
    CommitmentPolicy(fake_adapter).apply(loan)
    assert loan.terms == 6


def test_should_throw_policy_exception():
    with pytest.raises(PolicyException, match='Política negada: commitment'):
        fake_adapter = FakeExternalApiAdapter(900, Decimal(0.9))
        loan = Loan('name', 'cpf', datetime.date(2000, 7, 12), Decimal(2500), 6, Decimal(1000))
        loan.person_score = 900
        CommitmentPolicy(fake_adapter).apply(loan)
