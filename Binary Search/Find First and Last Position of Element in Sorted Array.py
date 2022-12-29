# Two binary searches to find lower and upper bound
# Time: O(nlogn); space: O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def find(find_first) -> int:
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:  # nums[mid] == target
                    if find_first:
                        if mid == 0 or nums[mid] != nums[mid - 1]:
                            return mid
                        else:  # Here mid > 0 and nums[mid] == nums[mid - 1]
                            right = mid - 1
                    else:  # find last
                        if mid == len(nums) - 1 or nums[mid] != nums[mid + 1]:
                            return mid
                        else:  # Here mid < len(nums) - 1 and nums[mid] == nums[mid + 1]
                            left = mid + 1
            return -1

        return [find(True), find(False)]

# class Solution:
#     def searchRange(self, nums: list[int], target: int) -> list[int]:
#         lower_bound = Solution.find_bound(nums, target, True)
#         if lower_bound == -1:
#             return [-1, -1]
#         upper_bound = Solution.find_bound(nums, target, False)
#         return [lower_bound, upper_bound]
#
#     @staticmethod
#     def find_bound(nums: list[int], target: int, find_lower_bound: bool) -> int:
#         low, high = 0, len(nums) - 1
#         while low <= high:
#             mid = (low + high) // 2
#             if nums[mid] == target:
#                 if find_lower_bound:
#                     # If there is no same value element on the left, then this is the leftmost target
#                     if mid == low or nums[mid] != nums[mid - 1]:
#                         return mid
#                     else:  # There is at least one element with the same target on the left
#                         high = mid - 1  # Using mid - 1 won't miss the target. Since at here we know nums[mid-1] == nums[mid] == target
#                 else:
#                     if mid == high or nums[mid] != nums[mid + 1]:
#                         return mid
#                     else:
#                         low = mid + 1
#
#             elif nums[mid] < target:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#
#         return -1

# Use more than two binary searches, not ideal
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         res = []

#         i = self.binarySearch(nums, target, 0, len(nums) - 1)
#         if(i < 0):
#             return [-1, -1]
#         else:
#             res.append(i)
#             res.append(i)

#         # Find the lowest index
#         low = 0
#         high = i - 1
#         while (low <= high):
#             pos = self.binarySearch(nums, target, low, high)
#             if pos == -1:
#                 break
#             else:
#                 res[0] = pos
#                 high = pos - 1

#         # Find the highest index
#         low = i + 1
#         high = len(nums) - 1
#         while (low <= high):
#             pos = self.binarySearch(nums, target, low, high)
#             if pos == -1:
#                 break
#             else:
#                 res[1] = pos
#                 low = pos + 1

#         return res

#     def binarySearch(self, nums: List[int], target: int, low: int, high: int) -> int:
#         while (low <= high):
#             mid = (low + high) // 2
#             #mid = low + (high-low)//2   # also works.

#             if target == nums[mid]:
#                 return mid
#             elif target < nums[mid]:
#                 high = mid - 1
#             else:
#                 low = mid + 1
#         return -1
