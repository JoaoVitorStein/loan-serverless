import boto3
import os
from src.domains.loan import Loan


class DynamoDBLoanAdapter:

    def __init__(self):
        self.dynamo_table = boto3.resource(
            'dynamodb').Table(os.environ['DYNAMODB_TABLE'])

    def create(self, item: Loan):
        self.dynamo_table.put_item(Item=item.__dict__)


dynamodb_adapter_instace = DynamoDBLoanAdapter()
