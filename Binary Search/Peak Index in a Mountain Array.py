# PS: arr is guaranteed to be a mountain array.
# You must solve it in O(log(arr.length)) time complexity


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        A = arr
        l, r = 0, len(A) - 1
        while l < r:
            m = (l + r) // 2
            if A[m] < A[m + 1]:  # A[m] to A[m+1] is ascending trend, peak can only be A[m+1] or after A[m+1]
                l = m + 1
            else:  # # A[m] to A[m+1] is descending trend, peak can only be A[m] or before A[m]
                r = m
        return l
