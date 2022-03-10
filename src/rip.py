import time
import random

# placeholder data
routing_table = [
    "host1",
    "host2",
    "host3",
    "host4",
    "host5",
    "host6",
    "host7"
]

while True:
    time.sleep(2)
    print(f"Sending packet to: {random.choice(routing_table)}")
