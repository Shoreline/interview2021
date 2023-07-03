# copied

# The idea is to find the longest palindromic subsequence(lps) of the given string.
# |lps - original string| <= k,
# then the string is k-palindrome.
#
# And find the longest palindromic subsequence(lps) of the given string
#   -> find the Longest Common Subsequence (LCS) of a string and its reversed string
# https://leetcode.com/problems/longest-palindromic-subsequence/description/

# This problem is essentially finding the Longest Palindromic Subsequence (LPS) of a string, which is the same as
# finding the Longest Common Subsequence (LCS) of a string and its reversed string (learned from this post:
# https://leetcode.com/problems/valid-palindrome-iii/discuss/397606/Find-Longest-Palindromic-Subsequence.).
# Finding LCS of two strings can be solved by using algorithm same as Edit Distance problem (reduced form while only
# "deletion" is allowed, as shown above by @cenkay ).

# Convert it into an edit distance problem (but this time only deletion/addition is allowed).
#   What's the minimum edits needed to make s the same as s[::-1]
# Also, if one character needs to be deleted, there will be 2 chars distance between the original string and the
# reversed string.
#   Ex) "abca" and "acba" has 2 edit distance.
#   So the allowed distance is 2 * k

# if one of them is empty we have to delete the entire other
# if last characters are the same then no need to delete any of these 2 chars
# if last characters are not the same then delete either one



# bottom up dp
# f(i,j) is the edit distance of s1[:i] and s2[:j] (i.e. the number of operations to make s1[:i] and s2[:j] the same)
#   Here s2 is reverted s1. So s2[x] = s1[n-x]
# f(0,j) = j and f(i,0) = i # if one string is empty, we have to delete all chars in the other string to make them the
# same
# if s1[i-1]==s2[j-1] then f(i,j) = f(i-1,j-1)
# if s1[i-1]!=s2[j-1] then f(i,j) = 1+min(f(i-1,j), f(i,j-1)) # delete one char from either s1 or s2 #
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        s2 = s[::-1]
        for i in range(n + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif s[i-1] == s2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])

        # why <= k * 2?
        # If one character needs to be deleted, there will be 2 chars distance between the original string and the reversed string.
        #   Ex) "abca" and "acba" has 2 edit distance.
        return dp[n][n] <= k * 2