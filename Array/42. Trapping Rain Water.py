# Two pointers
# - For any two columns, height[left] and height[right]. Assuming height[left] <= height[right]
# - Then for any i in [left, right], we can save max(0, height[left] - height[i]) amount of water.
# - if height[i] > height[left], let height[i] to be the new height[left]
# T O(n); S O(1)
class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) == 0:
            return 0

        res = 0
        left, right = 0, len(height) - 1

        while left < right:
            cur_wall_height = min(height[left], height[right])
            if height[left] < height[right]:
                while left < right and height[left] <= cur_wall_height:
                    res += cur_wall_height - height[left]
                    left += 1
            else:
                while right > left and height[right] <= cur_wall_height:
                    res += cur_wall_height - height[right]
                    right -= 1

        return res

