import sagemaker
from sagemaker.estimator import Estimator

role = 'arn:aws:iam::YOUR_ACCOUNT_ID:role/YOUR_SAGEMAKER_EXECUTION_ROLE'  # Replace with actual role
region = 'ap-south-1'
image_uri = 'koppsrini/ml-trainer:latest'  # DockerHub image URI
bucket = 'salespricelist'
input_data = f's3://{bucket}/train.csv'
output_path = f's3://{bucket}/output/'

sess = sagemaker.Session()

estimator = Estimator(
    image_uri=image_uri,
    role=role,
    instance_count=1,
    instance_type='ml.m5.large',
    output_path=output_path,
    sagemaker_session=sess
)

estimator.fit({'train': input_data})
