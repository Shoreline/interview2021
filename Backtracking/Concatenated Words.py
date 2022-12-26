# Backtracking + caching
#
# Cut each word in all possible pieces, and see if they are all members of the given words list.
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words_set = set(words)

        @lru_cache(None)
        def isConcatenatedWord(word):
            for i in range(1, len(word)):
                suffix = word[:i]
                postfix = word[i:]

                if suffix in words_set and (postfix in words_set or isConcatenatedWord(postfix)):
                    return True
            
            return False
        
        res = []
        for word in words_set:
            if isConcatenatedWord(word):
                res.append(word)
        
        return res

# class Solution:
#     def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
#         d = set(words)
#         memo = {}  # saves whether a word in words[] can be concatenated from other words

#         # Returns if a given word can be concatenated from other words
#         def dfs(word):
#             if word in memo:
#                 return memo[word]

#             memo[word] = False
#             for i in range(1, len(word)):  # we want at least one char in prefix and suffix
#                 prefix = word[:i]
#                 suffix = word[i:]

#                 # No need to do dfs(prefix), since dfs(prefix) is always false while reaching here.
#                 # If dfs(prefix) == True:
#                 #   -> prefix can be split into at least 2 words in dict
#                 #   -> Previous, we must have already gone through prfix = word1, suffix = word2+cur_suffix
#                 #   -> dfs(word2+cur_suffix) will later trigger dfs(cur_suffix), which is impossible, otherwise cur_suffix will already be in memo
#                 #   -> Therefore, word1 mustn't a word in dict
#                 # if (prefix in d or dfs(prefix)) and (suffix in d or dfs(suffix)): # 3x slower
#                 if prefix in d and (suffix in d or dfs(suffix)):
#                     memo[word] = True
#                     break

#             return memo[word]

#         res = []
#         for word in words:
#             if dfs(word):
#                 res.append(word)
#         return res
