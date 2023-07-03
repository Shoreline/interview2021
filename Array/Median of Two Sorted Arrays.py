# two ways: 1) find the k-th element of two sorted array; 2) binary search
# Note that if the two arrays have in total an even number of elements, return the average of two middle numbers.
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        if (total_len % 2 == 1):
            return self.findKth(nums1, nums2, total_len // 2)
        else:
            return (self.findKth(nums1, nums2, total_len // 2 - 1) + self.findKth(nums1, nums2, total_len // 2)) / 2

    # !! this findKth() function is not a general findKth() function. It only works for this find median of two sorted arry problem.
    # findKth: k is the index element of the combined list
    def findKth(self, long: List[int], short: List[int], k: int) -> float:
        if len(long) < len(short):
            long, short = short, long  # temp = (long, short)

        # final cases
        if len(short) == 0:
            return long[k]
        if k == len(long) + len(short) - 1:  # if looking for the largest element of both lists
            return max(long[-1], short[-1])  # Problem statement says both arrays are already sorted

        i = len(short) // 2  # Let i be the middle index of the short list

        # How do we know j is non-negative?
        #
        # The first round is non-negative for sure
        # Since in this problem, the given k has limited possibilities.
        #   - k can only be total_len//2, or total_len//2 - 1.
        #   - len(short)//2 can never be bigger than total_len//2 - 1. (We won't reach here if both lists are empty)
        # For normal findKth problem, k can be any value from 0 to total_len - 1.
        j = k - i

        # For the first i elements in short and first j elements in long (i+j = k)
        # 1) if short[i]>long[j], then in the combined sorted array, their locations will be:
        #   ____,long[j], ___, short[i], ___
        #   The element we are looing for must be between them (middle area)
        #   And elements in long[:j] are surely <= long[j], so looking for i-th element of the combined short[:i], long[j:]
        # 2) if short[i]<long[j], then in the combined sorted array, their locations will be:
        #   ____,short[i], ___, long[j], ___
        # The element we are looing for must still be between them (the middle area)
        # Here I assume it is O(1) to get A[:i] and B[j:]. In python, it's not but in cpp it is.
        if short[i] > long[j]:  # in this case, the k-th element we are looking for must be < short[i]
            return self.findKth(short[:i], long[j:], i)  # former half of short, latter half of long
        else:
            return self.findKth(short[i:], long[:j], j)

        ### another solution
# def findMedianSortedArrays(self, A, B):
#     l = len(A) + len(B)
#     if l % 2 == 1:
#         return self.kth(A, B, l // 2)
#     else:
#         return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.

# def kth(self, a, b, k):
#     if not a:
#         return b[k]
#     if not b:
#         return a[k]
#     ia, ib = len(a) // 2 , len(b) // 2
#     ma, mb = a[ia], b[ib]

#     # when k is bigger than the sum of a and b's median indices
#     if ia + ib < k:
#         # if a's median is bigger than b's, b's first half doesn't include k
#         if ma > mb:
#             return self.kth(a, b[ib + 1:], k - ib - 1)
#         else:
#             return self.kth(a[ia + 1:], b, k - ia - 1)
#     # when k is smaller than the sum of a and b's indices
#     else:
#         # if a's median is bigger than b's, a's second half doesn't include k
#         if ma > mb:
#             return self.kth(a[:ia], b, k)
#         else:
#             return self.kth(a, b[:ib], k)