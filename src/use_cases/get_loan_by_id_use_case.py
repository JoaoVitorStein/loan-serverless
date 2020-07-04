from src.ports.loan_port import LoanPort


class GetLoanByIdUseCase:
    def __init__(self, loan_port: LoanPort):
        self.loan_port = loan_port

    def execute(self, id):
        return self.loan_port.get_by_id(id)
