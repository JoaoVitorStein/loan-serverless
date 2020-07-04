

class ExternalApiPort:

    def __init__(self, adapter):
        self.adapter = adapter

    def get_person_score(self, cpf):
        return self.adapter.get_person_score(cpf)

    def get_person_commitment(self, cpf):
        return self.adapter.get_person_commitment(cpf)
