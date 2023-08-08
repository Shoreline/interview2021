# 3 soltuions:
# 1) Sort the array: time nlog(n), space o(1)
# 2) Heap of size k: time nlog(k), space o(k)
# 3) Quick select: time o(n^2), but avg o(n), space o(1)
# 4) counting sort (bucket sort): time O(n+m), space O(m). m = max_val - min_val

# The k-th largest -> nums[k-1] element after sorting in descending order
class Solution_sort:
    def findKthLargest(self, nums, k):
        nums.sort(reverse=True)
        return nums[k - 1]


class Solution_min_heap:
    def findKthLargest(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]


class Solution_quick_select:
    def findKthLargest(self, nums, k):
        def quick_select(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []

            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)

            # kth element in left
            if k <= len(left):
                return quick_select(left, k)

            # kth element in right
            if len(left) + len(mid) < k:
                return quick_select(right, k - len(left) - len(mid))

            # kth element in mid (all = pivot)
            return pivot

        return quick_select(nums, k)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_value = min(nums)
        max_value = max(nums)
        count = [0] * (max_value - min_value + 1)

        for num in nums:
            count[num - min_value] += 1

        remain = k
        for i in range(len(count) - 1, -1, -1):
            remain -= count[i]
            if remain <= 0:
                return min_value + i

        return -1


class Solution_quick_select_2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return float('inf')
        left, right = 0, len(nums) - 1
        while left <= right:
            p = self.partition(nums, left, right)
            if p == k - 1:
                return nums[p]
            elif p < k - 1:
                left = p + 1
            else:
                right = p - 1
        return float('inf')

    # Randomly pick an element ("pivot") within start and end
    # Move elements samller than pivot's value to the right
    # Return the pivot's index.
    # This way, the pivot is in its final sorted position
    def partition(self, nums: List[int], start: int, end: int) -> int:
        # For simplicity just always pick the nums[end] as pivot
        # If use random() function, swap nums[p] with nums[end] to start.
        p = random.randint(start, end)
        # can't just use tmp = nums[p]. We want the pivot is in its final sorted position.

        nums[p], nums[end] = nums[end], nums[p]
        left, right = start, end - 1
        while left <= right:
            if nums[left] > nums[end]:
                left += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1

        nums[end], nums[left] = nums[left], nums[end]
        return left

    # Change find kth largest to find len(nums) + 1- k th smallest
#
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         if len(nums) < k:
#             return -sys.maxsize
#         k = len(nums) + 1 - k
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             p = self.partition(nums, left, right)
#             if p == k - 1:
#                 return nums[p]
#             elif p < k - 1:
#                 left = p + 1
#             else:
#                 right = p - 1
#         return -sys.maxsize

#     # Randomly pick an element ("pivot") within start and end
#     # Move elements smaller than pivot's value to the left
#     # Return the pivot's index.
#     # This way, the pivot is in its final sorted position
#     def partition(self, nums: List[int], start: int, end: int) -> int:
#         # For simplicity just always pick the nums[end] as pivot
#         # If use random() function, swap nums[p] with nums[end] to start.
#         p = random.randint(start, end)
#         # can't just use tmp = nums[p]. We want the pivot is in its final sorted position.

#         nums[p], nums[end] = nums[end], nums[p]
#         left, right = start, end - 1
#         while left <= right:
#             if nums[left] > nums[end]:
#                 nums[left], nums[right] = nums[right], nums[left]
#                 right -=1
#             else:
#                 left +=1

#         nums[end], nums[left] = nums[left], nums[end]
#         return left

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         if len(nums) < k:
#             return -sys.maxsize
#         k = len(nums) + 1 - k
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             p = self.partition(nums, left, right)
#             if p == k - 1:
#                 return nums[p]
#             elif p < k - 1:
#                 left = p + 1
#             else:
#                 right = p - 1
#         return -sys.maxsize

#     # Randomly pick an element within start and end, moving elements smaller than it to the left, and return the index of pivot
#     def partition(self, nums: List[int], start: int, end: int) -> int:
#         # For simplicity just always pick the nums[end] as pivot
#         # If use random() function, swap nums[p] with nums[end] to start.
#         p = end
#         left, right = start, end - 1
#         while left <= right:
#             if nums[left] > nums[p]:
#                 nums[left], nums[right] = nums[right], nums[left]
#                 right -=1
#             else:
#                 left +=1

#         nums[p], nums[left] = nums[left], nums[p]
#         return left



