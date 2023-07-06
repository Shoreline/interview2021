class KthLargest:
    """
    The idea is to ALWAYS maintain a MIN heap with only K elements
    - in this case, the K-the largest element (in the stream)
    - will always be at the root position
    -
    - NO need to care elements bigger than the current k-th largest element
    """

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k  # beyond this size, pop the heap

        for num in nums:
            self.add(num)  # add elements using the function below

    def add(self, val: int) -> int:

        heapq.heappush(self.heap, val)

        # if after adding the new item causes
        # the heap size to increase beyond k,
        # then pop out the smallest element
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]  # always return heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)