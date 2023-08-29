import logging
import boto3
import paho.mqtt.client as mqtt
from typing import Any, Dict

from sqs_pusher import SQSPusher

logging.basicConfig(level=logging.INFO)


class MqttSubscriber:
    MQTT_ERR_SUCCESS = mqtt.MQTT_ERR_SUCCESS

    def __init__(self, broker: str, port: int, topic: str, client_id: str,
                 username: str, password: str, aws_access_key: str, aws_secret_key: str, aws_region: str,
                 queue_url: str):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.client_id = client_id
        self.username = username
        self.password = password
        self.aws_access_key = aws_access_key
        self.aws_secret_key = aws_secret_key
        self.aws_region = aws_region
        self.queue_url = queue_url

        self.client = self._connect_mqtt()

    def _on_connect(self, client: mqtt.Client, userdata: Any, flags: Dict[str, Any],
                    rc: int):
        if rc == self.MQTT_ERR_SUCCESS:
            logging.info("Connected to MQTT Broker!")
            client.subscribe(self.topic)
        else:
            logging.error("Failed to connect, return code %d", rc)

    def _connect_mqtt(self) -> mqtt.Client:
        client = mqtt.Client(self.client_id)
        client.username_pw_set(self.username, self.password)
        client.on_connect = self._on_connect
        client.connect(self.broker, self.port)
        return client

    def _push_to_sqs(self, payload):
        boto3.setup_default_session(aws_access_key_id=self.aws_access_key, aws_secret_access_key=self.aws_secret_key,
                                    region_name=self.aws_region)
        pusher = SQSPusher(self.queue_url)
        pusher.send_message(payload)

    def _on_message(self, client: mqtt.Client, userdata: Any, msg: mqtt.MQTTMessage):
        logging.info("Received message: %s", self.client_id)
        logging.info("Topic: %s", msg.topic)

        payload = msg.payload.decode()
        logging.info("Payload: %s", payload)
        logging.info("Payload type: %s", type(payload))

        self._push_to_sqs(payload)
        logging.info("=" * 20)

    def run(self):
        self.client.on_message = self._on_message
        logging.info("subscribing to topic: %s", self.topic)
        logging.info("client_id: %s", self.client_id)
        self.client.loop_forever()
