from src.policies.policy import Policy
from src.domains.loan import Loan
from src.exceptions.policy_exception import PolicyException


class FakePolicy(Policy):

    def __init__(self, should_approve: bool):
        self.should_approve = should_approve

    def apply(self, loan: Loan):
        if not self.should_approve:
            raise PolicyException('fake_policy')
