from src.ports.loan_port import LoanPort
from src.domains.loan import Loan


class CreateLoanUseCase:
    def __init__(self, loan_port: LoanPort):
        self.loan_port = loan_port

    def execute(self, loan: Loan):
        self.loan_port.save(loan)
