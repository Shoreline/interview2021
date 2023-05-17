from collections import deque
from threading import Lock


class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.en, self.de = Lock(), Lock()  # Both enque and deque need a lock
        self.q = deque()  # the queue itself
        self.capacity = capacity
        self.de.acquire()  # lock the de first, since now the queue is empty

    def enqueue(self, element: int) -> None:
        # Need to get en lock to proceed enque operation
        self.en.acquire()
        self.q.append(element)

        # If eligible for another enqueue, release the en lock
        if len(self.q) < self.capacity:
            self.en.release()

        # Now we have at lease one element in queue. So release de lock
        if self.de.locked():
            self.de.release()

    def dequeue(self) -> int:
        self.de.acquire()
        val = self.q.popleft()

        # If queue is not empty, release de lock (allow next deque)
        if len(self.q):
            self.de.release()

        # If there is an enque waiting, release en lock
        if self.en.locked():
            self.en.release()

        return val

    def size(self) -> int:
        return len(self.q)