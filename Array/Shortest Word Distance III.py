# Very similar to shortest word distance I
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        res = float('inf')
        w1, w2 = -1, -1
        for i, w in enumerate(wordsDict):
            if w == word1:
                w1 = i
                if w2 >= 0:
                    res = min(res, w1 - w2)

            if w == word2:
                w2 = i
                if w1 >= 0 and word1 != word2:
                    res = min(res, w2 - w1)

        return res