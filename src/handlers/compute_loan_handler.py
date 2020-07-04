import uuid
from src.domains.loan import Loan
import dateutil.parser
from src.handlers.app import compute_loan_use_case_instace
from decimal import Decimal


def compute(event, context):
    for record in event.get('Records'):
        if record.get('eventName') == 'INSERT':
            print(record)
            id = uuid.UUID(record['dynamodb']['Keys']['id']['S'])
            name = record['dynamodb']['NewImage']['name']['S']
            cpf = record['dynamodb']['NewImage']['cpf']['S']
            birthdate = dateutil.parser.isoparse(
                record['dynamodb']['NewImage']['birthdate']['S'])
            amount = Decimal(record['dynamodb']['NewImage']['amount']['N'])
            terms = int(record['dynamodb']['NewImage']['terms']['N'])
            income = Decimal(record['dynamodb']['NewImage']['income']['N'])
            loan = Loan(name, cpf, birthdate, amount, terms, income, id=id)
            compute_loan_use_case_instace.execute(loan)
