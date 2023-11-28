import boto3

AWS_REGION = "ap-south-1"
ec2 = boto3.client('ec2')
response = ec2.describe_key_pairs()
print(response)