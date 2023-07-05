# Just be careful that words in s is 1-indexed
class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        res = [''] * len(words)
        for word in words:
            res[int(word[-1]) - 1] = word[:len(word) - 1]

        return ' '.join(res)
