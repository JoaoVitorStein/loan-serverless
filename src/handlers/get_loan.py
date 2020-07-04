from src.handlers.app import get_loan_by_id_use_case_instance
import json
from src.decimalencoder import DecimalEncoder


def get_loan(event, context):
    try:
        id = event['pathParameters']['id']
        loan = get_loan_by_id_use_case_instance.execute(id)
        body = {'id': loan.id, 'status': loan.status, 'result': loan.result,
                'refused_policy': loan.refused_policy, 'amount': loan.amount, 'terms': loan.terms}
        return {
            'statusCode': 200,
            'body': json.dumps(body, cls=DecimalEncoder)
        }
    except Exception as e:
        body = {'errorMessage': getattr(e, 'message', str(e))}
        return {
            'statusCode': 500,
            'body': json.dumps(body)
        }
