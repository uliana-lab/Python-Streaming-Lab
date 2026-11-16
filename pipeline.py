"""
pipeline.py
----------------
This file launches BOTH producer and consumer using Python threads to simulate
a real streaming pipeline.

"""

import threading
from queue import Queue
from producer import CSVProducer
from consumer import Consumer

def main():
   q = Queue()                                          # shared queue
   producer = CSVProducer("transactions.csv", q, delay=0.5)
   consumer = Consumer(q)
   
   t_producer = threading.Thread(target=producer.start)
   t_consumer = threading.Thread(target=consumer.start)
   
   t_producer.start()
   t_consumer.start()
   
   t_producer.join()                                    # wait for both to finish
   t_consumer.join()


if __name__ == "__main__":
    print("Starting the Python Streaming Pipeline...")
    main()
