class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        k = len(nums1) - 1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # It's possible that some elements in nums2 haven't got moved to nums1.
        if j >= 0:
            nums1[:j + 1] = nums2[:j + 1]
            # while j >=0:
        #     nums1[k] = nums2[j]
        #     k -= 1
        #     j -= 1

        return

