import os
import boto3
from src.domains.loan import Loan
import dateutil.parser


class DynamoDBLoanAdapter:

    def __init__(self):
        self.dynamo_table = boto3.resource(
            'dynamodb').Table(os.environ['DYNAMODB_TABLE'])

    def save(self, item: Loan):
        item.birthdate = item.birthdate.isoformat()
        self.dynamo_table.put_item(Item=item.__dict__)

    def get_by_id(self, id) -> Loan:
        item = self.dynamo_table.get_item(Key={'id': id})['Item']
        print(item)
        loan = Loan(item['name'], item['cpf'], dateutil.parser.isoparse(item['birthdate']), item['amount'], item['terms'], item['income'], status=item['status'], result=item['result'], refused_policy=item['refused_policy'], id=item['id'])
        print(loan)
        return loan
