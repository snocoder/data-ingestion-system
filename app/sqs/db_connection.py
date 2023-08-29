import psycopg2
import logging
from typing import Tuple

logging.basicConfig(level=logging.INFO)


class DBConnection:
    def __init__(self, dbname: str, user: str, password: str, host: str, port: str) -> None:
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        self.connection = None
        self._connect()

    def _connect(self) -> None:
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            logging.info("Connected to the database.")
        except Exception as e:
            logging.error("Error:", e)

    def insert_data(self, data: Tuple) -> None:
        if not self.connection:
            logging.warning("No database connection established.")
            return

        try:
            with self.connection.cursor() as cursor:
                insert_query = "INSERT INTO data(BatteryID, Timestamp, A, B, C, D) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(insert_query, data)
            self.connection.commit()
            logging.info("Data inserted successfully.")
        except Exception as e:
            logging.error("Error:", e)

    def close(self) -> None:
        if self.connection:
            self.connection.close()
            logging.info("Database connection closed.")
