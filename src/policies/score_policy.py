from src.policies.policy import Policy
from src.exceptions.policy_exception import PolicyException
from src.domains.loan import Loan
from src.ports.external_api_port import ExternalApiPort


class ScorePolicy(Policy):

    def __init__(self, external_api_port: ExternalApiPort):
        self.external_api_port = external_api_port

    def apply(self, loan: Loan):
        person_score = self.external_api_port.get_person_score(loan.cpf)
        loan.person_score = person_score
        if person_score < 600:
            raise PolicyException('score')
