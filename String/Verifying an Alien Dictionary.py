# lexicographically: 按字典顺序排列
# If sorted -> if each pair of neighboring items are sorted.
#   Checking if sorted takes O(M) M is the total # of chars, costs less than sort the entire list.
# compare each pair of neighboring words, see if all of them are sorted lexicographically
# copied
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {} # <char, rank> map
        for index, val in enumerate(order):
            order_map[val] = index # index is the ranking.

        # Compare first j chars between each two adjacent words. j is the length of the first word.
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                word1 = words[i]  # word1 is sorted to be ahead of word2
                word2 = words[i + 1]
                # ex. "apple" shall not come before "app"
                if j >= len(word2):
                    return False

                if word1[j] != word2[j]:
                    if order_map[word1[j]] > order_map[word2[j]]:
                        return False
                    # Only check the first different char. For the remaining different chars, it's perfectly fine if
                    # word1 and word2 are not sorted base on them.
                    break

        return True
# O(NlogN) it's slower since this solution sort the whole list, more than what we actually need.
# class Solution:
#     def isAlienSorted(self, words: List[str], order: str) -> bool:
#         alien_dict = {}
#         for i, c in enumerate(order):
#             alien_dict[c] = chr(ord('a') + i)
#
#         return words == sorted(words, key=lambda x: ''.join([alien_dict[c] for c in x]))

