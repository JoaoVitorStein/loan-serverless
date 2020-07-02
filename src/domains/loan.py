from src.exceptions.validation_exception import ValidationException
import datetime
import uuid


class Loan:

    def __init__(self, name, cpf, birthdate, amount, terms, income):
        self.name = name
        self.cpf = cpf
        self.birthdate = birthdate
        self.amount = amount
        self.terms = terms
        self.income = income
        self.id = str(uuid.uuid4())
        self.validate()

    def validate(self):
        errors = []

        if not self.name:
            errors.append('Nome inválido')
        if not self.cpf:
            errors.append('CPF inválido')
        if isinstance(self.birthdate, datetime.datetime):
            errors.append('Data de nascimento inválida')
        if self.amount < 1000.0 or self.amount > 4000.0:
            errors.append('Valor desejado inválido')
        if self.terms not in [6, 9, 12]:
            errors.append('Quantidade de parcelas inválidas')
        if not self.income:
            errors.append('Renda mensal inválida')

        if len(errors) > 0:
            raise ValidationException(errors)
