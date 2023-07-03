# Your goal is to obtain k ribbons of all the same positive integer length.
# You are allowed to throw away any excess ribbon as a result of cutting.

# The crux of the problem is implementing Binary Search. The goal is to figure out what the maximum length of a 
# ribbon could be so that we get k ribbons of that max length. One way to think of it would be that the ribbon length
# could be anywhere from 1 to the max length of the a ribbon available in the list.

# So what we do is go through the list (using Binary Search since we need to optimize linear search), find the mid of
# the given array and then iterate through the list testing the length with each element and summing the number of
# ribbons that can be made with the mid value. Then change mid accordingly
class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        # The minimum length of the cut ribbons is 1
        low = 1
        # The maximum possible length of the cut ribbons is the longest raw ribbon
        high = max(ribbons)

        # In this binary search, we are trying to go through the origin list and figure out which integer(from 1 ->
        # ribbon of max length) is the desired length for the target k pieces
        while low <= high:
            mid = low + (high - low) // 2
            num_cut_ribbons = 0
            for i in ribbons:   # count how many ribbons of length mid can we get
                num_cut_ribbons += i // mid

            # If the value is >= target, we know that there could be a larger integer that will satisfy the same
            # condition
            if num_cut_ribbons >= k:
                low = mid + 1
            else:
                # If lesser than k, then there could be a value lesser than the mid that could satisfy the condition
                high = mid - 1
        return high
