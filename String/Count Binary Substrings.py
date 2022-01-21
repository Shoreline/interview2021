# The qualified sub-strings can only be the sub-strings of sub-strings that already group together AND have equal number of 0s and 1s in the input string.
# First, count the number of 1 or 0 already group together in the input string.
# For example "0110001111" will be [1, 2, 3, 4].

# Second, for any possible substrings with 1 and 0 grouped consecutively, the number of valid substring will be the minimum number of 0 and 1.
# For example "0001111", will be min(3, 4) = 3, ("01", "0011", "000111")


# Complexity
# Time O(N)
# Space O(1)
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        pre_count, cur_count = 0, 0
        result = 0

        for i, c in enumerate(s):
            cur_count += 1

            if i == len(s) - 1 or s[i + 1] != c:
                group_size = min(pre_count, cur_count)
                result += group_size
                pre_count = cur_count
                cur_count = 0

        return result

# Time O(N)
# Space O(N)
# class Solution:
#     def countBinarySubstrings(self, s: str) -> int:
#         # separate 0 groups and 1 groups in the input string
#         s = s.replace("01","0 1").replace("10","1 0")


#         group_lengths=[]
#         for i in s.split():
#             group_lengths.append(len(i))

#         count = 0
#         for len1, len2 in zip(group_lengths, group_lengths[1:]):
#             count += min(len1, len2)
#         return count
