
class FakeExternalApiAdapter:

    def __init__(self, score, commitment):
        self.score = score
        self.commitment = commitment

    def get_person_score(self, cpf):
        return self.score

    def get_person_commitment(self, cpf):
        return self.commitment
