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

    # Let K elements in points[left : right+1] be the smallest
    def qsort(self, points, left, right, K):
        if left < right:
            # Put random element as points[r] - this is the pivot
            k = random.randint(left, right)
            points[right], points[k] = points[k], points[right]

            p = self.partition(points, left, right)
            elements = p - left + 1
            if elements == K:
                return
            elif elements < K:
                # Found elements number of the closest elements, need K - elements more from the right side of points[p]
                self.qsort(points, p + 1, right, K - elements)
            else:
                self.qsort(points, left, p - 1, K)

    # Move elements in points so that points[l: pos+1] has distance <= points[pivot].
    # And returns pos
    def partition(self, points, left, right):
        pivot = points[right]
        pos = left
        # move elements <= pivot to the first half
        # pos is the first index can take the moved element.
        for i in range(left, right):
            if (points[i][0] ** 2 + points[i][1] ** 2) <= (pivot[0] ** 2 + pivot[1] ** 2):
                points[pos], points[i] = points[i], points[pos]
                pos += 1
        points[pos], points[right] = points[right], points[pos]
        # points[pos],pivot = pivot, points[pos] # wrong!
        return pos
# class Solution:
#     def kClosest(self, points, K):
#         self.qsort(points, 0, len(points) - 1, K)
#         return points[:K]
#
#     def qsort(self, points, l, r, K):
#         if l < r:
#             # Put random element as points[r] - this is the pivot
#             k = random.randint(l, r)
#             points[r], points[k] = points[k], points[r]
#
#             p = self.partition(points, l, r)
#             if p == K:
#                 return
#             elif p < K:
#                 self.qsort(points, p + 1, r, K)
#             else:
#                 self.qsort(points, l, p - 1, K)
#
#     # Move elements in points so that points[l: pos+1] has distance <= points[pivot].
#     # And returns pos
#     def partition(self, points, l, r):
#         pivot = points[r]
#         pos = l
#         # move elements <= pivot to the first half
#         # pos is the first index can take the moved element.
#         for i in range(l, r):
#             if (points[i][0] ** 2 + points[i][1] ** 2) <= (pivot[0] ** 2 + pivot[1] ** 2):
#                 points[pos], points[i] = points[i], points[pos]
#                 pos += 1
#         points[pos], points[r] = points[r], points[pos]
#         # points[pos],pivot = pivot, points[pos] # wrong!
#         return pos