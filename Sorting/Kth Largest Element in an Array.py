# 3 soltuions:
# 1) Sort the array: time nlog(n), space o(1)
# 2) Heap of size k: time nlog(k), space o(k)
# 3) Quick select: time o(n^2), but avg o(n), space o(1)

# The k-th largest -> nums[k-1] element after sorting in descending order
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def divide(left, right):
            p = random.randint(left, right)
            nums[right], nums[p] = nums[p], nums[right]

            pos = left
            for i in range(left, right):
                if nums[i] < nums[right]:
                    nums[pos], nums[i] = nums[i], nums[pos]
                    pos += 1
            nums[pos], nums[right] = nums[right], nums[pos] # easy to forget
            return pos

        K = len(nums) - k # K is the index of the sorted(nums)
        left, right = 0, len(nums) - 1
        while left <= right:
            p = divide(left, right)
            if p == K:
                return nums[p]
            elif p < K:
                left = p + 1
            else:
                right = p - 1

        # TLE if use below function!
        # def merge(left, right):
        #     if left > right:
        #         return
        #
        #     mid = divide(left, right)
        #     if mid == K:
        #         return
        #     elif mid < K:
        #         merge(left + 1, right)
        #     else:
        #         merge(left, right - 1)

        return float('inf')

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         if len(nums) < k:
#             return float('inf')
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             p = self.partition(nums, left, right)
#             if p == k - 1:
#                 return nums[p]
#             elif p < k - 1:
#                 left = p + 1
#             else:
#                 right = p - 1
#         return float('inf')
#
#     # Randomly pick an element ("pivot") within start and end
#     # Move elements smaller than pivot's value to the right
#     # Return the pivot's index.
#     # This way, the pivot is in its final sorted position
#     def partition(self, nums: List[int], start: int, end: int) -> int:
#         # For simplicity just always pick the nums[end] as pivot
#         # If use random() function, swap nums[p] with nums[end] to start.
#         p = random.randint(start, end)
#         # can't just use tmp = nums[p]. We want the pivot is in its final sorted position.
#
#         nums[p], nums[end] = nums[end], nums[p]
#         left, right = start, end - 1
#         while left <= right:
#             if nums[left] > nums[end]:
#                 left += 1
#             else:
#                 nums[left], nums[right] = nums[right], nums[left]
#                 right -= 1
#
#         nums[end], nums[left] = nums[left], nums[end]
#         return left

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



