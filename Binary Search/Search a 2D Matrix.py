# Two binary searches: first search the row may have the target; second search that row for target
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        low, high = 0, len(matrix) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                low = mid + 1
            else:
                high = mid - 1

        # now high < low, and matrix[high][0] < target < matrix[low][0]
        row = high
        low, high = 0, len(matrix[0]) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False

# Only one while loop, but hard to understand
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         m = len(matrix)
#         if m == 0:
#             return False
#         n = len(matrix[0])

#         # binary search
#         left, right = 0, m * n - 1
#         while left <= right:
#                 pivot_idx = (left + right) // 2
#                 pivot_element = matrix[pivot_idx // n][pivot_idx % n]
#                 if target == pivot_element:
#                     return True
#                 else:
#                     if target < pivot_element:
#                         right = pivot_idx - 1
#                     else:
#                         left = pivot_idx + 1
#         return False        