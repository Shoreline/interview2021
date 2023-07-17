# all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length
#   any two pairs nums[i] and nums[j] will always have either i<j or j < i
#   the condition simply means don't double count [nums[i], nums[j]] and [nums[j], nums[i]] as two pairs

# Binary search + sliding window
# Time: O(NlogW+NlogN), where N is the length of nums, and W = max(nums) - min(nums)

# Time Complexity: O(NlogW+NlogN), where N is the length of nums, and W is equal to nums[nums.length - 1] - nums[0].
# The logW factor comes from our binary search, and we do O(N) work inside our call to possible (or to calculate
# count in Java). The final O(NlogN) factor comes from sorting. Space Complexity: O(1). No additional space is used
# except for integer variables.
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # Returns the number pairs with distance <= input_distance in nums[]
        # sliding window
        # Note that here nums is already sorted
        # Time: O(N)
        def num_smaller_pairs(distance) -> bool:  # two pointers
            res, i, j = 0, 0, 0
            # Each iteration of while loop:
            #   how many elements in nums is bigger than this nums[i], and the diff <= distance
            while i < n:
                # diff is capped by distance
                # for a larger i, nums[i] is bigger, so no need to start j from i+1 again, instead
                # j can be at least as big as previous round.
                while j < n and nums[j] - nums[i] <= distance:
                    j += 1

                # j will be >= i, due to the inner while loop above
                res += j - i - 1
                i += 1

            return res

        nums.sort()
        n = len(nums)
        left, right = 0, nums[-1] - nums[0] # right is num_max - num_min
        while left < right:
            mid = left + (right - left) // 2
            count = num_smaller_pairs(mid)

            # Wrong!
            #   Even if count is already == k, it is possible to use a smaller dist that also leads to
            #   count(dist_smaller) == k
            # if count == k:
            #     return dist

            if count < k: # mid is too small. there is not enough pairs with distances smaller than mid
                left = mid + 1
            else:   # count >= k -> even count is already == k, it is possible to use a smaller dist.
                right = mid

        return left

from heapq import heappop, heappush
class Solution_heap:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        heap = [(nums[i + 1] - nums[i], i, i + 1) for i in range(n - 1)]
        heapify(heap)

        for _ in range(k):
            d, root, nei = heappop(heap)
            if nei + 1 < n:
                heappush(heap, (nums[nei + 1] - nums[root], root, nei + 1))

        return d