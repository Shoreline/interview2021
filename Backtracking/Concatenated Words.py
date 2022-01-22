# Backtracking
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        d = set(words)
        memo = {}  # saves whether a word in words[] can be concatenated from other words

        # Helper function that returns if the givn word can be concatenated from other words
        def dfs(word):
            if word in memo:
                return memo[word]

            memo[word] = False
            for i in range(1, len(word)):  # start from 1 since single char can't be a concatenated word
                prefix = word[:i]
                suffix = word[i:]

                # No need to do dfs(prefix), since we have been checking every prefix in previous loops
                if prefix in d and (suffix in d or dfs(suffix)):
                    memo[word] = True
                    break

            return memo[word]

        res = []
        for word in words:
            if dfs(word):
                res.append(word)
        return res