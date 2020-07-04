import os
import requests
import json


class NoverdeExternalApiAdapter:

    def __init__(self):
        self.noverde_api_base_url = os.environ.get('BASE_NOVERDE_API_URL', '')
        self.noverde_api_auth = {'x-api-key': os.environ.get('API_KEY', '')}

    def get_person_score(self, cpf):
        request_payload = {'cpf': cpf}
        response = requests.post(f'{self.noverde_api_base_url}/score',
                                 data=json.dumps(request_payload),
                                 headers=self.noverde_api_auth)
        if response.ok:
            body_response = json.loads(response.content)
            return body_response['score']
        else:
            raise Exception('Falha ao buscar score da pessoa')

    def get_person_commitment(self, cpf):
        request_payload = {'cpf': cpf}
        response = requests.post(f'{self.noverde_api_base_url}/commitment',
                                 data=json.dumps(request_payload),
                                 headers=self.noverde_api_auth)
        if response.ok:
            body_response = json.loads(response.content)
            return body_response['commitment']
        else:
            raise Exception('Falha ao buscar commitment da pessoa')
