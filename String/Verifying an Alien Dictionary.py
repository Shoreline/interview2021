# lexicographically: 按字典顺序排列
# If sorted -> if each pair of neighboring items are sorted.
#   Checking if sorted takes O(M) M is the total # of chars, costs less than sort the entire list.
# compare each pair of neighboring words, see if all of them are sorted lexicographically
# copied
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for index, val in enumerate(order):
            order_map[val] = index  # index is the ranking.

        # Compare first j chars between each two adjacent words. j is the length of the first word.
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                # ex. "apple" shall not come before "app"
                if j >= len(words[i + 1]):
                    return False

                if words[i][j] != words[i + 1][j]:
                    if order_map[words[i][j]] > order_map[words[i + 1][j]]:
                        return False
                    # Only check the first different char.
                    # For the remaining chars in word2, no need to examine.
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

