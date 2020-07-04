from src.policies.policy import Policy
from src.ports.external_api_port import ExternalApiPort
from src.domains.loan import Loan
from src.exceptions.policy_exception import PolicyException
from decimal import Decimal


class CommitmentPolicy(Policy):

    def __init__(self, external_api_port: ExternalApiPort):
        self.external_api_port = external_api_port

    def apply(self, loan: Loan):
        commitment = Decimal(self.external_api_port.get_person_commitment(loan.cpf))
        monthly_saving = loan.income - (loan.income * commitment)
        self.__find_monthly_payment(loan, monthly_saving)

    def __get_tax_percentages(self, score):
        if score >= 900:
            return {'6': 3.9, '9': 4.2, '12': 4.5}
        if score >= 800 and score <= 899:
            return {'6': 4.7, '9': 5.0, '12': 5.3}
        if score >= 700 and score <= 799:
            return {'6':  5.5, '9': 5.8, '12': 6.1}
        if score >= 600 and score <= 699:
            return {'6':  6.4,  '9': 6.6, '12': 6.9}

    def __find_monthly_payment(self, loan: Loan, monthly_saving):
        tax = self.__get_tax_percentages(loan.person_score)
        desired_terms_payment = self.__calculate_pmt(loan.amount, loan.terms, tax[str(loan.terms)])
        if desired_terms_payment > monthly_saving:
            del tax[str(loan.terms)]
            for key in tax:
                terms = int(key)
                other_term_payment = self.__calculate_pmt(loan.amount, terms, tax[key])
                if other_term_payment < monthly_saving:
                    loan.terms = terms
                    return
            raise PolicyException('commitment')

    def __calculate_pmt(self, value, terms, tax):
        real_tax = tax / 100
        partial_account = Decimal((1 + real_tax) ** terms * real_tax / ((1 + real_tax) ** terms - 1))
        monthly_payment = value * partial_account
        return monthly_payment
