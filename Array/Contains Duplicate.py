# No smart solution. Just either sort or hashset
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         seen = set()
#         for n in nums:
#             if n in seen:
#                 return True
#             seen.add(n)

#         return False