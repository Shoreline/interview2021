# Solution 1
# Sort the input array.
# Compared with previous number,
# the current number need to be at least prev + 1.
# Time Complexity: O(NlogN) for sorting
# Space: O(1) for in-space sort, or O(N) for other sorting tech
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        increments = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                increments += (nums[i - 1] + 1 - nums[i])
                nums[i] = nums[i - 1] + 1
        return increments

# Solution 2 (copied)
# T & S: O(n+ max(nums) - min(nums))
# class Solution:
#     def minIncrementForUnique(self, nums: List[int]) -> int:
#         max_val = max(nums)
#         min_val = min(nums)
#         count = collections.Counter(nums)
#         taken = [] # a stack

#         moves = 0
#         for x in range(min_val, len(nums) + max_val): # possible value after incrementing: [min, max + size)
#             if count[x] >= 2:
#                 for i in range(count[x] - 1):  # There are count[x] elements with same value, so count[x] - 1 are duplicated
#                     taken.append(x)
#             elif taken and x not in count: # x is an empty slot so we increment one of the duplicated elements to x
#                 moves += x - taken.pop()

#         return moves

# The list.extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.

# class Solution:
#     def minIncrementForUnique(self, nums: List[int]) -> int:
#         max_val = max(nums)
#         count = collections.Counter(nums)
#         taken = [] # a stack

#         moves = 0
#         for x in range(len(nums) + max_val):
#             if count[x] >= 2:
#                 taken.extend([x] * (count[x] - 1)) # There are count[x] elements with same value, so count[x] - 1 are duplicated
#             elif taken and count[x] == 0: # Found an empty slot so we can put one of the elements in taken
#                 moves += x - taken.pop()

#         return moves


