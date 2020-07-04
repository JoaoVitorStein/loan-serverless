# loan-serverless
O serviço usa API Gateway + Lambda + DynamoDB. Cada nova solicitação inserida pela API `POST /loan`, dispara a Lambda Function `ComputeLoan` via DynamoDB Streams.

### Deployando a aplicação
Para que seja possível deployar as APIs é necessário fazer os seguintes passos:

1. **Instalar o framework serverless via npm:**
```bash
npm install -g serverless
```

2. **Configurar as chaves de acesso da AWS de acordo com este [artigo](https://www.serverless.com/framework/docs/providers/aws/guide/credentials/):**

3. **Fazer o deploy com o seguinte comando do serverless(fazendo a substituição dos placeholders):**
```bash
serverless deploy --api_key ${YOUR_API_KEY} --base_noverde_api_url ${YOUR_API_URL}
```


### Rodando os teste unitários
Após fazer a instalação da biblioteca [pytest](https://pypi.org/project/pytest/), rodar o comando:
```bash
pytest
```