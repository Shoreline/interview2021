# same as course schedule I: https://leetcode.com/problems/course-schedule/
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_counts = [0] * numCourses
        out_map = collections.defaultdict(list)

        for p in prerequisites:
            in_counts[p[0]] += 1
            out_map[p[1]].append(p[0])

        takable = []
        for i in range(len(in_counts)):
            if in_counts[i] == 0:
                takable.append(i)

        res = []
        while takable:
            res.append(takable.pop())
            if res[-1] in out_map:
                for course in out_map[res[-1]]:
                    in_counts[course] -= 1
                    if in_counts[course] == 0:
                        takable.append(course)

        return res if len(res) == numCourses else []
