# a variant of prefix sum
# Idea: if for i < j and sum(nums[:i]) % k == sum(nums[:j]) % k, then sum(nums[i:j]) % k == 0 (vice versa)
# So we just need to use a dictionary to keep track of sum(nums[:i]) % k and the corresponding index i.
# Once some later sum(nums[:j]) % k == sum(nums[:i]) % k and j - i > 1, we return True.


# if prefix_sum_j % k == prefix_sum_i % k, and i < j then sum(nums[i:j]) % k == 0 -> shall return True
# If sum(nums[:j]) % k == sum(nums[:i]) % k, and i < j, then sum(nums[i:j]) % k == 0 -> shall return True
# So we just need to have a map to track the remainers

# Time complexity: O(n), space complexity: O(min(k, n)) if k != 0, else O(n).
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return len(nums) >= 2
        # <prefix_sum % k, first_shown_index>
        # 0:-1: to catch sum[nums[:i]] % k == 0
        remainder_to_index = {0:-1}
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            remainder = prefix_sum % k

            if remainder not in remainder_to_index:
                remainder_to_index[remainder] = i
            elif i - remainder_to_index[remainder] >= 2:
                 # need >=2 since the problem says subarray must have at least 2 elements
                return True
        return False


    # class Solution:
#     def checkSubarraySum(self, nums: List[int], k: int) -> bool:
#         dic = {0:-1} # <prefix_sum % k, index> (not index to prefix_sum!)
#         summ = 0
#         for i in range(len(nums)):
#             if k != 0:
#                 summ = (summ + nums[i]) % k
#             else:
#                 summ += nums[i] # can't divide zero. just adding up nums[i] works

#             if summ not in dic:
#                 dic[summ] = i
#             else:
#                 if i - dic[summ] >= 2: # need >=2 since the problem says subarray must have at least 2 elements
#                     return True
#         return False
