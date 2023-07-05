# PS: nums[i] is either 0 or 1
#   return the maximum length of a contiguous subarray with an EQUAL number of 0 and 1
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length = 0
        diff = 0  # diff between num_zeros and num_ones so far. +1 for nums[i]==0, otherwise -1
        mp = {}  # <diff, first_shown_index> # only saves first shown since we want the maximum length
        for i, num in enumerate(nums):

            if num == 0:
                diff -= 1  # decrement our diff if our current element is 0
            else:
                # increment our diff if current element is 1
                diff += 1

            if diff == 0:
                # if diff is 0, we have subarray of [nums[0], nums[i]] that qualifies.
                # It has to be the largest subarray so far.
                max_length = i + 1

            # if same diff val happened in the past (at index mp[diff])
            # meaning the subarray of [mp[diff], i-1] have equal number of 0s and 1s
            if diff in mp:
                max_length = max(max_length, i - mp[diff])
            else:
                mp[diff] = i

        return max_length
