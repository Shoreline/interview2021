# Take all takable courses, until there is no course can be taken. Then see if there is still any course remaining.
# one course can have multiple prerequisite courses.
import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # It is actually another map. <course_id, num>. num is the number of pre_courses needed for course_id
        inDegrees = [0] * numCourses
        # map<course_id, list[course_id]> pre_course -> courses can take after taking the pre_course
        outMap = collections.defaultdict(list)

        for course, pre_course in prerequisites:
            outMap[pre_course].append(course)
            inDegrees[course] += 1

        takable = []
        for course_id in range(len(inDegrees)):
            if inDegrees[course_id] == 0:
                takable.append(course_id)

        while takable:
            course_taken = takable.pop()
            if course_taken in outMap:
                for out_course in outMap[course_taken]:
                    inDegrees[out_course] -= 1
                    if inDegrees[out_course] == 0:
                        takable.append(out_course)
                outMap.pop(course_taken)

        return len(outMap) == 0
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         # It is actually another map. <course_id, num>. num is the number of pre_courses needed for course_id
#         inDegrees = [0] * numCourses
#         # map<course_id, list[course_id]> pre_course -> courses can take after taking the pre_course
#         outMap = {}
#
#         for p in prerequisites:
#             if p[1] in outMap:
#                 outMap[p[1]].append(p[0])
#             else:
#                 outMap[p[1]] = [p[0]]  # wrong: list(p[0])
#
#             inDegrees[p[0]] += 1
#
#         takable = []
#         for i in range(len(inDegrees)):
#             if inDegrees[i] == 0:
#                 takable.append(i)
#
#         while takable:
#             course = takable.pop()
#             if course in outMap:
#                 for out_course in outMap[course]:
#                     inDegrees[out_course] -= 1
#                     if inDegrees[out_course] == 0:
#                         takable.append(out_course)
#                 outMap.pop(course)
#
#         return len(outMap) == 0

# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         outmap = {}
#         pre_course_num = [0] * numCourses

#         for p in prerequisites:
#             if p[1] not in outmap:
#                 outmap[p[1]] = [p[0]] #list(p[0])
#             else:
#                 outmap[p[1]].append(p[0])

#         for key,val in outmap.items():
#             for course_id in val:
#                 pre_course_num[course_id] += 1

#         takable = []
#         for i in range(len(pre_course_num)):
#             if pre_course_num[i] == 0:
#                 takable.append(i)

#         count = 0
#         while takable:
#             takable_course = takable.pop()
#             count+=1
#             if takable_course in outmap:
#                 for course in outmap[takable_course]:
#                     pre_course_num[course] -= 1
#                     if pre_course_num[course] == 0:
#                         takable.append(course)

#         return True if count==numCourses else False







