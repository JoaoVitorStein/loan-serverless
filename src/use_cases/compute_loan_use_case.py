from src.ports.loan_port import LoanPort
from src.domains.loan import Loan
from src.exceptions.policy_exception import PolicyException


class ComputeLoanUseCase:
    def __init__(self, loan_port: LoanPort, policies_to_apply):
        self.loan_port = loan_port
        self.policies_to_apply = policies_to_apply

    def execute(self, item: Loan):
        self.__apply_policies(item)
        self.loan_port.save(item)
        return item

    def __apply_policies(self, loan: Loan):
        for policy in self.policies_to_apply:
            try:
                policy.apply(loan)
            except PolicyException as ex:
                self.__deny_loan(loan, ex.policy)
                return
        self.__approve_loan(loan)

    def __deny_loan(self, loan: Loan, policy):
        loan.refused_policy = policy
        loan.terms = None
        loan.result = 'refused'
        loan.status = 'completed'
        loan.amount = None

    def __approve_loan(self, loan: Loan):
        loan.status = 'completed'
        loan.result = 'approved'
