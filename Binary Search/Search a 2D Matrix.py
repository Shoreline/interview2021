# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.

# The 2d array can be treated as a 1d sorted array.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        # binary search
        left, right = 0, m * n - 1
        while left <= right:
            mid_idx = (left + right) // 2
            mid_val = matrix[mid_idx // n][mid_idx % n]  # important
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid_idx + 1
            else:
                right = mid_idx - 1

        return False

# Two binary searches: first search the row may have the target; second search that row for target
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#
#         low, high = 0, len(matrix) - 1
#         while low <= high:
#             mid = low + (high - low) // 2
#             if matrix[mid][0] == target:
#                 return True
#             elif matrix[mid][0] < target:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#
#         # now high < low, and matrix[high][0] < target < matrix[low][0]
#         row = high
#         low, high = 0, len(matrix[0]) - 1
#         while low <= high:
#             mid = low + (high - low) // 2
#             if matrix[row][mid] == target:
#                 return True
#             elif matrix[row][mid] < target:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#
#         return False