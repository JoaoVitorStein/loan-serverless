
class PolicyException(Exception):
    def __init__(self, policy):
        self.policy = policy
        super().__init__(f'Política negada: {policy}')
