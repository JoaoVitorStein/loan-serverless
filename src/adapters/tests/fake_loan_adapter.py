from src.domains.loan import Loan
import datetime


class FakeLoanAdapter:

    def save(self, item: Loan):
        return item

    def get_by_id(self, id) -> Loan:
        return Loan('test', 'cpf', datetime.date.today(), 1000, 6, 1000)
