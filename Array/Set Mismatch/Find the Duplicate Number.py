# Key point: nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# Here all numbers appear ONCE except for one; the XOR problem all numbers appear TWICE except for one

# Array as hashmap
# T:O(n); S:O(1)
# Keep setting nums[k] = k; stop while finding nums[0] = nums[k]. Obviously, now nums[0] = nums[k] = that_duplicated_num
# Note that the integers in nums are from 1 to n inclusive. So try to move numbers around till nums[0] = nums[nums[0]]
# The swap of nums[0] and nums[nums[0]], say nums[0]=k:
#   -> let nums[k] = k
#   move the value of nums[0] to the same index (nums[nums[0]]) so that after swapping nums[nums[0]] has index of nums[0], and value is nums[0]
#
# There is only one duplicated value. So if nums[0] = any nums[k], then nums[0] is the duplicated value

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        k = nums[0]
        while k != nums[k]:
            nums[k], k = k, nums[k] # k, nums[k] = nums[k], k is wrong!

        return k
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         while nums[0] != nums[nums[0]]:
#             # Swap value of nums[0] and nums[nums[0]]
#             # Note that changing nums[0]'s value will also change nums[nums[0]] at the same time
#             # So we have to update nums[nums[0]] first
#
#             nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
#             # nums[0], nums[nums[0]] = nums[nums[0]], nums[0] #does not work !
#         return nums[0]

# Cycle detection. Same as linked list cycle II
# T:O(n); S:O(1)
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         walker = nums[0]
#         runner = nums[0]
#         while True: # note that the initial values of walker and runner are the same
#             walker = nums[walker]
#             runner = nums[nums[runner]]
#             if walker == runner:
#                 break

#         walker2 = nums[0] # important! not nums[0]
#         while walker != walker2:
#             walker = nums[walker]
#             walker2 = nums[walker2]

#         return walker

# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         walker = nums[0]
#         runner = nums[nums[0]]
#         while walker != runner:
#             walker = nums[walker]
#             runner = nums[nums[runner]]

#         walker2 = 0 # important! not nums[0]
#         while walker != walker2:
#             walker = nums[walker]
#             walker2 = nums[walker2]

#         return walker