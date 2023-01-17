# Instead of finding all possible substrings and count unique characters in every and each one of them,
# we can count for every char in S, how many ways to be found as a unique char, and sum up the result for each char.
#
# One pass, time complexity O(N).
# Space complexity O(1).
#
# Let's think about how a character can be found as a unique character.

# Think about string "XAXAXXAX" and focus on making the second "A" a unique character.
# We can take "XA(XAXX)AX" and between "()" is our substring.
# We can see here, to make the second "A" counted as an uniq character, we need to:

# insert "(" somewhere between the first and second A
# insert ")" somewhere between the second and third A
# For step 1 we have "A(XA" and "AX(A", 2 possibility.
# For step 2 we have "A)XXA", "AX)XA" and "AXX)A", 3 possibilities.
# So when there are k characters between two 'A's, (or between string start to the first A; or between last A and string
# end), then there are k + 1 ways to slice. Number of ways to slice is the value we want to multiply.

# So there are in total 2 * 3 = 6 ways to make the second A an unique character in a substring.
# In other words, there are only 6 substring, in which this A contributes 1 point as unique string.

# Note that the 2 * 3 counting is for the previous 'A' (2nd one0, not the newest 'A'!
# Basically, we count unique substrings including an 'A' at s[i] when another 'A' appears at s[j] (j > i).
# Ss the last appearing 'A' is a corner case (Actually every last appearing char).

# Instead of counting all unique characters and struggling with all possible substrings,
# we can count for every char in S, how many ways to be found as a unique char.
# We count and sum, and it will be out answer.


# Explanation
# index[26][2] record last two occurrence index for every upper characters.
# Initialise all values in index to -1.
# Loop on string S, for every character c, update its last two occurrence index to index[c].
# Count during looping. For example, if "A" appears 3 times at index 3, 6, 9; we need to count:
# For the first A: (3 - (-1)) * (-1 - (-1)) = 0
# For the 2nd "A": (6-3) * (3-(-1))"
# For the 3rd "A": (9-6) * (6-3)"
# At the end: (N-9) * (9-6)"

# Don't forget at the end, len(s) can be considered as an occurrence of all chars

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # Records the most recent two occurrences index for every character in s
        last_shows = {c: [-1, -1] for c in s}

        res = 0
        for k, c in enumerate(s):
            i, j = last_shows[c]
            res += (j - i) * (k - j)
            last_shows[c] = [j, k] # update the most recent occurrences

        # The end of s is naturally another right boundary of substrings with unique char
        k = len(s)
        for c in last_shows:
            i, j = last_shows[c]
            res += (j - i) * (k - j)

        return res

