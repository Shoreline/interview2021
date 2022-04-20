# Heap: nlogk time and k space
# import heapq
# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         res = []
#         #for point in points:
#         for (x,y) in points:
#             dist = x*x + y*y
#             if len(res)<k:
#                 heapq.heappush(res, (-dist, (x,y))) # use -dist to get descending order
#             else:
#                 heapq.heappushpop(res, (-dist, (x,y)))

#         return [(x,y) for negtive_dist, (x,y) in res]

# Sorting costs O(nlogn) time
# But on average quick sort costs o(n) time
class Solution:
    def kClosest(self, points, K):
        self.qsort(points, 0, len(points) - 1, K)
        return points[:K]

    def qsort(self, points, l, r, K):
        if l < r:
            p = self.partition(points, l, r)
            if p == K:
                return
            elif p < K:
                self.qsort(points, p + 1, r, K)
            else:
                self.qsort(points, l, p - 1, K)

    def partition(self, points, l, r):
        pivot = points[r]  # here pivot is not randomly picked
        a = l
        # move elements <= pivot to the first half
        for i in range(l, r):
            if (points[i][0] ** 2 + points[i][1] ** 2) <= (pivot[0] ** 2 + pivot[1] ** 2):
                points[a], points[i] = points[i], points[a]
                a += 1
        points[a], points[r] = points[r], points[a]
        # points[a],pivot = pivot, points[a] # wrong!
        return a