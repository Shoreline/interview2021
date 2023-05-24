# dp[i][j]: LCS for s1[:i+1] and s2[:j+1]
#
# T: O(M * N). M, N: length of the two input Strings
# S: O(M * N) # can be further optimized
class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if s1[row - 1] == s2[col - 1]:
                    dp[row][col] = 1 + dp[row - 1][col - 1]
                else:
                    dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])

        # Followup: print the actual LCS
        # Create a string variable to store the lcs string
        lcs = ""
        # Start from the right-most-bottom-most corner and
        # one by one store characters in dp[][]
        i = m
        j = n
        while i > 0 and j > 0:
            # If current character in X[] and Y are same, then
            # current character is part of LCS
            if s1[i - 1] == s2[j - 1]:
                lcs += s1[i - 1]
                i -= 1
                j -= 1
            # If not same, then find the larger of two and
            # go in the direction of larger value
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

        # We traversed the table in reverse order
        # LCS is the reverse of what we got
        lcs = lcs[::-1]
        print("LCS of " + s1 + " and " + s2 + " is " + lcs)

        return dp[m][n]

# class Solution:
#     def longestCommonSubsequence(self, s1: str, s2: str) -> int:
#         m = len(s1)
#         n = len(s2)
#         if m < n:
#             return self.longestCommonSubsequence(s2, s1)
#         memo = [[0 for _ in range(n + 1)] for _ in range(2)]

#         for i in range(m):
#             for j in range(n):
#                 if s1[i] == s2[j]:
#                     memo[1 - i % 2][j + 1] = 1 + memo[i % 2][j]
#                 else:
#                     memo[1 - i % 2][j + 1] = max(memo[1 - i % 2][j], memo[i % 2][j + 1])

#         return memo[m % 2][n]


# Recursion solution
# T: O(M * N^2). M, N: length of the two input Strings
# S: O(M * N)
# class Solution:
#     def longestCommonSubsequence(self, s1: str, s2: str) -> int:
#         @lru_cache(None)
#         def helper(s1, s2, i, j):
#             if i == len(s1) or j == len(s2):
#                 return 0
#             if s1[i] == s2[j]:
#                 return 1 + helper(s1, s2, i + 1, j + 1)
#             else:
#                 return max(helper(s1, s2, i+1, j), helper(s1, s2, i, j + 1))


#         return helper(s1, s2, 0, 0)

