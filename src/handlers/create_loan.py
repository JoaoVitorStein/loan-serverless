import json
from src.exceptions.validation_exception import ValidationException
from src.use_cases.create_loan_use_case import create_loan_use_case_instace
from src.domains.loan import Loan


def create_loan(event, context):
    try:
        data = json.loads(event['body'])
        loan = Loan(data.get('name', ''), data.get('cpf', ''),
                    data.get('birthdate', ''), data.get('amount', 0),
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
