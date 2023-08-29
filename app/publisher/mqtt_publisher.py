import paho.mqtt.client as mqtt
import logging

logging.basicConfig(level=logging.INFO)


class MqttPublisher:
    MQTT_ERR_SUCCESS: int = mqtt.MQTT_ERR_SUCCESS

    def __init__(self, broker: str, port: int, topic: str, client_id: str, username: str, password: str):
        self.broker: str = broker
        self.port: int = port
        self.topic: str = topic
        self.client_id: str = client_id
        self.username: str = username
        self.password: str = password

        self.client: mqtt.Client = self._connect_mqtt()

    def _on_connect(self, client: mqtt.Client, userdata, flags, rc: int):
        if rc == self.MQTT_ERR_SUCCESS:
            logging.info("Connected to MQTT Broker!")
            self.client.subscribe(self.topic)
        else:
            logging.error(f"Failed to connect, return code {rc}")

    def _connect_mqtt(self) -> mqtt.Client:
        client: mqtt.Client = mqtt.Client(self.client_id)
        client.username_pw_set(self.username, self.password)
        client.on_connect = self._on_connect
        client.connect(self.broker, self.port)
        return client

    def publish_message(self, json_message: str):
        result = self.client.publish(self.topic, json_message)
        status = result.rc
        if status == self.MQTT_ERR_SUCCESS:
            logging.info(f"Sent {json_message} to topic {self.topic}")
        else:
            logging.error(f"Failed to send message {json_message} to topic {self.topic}")
