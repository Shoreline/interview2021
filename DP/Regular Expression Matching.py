# # DP
# # DP[i][j]: isMatch(text[i:], pattern[j:])
class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):  # start with the last charter of pattern
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j + 1 < len(pattern) and pattern[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]

        return dp[0][0]


# recursion + caching.
class Solutio2n:
    def isMatch(self, text: str, pattern: str) -> bool:
        # saves the results of isMatch(i, j).
        res = {}

        # isMatch(i, j): isMatch(text[i:], pattern[j:])
        def isMatch(i: int, j: int):
            if (i, j) not in res:
                # if reaching the end of pattern, then memo[i, j] is true only when also reaching the end of text
                # Note that we don't need to check further cases.
                if j == len(pattern):
                    res[i, j] = (i == len(text))  # same as res[(i,j)] = (i == len(text))
                else:
                    # if text[i] exists and matches with pattern[j]
                    ij_match = i < len(text) and pattern[j] in {text[i], '.'}

                    # if the next character of pattern, pattern[j+1], is *,
                    # then returns true if either
                    #   1) * matches preceeding char zero times-> simply skipping j and j+1 (*) in the pattern string -> whether isMatch(i, j) is true depends on if isMatch(i, j+2) is true
                    #   2) * matches preceeding char for at least once ->isMatch(i, j) to be true needs a) text[i], pattern[j] match, and b) isMatch(i+1, j) is true
                    #           -> pattern[j]* match text[i], keep checking if they also match text[i+1]
                    if j + 1 < len(pattern) and pattern[j + 1] == '*':
                        res[i, j] = isMatch(i, j + 2) or (ij_match and isMatch(i + 1, j))

                    # returns true if text[i], pattern[j] match and text[i+1:], pattern[j+1:] match
                    else:
                        res[i, j] = ij_match and isMatch(i + 1, j + 1)

            return res[i, j]

        return isMatch(0, 0)