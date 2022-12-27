# Construct a BST from n nodes:
#   1. pick one node as the root;
#   2. Use k nodes to construct the left sub-BST;
#   3. Use the remaining n-k-1 nodes to construct the right sub-BST
# /*
#  * DP
#  *
#  * Time: O(N^2); Space: O(N)
#  *
#  * 1D array, but two nested loops
#  *
#  * dp[i]: how many unique BSTs for i different numbers.
#   dp[i] = sigma(dp[left] * dp[right]), while left + right = i - 1
# Since nodes of this problem is from 1 ~ n. The possible node number of left tree is from 0 to n-1, say k.
# And meanwhile the possible node number of the right tree will be n-1-k (n - 1 - k: minus the root, then minus the node count in left tree )
#  */

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1): # number of nodes: from 2 to n
            for k in range(i): # number of left tree nodes: from 0 to i - 1 (there has to be one root node, so i - 1 instead of i)
                dp[i] += dp[k] * dp[i - 1 - k]
        
        return dp[-1]
# class Solution:
#     def numTrees(self, n: int) -> int:
#         dp = [0] * (n + 1)
#         dp[0] = 1
#         dp[1] = 1

#         for i in range(2, n + 1):
#             for k in range(i):  # use k (a number) as the root. k is [0,i).
#                 dp[i] += dp[k] * dp[
#                     i - k - 1]  # numTrees of the two sub trees. Note that the maximum number of nodes in each subtree is i-1 (there has to be a root node)

#         return dp[-1]
