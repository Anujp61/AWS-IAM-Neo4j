import boto3

class AWSUserFetcher:
    def __init__(self, access_key, secret_key, region):
        self.client = boto3.client(
            "iam",
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region,
        )

    def fetch_users(self):
        
        users = []
        paginator = self.client.get_paginator("list_users")
        for page in paginator.paginate():
            for user in page["Users"]:
                users.append(user["UserName"])
        return users
