# Items are unique!
# Not the same algo as looking for a specific value in rotated ordered array.
# If nums[i] is the smallest element in a rotated sorted array,
# Then   nums[i-1] > nums[i] -> to find nums[i] meaning to find somewhere nums[i-1] > nums[i]
# -> to find the non-sorted part

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2

            if mid > 0 and nums[mid] < nums[mid - 1]:  # early return, optional
                return nums[mid]

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]

    # class Solution:
#     def findMin(self, nums: List[int]) -> int:

#         low, high = 0, len(nums) - 1
#         if nums[low] <= nums[high]:
#             return nums[low]

#         while low <= high:
#             mid = low + (high - low) // 2

#             if nums[mid - 1] > nums[mid]:
#                 return nums[mid]
#             elif nums[mid] > nums[mid + 1]:
#                 return nums[mid + 1]


#             if nums[mid] > nums[0]: # left part is sorted, so right part is non-sorted
#                 low = mid + 1
#             else:
#                 high = mid - 1

# class Solution:
#     def findMin(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         # set left and right bounds
#         left, right = 0, len(nums)-1

#         # left and right both converge to the minimum index;
#         # DO NOT use left <= right because that would loop forever
#         while left < right:
#             # find the middle value between the left and right bounds (their average);
# 			# can equivalently do: mid = left + (right - left) // 2,
# 			# if we are concerned left + right would cause overflow (which would occur
# 			# if we are searching a massive array using a language like Java or C that has
# 			# fixed size integer types)
#             mid = (left + right) // 2

#             # the main idea for our checks is to converge the left and right bounds on the start
#             # of the pivot, and never disqualify the index for a possible minimum value.

#             # in normal binary search, we have a target to match exactly,
#             # and would have a specific branch for if nums[mid] == target.
#             # we do not have a specific target here, so we just have simple if/else.

#             if nums[mid] > nums[right]:
#                 # we KNOW the pivot must be to the right of the middle:
#                 # if nums[mid] > nums[right], we KNOW that the
#                 # pivot/minimum value must have occurred somewhere to the right
#                 # of mid, which is why the values wrapped around and became smaller.

#                 # example:  [3,4,5,6,7,8,9,1,2]
#                 # in the first iteration, when we start with mid index = 4, right index = 9.
#                 # if nums[mid] > nums[right], we know that at some point to the right of mid,
#                 # the pivot must have occurred, which is why the values wrapped around
#                 # so that nums[right] is less then nums[mid]

#                 # we know that the number at mid is greater than at least
#                 # one number to the right, so we can use mid + 1 and
#                 # never consider mid again; we know there is at least
#                 # one value smaller than it on the right
#                 left = mid + 1

#             else:
#                 # here, nums[mid] <= nums[right]:
#                 # we KNOW the pivot must be at mid or to the left of mid:
#                 # if nums[mid] <= nums[right], we KNOW that the pivot was not encountered
#                 # to the right of middle, because that means the values would wrap around
#                 # and become smaller (which is caught in the above if statement).
#                 # this leaves the possible pivot point to be at index <= mid.

#                 # example: [8,9,1,2,3,4,5,6,7]
#                 # in the first iteration, when we start with mid index = 4, right index = 9.
#                 # if nums[mid] <= nums[right], we know the numbers continued increasing to
#                 # the right of mid, so they never reached the pivot and wrapped around.
#                 # therefore, we know the pivot must be at index <= mid.

#                 # we know that nums[mid] <= nums[right].
#                 # therefore, we know it is possible for the mid index to store a smaller
#                 # value than at least one other index in the list (at right), so we do
#                 # not discard it by doing right = mid - 1. it still might have the minimum value.
#                 right = mid

#         # at this point, left and right converge to a single index (for minimum value) since
#         # our if/else forces the bounds of left/right to shrink each iteration:

#         # when left bound increases, it does not disqualify a value
#         # that could be smaller than something else (we know nums[mid] > nums[right],
#         # so nums[right] wins and we ignore mid and everything to the left of mid).

#         # when right bound decreases, it also does not disqualify a
#         # value that could be smaller than something else (we know nums[mid] <= nums[right],
#         # so nums[mid] wins and we keep it for now).

#         # so we shrink the left/right bounds to one value,
#         # without ever disqualifying a possible minimum
#         return nums[left]
