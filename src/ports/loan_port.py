from src.domains.loan import Loan


class LoanPort:

    def __init__(self, adapter):
        self.adapter = adapter

    def save(self, item: Loan):
        self.adapter.save(item)

    def get_by_id(self, id) -> Loan:
        loan = self.adapter.get_by_id(id)
        print(loan.__dict__)
        return loan
