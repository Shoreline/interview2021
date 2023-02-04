# Time: O(N*K): N is the length of strs; K is the longest string in strs
# Space: O(N*K)
# Build a <tuple, list[string]> map. Key is a tuple made up of counting of letters. Ex: (1, 2, 0,...0) represents "abb"
#   Value is each anagram having that counting of letters.
#   can't use a list as the key, since list is unhashable.
# Note: use tuple(a_list) to make a tuple, so it can be used as map key
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_count_map = collections.defaultdict(list)
        for str in strs:
            char_count = [0] * 26
            for c in str:
                char_count[ord(c) - ord('a')] += 1

            char_count_map[tuple(char_count)].append(str)
        return list(char_count_map.values())

# class Solution:
#     def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
#         ans = collections.defaultdict(list)
#         for s in strs:
#             count = [0] * 26
#
#             for c in s:
#                 count[ord(c) - ord('a')] += 1
#
#             ans[tuple(count)].append(s)  # ans[count].append(s) will fail. count, as a list, is unhashable.
#
#         return ans.values()
