# The task is to do sampling with weight.

# Prefix sum + binary search insert
# Where to insert depends on the weights of each number
# Get a random number target in [0, total_weight), then do a binary search to find the index to insert target in the
# prefix sum array.

class Solution:
    def __init__(self, w: List[int]):
        self.prefix_sums = []
        cur_sum = 0
        for weight in w:
            cur_sum += weight
            self.prefix_sums.append(cur_sum)
        self.total_weight = cur_sum

    def pickIndex(self) -> int:
        target = self.total_weight * random.random()
        left, right = 0, len(self.prefix_sums)
        while left < right:
            mid = left + (right - left) // 2
            if target > self.prefix_sums[mid]:
                left = mid + 1
            else:
                right = mid

        return left

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()