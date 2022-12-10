# Pick tuple elements from 4 arrays (one from each), not just from one array!
# Note: unlike the 4sum problem where we need to avoid duplicated elements, we don't have such need here. Because a
# result tuple is made of 4 indices, which will never be the same

# T/S: O(2*n^2) -> O(n^2)
# Count the frequency of all a + b values from nums1 and nums2;
# For all c + d from nums3 and nums4, see how many count do we have for -(c+d)
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        m = collections.defaultdict(int)

        for a in nums1:
            for b in nums2:
                m[a + b] += 1

        for c in nums3:
            for d in nums4:
                count += m[-(c + d)] # if -(c+d) does not exist in m, m[-(c+d)] = 0
        return count

# Generalized solution for k-Sum II issues Divide k arrays into two groups. For the first group, we will have k/2
# nested loops to count sums. Another k/2 nested loops will enumerate arrays in the second group and search for
# complements (target, which is 0 in this problem).

# class Solution:
#     def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
#         m = collections.defaultdict(int)

#         def nSumCount(lists: List[List[int]]) -> int:
#             addToHash(lists, 0, 0)  # Count sum for the first k//2 lists
#             return countComplements(lists, len(lists) // 2, 0)  # Search for target in the rest k - k//2 lists

#         def addToHash(lists: List[List[int]], i: int, sum: int) -> None:
#             if i == len(lists) // 2:  # stop condition. Don't do anything for i == k//2, but update the sum
#                 m[sum] += 1
#             else:
#                 for a in lists[i]:
#                     addToHash(lists, i + 1, sum + a)

#         def countComplements(lists: List[List[int]], i: int, target: int) -> int:
#             if i == len(lists):
#                 return m[target]
#             count = 0
#             for a in lists[i]:
#                 count += countComplements(lists, i + 1, target - a)
#             return count

#         return nSumCount([nums1, nums2, nums3, nums4])