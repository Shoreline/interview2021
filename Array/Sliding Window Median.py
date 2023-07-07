# Two heaps
#   - one max_heap, one min_heap
# TC - O((n - k)*log(k)) -> O(nlogk)
# SC - O(k)
#
# After we build our window, the length of window will ALWAYS be the same
#   we will keep the length of valid elements in max_heap and min_heap the same too
#
# Based on this, when we slide our window, the balance variable can be equal to 0, 2 or -2. It will NEVER be -1 or 1.
#
# Examples:
# 0 -> when we remove an element from max_heap and then add a new one back to max_heap (or the same for min_heap)
# -2 -> when we remove an element from max_heap and then add a new one to min_heap (max_heap will have two less elements)
# 2 -> when we remove an element from min_heap and then add a new one to max_heap (min_heap will have two less elements)
# Based on this - it is enough for us to move 1 element from one heap to another when the balance variable is equal to 2 or -2
class Solution:
    def find_median(self, max_heap, min_heap, heap_size):
        if heap_size % 2 == 1:
            return -max_heap[0]
        else:
            return (-max_heap[0] + min_heap[0]) / 2

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        max_heap = []  # saves vals >= median
        min_heap = []  # saves vals < median
        heap_dict = defaultdict(int)  # <val, val_freq> that tracks invalid numbers but still in heap
        result = []

        # construct the inital heaps based on the first k elements (first sliding window)
        for i in range(k):
            heappush(max_heap, -nums[i])
            heappush(min_heap, -heappop(max_heap))
            if len(min_heap) > len(max_heap):
                heappush(max_heap, -heappop(min_heap))

        median = self.find_median(max_heap, min_heap, k)
        result.append(median)

        # process remaining sliding windows
        for i in range(k, len(nums)):
            prev_num = nums[i - k]  # the num needs to be removed from the new sliding window
            heap_dict[prev_num] += 1

            # heaps' balance factor
            balance = -1 if prev_num <= median else 1

            if nums[i] <= median:
                balance += 1
                heappush(max_heap, -nums[i])
            else:
                balance -= 1
                heappush(min_heap, nums[i])

            # if < 0 -> move one element from min_heap to max_heap
            # if > 0 -> vice versa
            if balance < 0:
                heappush(max_heap, -heappop(min_heap))
            elif balance > 0:
                heappush(min_heap, -heappop(max_heap))

            # clean up invalided elements which are on top of each heap
            while max_heap and heap_dict[-max_heap[0]] > 0:
                heap_dict[-max_heap[0]] -= 1
                heappop(max_heap)

            while min_heap and heap_dict[min_heap[0]] > 0:
                heap_dict[min_heap[0]] -= 1
                heappop(min_heap)

            median = self.find_median(max_heap, min_heap, k)
            result.append(median)

        return result