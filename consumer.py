"""
consumer.py
----------------
This file contains the logic for a Consumer that continuously reads messages
from the queue and processes them.

The Consumer runs forever, just like a streaming system.
"""

import time
from queue import Queue

class Consumer:
    def __init__(self, q):
       self.q = q
       self.total = 0.0      # running total (our "state")
       self.count = 0
        

    def start(self):
       while True:
            event = self.q.get()     # blocks until an event arrives
            if event is None:        # producer says it's finished
                print(f"[Consumer] Done. {self.count} events, total = {self.total:.2f}")
                break
            print(f"[Consumer] Received: {event}")
            self.process(event)
    

    def process(self, event):
        time.sleep(0.3)                          # simulate processing time
        amount = float(event["amount"])          # CSV values are strings
        self.total += amount
        self.count += 1
        print(f"[Consumer] Processed transaction {event['transaction_id']}: "
              f"amount={amount:.2f}, running total={self.total:.2f}")

   

# Debugging test

if __name__ == "__main__":
    q = Queue()
    consumer = Consumer(q)
    consumer.start()
