# FIFO, use queue((timestamp, count))
# Note that the timestamp of operations can never decrease
# hit() adds a hit in queue. A hit is just an integer of its timestamp
# getHits() pops outdated hits and return the remaining hit count
# from collections import deque
# class HitCounter:

#     def __init__(self):
#         self.hits = deque()

#     def hit(self, timestamp: int) -> None:
#         self.hits.append(timestamp)
#         return

#     def getHits(self, timestamp: int) -> int:
#         while self.hits and timestamp - self.hits[0] >= 300:
#             self.hits.popleft()

#         return len(self.hits)

# Follow up: What if the number of hits per second could be huge? Does your design scale?
# Still use a queue, but queue element becomes [timestamp, hit_count]; also add a total_hit_counter
# T and S for getHits() is still O(n), same as before. But that's worst case, on avarage both time and space is improved
from collections import deque


class HitCounter:

    def __init__(self):
        self.hits = deque()
        self.total_hits = 0

    def hit(self, timestamp: int) -> None:
        if not self.hits or self.hits[-1][0] != timestamp:
            self.hits.append([timestamp, 1])
        else:
            self.hits[-1][1] += 1
        self.total_hits += 1
        return

    def getHits(self, timestamp: int) -> int:
        while self.hits and timestamp - self.hits[0][0] >= 300:
            self.total_hits -= self.hits[0][1]
            self.hits.popleft()

        return self.total_hits

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)