# time O(NlogN): sorting takes nlogn
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # https://cloud.tencent.com/developer/article/1760142?from=article.detail.1435388
        intervals.sort(key=lambda x: x[0])  # sort by the [0] element
        # Alternative:
        # def compare(interval: List[int]):
        #     return interval[0]
        # intervals.sort(key=compare)

        # Java:  Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        # C++: sort(intervals.begin(), intervals.end());

        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])

        return res

# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         # https://cloud.tencent.com/developer/article/1760142?from=article.detail.1435388
#         intervals.sort(key=lambda x:x[0]) # sort by the [0] element

#         res = []
#         tmp = intervals[0]
#         for i in range(1, len(intervals)):
#             if intervals[i][0]<=tmp[1]:
#                 tmp[1] = max(tmp[1], intervals[i][1])
#             else:
#                 res.append(tmp) #copy.deepcopy(tmp)) If not using deepcopy, elements in the input intervals are also changed.
#                 tmp = intervals[i]
#         res.append(copy.deepcopy(tmp))
#         return res

