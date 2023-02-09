# Use an output stack to keep track of only non-duplicate characters.
# T: O(N); S:O(N-D): D is the total length of all duplicates. Worst case O(N)
class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []
        for c in s:
            if res and res[-1] == c:  # found a duplicate
                res.pop()  # skip c, and also pop stack[-1]
            else:
                res.append(c)
        return ''.join(res)
