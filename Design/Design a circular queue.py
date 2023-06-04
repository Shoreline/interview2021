class MyCircularQueue:

    def __init__(self, k: int):
        self.head = self.tail = self.size = 0
        self.arr = [0] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.arr[self.tail] = value
        self.tail = (self.tail + 1) % len(self.arr)
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.head = (self.head + 1) % len(self.arr)
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.arr[self.head]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.arr[self.tail-1]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.arr)


from threading import Lock

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [0]*k
        self.headIndex = 0
        self.count = 0
        self.capacity = k
        # the additional attribute to protect the access of our queue
        self.queueLock = Lock()

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        # automatically acquire the lock when entering the block
        with self.queueLock:
            if self.count == self.capacity:
                return False
            self.queue[(self.headIndex + self.count) % self.capacity] = value
            self.count += 1
        # automatically release the lock when leaving the block
        return True


class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode


class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.capacity = k
        self.head = None
        self.tail = None
        self.count = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.count == self.capacity:
            return False

        if self.count == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode
        self.count += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.count == 0:
            return False
        self.head = self.head.next
        self.count -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.count == 0:
            return -1
        return self.head.value

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        # empty queue
        if self.count == 0:
            return -1
        return self.tail.value

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.count == self.capacity