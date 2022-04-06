# Bucket sort
# Time: O(N): N is the size of nums (not the distinct values in nums)
# 1 Create list of empty lists for bucktes: for frequencies 1, 2, ..., n.
# 2 Use Counter to count frequencies of elements in nums
# 3 Iterate over our Counter and add elements to corresponding buckets.
# 4 buckets is list of lists now, create one big list out of it.
# 5 Finally, take the k last elements from this list, these elements will be top K frequent elements.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # there can be multiple num having the same frequency, so we need a list
        bucket = [[] for _ in range(len(nums) + 1)]

        # Wrong! # Shallow copy. Every bucket[i] points to the same list
        # bucket = [[]] * (len(nums) + 1)

        count = Counter(nums)
        for num, freq in count.items():
            bucket[freq].append(num)

        res = []
        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i]:
                for num in bucket[i]:
                    res.append(num)

        return res[:k]

# Simply count the frequency O(n), and use a heap to find the k largest elements O(NlogK)
# S: O(n+k)
# from collections import Counter
# import heapq
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = Counter(nums)

#         # Return k largest from count.keys(), and let comparison function be count.get
#         # -> sort count.keys() by count.get(each_key)
#         return heapq.nlargest(k, count.keys(), key=count.get) 