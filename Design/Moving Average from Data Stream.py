from collections import deque


# Solution I: Double-ended Queue
class MovingAverage:
    def __init__(self, size: int):
        self.queue = deque()
        self.total = 0
        self.size = size

    def next(self, val: int) -> float:
        self.queue.append(val)
        if len(self.queue) > self.size:
            self.total -= self.queue.popleft()
        self.total += val
        return self.total / len(self.queue)


# Solution II: Circular Array, also T(1)
class MovingAverage2:
    def __init__(self, size: int):
        self.size = size
        self.queue = [0] * self.size
        self.head = self.window_sum = 0
        # number of elements seen so far
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1

        # Increment the head
        self.head = (self.head + 1) % self.size

        # calculate the new sum by shifting the window
        # the new head will be overriden by the new value
        self.window_sum = self.window_sum - self.queue[self.head] + val

        # Override the index pointed by the incremented new head
        self.queue[self.head] = val

        return self.window_sum / min(self.size, self.count)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
