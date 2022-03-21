# Saves the indices of each word in the constructor
# For each query, pull out indices of the two input words, and do a (non-brute force) search
# for the cloest pair
#
# Constructor: T: O(n), S: O(n)
# query: T:O(n), S:O(1)
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.word_indices = collections.defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.word_indices[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        w1_indices = self.word_indices[word1]
        w2_indices = self.word_indices[word2]

        i, j = 0, 0
        res = float('inf')
        while i < len(w1_indices) and j < len(w2_indices):
            res = min(res, abs(w1_indices[i] - w2_indices[j]))

            if w1_indices[i] < w2_indices[j]:
                i += 1
            else:
                j += 1

        return res

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)