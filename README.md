# Mini Data Ingestion System using Pub-Sub Model with MQTT

## Problem Statement

Build a data ingestion system with the following components:

1. **MQTT Server Setup**: Set up an MQTT server capable of handling approximately 10,000 publishers concurrently.

2. **Python Publishers**: Create Python publishers that utilize asynchronous programming or multiprocessing to send data to the MQTT server. Implement 10 such publishers, each generating data packets with the following headers:
   - BatteryID (4-character string, unique for each publisher)
   - Timestamp (epoch)
   - A (double)
   - B (double)
   - C (integer)
   - D (binary)

3. **Python Consumer**: Develop a Python consumer that can process MQTT messages in parallel. Choose between multiprocessing, multithreading, or asynchronous programming. The consumer should retrieve messages from the MQTT server and enqueue them into a queue.

4. **Queueing**: Implement a queuing mechanism (e.g., Python queue, SQS, or open-source queue) to handle the data packets received by the consumer. The queued data will be further processed and stored.

5. **Database Script**: Create a script that dequeues data from the queue and inserts it into a relational database such as MySQL. Implement error handling to address potential issues during the data insertion process.

