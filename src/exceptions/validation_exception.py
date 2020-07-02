
class ValidationException(Exception):

    def __init__(self, errors):
        self.errors = errors
        self.message = f"Erros: {', '.join(errors)}"
        super().__init__(self.message)
