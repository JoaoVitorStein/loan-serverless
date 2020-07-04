from src.adapters.tests.fake_loan_adapter import FakeLoanAdapter
from src.policies.tests.fake_policy import FakePolicy
from src.use_cases.compute_loan_use_case import ComputeLoanUseCase
from src.ports.loan_port import LoanPort
from src.domains.loan import Loan
import datetime


def test_should_approve_loan():
    loan = Loan('name', 'cpf', datetime.date(2000, 7, 12), 1000, 6, 1000)
    policies_to_apply = [FakePolicy(True)]
    port = LoanPort(FakeLoanAdapter())
    ComputeLoanUseCase(port, policies_to_apply).execute(loan)
    assert loan.status == 'completed'
    assert loan.result == 'approved'


def test_shouldnt_approve_loan():
    loan = Loan('name', 'cpf', datetime.date(2000, 7, 12), 1000, 6, 1000)
    policies_to_apply = [FakePolicy(False)]
    port = LoanPort(FakeLoanAdapter())
    ComputeLoanUseCase(port, policies_to_apply).execute(loan)
    assert loan.refused_policy == 'fake_policy'
    assert loan.result == 'refused'
    assert loan.status == 'completed'
    assert loan.terms is None
    assert loan.amount is None
