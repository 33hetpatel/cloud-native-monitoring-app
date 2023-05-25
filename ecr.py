import boto3

# Create an Amazon ECR client
ecr_client = boto3.client('ecr')

# Specify the name for the ECR repository
repository_name = "my_monitoring_app_image"

# Create the ECR repository
response = ecr_client.create_repository(repositoryName=repository_name)

# Retrieve the URI of the created ECR repository
repository_uri = response['repository']['repositoryUri']

# Print the URI of the ECR repository
print(repository_uri)
