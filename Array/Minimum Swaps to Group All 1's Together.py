# 1. Count how many 1s in the array (c)
# 2. Run a sliding window of size c, return the window has the least amount of 0s
# T O(n), S O(1)
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        one_count = data.count(1)

        cur_zero_count = data[:one_count].count(0)
        res = cur_zero_count

        for i in range(one_count, len(data)):
            if data[i] == 0:
                cur_zero_count += 1
            if data[i - one_count] == 0:
                cur_zero_count -= 1
            res = min(res, cur_zero_count)

        return res
