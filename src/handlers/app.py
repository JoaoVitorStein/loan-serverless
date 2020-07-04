from src.use_cases.create_loan_use_case import CreateLoanUseCase
from src.use_cases.compute_loan_use_case import ComputeLoanUseCase
from src.use_cases.get_loan_by_id_use_case import GetLoanByIdUseCase
from src.adapters.dynamodb_loan_adapter import DynamoDBLoanAdapter
from src.adapters.noverde_external_api_adapter import NoverdeExternalApiAdapter
from src.policies.commitment_policy import CommitmentPolicy
from src.policies.score_policy import ScorePolicy
from src.policies.age_policy import AgePolicy
from src.ports.external_api_port import ExternalApiPort
from src.ports.loan_port import LoanPort


dynamodb_adapter_instace = DynamoDBLoanAdapter()
noverde_external_api_adapter_instance = NoverdeExternalApiAdapter()

external_api_port_instance = ExternalApiPort(noverde_external_api_adapter_instance)
loan_port_instance = LoanPort(dynamodb_adapter_instace)


commitment_policy_instace = CommitmentPolicy(external_api_port_instance)
score_policy_instace = ScorePolicy(external_api_port_instance)
age_policy_instance = AgePolicy()
policies = [age_policy_instance, score_policy_instace, commitment_policy_instace]


create_loan_use_case_instace = CreateLoanUseCase(loan_port_instance)
compute_loan_use_case_instace = ComputeLoanUseCase(loan_port_instance, policies)
get_loan_by_id_use_case_instance = GetLoanByIdUseCase(loan_port_instance)
