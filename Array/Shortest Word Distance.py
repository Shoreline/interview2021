class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        res = len(wordsDict)
        latest_w1, latest_w2 = -1, -1

        for i, word in enumerate(wordsDict):
            if word == word1:
                latest_w1 = i
            elif word == word2:
                latest_w2 = i

            if latest_w1 >= 0 and latest_w2 >= 0:
                res = min(res, abs(latest_w1 - latest_w2))

        return res

