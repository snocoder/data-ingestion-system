import boto3
import logging
import os
from dotenv import load_dotenv

from message_parser_util import parse_message
from db_connection import DBConnection

logging.basicConfig(level=logging.INFO)
load_dotenv(dotenv_path="development.env")

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")


class SQSReceiver:
    def __init__(self, queue_url):
        self.sqs = boto3.client('sqs')
        self.queue_url = queue_url

    def _delete_message(self, message):
        self.sqs.delete_message(
            QueueUrl=self.queue_url,
            ReceiptHandle=message['ReceiptHandle']
        )

    @staticmethod
    def add_to_database(data):
        db_connection = DBConnection(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
        db_connection.insert_data((data["BatteryID"], data["Timestamp"], data["A"], data["B"], data["C"], data["D"]))

    def receive_messages(self):
        while True:
            try:
                response = self.sqs.receive_message(
                    QueueUrl=self.queue_url,
                    MaxNumberOfMessages=1,
                    WaitTimeSeconds=20  # Wait for up to 20 seconds for a message
                )

                if 'Messages' in response:
                    for message in response['Messages']:
                        body = message['Body']
                        parsed_body = parse_message(body)
                        logging.info("Parsed body: ", parsed_body)

                        # Insert into db
                        self.add_to_database(parsed_body)

                        # Delete the received message from the queue
                        self._delete_message(message)
            except Exception as e:
                logging.error("Error while receiving messages: %s", str(e))
