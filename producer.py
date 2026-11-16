"""
producer.py
----------------
This file contains the logic for a Producer that simulates a real-time data
stream by reading events from a CSV file and sending them one by one into a queue.

"""

import csv
import time
import random
from queue import Queue

class CSVProducer:
    def __init__(self, csv_path, q, delay=1.0):
        """
        PARAMETERS: """
        self.csv_path = csv_path 
        self.q = q     # : queue acting as our 'topic'
        self.delay = delay  # : time to wait between sending each row (float) 

    def start(self):
        with open(self.csv_path, newline="") as f: #opens the file
             reader = csv.DictReader(f)          # each row becomes a dict
             for row in reader:
                print(f"[Producer] Sending: {row}")
                self.q.put(row)                  # push the event into the queue
                # delay plus a little random jitter to mimic a real network
                time.sleep(self.delay + random.uniform(0, 0.3))
        self.q.put(None) 
      


# Debugging test

if __name__ == "__main__":
    q = Queue ()
    CSVProducer("transactions.csv", q, delay=0.5).start()
    
   
