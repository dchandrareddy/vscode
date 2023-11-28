import boto3

ec2_cli=boto3.client(service_name='ec2')

for each_region in ec2_cli.describe_regions()['Regions']:
  print (each_region["RegionName"])