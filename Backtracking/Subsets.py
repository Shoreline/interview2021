# t: o(n * 2^n): call dfs 2^n times, each time deepcopy takes n
# s: o(n * 2^n) (to save all result)
# For subset, don't wait till pos == len(nums) to add tmp[:] to res[]

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def bt(pos, tmp):            
            # 1) add none of the remaining elements
            res.append(tmp[:]) 
            # 2) add one of the remaining elements and continue
            for i in range(pos, len(nums)):
                tmp.append(nums[i])
                bt(i+1, tmp)
                tmp.pop()
        
        bt(0, [])
        return res

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []

#         def dfs(pos: int, tmp: list[int]):
#             # WRONG
#             # if pos == len(nums):
#             #     res.append(tmp[:])
#             #     return

#             # 1) add none of the remaining elements
#             res.append(tmp[:])
#             # 2) add one of the remaining elements and continue dfs
#             for i in range(pos, len(nums)):
#                 tmp.append(nums[i])
#                 dfs(i + 1, tmp)
#                 tmp.pop()

#         dfs(0, [])
#         return res

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         self.dfs(nums, 0, [], res)
#         return res

#     # Each call of dfs: add current tmp and try adding one element of the remaining array
#     def dfs(self, nums: List[int], pos: int, tmp: List[int], res: List[List[int]]):
#         # Two situations: 1) add none of the remaining array; 2) add at least one char of the remaining array
#         res.append(tmp[:])
#         for i in range(pos, len(nums)):
#             tmp.append(nums[i])
#             self.dfs(nums, i+1, tmp, res)
#             tmp.pop() # the nums[i] added two lines above will be poped out. (each call of dfs pushes an ele to tmp but later pops it out)

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         self.dfs(nums, 0, [], res)
#         return res

#     def dfs(self, nums: List[int], pos: int, tmp: List[int], res: List[List[int]]):
#         # At this moment.
#         # Possibility tree: 1) don't use any of the remaining elements in nums -> res.append(tmp[:]);
#         # 2) Always use nums[pos] in every following subset. Following subsets is a problem of self.dfs(nums, i+1, tmp, res)
#         # 3) Always not use nums[pos], but always use nums[pos + 1] in every following subset, ...
#         # 4) Always not use nums[pos] and nums[pos+1], but always use nums[pos + 2] in every following subset, ...
#         res.append(tmp[:])
#         for i in range(pos, len(nums)):
#             tmp.append(nums[i])
#             self.dfs(nums, i+1, tmp, res)
#             tmp.pop()

# Wrong: repeated adding
# Try to cover two possible cases: skip nums[i] or add nums[i] to tmp. But later will repeatedly do some adding.
# e.g. for [1,2]: there are 6 outcome, not 4! when initial pos = 0, 4 outcome; then when inital pos = 1, 2 outcome -> 6 in total
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         self.dfs(nums, 0, [], res)
#         return res

#     def dfs(self, nums: List[int], pos: int, tmp: List[int], res: List[List[int]]):
#         if(pos == len(nums)):
#             res.append(tmp[:])
#             return

#         for i in range(pos, len(nums)):
#             self.dfs(nums, i+1, tmp, res)
#             tmp.append(nums[i])
#             self.dfs(nums, i+1, tmp, res)
#             tmp.pop()
