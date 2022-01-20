# Instead of finding all possible substrings and count unique characters in every and each one of them,
# we can count for every char in S, how many ways to be found as a unique char, and sum up the result for each char.
#
# One pass, time complexity O(N).
# Space complexity O(1).
#
# Let's think about how a character can be found as a unique character.

# Think about string "XAXAXXAX" and focus on making the second "A" a unique character.
# We can take "XA(XAXX)AX" and between "()" is our substring.
# We can see here, to make the second "A" counted as a uniq character, we need to:

# insert "(" somewhere between the first and second A
# insert ")" somewhere between the second and third A
# For step 1 we have "A(XA" and "AX(A", 2 possibility.
# For step 2 we have "A)XXA", "AX)XA" and "AXX)A", 3 possibilities.

# So there are in total 2 * 3 = 6 ways to make the second A a unique character in a substring.
# In other words, there are only 6 substring, in which this A contribute 1 point as unique string.

# Instead of counting all unique characters and struggling with all possible substrings,
# we can count for every char in S, how many ways to be found as a unique char.
# We count and sum, and it will be out answer.


# Explanation
# index[26][2] record last two occurrence index for every upper characters.
# Initialise all values in index to -1.
# Loop on string S, for every character c, update its last two occurrence index to index[c].
# Count during looping. For example, if "A" appears twice at index 3, 6, 9 seperately, we need to count:
# For the first A: (3 - (-1)) * (-1 - (-1)) = 0
# For the 2nd "A": (6-3) * (3-(-1))"
# For the 3rd "A": (9-6) * (6-3)"
# For the 4th "A": (N-9) * (9-6)"

# Don't forget at the end, len(s) can be considered as an occurrence of all chars

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # Record last two occurrence index for every character in s
        index = {c: [-1, -1] for c in s}

        res = 0

        for i, c in enumerate(s):
            m, n = index[c]
            res += (i - n) * (n - m)
            index[c] = [n, i]

        for c in index:
            k, j = index[c]
            m, n = index[c]
            res += (len(s) - n) * (n - m)

        return res  # % (10**9 + 7) to avoid overflow