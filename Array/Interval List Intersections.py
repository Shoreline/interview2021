# Two pointers
# one for first_list, one for second_list
#
# overlapping condition: either interval's start is between another interval's [start, end]
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = []

        while i < len(firstList) and j < len(secondList):
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]

            # if b_start <= a_end and a_start <= b_end:
            if a_start <= b_start <= a_end or b_start <= a_start <= b_end:
                res.append([max(a_start, b_start), min(a_end, b_end)])

            if a_end <= b_end:  # exhausted a's range. Go to next a
                i += 1
            else:
                j += 1

        return res
