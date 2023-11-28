import boto3

AWS_REGION = "ap-south-1"

client = boto3.client("s3", region_name=AWS_REGION)

bucket_name = "chandra-bucket144"
location = {'LocationConstraint': AWS_REGION}

response = client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)

print("Amazon S3 bucket has been created")