# The output is a list saving the maximum value within each sliding window

# DP of another type
# Use two additional helper arrays to save supporting info
# Divide nums[] into blocks of length k. So it is guaranteed that a sliding window
# can be either in one block or 2 adjacent blocks.
# The helper arrays saves 1) the max of the right block (left[j]); 2) the max from the left block (right[i])
# So maximum between nums[i] - nums[j] will be max(left[i], right[j])

# Note that the last block may have less than k elements
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # left: the maximum value so far in a block (starting from left)
        # right: the maximum vlaue so far in a block (starting from right)
        left, right = [0] * len(nums), [0] * len(nums)
        rem = len(nums) % k

        for i in range(len(nums)):
            if i % k == 0:  # the first element in this block
                left[i] = nums[i]
            else:
                left[i] = max(nums[i], left[i - 1])

            j = len(nums) - 1 - i
            # j == len(nums) - 1: corner case: the last special block
            # if j == len(nums) - 1 or (j + 1) % k == 0:
            if i == 0 or (i - rem) % k == 0:
                right[j] = nums[j]
            else:
                right[j] = max(nums[j], right[j + 1])

        res = []
        i = 0
        while i + k - 1 < len(nums):  # the window length is k, so i + k - 1 is the last element in the window
            j = i + k - 1
            res.append(max(right[i], left[j]))  # right[i], not left[i]!
            i += 1

        # res will have size len(nums) - (k-1)
        # res = [0] * (len(nums) - k+1) #
        # for i in range(len(res)):
        #     j = i + k - 1 # The size of sliding window is k, so the index of the end of window is i + k-1
        #     res[i] = max(right[i], left[j])

        return res


