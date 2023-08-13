# You are given two strings order and s. All the characters of order are unique and were sorted in some custom order
# previously.

# Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x
# occurs before a character y in order, then x should occur before y in the permuted string.

# Return any permutation of s that satisfies this property.
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Since characters in s are not necessarily unique
        # To build the res string, we count the occurences of each char in s
        counter = Counter(s)

        res = []
        for c in order:  # Check each char in 'order' orderly
            if c in counter:
                # res.extend([c] * counter[c]) # add char c to res by its frequency in s
                res += [c] * counter[c]
                counter.pop(c)  # since there will be other handling for chars in 's' but not in 'order'

        # Add the chars not mentioned in 'order'
        for c in counter:
            # res.extend([c] * counter[c])
            res += [c] * counter[c]

        return ''.join(res)
