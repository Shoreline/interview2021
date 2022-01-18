# dp[i][j]: the minDistance of the first i characters in word1 and first j
# characters in word2.
# Note: i and j are 0-indexed. So dp's size needs to be [len(word1) + 1][len(word2)+1]
# the i-th character of word1 is word1[i - 1]
# the j-th character of word2 is word2[j - 1]

# time and space: m*n
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return max(len(word1), len(word2))
        #          columns                             rows
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0:  # when i = 0, means we need j operations to build first j chars in word2
                    dp[i][j] = j
                elif j == 0:  # when j = 0, means we need i operations to build first i chars in word1
                    dp[i][j] = i
                elif word1[i - 1] == word2[j - 1]:  # when i-th char of word1 is the same as j-th char of word2
                    dp[i][j] = dp[i - 1][j - 1]
                else:  # 1 + min (replace, min(insert from word1, insert from word2))
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1]))

        return dp[-1][-1]
