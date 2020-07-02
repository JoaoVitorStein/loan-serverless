from src.ports.loan_port import loan_port_instance


class CreateLoanUseCase:
    def __init__(self, loan_port):
        self.loan_port = loan_port

    def execute(self, loan):
        return self.loan_port.create(loan)


create_loan_use_case_instace = CreateLoanUseCase(loan_port_instance)
