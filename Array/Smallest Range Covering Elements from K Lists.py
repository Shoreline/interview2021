# Each individual list in nums is sorted, and not empty

# Time complexity : O(n∗log(m)). Heapification of m elements requires O(log(m)) time. This step could be done
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = []
        right = nums[0][0]
        for i, num_list in enumerate(nums):
            heapq.heappush(pq, (num_list[0], i, 0))
            right = max(right, nums[i][0])

        # initial range is [min, max] of the first elements of each list in nums
        # Note that this is not the [min, max] of all elements in nums, which is unnecssary.
        res = pq[0][0], right

        # Keep shrinking the result range.
        # left: the min val in heap
        # right: the max val in heap
        while pq:
            # since each list is already sorted
            # the heap gives the next smallest value from all lists
            left, i, j = heapq.heappop(pq)
            if right - left < res[1] - res[0]:
                res = left, right

            # if any list in nums has ended, return
            # the list
            if j + 1 == len(nums[i]):
                return res

            # push the next element of that list into heap    
            v = nums[i][j + 1]
            right = max(right, v)
            heapq.heappush(pq, (v, i, j + 1))

        return res
