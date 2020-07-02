from src.adapters.dynamodb_loan_adapter import dynamodb_adapter_instace
from src.domains.loan import Loan


class LoanPort:

    def __init__(self, adapter):
        self.adapter = adapter

    def create(self, item: Loan):
        self.adapter.create(item)


loan_port_instance = LoanPort(dynamodb_adapter_instace)
