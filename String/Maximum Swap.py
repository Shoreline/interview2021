# Iterate through num.
#   For each digit num[i], if there exist a digit d (d must in num) that d > num[i], and d shows after nums[i], then
#   swap them.
#   If there are multiple d after nums[i], only swap with the last one.
#   Once a swap is done, we have finished.
class Solution:
    def maximumSwap(self, num: int) -> int:
        # a = list(map(int, str(num)))
        nums = [int(c) for c in str(num)]  # convert num into a list of digits
        last = {x: i for i, x in enumerate(nums)}  # a map of <digit, last_shown_index>
        for i in range(len(nums)):
            for d in range(9, nums[i], -1):  # check all digits > nums[i]
                if d in last and last[d] > i:  # if there is a larger digit AFTER nums[i], we can stop and return
                    nums[last[d]], nums[i] = nums[i], nums[last[d]]  # swap that digit with nums[i]
                    return int(''.join([str(n) for n in nums]))
        return num

# Wrong for 10909091
# class Solution_wrong:
#     def maximumSwap(self, num: int) -> int:
#         num_str = list(str(num))
#         first_idx = -1 # first index that num[i] < num[i+1], if there are consecutive nums[i] of this value, use the first one
#         max_next = -1 # biggest nums[i] after first index, if there are consecutive nums[i] of this value, use the last one
#         for i in range(len(num_str)):
#             if first_idx < 0 and i > 0 and num_str[i - 1] < num_str[i]:
#                 k = i - 1
#                 while k > 0 and num_str[k] == num_str[k-1]:
#                     k -= 1
#                 first_idx = k
#             if first_idx >= 0 and i > first_idx:
#                 if max_next == -1 or num_str[max_next] <= num_str[i]:
#                     max_next = i

#         num_str[first_idx], num_str[max_next] = num_str[max_next], num_str[first_idx]
#         return int(''.join(num_str))