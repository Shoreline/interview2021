# two pointers. Keep saving unique elements to the former part of the array.
# O(n) time
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ptr = 0  # points to the last confirmed non-duplicated nums[ptr]
        for i in range(1, len(nums)):
            if nums[i] != nums[ptr]:
                ptr += 1  # increment ptr, then do nums[ptr] = nums[i]
                nums[ptr] = nums[i]

        return ptr + 1

    # O(2n) time
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         if not nums:
#             return 0

#         DUPLICATE_LABEL = nums[0] - 1
#         cur = nums[0]
#         for i in range(1, len(nums)):
#             if nums[i] == cur:
#                 nums[i] = DUPLICATE_LABEL
#             else:
#                 cur = nums[i]

#         ptr = 1 # points to the first nums[ptr] that is ok to be filled
#         for i in range(1, len(nums)):
#             if nums[i] != DUPLICATE_LABEL:
#                 nums[ptr] = nums[i]
#                 ptr += 1

#         return ptr 