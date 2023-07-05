# Note that the input arr is already sorted

# Binary search
# O(logN)
#
# If there are m numbers not missing,
#   -> They must be A[0], A[1] .. A[m-1],
# the number of missing under A[m] is A[m] - 1 - m.
# If A[m] - 1 - m < k, m is too small, we update left = m + 1
# If A[m] - 1 - m >= k, m is big enough, we update right = m - 1.
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            pivot = (left + right) // 2
            # If number of positive integers
            # which are missing before arr[pivot]
            # is less than k -->
            # continue to search on the right.
            if arr[pivot] - pivot - 1 < k:
                left = pivot + 1
            # Otherwise, go left.
            else:
                right = pivot - 1

        # At the end of the loop, left = right + 1,
        # and the kth missing is in-between arr[right] and arr[left].
        # The number of integers missing before arr[right] is
        # arr[right] - right - 1 -->
        # the number to return is
        # arr[right] + [k - (arr[right] - right - 1)] = k + left

        # my explanation:
        # arr[right] is now the closest arr[m] that has num of missing integers less than k
        # there are right+1 integers before arr[right] not missing.
        # so the kth-missing integer needs to be right + 1 integers after k
        #   -> res = k + right + 1 = k + left
        return k + right + 1
