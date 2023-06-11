# You are given two strings order and s. All the characters of order are unique and were sorted in some custom order
# previously.

# Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x
# occurs before a character y in order, then x should occur before y in the permuted string.

# Return any permutation of s that satisfies this property.
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)

        res = []
        for c in order:  # check the characters in 'order' sequentially
            if c in counter:    # if this character exist in the input string 's', add to res by order.
                res.extend([c] * counter[c])
                counter.pop(c)

        for c in counter:
            res.extend([c] * counter[c])

        return ''.join(res)
