# Note: Sort the words with the same frequency by their lexicographical order.
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)

        # sort by (-count[x],x) , but returns their keys.
        return heapq.nsmallest(k, count.keys(), key=lambda x: (-count[x], x))

        # Same
        # res = sorted(count, key=lambda x: (-count[x], x))
        # return res[:k]

# Bucket sort
# class Solution:
#     def topKFrequent(self, words: List[str], k: int) -> List[str]:        