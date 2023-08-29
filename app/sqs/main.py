import boto3
import os
from dotenv import load_dotenv

from sqs_receiver import SQSReceiver

load_dotenv(dotenv_path="development.env")

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_REGION = os.getenv("AWS_REGION")
SQS_QUEUE_URL = os.getenv("SQS_QUEUE_URL")


def run_sqs_receiver():
    boto3.setup_default_session(aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY,
                                region_name=AWS_REGION)
    receiver = SQSReceiver(SQS_QUEUE_URL)
    receiver.receive_messages()


if __name__ == '__main__':
    run_sqs_receiver()
