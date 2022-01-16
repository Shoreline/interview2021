# Backtrack.
# Manipulate the input nums List to get permutations
# - Update the input nums in-place to keep the unused numbers at the latter half.
# Time: a rough estimation will be O(N*N!). O(N) to find one solution?
# Space: O(N!) there are N! solutions
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(pos: int):
            # nums[0, pos] is current permutation.
            if pos >= len(nums):
                res.append(list(nums))
                return

            # Try each one of the remaining unused elements, to add to the current permutation
            # The current permutation grows one element per call of backtrack()
            for i in range(pos, len(nums)):
                nums[i], nums[pos] = nums[pos], nums[i]
                backtrack(pos + 1)
                nums[i], nums[pos] = nums[pos], nums[i]

            return

        backtrack(0)

        return res

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         used = [False] * len(nums)
#         self.dfs(nums, used, [], res)
#         return res

#     def dfs(self, nums: List[int], used: List[bool], tmp: List[int], res: List[List[int]]):
#         if len(tmp) == len(nums):
#             res.append(tmp[:])
#             return

#         for i in range(len(nums)):
#             if used[i]:
#                 continue

#             tmp.append(nums[i])
#             used[i] = True
#             self.dfs(nums, used, tmp, res)
#             tmp.pop()
#             used[i] = False

#         return