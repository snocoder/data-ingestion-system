import os
import concurrent.futures
from dotenv import load_dotenv

from thread_publisher import ThreadPublisher
from unique_id_generator import UniqueIDGenerator

# Constants
NUM_THREADS = 1

battery_id_generator = UniqueIDGenerator()

load_dotenv(dotenv_path="development.env")

BROKER = os.getenv("BROKER")
PORT = int(os.getenv("PORT"))
TOPIC = os.getenv("TOPIC")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")


def handle_thread_run():
    thread_publisher = ThreadPublisher(battery_id_generator, BROKER, PORT, TOPIC, USERNAME, PASSWORD)
    thread_publisher.publish_messages()


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
        # Submit tasks to the executor
        futures = [executor.submit(handle_thread_run) for i in range(1, NUM_THREADS + 1)]
        # Wait for all tasks to complete
        concurrent.futures.wait(futures)


if __name__ == "__main__":
    main()
