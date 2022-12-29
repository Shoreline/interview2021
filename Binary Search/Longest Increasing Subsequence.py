# Try maintaining a res list. Append/update res list element for each given element in nums.
# Need bisect_left(res, nums[i]), returns the index in res to set res[idx] = nums[i]
# if num > res[-1]: res.append(num)
# otherwise (num <= res[-1]): replace the smallest element in res which >= num
# O(NlogN) time.
#
# The final res[] is not guaranteed to be the actual maximum length LIS. But its length is the same as the actual
# maximum length LIS.

# 1)
# Use Python's build-in binary search function bisect
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         res = [nums[0]]
#         for i in range(1, len(nums)):
#             if nums[i] > res[-1]:
#                 res.append(nums[i])
#             else:
#                 idx = bisect.bisect_left(res, nums[i])
#                 res[idx] = nums[i]
#         return len(res)

# 2) write custom binary search function
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > res[-1]:
                res.append(nums[i])
            else:
                res[self.binarysearch(res, nums[i])] = nums[i]
        return len(res)

    def binarysearch(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

# Even DP needs O(n^2) time
# dp[i]: the length of the longest increasing subsequence that ends with the element at index i.
#   - note that initial value of dp[] is all 1
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         dp = [1] * len(nums)
#         res = 1
#         for i in range(len(nums)):
#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     dp[i] = max(dp[i], dp[j] + 1)
#                     res = max(dp[i], res)
#         return res