# Naive method takes O(n*k) time. But we can use partial sum method to only use O(n+2) time.
# For each update[i]: let the res[] to add inc since index start, and subtract inc since end+1
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0] * length
        for start, end, inc in updates:
            res[start] += inc

            if end + 1 < length:
                res[end + 1] -= inc

        cur_sum = 0
        for i in range(len(res)):
            cur_sum += res[i]
            res[i] = cur_sum

        return res