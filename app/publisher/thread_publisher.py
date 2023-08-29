import time

from mqtt_publisher import MqttPublisher
from message_generator_util import prepare_message


class ThreadPublisher:
    MESSAGES_PER_THREAD = 1

    def __init__(self, battery_id_generator, broker, port, topic, username, password):
        self.battery_id_generator = battery_id_generator
        self.broker = broker
        self.port = port
        self.topic = topic
        self.username = username
        self.password = password

        self.battery_id = battery_id_generator.generate_unique_id()
        self.client_id = self.battery_id
        self.publisher = None

        self._initialize_publisher()

    def _initialize_publisher(self):
        self.publisher = MqttPublisher(self.broker, self.port, self.topic, self.client_id,
                                       self.username, self.password)
        self.publisher.client.loop_start()
        time.sleep(1)

    def publish_single_message(self, json_message):
        self.publisher.publish_message(json_message)

    def publish_messages(self):
        for _ in range(self.MESSAGES_PER_THREAD):
            json_message = prepare_message(self.battery_id)
            self.publish_single_message(json_message)
            time.sleep(1)
