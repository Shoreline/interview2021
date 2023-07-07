# PS: input array is already sorted!
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]

# Binary Search To Find The Left Bound
# O(log(N−k)+k)
# At most one of A[mid] and A[mid + k] can be in the res list -> there are k+1 array items between them (inclusively)
# if A[mid + k] is closer to x than A[mid] -> A[mid] can't be the left bound (inclusively)
# if A[mid] is closer or at the same distance to x than A[mid + k]
#   -> A[mid + k] can't in the res list
#   -> left bound is at mid or even more left -> right = mid
#
# use x - A[mid] > A[mid + k] - x instead of abs
# if x is on the left of both A[mid] & A[mid+k] -> x - A[mid] is negative, while A[mid + k] - x  is positive -> correct
# ...
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        A = arr
        left = 0
        right = len(A) - k  # not len(A) - 1!
        while left < right:
            mid = (left + right) // 2

            # if abs(x - A[mid]) > abs(A[mid + k] - x): # wrong!
            # The corner case that breaks abs(x - arr[mid]) > abs(arr[mid + k] - x) is when arr[mid] to arr[mid + k] are all the same and the numbers are smaller than x
            if x - A[mid] > A[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return A[left:left + k]

    # Binary search + sliding window


# O(log(N)+k)
class Solution2:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Base case
        if len(arr) == k:
            return arr

        # Find the closest element and initialize two pointers
        left = bisect_left(arr, x) - 1
        right = left + 1

        # While the window size is less than k
        while right - left - 1 < k:
            # Be careful to not go out of bounds
            if left == -1:
                right += 1
                continue

            # Expand the window towards the side with the closer number
            # Be careful to not go out of bounds with the pointers
            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1

        # Return the window
        return arr[left + 1:right]


