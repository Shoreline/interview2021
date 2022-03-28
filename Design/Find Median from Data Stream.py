# Follow-ups
# 1. If all integer numbers from the stream are between 0 and 100, how would you optimize it?
# We can maintain an integer array of length 100 to store the count of each number along with a total count. Then, we can iterate over the array to find the middle value to get our median.
# Time and space complexity would be O(100) = O(1).

# 2. If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
# In this case, we need an integer array of length 100 and a hashmap for these numbers that are not in [0,100].


# Many solutions.
# Use two Heaps for simplicity: one minHeap to save the larger half of numbers, one maxHeap to save the smaller half of numbers
# minHeap: root node is the smallest value. Python's default heap operations use minHeap.
# How to balance the two heaps is the key.
# T: O(logN); S: O(N). Heap push takes logN, and getMin/Max from a Heap takes O(1)
#import heapq as hq # PriorityQueue only takes key-value pair as element

class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = [] # still a min_heap. Just save num as -num
        return

    # If the total elements is a odd number, let the max_heap save that additional element
    # heappushpop: push first, then pop the min. element number is not changed.
    def addNum(self, num: int) -> None:
        if len(self.min_heap) == len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num)) # add one more to max_heap
        else:
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num)) # add one more to min_heap
        return

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return float((self.min_heap[0] + (-self.max_heap[0]))/2)
        else:
            return float(-self.max_heap[0])

# class MedianFinder:
#     def __init__(self):
#         self.min_heap = []
#         self.max_heap = [] # still a min_heap. Just save num as -num
#         return

#     # If the total elements is a odd number, let the max_heap save that additional element
#     # heappushpop: push first, then pop the min. element number is not changed.
#     def addNum(self, num: int) -> None:
#         if len(self.min_heap) == len(self.max_heap):
#             heappush(self.max_heap, -heappushpop(self.min_heap, num))
#         else:
#             heappush(self.min_heap, -heappushpop(self.max_heap, -num))
#         return

#     def findMedian(self) -> float:
#         if len(self.min_heap) == len(self.max_heap):
#             return float((self.min_heap[0] + (-self.max_heap[0]))/2)
#         else:
#             return float(-self.max_heap[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()