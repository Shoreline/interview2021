# Similar to https://leetcode.com/problems/largest-rectangle-in-histogram/
# 1)
# Sequence of subarrays doesn't matter
# Say x is the min element of N sub-arrays, then in total these N arrays contributes x * N in the total sum
# The problem becomes: for every element x in the array, count how many sub-arrays have min = x
#
# 2) Each sub-array can be defined by left_boundary_index and right_boundary_index
# So sub-arrays with min = A[i], are the ones have left_b_i < i, and right_b_i > i, where within in the reange all elements are > A[i]. Then with left_min and right_max, there are (i - left_min) * (right_max - i) sub-arrays
#   Use a non-decrasing stack to save indice
#   for n in array, sum ( n * (indexof(n) - left_bounday) * (right_bounday - indexof(n)) )
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        stack = []  # The stack saves the INDEX of previous biggest element (non-decreasing)
        arr = [float('-inf')] + arr + [float('-inf')]
        for i, val in enumerate(arr):
            while stack and val < arr[stack[-1]]: # when n is smaller than previous biggest element in stack
                cur = stack.pop() # previous biggest element index
                #         n * (indexof(n) - left_bounday) * (right_bounday - indexof(n))
                res += arr[cur] * (cur - stack[-1]) * (i - cur)
            stack.append(i)
        return res % (10**9 + 7)