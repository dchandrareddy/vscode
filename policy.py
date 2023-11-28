import boto3
import json

def create_iam_policy(policyname):
    # Create IAM client
    iam = boto3.client('iam')

    # Create a policy
    my_managed_policy = {
        "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "fms:*",
                "waf:*",
                "waf-regional:*",
                "elasticloadbalancing:SetWebACL",
                "organizations:DescribeOrganization"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
    response = iam.create_policy(
        PolicyName='AWSFMAdminFullAccess',
        PolicyDocument=json.dumps(my_managed_policy)
    )
    print(response)

create_iam_policy("AWSFMAdminFullAccess")