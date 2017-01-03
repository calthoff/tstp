# IF YOU ARE READING THIS YOU ARE READING 
# AN OUTDATED VERSION OF THE BOOK.
# I am working with Amazon to resolve this.
# The new version is much better and has correctly formatted code examples
# In the book.
# Please email me at cory@theselftaughtprogrammer.io
# For an updated version

import time
import random


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def simulate_line(time_till_show, max_time_per_ticket):
    person_queue = Queue()
    tickets_sold_to = []

    for i in range(100):
        person_queue.enqueue("person" + str(i))

    t_end = time.time() + time_till_show
    while time.time() < t_end and not person_queue.is_empty():
        time.sleep(random.randint(0, max_time_per_ticket))
        tickets_sold_to.append(person_queue.dequeue())
    return tickets_sold_to

print(simulate_line(5, 2))
