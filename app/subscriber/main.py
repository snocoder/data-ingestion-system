import os
from dotenv import load_dotenv

from mqtt_subscriber import MqttSubscriber

load_dotenv(dotenv_path="development.env")

BROKER = os.getenv("BROKER")
PORT = int(os.getenv("PORT"))
TOPIC = os.getenv("TOPIC")
CLIENT_ID = os.getenv("CLIENT_ID")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_REGION = os.getenv("AWS_REGION")
SQS_QUEUE_URL = os.getenv("SQS_QUEUE_URL")


def run_subscriber():
    subscriber = MqttSubscriber(BROKER, PORT, TOPIC, CLIENT_ID, USERNAME, PASSWORD, AWS_ACCESS_KEY, AWS_SECRET_KEY,
                                AWS_REGION, SQS_QUEUE_URL)
    subscriber.run()


if __name__ == '__main__':
    run_subscriber()
