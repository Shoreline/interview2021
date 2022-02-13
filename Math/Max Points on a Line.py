# /*
#  * The idea is to compute and compare the slopes.
#  *
#  * For a straight line that passes Pi, Pj: slope = ((double)xi-xj)/(yi-yj)
#  *
#  * For each point Pi, compute all slopes for Pj -> O(N^2) time complexity
#  *
#  * There are just N^2 different straight lines.
#  *
#  * *Note: 1) handle horizontal lines (slope is infinite) 2) duplicated points;
#  * 3) convert int to double while computing slope (may have precision issue. But works for the x,y range in problem statement)
#  */

# points: [[x1, y1], [x2, y2], ...]
# helper(currentPoint, points) returns the maximum number of points for all lines passing currentPoint
#   It computes the slops of lines fomred by the currentPoint and each point in points.
#   Needs to handle duplicates and also don't forget to count currentPoint itself in
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def helper(currentPoint, points):
            x1, y1 = currentPoint
            slopes = collections.defaultdict(int)
            duplicates = 0
            max_count = 0
            for x2, y2 in points:
                # If the points are same increment duplicate counter.
                if x1 == x2 and y1 == y2:
                    duplicates += 1  # duplicated points are ignored
                # else find the slop and add in dic
                else:
                    slope = (x2 - x1) / (y2 - y1) if y2 != y1 else 'inf'
                    slopes[slope] += 1
                    max_count = max(max_count, slopes[slope])
            return max_count + 1 + duplicates  # "1" is this point itself

        res = 0
        # avoid duplicated checking
        # If there are max 3 points p1, p2, p3 on one line, then max_points_on_same_line_inlucding_point(a_point) is the same for p1, p2, p3, so only need to run this function onece for p1. And ok to exclude p1 for further computation
        while points:
            currentPoint = points.pop()
            res = max(res, helper(currentPoint, points))
        return res