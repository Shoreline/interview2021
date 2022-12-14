# /*
#  * Greedy algorithm. Here the greedy method is
#  * actually to find "the maximum reachable range after N jumps". Once the
#  * maximum reachable range >= last_index_of_nums then the current jump times will be the
#  * result
#  */

# Time: O(N); space O(1)
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        pos = 0  # current position
        cur_reach = 0
        # we are told that we can surely reach the end, so ok to use this as while loop condition
        while cur_reach < len(nums) - 1:
            next_reach = cur_reach
            while pos <= cur_reach:
                next_reach = max(next_reach, pos + nums[pos])
                pos += 1

            cur_reach = next_reach
            jumps += 1

        return jumps

# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         jumps = 0
#         i = 0
#         cur_reach = 0
#         while(cur_reach < len(nums) - 1): # we are told that we can surely reach the end, so ok to use this as while loop condition
#             next_reach = cur_reach
#             for j in range(i, cur_reach + 1):
#                 next_reach = max(next_reach, nums[j] + j)

#             # it's guaranteed that we can reach cur_reach + 1 (since we are told that we can reach the end)
#             # actually, we don't need j, can keep using i
#             i = cur_reach + 1

#             cur_reach = next_reach
#             jumps += 1

#         return jumps

