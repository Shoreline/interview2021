# prefix sum technique for the problems like "Find a number of CONTINUOUS subarrays/submatrices/tree paths that sum to target".
# Say n1, n2 are two nodes, and n1 is the ascendant of n2. Then prefix_sum_n2 - prefix_sum_n1 = sum_of_nodes_between_n1_n2 (sum(n1, n2])
#
# prefix_sum_count<prefix_sum_val, path_count>
#   key is prefix_sum of all nodes till the current one; value is the count of paths
#   prefix_sum_count only saves info about the path from the root to current node


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# $PrefixSum: a map saves from root to current node, <prefix_sum_val, num_paths>
#   Initial state: Counter({0:1})
from collections import Counter


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.res = 0

        # The prefix_sum_count is a counter of how many paths for each prefix_sum value.
        # It is just like the usual tmp[] used in dfs()
        def dfs(root: TreeNode, curSum: int, prefix_sum_count: Counter[int]):
            if not root:
                return

            curSum += root.val
            # If in prefix_sum there is any prefix_sum = curSum - targetSum:
            #   Then targetSum = curSum - prefix_sum -> matching path
            self.res += prefix_sum_count[curSum - targetSum]

            prefix_sum_count[curSum] += 1
            dfs(root.left, curSum, prefix_sum_count)
            dfs(root.right, curSum, prefix_sum_count)
            prefix_sum_count[curSum] -= 1

        dfs(root, 0, Counter({0: 1}))  # important initial state!
        return self.res;

    # class Solution:
#     def pathSum(self, root: TreeNode, targetSum: int) -> int:
#         ans = [0]
#         prefix_sum = collections.defaultdict(int) # use a map, since there can be >1 nodes with the same prefix_sum value
#         self.helper(root, targetSum, 0, prefix_sum, ans)
#         return ans[0]

#     def helper(self, root: TreeNode, targetSum: int, curSum:int, prefix_sum, ans: List[int]) ->None:
#         if not root:
#             return

#         curSum += root.val
#         if curSum == targetSum:
#             ans[0]+= 1

#         # if in prefix_sum there is any prefix_sum = curSum - targetSum; then targetSum = curSum - prefix_sum -> matching path
#         ans[0] += prefix_sum[curSum - targetSum]   
#         prefix_sum[curSum] += 1

#         self.helper(root.left, targetSum, curSum, prefix_sum, ans)
#         self.helper(root.right, targetSum, curSum, prefix_sum, ans)

#         prefix_sum[curSum] -= 1