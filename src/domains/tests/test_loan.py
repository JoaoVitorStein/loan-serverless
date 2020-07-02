from src.domains.loan import Loan
from datetime import date
from src.exceptions.validation_exception import ValidationException
import pytest
from uuid import UUID


def test_should_construct_loan():
    name = 'teste'
    cpf = '123123'
    birthdate = date.today()
    amount = 1000
    terms = 6
    income = 1000
    loan = Loan(name, cpf, birthdate, amount, terms, income)
    assert name == loan.name
    assert cpf == loan.cpf
    assert birthdate == loan.birthdate
    assert amount == loan.amount
    assert terms == loan.terms
    assert income == loan.income
    UUID(hex=loan.id, version=4)


def test_should_not_construct_loan():
    with pytest.raises(ValidationException,
                       match='Erros: Nome inválido, CPF inválido, Valor ' +
                       'desejado inválido, Quantidade de parcelas inválidas'):
        name = ''
        cpf = ''
        birthdate = 'date.today()'
        amount = 999
        terms = 5
        income = 1000
        Loan(name, cpf, birthdate, amount, terms, income)
