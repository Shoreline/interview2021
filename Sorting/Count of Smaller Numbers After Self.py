# A variant of merge sort
#   - For each element i, use the merge_sort(i) function to return the number of elements jumping from i's right to i's left during the merge sort.
#   -
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # keeps tracking the value and index. Can't use map since same value can happen multiple times
        arr = [[val, i] for i, val in enumerate(nums)]
        result = [0] * n

        # Typical merge_sort function
        # Note that the index range to sort is [left, right - 1]
        def merge_sort(arr, left, right):
            # merge sort [left, right) from small to large, in place
            if right - left <= 1:
                return
            mid = (left + right) // 2
            merge_sort(arr, left, mid)
            merge_sort(arr, mid, right)
            merge(arr, left, right, mid)

        # merge [left, mid) and [mid, right)
        def merge(arr, left, right, mid):
            i = left  # current index for the (already sorted) left array
            j = mid  # current index for the (already sorted) right array

            # use temp to temporarily store sorted array of arr.
            # tmp has same structure as arr: [ [a,b], [c,d], ...]
            temp = []

            while i < mid and j < right:
                # arr[x][0] is a value, arr[x][1] is that value's original index in the inital array
                if arr[i][0] <= arr[j][0]:  # equivalent to arr[i][0] > arr[k][0] while mid <= k < j
                    temp.append(arr[i])
                    # j - mid numbers will jump to the left side of arr[i]
                    result[arr[i][1]] += j - mid
                    i += 1  # done with arr[i]
                else:
                    temp.append(arr[j])
                    j += 1

            # when one of the subarrays is empty
            while i < mid:
                result[arr[i][1]] += j - mid
                temp.append(arr[i])
                i += 1
            while j < right:
                temp.append(arr[j])
                j += 1

            # Copy the sorted temp to its conrresponding range of arr
            for i in range(len(temp)):
                arr[left + i] = temp[i]

        merge_sort(arr, 0, n)

        return result

# # Binary indexed tree
# # https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/tutorial/
# # impossible to solve it unless you already know this data structure
# class Solution:
#     def countSmaller(self, nums: List[int]) -> List[int]:
#         # Can't use nums.sort(), we want to keep the original sequence of nums
#         # The smallest number will be rank 1, the second smallest will be rank 2.
#         # If there are duplicated smallest numbers, the rank will be 2, and the 2nd smallest will be 3
#         rank = {val: i + 1 for i, val in enumerate(sorted(nums))}

#         N = len(nums)
#         res = []
#         BITree = [0] * (N + 1)

#         def update(i):
#             while i <= N:
#                 BITree[i] += 1
#                 i += (i & -i) # (i & -i) gives the last set bit in a number i

#         def getSum(i):
#             s = 0
#             while i:
#                 s += BITree[i]
#                 i -= (i & -i)
#             return s

#         for x in reversed(nums):
#             res += getSum(rank[x] - 1),
#             update(rank[x])
#         return res[::-1]