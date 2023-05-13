import collections
from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        counter = 0
        for num in nums:
            counter += seen[num-k] + seen[num+k]
            seen[num] += 1
        return counter

# class Solution:
#     def countKDifference(self, nums: List[int], k: int) -> int:
#         c = Counter(nums)
#         res = 0
#         for num in c:
#             res += c[num + k] * c[num]
#             res += c[num - k] * c[num]
#
#         return res // 2

# Coupang
# 1. Condition: nums[i] = nums[j] and |i-j| is at most k.
# nums = [1,2,3,1], k = 3
# true
# nums = [1,0,1,1], k = 1
# true
# nums = [1,2,3,1,2,3], k = 2
# false
def count(nums: List[int], k: int) -> int:
    cnt_in_window = collections.defaultdict(int)
    res = 0
    for i, num in enumerate(nums):
        res += cnt_in_window[num]

        cnt_in_window[num] += 1
        if i >= k:
            cnt_in_window[nums[i - k]] -= 1

    return res


# 2. Condition: |i-j| is at most k and |nums[i] - nums[j]| is at most t.
# nums = [1,2,3,1], k = 3, t = 0
# true
# nums = [1,0,1,1], k = 1, t = 2
# true
# nums = [1,5,9,1,5,9], k = 2, t = 3
# false
def count2(nums: List[int], k: int, t: int) -> int:
    cnt_in_window = collections.defaultdict(int)
    res = 0
    for i, num in enumerate(nums):
        # for j in range(t+1): # O(N*t)
        #     res += cnt_in_window[num + j]
        #     res += cnt_in_window[num - j]

        for n, cnt in cnt_in_window.items(): # O(N * k)
            if abs(num - n) <= t:
                res += cnt

        cnt_in_window[num] += 1
        if i >= k:
            cnt_in_window[nums[i - k]] -= 1

    return res


q = [([1,2,3,1], 3), ([1,0,1,1], 1), ([1,2,3,1,2,3], 2)]
q2 = [([1,2,3,1], 3, 0), ([1,0,1,1], 1, 2), ([1,5,9,1,5,9], 2, 3)]
for nums, k in q:
    print(count(nums, k))
    print('===================')

print('========== follow up =========')
for nums, k, t in q2:
    print(count2(nums, k, t))
    print('===================')