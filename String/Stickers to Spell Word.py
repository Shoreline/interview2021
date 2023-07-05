# Note: each sticker can be used more than once
#
# sort the stickers according to length.
# check whether there is one sticker to spell the target. If so, just return 1.
# by @zestypanda's idea, check if target[0] is in sticker, if not,continue.
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # Convert stickers into a stickers_freq map: <sticker_index, <char, char_freq>
        stickers = [collections.Counter(x) for x in stickers]

        # the min num of stickers to get string "target"
        @lru_cache(None)
        def dfs(target):
            res = float('inf')
            for sticker in stickers:
                # optional optimization (why?)
                # if target[0] not in sticker:
                #     continue

                new_target = target;
                for s in sticker:
                    # replace the first sticker[s] occurencies of char s with ""
                    new_target = new_target.replace(s, "", sticker[s])
                if new_target == "":  # the best result is found, just return 1
                    return 1
                elif new_target != target:  # part of target can be removed
                    res = min(res, 1 + dfs(new_target))
            return res

        res = dfs(target)
        return -1 if res == float('inf') else res

# dp[s] is the minimum stickers required for string s (-1 if impossible). Note s is sorted.
# clearly, dp[""] = 0, and the problem asks for dp[target].
# dp[s] = min(1+dp[reduced_s]) for all stickers,
# here reduced_s is a new string after certain sticker applied
# class Solution2:
#     def minStickers(self, stickers: List[str], target: str) -> int:
#         m = len(stickers)
#         mp = [[0]*26 for y in range(m)] # <sticker_index, <char, char_freq>>
#         for i in range(m):
#             for c in stickers[i]:
#                 mp[i][ord(c)-ord('a')] += 1

#         dp = {}
#         dp[""] = 0

#         def helper(dp, mp, target):
#             if target in dp:
#                 return dp[target]

#             n = len(mp)
#             tar = [0]*26
#             for c in target:
#                 tar[ord(c)-ord('a')] += 1

#             ans = float('inf')
#             for i in range(n):
#                 if mp[i][ord(target[0])-ord('a')] == 0:
#                     continue

#                 s = ''
#                 for j in range(26):
#                     if tar[j] > mp[i][j]:
#                         s += chr(ord('a')+j)*(tar[j] - mp[i][j])
#                 tmp = helper(dp, mp, s)
#                 if (tmp != -1):
#                     ans = min(ans, 1+tmp)
#             dp[target] = -1 if ans == float('inf') else ans
#             return dp[target]

#         return helper(dp, mp, target)