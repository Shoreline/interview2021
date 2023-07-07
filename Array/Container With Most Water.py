# Two approaching pointers
# Keep moving the shorter wall closer to the other wall
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # i and j are indices of the two pointers
        i, j = 0, len(height) - 1
        res = 0

        while i < j:
            res = max(res, min(height[i], height[j]) * (j - i))
            # move the side with less height
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res
