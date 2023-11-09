import os
import boto3
from botocore.exceptions import NoCredentialsError
from Analyst import Analyst

mybucket = "cctv-sollentuna"
role_arn = "arn:aws:iam::234443379770:role/cctv-role"
session_name = "AssumeRoleSession"

class AWSAnalyst(Analyst):
    def __init__(self, dataFolder):
        super().__init__("AWS", dataFolder) 
        initialize_aws()

def initialize_aws(self):
    # Create a new session
    session = boto3.session.Session()

    # Assume the specified role
    sts_client = session.client('sts')
    assumed_role = sts_client.assume_role(RoleArn=role_arn, RoleSessionName=session_name)

    # Credentials to be used for the session with the assumed role
    credentials = assumed_role['Credentials']

    # Use the assumed credentials
    aws_access_key_id = credentials['AccessKeyId']
    aws_secret_access_key = credentials['SecretAccessKey']
    aws_session_token = credentials['SessionToken']

    # Create a new client with the assumed role credentials
    self.s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token,
        )
    # test reading an object from a bucket
    obj = self.s3_client.get_object(Bucket=mybucket, Key='/Users/machi/code/docureader/data/motions/deck/20231105-211036.jpg')
    print("You have the permissions to read the object from the bucket")

    self.rekognition_client = boto3.client(
            'rekognition',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token,
        )
    
def upload_to_aws(self, local_file, bucket, s3_file):
    files = os.listdir(self.data_folder)

    for file in files:
        file = os.path.join(self.data_folder, file)
        try:
            self.s3_client.upload_file(file, mybucket, file)
        except NoCredentialsError:
            print("Credentials not available")

        print(f"{file} uploaded to AWS S3 bucket")
        # remove the file
        # os.remove(file)

def analyze_images(self):
    images = self.s3_client.list_objects(Bucket=mybucket, Prefix=self.data_folder).get('Contents')

    for image in images:
        # call the AWS rekognition API
        print(image)
        file = image.get('Key')
        print(f"calling AWS rekognition API for {file}")
        response = self.rekognition_client.detect_labels(
            Image={
                'S3Object': {
                    'Bucket': mybucket,
                    'Name': file
                }
            },
            MaxLabels=10,
            MinConfidence=90
        )

        # print the labels names
        print("Labels:")
        for label in response['Labels']:
            print(label['Name'])
