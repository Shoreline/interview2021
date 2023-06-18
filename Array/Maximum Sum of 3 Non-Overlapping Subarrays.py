# Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and
# return them.

# Return the result as a list of indices representing the starting position of each interval (0-indexed). If there
# are multiple answers, return the lexicographically smallest one.
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        win_sums = []  # array of {sums of sliding_window}
        cur_window_sum = 0
        for i, x in enumerate(nums):
            cur_window_sum += x
            if i >= k:
                cur_window_sum -= nums[i - k]
            if i >= k - 1:
                win_sums.append(cur_window_sum)

        left = [0] * len(win_sums)  # index of sofar the biggest sliding_window from left
        best = 0
        for i in range(len(win_sums)):
            if win_sums[i] > win_sums[best]:
                best = i
            left[i] = best

        right = [0] * len(win_sums)  # index of sofar the biggest sliding_window from right
        best = len(win_sums) - 1
        for i in range(len(win_sums) - 1, -1, -1):
            if win_sums[i] >= win_sums[best]:
                best = i
            right[i] = best

        res = None
        # i: index of current sliding window
        # j: index of the biggest sliding window starting before i - k
        # l: index of the biggest sliding window starting after i + k
        for j in range(k, len(win_sums) - k):
            i, l = left[j - k], right[j + k]

            # Found a bigger solution.
            if res is None or (win_sums[i] + win_sums[j] + win_sums[l] > win_sums[res[0]] + win_sums[res[1]] + win_sums[res[2]]):
                res = [i, j, l]
        return res
