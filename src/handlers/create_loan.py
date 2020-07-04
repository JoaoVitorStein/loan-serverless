import json
from src.exceptions.validation_exception import ValidationException
from src.handlers.app import create_loan_use_case_instace
from src.domains.loan import Loan
import datetime


def create_loan(event, context):
    try:
        data = json.loads(event['body'])
        birthdate = datetime.datetime.strptime(
                data.get('birthdate'), '%Y-%m-%d') if 'birthdate' in data else None
        loan = Loan(data.get('name', ''), data.get('cpf', ''),
                    birthdate, data.get('amount', 0),
                    data.get('terms', 0), data.get('income', ''))
        create_loan_use_case_instace.execute(loan)
        body = {'id': loan.id}
        return {
            'statusCode': 200,
            'body': json.dumps(body)
        }
    except ValidationException as ex:
        body = {'errors': ex.errors}
        return {
            'statusCode': 400,
            'body': json.dumps(body)
        }
    except Exception as e:
        body = {'errorMessage': getattr(e, 'message', str(e))}
        return {
            'statusCode': 500,
            'body': json.dumps(body)
        }
