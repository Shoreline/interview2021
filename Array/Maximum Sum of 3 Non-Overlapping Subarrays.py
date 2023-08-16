# Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and
# return them.

# Return the result as a list of indices representing the starting position of each interval (0-indexed). If there
# are multiple answers, return the lexicographically smallest one.

# Brute force
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        W = []  # array#1: every size_k_sliding_window_sum
        curr_sum = 0
        for i, x in enumerate(nums):
            curr_sum += x
            if i >= k:
                curr_sum -= nums[i - k]
            if i >= k - 1:
                W.append(curr_sum)

        left = [0] * len(W)  # Array#2: saves each index of {sofar the biggest sliding_window from left}
        best = 0
        for i in range(len(W)):
            if W[i] > W[best]:
                best = i
            left[i] = best

        right = [0] * len(W)  # Array#3: index of sofar the biggest sliding_window from right
        best = len(W) - 1
        for i in range(len(W) - 1, -1, -1):
            if W[i] >= W[best]:
                best = i
            right[i] = best

        ans = None
        # j: index of current sliding window
        # i: index of the biggest sliding window starting before j - k | before j - k -> no overlap with cur window
        # l: index of the biggest sliding window starting after j + k | after j + k -> no overlap with cur window
        for j in range(k, len(W) - k):
            i, l = left[j - k], right[j + k]

            # Found a bigger solution.
            if ans is None or (W[i] + W[j] + W[l] > W[ans[0]] + W[ans[1]] + W[ans[2]]):
                ans = [i, j, l]
        return ans
